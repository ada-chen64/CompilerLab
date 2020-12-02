import sys
sys.path.append('..')
from ..utils import *

class IRInstr:
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return ""

class Const(IRInstr):
    def __init__(self, v:int):
        assert (MIN_INT < v) and (v < MAX_INT)
        self.v = v

    def __str__(self):
        return f"const {self.v}"


class Ret(IRInstr):
    def __str__(self):
        return f"ret"

class Neg(IRInstr):
    def __str__(self):
        return f"neg"

class Not(IRInstr):
    def __str__(self):
        return f"not"

class LNOT(IRInstr):
    def __str__(self):
        return f"lnot"
class Binaries(IRInstr):
    def __init__(self, op:str):
        self.op = op
    def __str__(self):
        return binsymbols[self.op]

class Equalities(IRInstr):
    def __init__(self, op:str):
        self.op = op
    def __str__(self):
        return eqsymbols[self.op]

class Relational(IRInstr):
    def __init__(self, op:str):
        self.op = op
    def __str__(self):
        return relatesymbols[self.op]

class Logical(IRInstr):
    def __init__(self, op:str):
        self.op = op
    def __str__(self):
        return logicsymbols[self.op]
class FrameAddr(IRInstr):
    def __init__(self, fpOffset:int):
        if fpOffset is not None:
            assert fpOffset < 0
        self.offset = fpOffset
    def __str__(self):
        return f"frameaddr {self.offset}"

class Load(IRInstr):
    def __str__(self):
        return f"load"

class Store(IRInstr):
    def __str__(self):
        return f"store"

class Pop(IRInstr):
    def __str__(self):
        return f"pop"

class Branch(IRInstr):
    def __init__(self, op:str, label:str):
        assert op in branchOp
        self.op = op
        self.label = label
    def __str__(self):
        return f"{self.op} {self.label}"

class Label(IRInstr):
    def __init__(self, label:str):
        self.label = label
    def __str__(self):
        return f"label {self.label}"
class Comment(IRInstr):
    def __init__(self, comment:str):
        self.comment = comment
    def __str__(self):
        return f"# {self.comment}"

class Call(IRInstr):
    def __init__(self, func_name:str):
        self.func_name = func_name
    def __str__(self):
        return f"call {self.func_name}"
class GlobalAddr(IRInstr):
    def __init__(self, symbol):
        self.symbol = symbol
    def __str__(self):
        return f"globaladdr {self.symbol}"