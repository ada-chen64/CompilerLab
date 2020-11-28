from .instr import IRInstr
from .funcmanage import ParamInfo
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
class IRProg:
    def __init__(self, funcs:IRFunc):
        self.funcs = funcs

    def __str__(self):
        return "\n\n".join(map(str, self.funcs))

class IREmitter:
    def __init__(self):
        self.funcs = []
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
    def getIR(self):
        return IRProg(self.funcs)

    def __call__(self, ir:IRInstr):
        #print("emitter called")
        #print(ir)
        self.emit(ir)

