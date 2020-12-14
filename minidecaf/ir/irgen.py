from . import *
from .funcmanage import *
from .typer import *
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


class LabelCounter:
    def __init__(self):
        self._labels = {}
    def addLabel(self, lab= "LABEL"):
        if lab not in self._labels:
            self._labels[lab] = 1
        else:
            self._labels[lab] += 1
        return f"{lab}{self._labels[lab]}"
    def getLabel(self, lab= "LABEL"):
        return f"{lab}{self._labels[lab]}"
class StackIRGen(ExprVisitor):
    def __init__(self, emitter:IREmitter, typeInfo):
        self._E = emitter
        self.typeInfo = typeInfo
        # self._offtable = {}
        # self._top = 0
        self._functionManager = FunctionManager()
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
    
    def doGlobalInitializer(self, ctx:ExprParser.ExpressionContext):
        if ctx is None:
            return None
        try:
            init = eval(text(ctx), {}, {})
            return init
        except:
            raise ExprLocatedError(ctx, f"global variable must be constant")
    def visitGlobDecl(self, ctx:ExprParser.GlobDeclContext):
        #print("visitGlobDecl")
        ctx = ctx.declaration()
        init = self.doGlobalInitializer(ctx.expression())
        ident = text(ctx.Identifier())
        if ident in self._functionManager.paramInfos:
            raise ExprLocatedError(ctx, f"conflict global variable and function {func}")
        var = Variables(ident, None)
        globInfo = GlobalInfo(INT_SIZE, var, init)
        if ident in self._varstack.peek():
            prevVar = self._varstack[ident]
            prevGlobalInfo = self._functionManager.globalInfos[prevVar]
            if prevGlobalInfo.init is not None:
                if globInfo is not None:
                    raise ExprLocatedError(ctx, f"redefinition of variable {ident}")
            elif globInfo is not None:
                self._functionManager.globalInfos[preVar].init = init
        else:
            self._varstack[ident] = var
            self._functionManager.globalInfos[var] = globInfo
        self._E.emitGlobalInfo(globInfo)
    def visitFuncDef(self, ctx:ExprParser.FuncDefContext):
        func_name = text(ctx.Identifier())
        if func_name in self._functionManager.functions:
            raise ExprLocatedError(ctx, f"redefinition of function {func}")
        for var, value in self._functionManager.globalInfos.items():
            if func_name == var.ident:
                raise ExprLocatedError(ctx, f"conflict global variable and function {func_name}")  
        self.newBlock(ctx)
        paramInfo = ParamInfo(ctx.param_list().accept(self))
        if func_name in self._functionManager.paramInfos:
            if not self._functionManager.paramInfos[func_name].compatible(paramInfo):
                raise ExprLocatedError(ctx, f"conflicting types for {func}")
        self._functionManager.enterfunction(func_name, paramInfo)
        self._E.enterfunction(func_name, paramInfo)
        ctx.temp_stmt().accept(self)
        self.popBlock(ctx)
        self._E.exitfunction()
    def visitFuncDecl(self, ctx:ExprParser.FuncDeclContext):
        #print("in func decl")
        func_name = text(ctx.Identifier())
        #print(f"func name: {func_name}")
        for var, value in self._functionManager.globalInfos.items():
            if func_name == var.ident:
                raise ExprLocatedError(ctx, f"conflict global variable and function {func_name}")  
        self.newBlock(ctx)
        paramInfo = ParamInfo(ctx.param_list().accept(self))
        if func_name in self._functionManager.paramInfos:
            if not self._functionManager.paramInfos[func_name].compatible(paramInfo):
                raise ExprLocatedError(ctx, f"conflicting types for {func}")
        elif func_name not in self._functionManager.paramInfos:
            self._functionManager.paramInfos[func_name] = paramInfo
        self.popBlock(ctx)
    def visitCompound_statement(self, ctx:ExprParser.Compound_statementContext):
        self._E(instr.Comment("new Block cmpd_stmt"))
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
            raise ExprLocatedError(ctx, f"redefinition of {text(ident)}")
        self.decVar(ctx, ident)
        #self.offset.addVar(var)
        
        #self.addVar(var)
    def visitCondStmt(self, ctx:ExprParser.CondStmtContext):
        #first take care of the if condition expression
        self._E(instr.Comment("if statement"))
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
    
    def visitForStmt(self, ctx:ExprParser.ForStmtContext):
        #first do initialize expression
        self._E(instr.Comment("for Block"))
        self.newBlock(ctx)
        if ctx.init is not None:
            ctx.init.accept(self)
        begin_looplabel = self._labelCounter.addLabel("beginloop_Label")
        break_label = self._labelCounter.addLabel("breakloop_Label")
        cont_label = self._labelCounter.addLabel("continue_Label")
        self._E(instr.Label(begin_looplabel))
        if ctx.cond is not None:
            ctx.cond.accept(self)
            self._E(instr.Branch("beqz", break_label))
        ctx.statement().accept(self)
        self._E(instr.Label(cont_label))
        if ctx.incr is not None:
            ctx.incr.accept(self)
            self._E(instr.Pop())
        self._E(instr.Branch("br", begin_looplabel))
        self._E(instr.Label(break_label))
        pt = self.popBlock(ctx)
        #print("pop time",pt)
        self._E(instr.Comment("for Pop"))
        for i in range(pt):
            self._E(instr.Pop())
    
    def visitForDeclStmt(self, ctx:ExprParser.ForDeclStmtContext):
        self._E(instr.Comment("for Block"))
        self.newBlock(ctx)
        ctx.declaration().accept(self)
        begin_looplabel = self._labelCounter.addLabel("beginloop_Label")
        break_label = self._labelCounter.addLabel("breakloop_Label")
        cont_label = self._labelCounter.addLabel("continue_Label")
        self._E(instr.Label(begin_looplabel))
        if ctx.cond is not None:
            ctx.cond.accept(self)
            self._E(instr.Branch("beqz", break_label))
        ctx.statement().accept(self)
        self._E(instr.Label(cont_label))
        if ctx.incr is not None:
            ctx.incr.accept(self)
            self._E(instr.Pop())
        self._E(instr.Branch("br", begin_looplabel))
        self._E(instr.Label(break_label))
        pt = self.popBlock(ctx)
        #print("pop time",pt)
        for i in range(pt):
            self._E(instr.Comment("Pop"))
            self._E(instr.Pop())
    def visitWhileStmt(self, ctx:ExprParser.WhileStmtContext):
        begin_looplabel = self._labelCounter.addLabel("beginloop_Label")
        break_label = self._labelCounter.addLabel("breakloop_Label")
        cont_label = self._labelCounter.addLabel("continue_Label")
        self._E(instr.Label(begin_looplabel))
        ctx.expression().accept(self)
        self._E(instr.Branch("beqz", break_label))
        ctx.statement().accept(self)
        self._E(instr.Label(cont_label))
        self._E(instr.Branch("br", begin_looplabel))
        self._E(instr.Label(break_label))


    def visitDoStmt(self, ctx:ExprParser.DoStmtContext):
        begin_looplabel = self._labelCounter.addLabel("beginloop_Label")
        break_label = self._labelCounter.addLabel("breakloop_Label")
        cont_label = self._labelCounter.addLabel("continue_Label")
        self._E(instr.Label(begin_looplabel))
        ctx.expression().accept(self)
        self._E(instr.Branch("beqz", break_label))
        ctx.statement().accept(self)
        self._E(instr.Label(cont_label))
        self._E(instr.Branch("br", begin_looplabel))
        self._E(instr.Label(break_label))

    
    def visitBreakStmt(self, ctx:ExprParser.BreakStmtContext):
        self._E(instr.Branch("br", self._labelCounter.getLabel("breakloop_Label")))

    def visitContStmt(self, ctx:ExprParser.ContStmtContext):
        self._E(instr.Branch("br", self._labelCounter.getLabel("continue_Label")))

    def visitAtomIdentifier(self, ctx:ExprParser.AtomIdentifierContext):
        #print("AtomIdentifier")
        ident = ctx.Identifier()
        #print(f"ident: {ident}")
        var = self.getVar(ctx, ident)
        off = var.offset
        #off = self.offset.getVar(var)
        #off = self._offtable[var]
        if off is None:
            self._E(instr.GlobalAddr(ident))
        else:
            self._E(instr.FrameAddr(off))
            self._E(instr.Comment("frameaddress load done"))
        if not isinstance(self.typeInfo[ctx], ArrayType):
            self._E(instr.Load())
        
    def computeLValue(self, lvalue):
        if isinstance(lvalue,ExprParser.TUnaryContext):
            return self.computeLValue(lvalue.postfix())
        if isinstance(lvalue, ExprParser.TPostFixContext):
            return self.computeLValue(lvalue.atom())
        if isinstance(lvalue, ExprParser.AtomIdentifierContext):
            #identifier = expression
            ident = lvalue.Identifier()
            var = self.getVar(lvalue, ident)
            off = var.offset
            if off is None:
                self._E(instr.GlobalAddr(ident))
            else:
                self._E(instr.Comment("frameaddress store"))
                self._E(instr.FrameAddr(off))
            return
        elif isinstance(lvalue, ExprParser.AtomParenContext):
            return self.computeLValue(lvalue.expression())
        raise ExprLocatedError(lvalue, f"{text(lvalue)} is not an lvalue")
    def emitLoc(self, ctx):
        locs = self.typeInfo.lvalueLoc(ctx)
        for loc in locs:
            if isinstance(loc, IRInstr):
                self._E(loc)
            else:
                loc.accept(self)
    def visitTAssign(self, ctx:ExprParser.TAssignContext):
        ctx.expression().accept(self)
        self.emitLoc(ctx.unary())
        self._E(instr.Store())
        self._E(instr.Comment("frameaddress store done"))
        

    def visitCUnary(self, ctx:ExprParser.UnaryContext):
        #print("visit expression")
        op = text(ctx.unaryOp())
        if op == '&':
            self.emitLoc(ctx.unary())
        else: 
            self.visitChildren(ctx)
            if op == '*':
                self._E(instr.Load())
            elif op == '~':
                self._E(instr.Not())
            elif op == '-':
                self._E(instr.Neg())
            elif op == '!':
                self._E(instr.LNOT())
        # self.visitChildren(ctx)
        # sym = text(ctx.unaryOp())
        
        # if sym == '~':
        #     self._E(instr.Not())
        # if sym == '-':
        #     self._E(instr.Neg())
        # if sym == '!':
        #     self._E(instr.LNOT())
       
    def visitFunction(self, ctx:ExprParser.FunctionContext):
        func_name = text(ctx.Identifier())
        assert func_name == "main"
        self.visitChildren(ctx)

    def visitAtomInteger(self, ctx:ExprParser.AtomIntegerContext):
        v = int(text(ctx.Integer()))
        #print(v)
        self._E(instr.Const(v))
    def _addExpr(self, ctx, op, lhs, rhs):
        if isinstance(self.typeInfo[lhs], PtrType):
            sz = self.typeInfo[lhs].sizeof()
            if isinstance(self.typeInfo[rhs], PtrType): # ptr - ptr
                lhs.accept(self)
                rhs.accept(self)
                self._E(instr.Binaries(op))
                self._E(instr.Const(sz))
                self._E(instr.Binaries('/'))
            else: # ptr +- int
                lhs.accept(self)
                rhs.accept(self)
                self._E(instr.Const(sz))
                self._E(instr.Binaries('*'))
                self._E(instr.Binary(op))
        else:
            sz = self.typeInfo[rhs].sizeof()
            if isinstance(self.typeInfo[rhs], PtrType): # int +- ptr
                lhs.accept(self)
                self._E(instr.Const(sz))
                self._E(instr.Binaries('*'))
                rhs.accept(self)
                self._E(instr.Binaries(op))
            else: # int +- int
                self.visitChildren(ctx)
                self._E(instr.Binaries(op))
    def visitAddOpMult(self, ctx:ExprParser.AddOpMultContext):
        self._addExpr(ctx, text(ctx.addOp()), ctx.add(), ctx.mult())
        #print(op)
    def visitMultOpUnary(self, ctx:ExprParser.MultOpUnaryContext):
        self.visitChildren(ctx)
        op = text(ctx.mulOp())
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
        self._E(instr.Comment("relational"))
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
    def visitParam_list(self, ctx:ExprParser.Param_listContext):
        self.visitChildren(ctx)
        def f(decl):
            return self._varstack[text(decl.Identifier())]
        return list(map(f, ctx.declaration()))
    def visitCPostFix(self, ctx:ExprParser.CPostFixContext):
        func_name = text(ctx.Identifier())
        args = ctx.expr_list().expression()
        # print(func_name)
        # for key, value in self._functionManager.paramInfos.items():
        #     print(key)
        #     print(self._functionManager.paramInfos)
        if len(args) != self._functionManager.paramInfos[func_name].param_num:
            raise ExprLocatedError(ctx, f"wrong argument number")
        for arg in reversed(args):
            arg.accept(self)
        self._E(instr.Call(func_name))
