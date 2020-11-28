import sys
sys.path.append('..')
from ..utils import *
class Variables:
    _varcnt = {}
    def __init__(self, ident:str, offset:int):
        incorInit(Variables._varcnt, ident)
        self.id = Variables._varcnt
        self.ident = ident
        self.offset = offset
    def __eq__(self, other):
        return self.id == other.id and self.ident == other.ident and\
            self.offset == other.offset

    def __str__(self):
        return f"{self.ident}({self.id})"

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash((self.ident, self.id, self.offset))
class FunctionInfo:
    def __init__(self):
        self._v = {}
class ParamInfo:
    def __init__(self, vars:[Variables]):
        self.vars = vars
        self.param_num = len(vars)
    def __str__(self):
        return f"{self.param_num}"
    def compatible(self, other):
        return self.param_num == other.param_num
class FunctionManager:
    def __init__(self):
        self.paramInfos = {}
        self.functions = []
    def enterfunction(self, func_name: str,paramInfo: ParamInfo):
        self.paramInfos[func_name] = paramInfo
        self.functions.append(func_name)