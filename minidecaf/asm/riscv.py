import sys
sys.path.append('..')
from ..ir.instr import *
from ..utils import *
from . import *

equalinstr = {'==' : 'seqz' , '!=' : 'snez'}
relateinstr = {'<' : 'slt', '>' : 'sgt'}
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
def load():
    return pop("t1") + [f"lw t1, 0(t1)"] + push("t1")

@Instrs
def store():
    return pop("t2", "t1") + [f"sw t1, 0(t2)"] + push("t1")

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

@Instrs
def equality(op):
    inst = equalinstr[op]
    
    return pop("t1", "t2") + [f"sub t1, t2, t1", f"{inst} t1, t1"] + push("t1")
    

@Instrs
def relation(op):
    if(op == '<') or (op == '>'):
        inst = relateinstr[op]
        return pop("t1", "t2") + [f"{inst} t1, t2, t1"] + push("t1")
    if(op == '<='):
        return relation('>') + LNot("t1")
    if(op == '>='):
        return relation('<') + LNot("t1")
@Instrs
def logical(op):
    inst = logicsymbols[op]
    if(inst == 'land'):
        return pop("t1", "t2") + [f"snez t1, t1", f"snez t2, t2", f"and t1, t2, t1"] + push("t1")
    elif(inst == 'lor'):
        return pop("t1", "t2") + [f"or t1, t2, t1", f"snez t1, t1"] + push("t1")

@Instrs
def branch(op, label:str):
    if op is 'br':
        return [f"j {label}"]
    else:
        return pop("t1") + [f"{op} t1, {label}"]


@Instrs
def frameAddr(k):
    return push("fp", k) + binary("+")

@Instrs
def ret(func:str):
    return [f"beqz x0, {func}_epilogue"]



class RISCVAsmGen:
    def __init__(self, emitter):
        self._E = emitter

    def genRet(self, instr:Ret):
        self._E(ret("main"))

    def genConst(self, instr:Const):
        self._E(push(instr.v))
    
    def genPop(self, instr:Pop):
        self._E(pop())

    def genNeg(self, instr:Neg):
        self._E(neg("t1"))

    def genNot(self, instr:Not):
        self._E(NOT("t1"))

    def genLNot(self, instr:LNot):
        self._E(LNot("t1"))
    def genBinary(self, instr:Binaries):
        self._E(binary(instr.op))
    
    def genEqualities(self, instr:Equalities):
        self._E(equality(instr.op))
    
    def genRelational(self, instr:Relational):
        self._E(relation(instr.op))
    
    def genLogical(self, instr:Logical):
        self._E(logical(instr.op))
    
    def genFrameAddr(self, instr:FrameAddr):
        self._E(frameAddr(instr.offset))
    
    def genStore(self, instr: Store):
        self._E(store())
    
    def genLoad(self, instr:Load):
        self._E(load())
    
    def genLabel(self, instr:Label):
        self._E([AsmLabel(instr.label)])
    
    def genBranch(self, instr:Branch):
        self._E(branch(instr.op, instr.label))

    def genPrologue(self, funcname:str):
        self._E([
            AsmBlank(),
            AsmDirective(".text"),
            AsmDirective(f".globl {funcname}"),
            AsmLabel(f"{funcname}")]) 
        self._E(push("ra", "fp")) 
        self._E([
            AsmInstr("mv fp, sp"),
            AsmComment("End Prologue"),
            AsmBlank()])

    def genEpilogue(self, funcname:str):
        self._E([
            AsmBlank(),
            AsmComment("BEGIN EPOLOGUE")] +
            push(0) + [
            AsmLabel(f"{funcname}_epilogue"),
            AsmInstr(f"lw a0, 0(sp)"),
            AsmInstr(f"mv sp, fp")] +
            pop("fp", "ra") + [
            AsmInstr("jr ra")
        ])
    def gen(self, ir):
        self.genPrologue("main")
        for instr in ir.instrs:
           # print(type(instr))
            _g[type(instr)](self, instr)
        self.genEpilogue("main")

_g = { Ret: RISCVAsmGen.genRet, Const: RISCVAsmGen.genConst, \
LNOT: RISCVAsmGen.genLNot, Not: RISCVAsmGen.genNot, Neg: RISCVAsmGen.genNeg, \
Binaries: RISCVAsmGen.genBinary, Equalities: RISCVAsmGen.genEqualities, \
Relational : RISCVAsmGen.genRelational, Logical: RISCVAsmGen.genLogical, \
Pop: RISCVAsmGen.genPop, Store: RISCVAsmGen.genStore, Load: RISCVAsmGen.genLoad, \
FrameAddr: RISCVAsmGen.genFrameAddr, Label: RISCVAsmGen.genLabel, Branch: RISCVAsmGen.genBranch}

