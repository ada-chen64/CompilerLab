from . import *
import sys
sys.path.append('..')
from ..utils import *
from ..ExprParser import ExprParser
from ..ExprVisitor import ExprVisitor
class OffsetManage:
    def __init__(self):
        self._offtable = {}
        self._top = 0
    def getVar(self, var):
        return self._offtable[var]
    def addVar(self, var=None):
        # assert var not in self._offtable
        self._top -= INT_SIZE
        if var is not None:
            self._offtable[var] = self._top
        return self._top
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


class LabelCounter:
    def __init__(self):
        self._labels = {}
    def addLabel(self, lab= "LABEL"):
        if lab not in self._labels:
            self._labels[lab] = 1
        else:
            self._labels[lab] += 1
        return f"{lab}{self._labels[lab]}"
class StackIRGen(ExprVisitor):
    def __init__(self, emitter:IREmitter):
        self._E = emitter
        # self._offtable = {}
        # self._top = 0
        self._labelCounter = LabelCounter()
        self._frameSlots = [] #keeps track of frame slots used for each block
        self._curFrameSlot = 0 #frame slots used for THIS block
        self._varstack = stack_dict() #dict entry for each block
    def decVar(self, ctx, ident):
        self._curFrameSlot += 1
        self._varstack[text(ident)] = Variables(text(ident), -INT_SIZE * self._curFrameSlot)
    def getVar(self, ctx, ident):
        return self._varstack[text(ident)]
    def newBlock(self, ctx):
        self._varstack.push()
        self._frameSlots.append(self._curFrameSlot)
    def popBlock(self, ctx):
        slots_to_release = self._curFrameSlot - self._frameSlots[-1]
        self._varstack.pop()
        self._curFrameSlot = self._frameSlots[-1]
        self._frameSlots.pop()
        return slots_to_release
        #self.offset = OffsetManage()
    # def addVar(self, var=None):
    #     assert var not in self._offtable
    #     self._top -= INT_SIZE
    #     if var is not None:
    #         self._offtable[var] = self._top
    #     return self._top
    def visitCompound_statement(self, ctx:ExprParser.Compound_statementContext):
        self._E(instr.Comment("new Block"))
        self.newBlock(ctx)
        self.visitChildren(ctx)
        pt = self.popBlock(ctx)
        #print("pop time",pt)
        for i in range(pt):
            self._E(instr.Comment("Pop"))
            self._E(instr.Pop())
    def visitReturnStmt(self, ctx:ExprParser.ReturnStmtContext):
        #print("visit return")
        self.visitChildren(ctx)
        self._E(instr.Ret())
    def visitExprStmt(self, ctx:ExprParser.ExprStmtContext):
        if ctx.expression() is not None:
            ctx.expression().accept(self)
        self._E(instr.Comment("Pop due to expr"))
        self._E(instr.Pop())
    def visitDeclaration(self, ctx:ExprParser.DeclarationContext):
        
        ident = ctx.Identifier()
        self._E(instr.Comment(f"new declaration {text(ident)}"))
        if ctx.expression() is not None:
            ctx.expression().accept(self)
        else:
            self._E(instr.Const(0))
        if text(ident) in self._varstack.peek():
            raise MiniDecafLocatedError(ctx, f"redefinition of {var}")
        self.decVar(ctx, ident)
        #self.offset.addVar(var)
        
        #self.addVar(var)
    def visitCondStmt(self, ctx:ExprParser.CondStmtContext):
        #first take care of the if condition expression
        ctx.expression().accept(self) 
        #make labels for exit and else
        exit_label = self._labelCounter.addLabel("end_Label")
        else_label = self._labelCounter.addLabel("else_Label")
        if ctx.c_el is not None:
            #if it has else, then branch to else
            self._E(instr.Branch("beqz", else_label))
            #then do the case_if statement
            ctx.c_if.accept(self)
            #branch to end_label
            self._E(instr.Branch("br", exit_label))
            #now do the case_else
            self._E(instr.Label(else_label))
            ctx.c_el.accept(self)
            #end_label here
            self._E(instr.Label(exit_label))
        else:
            #no else, then just go to end_label
            self._E(instr.Branch("beqz", exit_label))
            ctx.c_if.accept(self)
            self._E(instr.Label(exit_label))

    def visitAtomIdentifier(self, ctx:ExprParser.AtomIdentifierContext):
        ident = ctx.Identifier()
        var = self.getVar(ctx, ident)
        off = var.offset
        #off = self.offset.getVar(var)
        #off = self._offtable[var]
        self._E(instr.Comment("frameaddress load"))
        self._E(instr.FrameAddr(off))
        self._E(instr.Load())
    
    def visitTAssign(self, ctx:ExprParser.TAssignContext):
        self.visitChildren(ctx)
        ident = ctx.Identifier()
        var = self.getVar(ctx, ident)
        off = var.offset
        #off = self._offtable[var]
        #off = self.offset.getVar(var)
        self._E(instr.Comment("frameaddress store"))
        self._E(instr.FrameAddr(off))
        self._E(instr.Store())
        

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
    def visitTCond(self, ctx:ExprParser.TCondContext):
        #logical_or '?' expression ':' conditional
        #if logical_or is true, do expression, else do conditional
        ctx.logical_or().accept(self)
        #make end and else labels
        exit_label = self._labelCounter.addLabel("end_Label")
        else_label = self._labelCounter.addLabel("else_Label")
        self._E(instr.Branch("beqz", else_label))
        #then do theexpresion
        ctx.expression().accept(self)
        #branch to end_label
        self._E(instr.Branch("br", exit_label))
        #now do the conditional
        self._E(instr.Label(else_label))
        ctx.conditional().accept(self)
        #end_label here
        self._E(instr.Label(exit_label))