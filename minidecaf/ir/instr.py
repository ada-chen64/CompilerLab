import sys
sys.path.append('..')
from ..utils import *

class IRInstr:
    def __repr__(self):
        return self.__str__()


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

    
