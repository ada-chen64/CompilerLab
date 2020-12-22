from . import *
from .types import *
from .funcmanage import *
import sys
sys.path.append('..')
from ..utils import *
from ..ExprParser import ExprParser
from ..ExprVisitor import ExprVisitor
class TypeInfo:
    def __init__(self):
        self.loc = {} # ctx -> (IRInstr|ctx)+
        self.funcs = {} # str -> FuncTypeInfo
        self._t = {} # ctx -> Type

    def lvalueLoc(self, ctx):
        return self.loc[ctx]

    def setLvalueLoc(self, ctx, loc:list):
        #print("setLvalueLoc:")
        #print("ctx:", ctx)
        #print("loc:", loc)
        self.loc[ctx] = loc

    def __str__(self):
        res = "Lvalue analysis result: (location of expr at lhs == value of rhs):\n\t"
        def p(c):
            return f"{c.start.line},{c.start.column}~{c.stop.line},{c.stop.column}"
        def g(locStep):
            if isinstance(locStep, IRInstr):
                return f"{locStep}"
            else:
                return f"[{p(locStep)}]"
        def f(cl):
            ctx, loc = cl
            ctxStr = f"{p(ctx)}"
            locStr = " :: ".join(map(g, loc))
            return f"{ctxStr:>32} : {locStr}"
        res += "\n\t".join(map(f, self.loc.items()))
        res += "\n\nType info for funcs:\n\t"
        def f(nf):
            name, funcInfo = nf
            return f"{name:>32} : ({funcInfo.paramType}) -> {funcInfo.retType}"
        res += "\n\t".join(map(f, self.funcs.items()))
        return res

    def __getitem__(self, ctx):
        return self._t[ctx]
class FuncTypeInfo:
    def __init__(self, retType:Type, paramType:list):
        self.retType = retType
        self.paramType = paramType

    def compatible(self, other):
        return self.retType == other.retType and self.paramType == other.paramType

    def call(self):
        @TypeRule
        def callRule(ctx, argType:list):
            if self.paramType == argType:
                return self.retType
            return f"bad argument types"
        return callRule

def SaveType(f):
    def g(self, ctx):
        typ = f(self, ctx)
        self.typeInfo._t[ctx] = typ
        return typ
    return g

class Typer(ExprVisitor):
    def __init__(self):
        self.typeInfo = TypeInfo()
        self._vartype = {} #variable ->Type
        self._curFunc = None
        self._functionManager = FunctionManager()
        self._frameSlots = [] #keeps track of frame slots used for each block
        self._curFrameSlot = 0 #frame slots used for THIS block
        self._varstack = stack_dict() #dict entry for each block
        self.locator = Locator(self.typeInfo)
    def decVar(self, ctx, ident, numInts=1):
        self._curFrameSlot += numInts
        self._varstack[text(ident)] = Variables(text(ident), -INT_SIZE * self._curFrameSlot, INT_SIZE * numInts)
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
    def _getdecltype(self, ctx):
        basetype = ctx.typ().accept(self)
        dims = [int(text(x)) for x in reversed(ctx.Integer())]
        if len(dims) == 0:
            return basetype
        else:
            return ArrayType.make(basetype, dims)
    def _getargType(self,ctx:ExprParser.Expr_listContext):
        args = list(map(lambda x: x.accept(self), ctx.expression()))
        #print(args)
        return args
    def getVarsize(self, ctx:ExprParser.DeclarationContext):
        size = product([int(text(x)) for x in ctx.Integer()])
        if size <= 0:
            raise ExprLocatedError(ctx, f"array size cannot be zero")
        if size > MAX_INT:
            raise ExprLocatedError(ctx, f"array size too big")
        return size
    def _getparamType(self, ctx:ExprParser.Param_listContext):
        typs = []
        for decl in ctx.declaration():
            if decl.expression() is not None:
                raise ExprLocatedError(decl, f"Parameter cannot be initialized")
            paramType = self._getdecltype(decl)
            if isinstance(paramType, ArrayType):
                raise ExprLocatedError(decl, f"Parameter cannot be ArrayType")
            typs += [paramType]
        #print("paramtypes: ",typs)
        return typs
    def _getfuncTypeInfo(self, ctx):
        #print("getting func type")
        retType = ctx.typ().accept(self)
        paramType = self._getparamType(ctx.param_list())
        return FuncTypeInfo(retType, paramType)
    def checkUnary(self, ctx, op:str, ty:Type):
        rule = expandIterableKey([
            (['-', '!', '~'],   intUnaopRule),
            (['&'],             addrofRule),
            (['*'],             derefRule),
        ])[op]
        return rule(ctx, ty)
    def checkBinary(self, ctx, op:str, lhs:Type, rhs:Type):
        #print(op)
        rule = expandIterableKey([
            (['*', '/', '%', '&&', '||'],    intBinOpRule),
            (['==', '!='],                         eqRule),
            (['<', '>', '<=', '>='],              relRule),
            (['='],                         asgnRule),
            (['+'],                         tryEach('+', intBinOpRule, ptrArithRule)),
            (['-'],                         tryEach('-', intBinOpRule, ptrArithRule, ptrDiffRule)),
        ])[op]
        return rule(ctx, lhs, rhs)
    def locate(self, ctx):
        loc = self.locator.locate(self._curFunc, ctx, self._varstack)
        if loc is None:
            raise ExprLocatedError(ctx, f"lvalue expected")
        self.typeInfo.setLvalueLoc(ctx, loc)
    def visitChildren(self, ctx):
        typ = ExprVisitor.visitChildren(self, ctx)
        self.typeInfo._t[ctx] = typ
        return typ
    def visitCompound_statement(self, ctx:ExprParser.Compound_statementContext):
        self.newBlock(ctx)
        self.visitChildren(ctx)
        pt = self.popBlock(ctx)
        #print("pop time",pt)
        
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
        typ = self._getdecltype(ctx)
        init = self.doGlobalInitializer(ctx.expression())
        ident = text(ctx.Identifier())
        if ident in self._functionManager.paramInfos:
            raise ExprLocatedError(ctx, f"conflict global variable and function {func}")
        var = Variables(ident, None, INT_SIZE * self.getVarsize(ctx))
        globInfo = GlobalInfo(INT_SIZE * self.getVarsize(ctx), var, init)
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
        if var in self._vartype:
            prevTyp = self._vartype[var]
            if prevTyp != typ:
                raise ExprLocatedError(ctx, f"conflict global variable type for {ident}, expected {prevTyp} got {typ}")
        else:
            self._vartype[var] = typ
        if ctx.expression() is not None:
            initType = ctx.expression().accept(self)
            asgnRule(ctx, typ, initType)
    def visitDeclaration(self, ctx:ExprParser.DeclarationContext):
        #print("in visit declaration")
        ident = ctx.Identifier()
        typ = self._getdecltype(ctx)
        if ctx.expression() is not None:
            initType = ctx.expression().accept(self)
            asgnRule(ctx, typ, initType)
        if text(ident) in self._varstack.peek():
            raise ExprLocatedError(ctx, f"redefinition of {text(ident)}")
        self.decVar(ctx, ident, self.getVarsize(ctx))
        var = self._varstack[text(ident)]
        self._vartype[var] = typ
        return typ
    def checkFunc(self, ctx):
        func = text(ctx.Identifier())
        #print(func)
        funcTypeInfo = self._getfuncTypeInfo(ctx)
        if func in self.typeInfo.funcs:
            prevFuncTypeInfo = self.typeInfo.funcs[func]
            if not funcTypeInfo.compatible(prevFuncTypeInfo):
                raise ExprLocatedError(ctx, f"conflicting types for {func}")
        else:
            self.typeInfo.funcs[func] = funcTypeInfo
    def visitFuncDef(self, ctx:ExprParser.FuncDefContext):
        
        func_name = text(ctx.Identifier())
        #print(f"in func def: {func_name}")
        self._curFunc = func_name
        if func_name in self._functionManager.functions:
            raise ExprLocatedError(ctx, f"redefinition of function {func}")
        for var, value in self._functionManager.globalInfos.items():
            if func_name == var.ident:
                raise ExprLocatedError(ctx, f"conflict global variable and function {func_name}")  
        self.newBlock(ctx)
        self.checkFunc(ctx)
        paramInfo = ParamInfo(ctx.param_list().accept(self))
        if func_name in self._functionManager.paramInfos:
            if not self._functionManager.paramInfos[func_name].compatible(paramInfo):
                raise ExprLocatedError(ctx, f"conflicting types for {func}")
        self._functionManager.enterfunction(func_name, paramInfo)
        
        ctx.temp_stmt().accept(self)
        self._curFunc = None
        self.popBlock(ctx)
        #print("func def done")
    def visitParam_list(self, ctx:ExprParser.Param_listContext):
        self.visitChildren(ctx)
        def f(decl):
            return self._varstack[text(decl.Identifier())]
        return list(map(f, ctx.declaration()))
    def visitFuncDecl(self, ctx:ExprParser.FuncDeclContext):
        #print("in func decl")
        func_name = text(ctx.Identifier())
        self.checkFunc(ctx)
        self._curFunc = func_name
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
        self._curFunc = None
        self.popBlock(ctx)
    def visitIntType(self, ctx:ExprParser.IntTypeContext):
        return IntType()
    def visitPtrType(self, ctx:ExprParser.PtrTypeContext):
        return PtrType(ctx.typ().accept(self))
    
    @SaveType
    def visitTypUnary(self, ctx:ExprParser.TypUnaryContext):
        typ = ctx.typ().accept(self)
        #print(typ)
        ctx.unary().accept(self)
        return typ
    @SaveType
    def visitAtomParen(self, ctx:ExprParser.AtomParenContext):
        return ctx.expression().accept(self)
    @SaveType
    def visitCUnary(self, ctx:ExprParser.CUnaryContext):
        #print(text(ctx.unaryOp()))
        res = self.checkUnary(ctx.unaryOp(), text(ctx.unaryOp()), ctx.unary().accept(self))
        if text(ctx.unaryOp()) == '&':
            self.locate(ctx.unary())
        return res
    #check Binaries
    @SaveType
    def visitAddOpMult(self, ctx:ExprParser.AddOpMultContext):
        #print("addopMult")
        return self.checkBinary(ctx.addOp(), text(ctx.addOp()), 
                ctx.add().accept(self), ctx.mult().accept(self))
    @SaveType
    def visitMultOpUnary(self, ctx:ExprParser.MultOpUnaryContext):
        #print("multopUnary")
        return self.checkBinary(ctx.mulOp(), text(ctx.mulOp()),
                ctx.mult().accept(self), ctx.unary().accept(self))
    @SaveType
    def visitTRelational(self, ctx:ExprParser.TRelationalContext):
        #print("trelational")
        return self.checkBinary(ctx.InEqOp(), text(ctx.InEqOp()),
                ctx.relational().accept(self), ctx.add().accept(self))
    @SaveType
    def visitTEquality(self, ctx:ExprParser.TEqualityContext):
        #print("tequality")
        return self.checkBinary(ctx.EqOp(), text(ctx.EqOp()),
                ctx.equality().accept(self), ctx.relational().accept(self))
    @SaveType
    def visitTLog_or(self, ctx:ExprParser.TLog_orContext):
        #print("tlog_or")
        return self.checkBinary(ctx, '||', ctx.logical_or().accept(self),
                ctx.logical_and().accept(self))
    @SaveType
    def visitTLog_and(self, ctx:ExprParser.TLog_andContext):
        #print("tlog_and")
        return self.checkBinary(ctx, '&&', ctx.logical_and().accept(self),
                ctx.equality().accept(self))
    @SaveType
    def visitTAssign(self, ctx:ExprParser.TAssignContext):
        #print("tassign")
        res = self.checkBinary(ctx.asgnOp(), text(ctx.asgnOp()),
            ctx.unary().accept(self),ctx.expression().accept(self))
        self.locate(ctx.unary())
        return res
    @SaveType
    def visitTCond(self, ctx:ExprParser.TCondContext):
        return condRule(ctx, ctx.logical_or().accept(self), ctx.expression().accept(self),
                ctx.conditional().accept(self))
    @SaveType
    def visitAtomInteger(self, ctx:ExprParser.AtomIntegerContext):
        return IntType()
    @SaveType
    def visitAtomIdentifier(self, ctx:ExprParser.AtomIdentifierContext):
        #print(text(ctx.Identifier()))
        var = self._varstack[text(ctx.Identifier())]
        return self._vartype[var]
    @SaveType
    def visitCPostFix(self, ctx:ExprParser.CPostFixContext):
        argType = self._getargType(ctx.expr_list())
        func = text(ctx.Identifier())
        rule = self.typeInfo.funcs[func].call()
        return rule(ctx, argType)
    @SaveType
    def visitAPostFix(self, ctx:ExprParser.APostFixContext):
        return arrayRule(ctx, ctx.postfix().accept(self), ctx.expression().accept(self))
    
    def visitReturnStmt(self, ctx:ExprParser.ReturnStmtContext):
        expectedType = self.typeInfo.funcs[self._curFunc].retType
        gotType = ctx.expression().accept(self)
        retRule(ctx, expectedType, gotType)
    def visitCondStmt(self, ctx:ExprParser.CondStmtContext):
        self.visitChildren(ctx)
        stmtCondRule(ctx, ctx.expression().accept(self))
    def visitForStmt(self, ctx:ExprParser.ForStmtContext):
        self.newBlock(ctx)
        self.visitChildren(ctx)
        if ctx.cond is not None:
            stmtCondRule(ctx, ctx.cond.accept(self))
        self.popBlock(ctx)
    def visitForDeclStmt(self, ctx:ExprParser.ForDeclStmtContext):
        self.newBlock(ctx)
        self.visitChildren(ctx)
        if ctx.cond is not None:
            stmtCondRule(ctx, ctx.cond.accept(self))
        self.popBlock(ctx)
    def visitWhileStmt(self, ctx:ExprParser.WhileStmtContext):
        self.visitChildren(ctx)
        stmtCondRule(ctx, ctx.expression().accept(self))
    def visitDoStmt(self, ctx:ExprParser.DoStmtContext):
        self.visitChildren(ctx)
        stmtCondRule(ctx, ctx.expression().accept(self))

class Locator(ExprVisitor):
    def __init__(self, typeInfo):
        self.typeInfo = typeInfo
    def locate(self, func:str, ctx, varstack):
        self._varstack = varstack
        self.func = func
        res = ctx.accept(self)
        self.func = None
        return res
    
    def visitAtomIdentifier(self, ctx:ExprParser.AtomIdentifierContext):
        var = self._varstack[text(ctx.Identifier())]
        if var.offset is None:
            return [instr.GlobalAddr(var.ident)]
        else:
            return [instr.FrameAddr(var.offset)]

    def visitCUnary(self, ctx:ExprParser.CUnaryContext):
        op = text(ctx.unaryOp())
        if op == '*':
            return [ctx.unary()]
    def visitAtomParen(self, ctx:ExprParser.AtomParenContext):
        return ctx.expression().accept(self)

    def visitAPostFix(self, ctx:ExprParser.APostFixContext):
        fixupMult = self.typeInfo[ctx.postfix()].basetype.sizeof()
        return [ctx.postfix(), ctx.expression(), instr.Const(fixupMult), 
            instr.Binaries('*'), instr.Binaries('+')]