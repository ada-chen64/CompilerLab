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

    def visitExpression(self, ctx:ExprParser.ExpressionContext):
        #print("visit expression")
        v = int(text(ctx.Integer()))
        self._E(instr.Const(v))
    def visitFunction(self, ctx:ExprParser.FunctionContext):
        func_name = text(ctx.Identifier())
        assert func_name == "main"
        self.visitChildren(ctx)