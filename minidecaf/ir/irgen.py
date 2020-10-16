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
    def visitAddOpMult(self, ctx:ExprParser.AddOpMultContext):
        self.visitChildren(ctx)
        if(ctx.Add()):
            op = text(ctx.Add())
        if(ctx.Sub()):
            op = text(ctx.Sub())
        self._E(instr.Binaries(op))
        #print(op)
    def visitMultOpUnary(self, ctx:ExprParser.MultOpUnaryContext):
        self.visitChildren(ctx)
        op = text(ctx.MulOp())
        self._E(instr.Binaries(op))
        #print(op)
    
    def visitTLog_or(self, ctx:ExprParser.TLog_orContext):
        self.visitChildren(ctx)
        op = text(ctx.LOr())
        self._E(instr.Logical(op))
    def visitTLog_and(self, ctx:ExprParser.TLog_andContext):
        self.visitChildren(ctx)
        op = text(ctx.Land())
        self._E(instr.Logical(op))
    def visitTEquality(self, ctx:ExprParser.TEqualityContext):
        self.visitChildren(ctx)
        op = text(ctx.EqOp())
        self._E(instr.Equalities(op))
    def visitTRelational(self, ctx:ExprParser.TRelationalContext):
        self.visitChildren(ctx)
        op = text(ctx.InEqOp())
        self._E(instr.Relational(op))