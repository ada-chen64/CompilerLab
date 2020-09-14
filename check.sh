#!/bin/bash
export CC="riscv64-unknown-elf-gcc  -march=rv32im -mabi=ilp32"
export QEMU=qemu-riscv32

USE_PARALLEL=${true:-$USE_PARALLEL}
JOBS=(`find testcases -name '*.c'`)
FAILJOBS=(`find failcases -name '*.c'`)


gen_asm() {
    cfile=$1
    asmfile=$2

    if [[ -f ../minidecaf/minidecaf/requirements.txt ]]; then       # Python
        PYTHONPATH=../minidecaf python -m minidecaf $cfile >$asmfile
    elif [[ -f ../minidecaf/Cargo.toml ]]; then                     # Rust
        ../minidecaf/target/debug/minidecaf $cfile >$asmfile
    else
        echo "======== No compiler set! Check gen_asm! ========"
        touch no_compiler_set
    fi
}
export -f gen_asm


run_job() {
    infile=$1
    outbase=${infile%.c}

    rm $outbase.{gcc,expected,err,my,actual,s} 1>/dev/null 2>&1

    $CC $infile -o $outbase.gcc
    $QEMU $outbase.gcc
    echo $? > $outbase.expected

    ( set -e
      gen_asm $infile $outbase.s
      $CC $outbase.s -o $outbase.my
    ) >$outbase.err 2>&1
    if [[ $? != 0 ]]; then
        echo "ERR ${infile}"
        return 2
    fi
    $QEMU $outbase.my
    echo $? > $outbase.actual

    if ! diff -qZ $outbase.expected $outbase.actual >/dev/null ; then
        echo "FAIL ${infile}"
        return 1
    else
        echo "OK ${infile}"
        return 0
    fi
}
export -f run_job


run_failjob() {
    infile=$1
    outbase=${infile%.c}

    if ( set -e
      gen_asm $infile $outbase.s
      $CC $outbase.s -o $outbase.my ) >/dev/null 2>&1
    then
        echo "FAIL ${infile}"
        return 1
    else
        echo "OK ${infile}"
        return 0
    fi
}
export -f run_failjob


check_env_and_parallel() {
    if $CC --version >/dev/null 2>&1; then
        echo "gcc found"
    else
        echo "gcc not found"
        exit 1
    fi

    if $QEMU -version >/dev/null 2>&1; then
        echo "qemu found"
    else
        echo "qemu not found"
        exit 1
    fi

    if parallel --version >/dev/null 2>&1; then
        if $USE_PARALLEL; then
            echo "parallel found"
            return 0
        else
            echo "parallel found but not used"
            return 1
        fi
    else
        echo "parallel not found"
        return 1
    fi
}


main() {
    if check_env_and_parallel; then
        parallel --halt now,fail=1 run_job ::: ${JOBS[@]} || exit 1
        parallel --halt now,fail=1 run_failjob ::: ${FAILJOBS[@]} || exit 1
    else
        for job in ${JOBS[@]}; do
            if ! run_job $job; then exit 1; fi
        done
        for job in ${FAILJOBS[@]}; do
            if ! run_failjob $job; then exit 1; fi
        done
    fi
}


if ! [[ -d ../minidecaf ]]; then
    echo "Put your code in ../minidecaf"
    exit 1
fi

if ! (main); then
    [[ -f no_compiler_set ]] && { echo "Change gen_asm first!" ; rm no_compiler_set; }
    echo FAILED
    exit 1;
fi

echo PASSED
