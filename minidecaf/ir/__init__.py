from .instr import IRInstr
from .typer import Typer
from .funcmanage import ParamInfo, GlobalInfo

 
def typecheck(tree):
    typer = Typer()
    typer.visit(tree)
    return typer.typeInfo


class IRFunc:
    def __init__(self, name:str, param:ParamInfo, instrs:[IRInstr]):
        self.name = name
        self.param = param
        self.instrs = instrs
    def __str__(self):
        def f(i):
            if type(i) is instr.Comment:
                return f"\t\t\t\t{i}"
            if type(i) is instr.Label:
                return f"{i}"
            return f"\t{i}"
        body = '\n'.join(map(f, self.instrs))
        return f"{self.name}({self.param}):\n{body}"

class IRGlobals:
    def __init__(self, symbol:str, size:int, init, align=4):
        self.symbol = symbol
        self.size = size
        self.init = init
        self.align = align
    def genfromGlobalInfo(globalInfo):
        assert globalInfo.var.offset is None
        return IRGlobals(globalInfo.var.ident, globalInfo.size, globalInfo.init)
    def __str__(self):
        return f"{self.symbol}:\n\tsize={self.size}, align={self.align}\n\t{self.initStr()}"
    def initStr(self):
        if self.init is None:
            return f"uninitialized"
        else:
            return f"initialized: {self.init}"
class IRProg:
    def __init__(self, funcs:IRFunc, glob: IRGlobals):
        self.funcs = funcs
        self.globals = glob
    def __str__(self):
        return "\n\n".join(map(str, self.funcs))
        
class IREmitter:
    def __init__(self):
        self.funcs = []
        self.globals = []
        #self.instrs = []
        self.cur_func = None
        self.cur_param = None
        self.cur_instrs = []
    def enterfunction(self, func_name: str, paramInfo:ParamInfo):
        self.cur_func = func_name
        self.cur_param = paramInfo
        self.cur_instrs = []
    def exitfunction(self):
        self.funcs.append(IRFunc(self.cur_func,self.cur_param, self.cur_instrs))

    def emit(self, ir:IRInstr):
        self.cur_instrs.append(ir)
        #print(self.instrs)
    def emitGlobalInfo(self, globalInfo: GlobalInfo):
        self.globals.append(IRGlobals.genfromGlobalInfo(globalInfo))
    def getIR(self):
        return IRProg(self.funcs, self.globals)

    def __call__(self, ir:IRInstr):
        #print("emitter called")
        #print(ir)
        self.emit(ir)

