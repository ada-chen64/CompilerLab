from . import *
import sys
sys.path.append('..')
from ..utils import *
from ..ExprParser import ExprParser
from ..ExprVisitor import ExprVisitor

class StackIRGen(ExprVisitor):
    def __init__(self, emitter:IREmitter):
        self._E = emitter

    def visitReturnStmt(self, ctx:ExprParser.ReturnStmtContext):
        #print("visit return")
        self.visitChildren(ctx)
        self._E(instr.Ret())

    def visitCUnary(self, ctx:ExprParser.UnaryContext):
        #print("visit expression")
        self.visitChildren(ctx)
        
        if(ctx.Not()):
            sym = text(ctx.Not())
            self._E(instr.Not())
        if(ctx.Sub()):
            sym = text(ctx.Sub())
            self._E(instr.Neg())
        if(ctx.LNot()):
            sym = text(ctx.LNot())
            self._E(instr.LNOT())
       
    def visitFunction(self, ctx:ExprParser.FunctionContext):
        func_name = text(ctx.Identifier())
        assert func_name == "main"
        self.visitChildren(ctx)

    def visitAtomInteger(self, ctx:ExprParser.AtomIntegerContext):
        v = int(text(ctx.Integer()))
        #print(v)
        self._E(instr.Const(v))