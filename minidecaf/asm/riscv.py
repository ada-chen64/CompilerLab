import sys
sys.path.append('..')
from ..ir.instr import *
from ..utils import *
from . import *


def Instrs(f):
    def g(*args, **kwargs):
        instrs = f(*args, *kwargs)
        return [AsmInstr(x) for x in instrs]
    return g

@Instrs
def _push(val):
    if type(val) is int:
        return [f"addi sp, sp, -8", f"li t1, {val}", f"sw t1, 0(sp)"] #push integer
    else:
        return [f"addi sp, sp, -8", f"sw {val}, 0(sp)"] # push register
def push(*vals):
    return flatten(map(_push, vals))
@Instrs
def _pop(reg):
    if reg is None:
        return [f"addi sp, sp, 8"]
    return [f"lw {reg}, 0(sp)"] + [f"addi sp, sp, 8"]
def pop(*regs):
    return flatten(map(_pop, regs))


@Instrs
def neg(reg):
    #print(pop(reg) + [f"neg {reg}, {reg}"] + push(reg))
    return pop(reg) + [f"neg {reg}, {reg}"] + push(reg)

@Instrs
def NOT(reg):
    #print("NOT")
    #print(pop(reg) + [f"not {reg}, {reg}"] + push(reg))
    return pop(reg) + [f"not {reg}, {reg}"] + push(reg)

@Instrs
def LNot(reg):
    return pop(reg) + [f"seqz {reg}, {reg}"] + push(reg)

@Instrs
def binary(op):
    inst = binsymbols[op]
    return pop("t1", "t2") + [f"{inst} t1, t2, t1"] + push("t1")
    #print(inst)

class RISCVAsmGen:
    def __init__(self, emitter):
        self._E = emitter

    def genRet(self, instr:Ret):
        self._E(pop("a0"))

    def genConst(self, instr:Const):
        self._E(push(instr.v))

    def genNeg(self, instr:Neg):
        self._E(neg("t1"))

    def genNot(self, instr:Not):
        self._E(NOT("t1"))

    def genLNot(self, instr:LNot):
        self._E(LNot("t1"))
    def genBinary(self, instr:Binaries):
        self._E(binary(instr.op))
    
    def gen(self, ir):
        self._E([
            AsmDirective(".text"),
            AsmDirective(".globl main"),
            AsmLabel("main")])
        for instr in ir.instrs:
           # print(type(instr))
            _g[type(instr)](self, instr)
        self._E([
            AsmInstr("jr ra")])

_g = { Ret: RISCVAsmGen.genRet, Const: RISCVAsmGen.genConst, LNOT: RISCVAsmGen.genLNot, Not: RISCVAsmGen.genNot, Neg: RISCVAsmGen.genNeg, Binaries: RISCVAsmGen.genBinary}

