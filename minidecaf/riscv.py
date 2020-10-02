from antlr4 import *


def _push(val):
    if type(val) is int:
        return [f"addi sp, sp, -{INT_BYTES}", f"li t1, {val}", f"sw t1, 0(sp)"] # push int
    else:
        return [f"addi sp, sp, -{INT_BYTES}", f"sw {val}, 0(sp)"] # push register

def _pop(reg):
    return ([f"lw {reg}, 0(sp)"] if reg is not None else []) + [f"addi sp, sp, {INT_BYTES}"]

