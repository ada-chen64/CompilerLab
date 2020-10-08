# Generated from Expr.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write("T\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\6\2\32\n\2")
        buf.write("\r\2\16\2\33\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\7\5\7\63\n\7")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\7\t=\n\t\f\t\16\t@\13")
        buf.write("\t\3\n\3\n\3\n\3\n\7\nF\n\n\f\n\16\nI\13\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\5\13P\n\13\3\f\3\f\3\f\2\3\20\r\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\2\5\4\2\t\t\f\r\3\2\b\t\3\2\n\13\2")
        buf.write("M\2\31\3\2\2\2\4\37\3\2\2\2\6\'\3\2\2\2\b)\3\2\2\2\n-")
        buf.write("\3\2\2\2\f\62\3\2\2\2\16\64\3\2\2\2\20\66\3\2\2\2\22A")
        buf.write("\3\2\2\2\24O\3\2\2\2\26Q\3\2\2\2\30\32\5\4\3\2\31\30\3")
        buf.write("\2\2\2\32\33\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34\35")
        buf.write("\3\2\2\2\35\36\7\2\2\3\36\3\3\2\2\2\37 \5\6\4\2 !\7\22")
        buf.write("\2\2!\"\7\3\2\2\"#\7\4\2\2#$\7\5\2\2$%\5\b\5\2%&\7\6\2")
        buf.write("\2&\5\3\2\2\2\'(\7\20\2\2(\7\3\2\2\2)*\7\21\2\2*+\5\n")
        buf.write("\6\2+,\7\7\2\2,\t\3\2\2\2-.\5\f\7\2.\13\3\2\2\2/\63\5")
        buf.write("\24\13\2\60\61\t\2\2\2\61\63\5\f\7\2\62/\3\2\2\2\62\60")
        buf.write("\3\2\2\2\63\r\3\2\2\2\64\65\5\20\t\2\65\17\3\2\2\2\66")
        buf.write("\67\b\t\1\2\678\5\22\n\28>\3\2\2\29:\f\4\2\2:;\t\3\2\2")
        buf.write(";=\5\22\n\2<9\3\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2\2\2?\21")
        buf.write("\3\2\2\2@>\3\2\2\2AG\5\24\13\2BC\5\26\f\2CD\5\24\13\2")
        buf.write("DF\3\2\2\2EB\3\2\2\2FI\3\2\2\2GE\3\2\2\2GH\3\2\2\2H\23")
        buf.write("\3\2\2\2IG\3\2\2\2JK\7\3\2\2KL\5\16\b\2LM\7\4\2\2MP\3")
        buf.write("\2\2\2NP\7\16\2\2OJ\3\2\2\2ON\3\2\2\2P\25\3\2\2\2QR\t")
        buf.write("\4\2\2R\27\3\2\2\2\7\33\62>GO")
        return buf.getvalue()


class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "'+'", 
                     "'-'", "'*'", "'/'", "'!'", "'~'", "<INVALID>", "<INVALID>", 
                     "'int'", "'return'", "<INVALID>", "'.'" ]

    symbolicNames = [ "<INVALID>", "Lparen", "Rparen", "Lbrace", "Rbrace", 
                      "Semicolon", "Add", "Sub", "Mul", "Div", "LNot", "Not", 
                      "Integer", "Whitespace", "Int", "Return", "Identifier", 
                      "Error" ]

    RULE_program = 0
    RULE_function = 1
    RULE_typ = 2
    RULE_statement = 3
    RULE_expression = 4
    RULE_unary = 5
    RULE_expr = 6
    RULE_add = 7
    RULE_mul = 8
    RULE_atom = 9
    RULE_mulOp = 10

    ruleNames =  [ "program", "function", "typ", "statement", "expression", 
                   "unary", "expr", "add", "mul", "atom", "mulOp" ]

    EOF = Token.EOF
    Lparen=1
    Rparen=2
    Lbrace=3
    Rbrace=4
    Semicolon=5
    Add=6
    Sub=7
    Mul=8
    Div=9
    LNot=10
    Not=11
    Integer=12
    Whitespace=13
    Int=14
    Return=15
    Identifier=16
    Error=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExprParser.EOF, 0)

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.FunctionContext)
            else:
                return self.getTypedRuleContext(ExprParser.FunctionContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ExprParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.function()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ExprParser.Int):
                    break

            self.state = 27
            self.match(ExprParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(ExprParser.TypContext,0)


        def Identifier(self):
            return self.getToken(ExprParser.Identifier, 0)

        def Lparen(self):
            return self.getToken(ExprParser.Lparen, 0)

        def Rparen(self):
            return self.getToken(ExprParser.Rparen, 0)

        def Lbrace(self):
            return self.getToken(ExprParser.Lbrace, 0)

        def statement(self):
            return self.getTypedRuleContext(ExprParser.StatementContext,0)


        def Rbrace(self):
            return self.getToken(ExprParser.Rbrace, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = ExprParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.typ()
            self.state = 30
            self.match(ExprParser.Identifier)
            self.state = 31
            self.match(ExprParser.Lparen)
            self.state = 32
            self.match(ExprParser.Rparen)
            self.state = 33
            self.match(ExprParser.Lbrace)
            self.state = 34
            self.statement()
            self.state = 35
            self.match(ExprParser.Rbrace)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_typ

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IntTypeContext(TypContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.TypContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Int(self):
            return self.getToken(ExprParser.Int, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIntType" ):
                listener.enterIntType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIntType" ):
                listener.exitIntType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntType" ):
                return visitor.visitIntType(self)
            else:
                return visitor.visitChildren(self)



    def typ(self):

        localctx = ExprParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_typ)
        try:
            localctx = ExprParser.IntTypeContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(ExprParser.Int)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ReturnStmtContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Return(self):
            return self.getToken(ExprParser.Return, 0)
        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)

        def Semicolon(self):
            return self.getToken(ExprParser.Semicolon, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = ExprParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            localctx = ExprParser.ReturnStmtContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(ExprParser.Return)
            self.state = 40
            self.expression()
            self.state = 41
            self.match(ExprParser.Semicolon)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(ExprParser.UnaryContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ExprParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.unary()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class UnaryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_unary

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TUnaryContext(UnaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.UnaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(ExprParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTUnary" ):
                listener.enterTUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTUnary" ):
                listener.exitTUnary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTUnary" ):
                return visitor.visitTUnary(self)
            else:
                return visitor.visitChildren(self)


    class CUnaryContext(UnaryContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.UnaryContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unary(self):
            return self.getTypedRuleContext(ExprParser.UnaryContext,0)

        def Sub(self):
            return self.getToken(ExprParser.Sub, 0)
        def LNot(self):
            return self.getToken(ExprParser.LNot, 0)
        def Not(self):
            return self.getToken(ExprParser.Not, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCUnary" ):
                listener.enterCUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCUnary" ):
                listener.exitCUnary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCUnary" ):
                return visitor.visitCUnary(self)
            else:
                return visitor.visitChildren(self)



    def unary(self):

        localctx = ExprParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExprParser.Lparen, ExprParser.Integer]:
                localctx = ExprParser.TUnaryContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.atom()
                pass
            elif token in [ExprParser.Sub, ExprParser.LNot, ExprParser.Not]:
                localctx = ExprParser.CUnaryContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.Sub) | (1 << ExprParser.LNot) | (1 << ExprParser.Not))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 47
                self.unary()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def add(self):
            return self.getTypedRuleContext(ExprParser.AddContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = ExprParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.add(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AddContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def mul(self):
            return self.getTypedRuleContext(ExprParser.MulContext,0)


        def add(self):
            return self.getTypedRuleContext(ExprParser.AddContext,0)


        def Add(self):
            return self.getToken(ExprParser.Add, 0)

        def Sub(self):
            return self.getToken(ExprParser.Sub, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_add

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)



    def add(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.AddContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_add, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.mul()
            self._ctx.stop = self._input.LT(-1)
            self.state = 60
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.AddContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add)
                    self.state = 55
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 56
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==ExprParser.Add or _la==ExprParser.Sub):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 57
                    self.mul() 
                self.state = 62
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class MulContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.AtomContext)
            else:
                return self.getTypedRuleContext(ExprParser.AtomContext,i)


        def mulOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.MulOpContext)
            else:
                return self.getTypedRuleContext(ExprParser.MulOpContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_mul

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul" ):
                listener.enterMul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul" ):
                listener.exitMul(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMul" ):
                return visitor.visitMul(self)
            else:
                return visitor.visitChildren(self)




    def mul(self):

        localctx = ExprParser.MulContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_mul)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.atom()
            self.state = 69
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 64
                    self.mulOp()
                    self.state = 65
                    self.atom() 
                self.state = 71
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AtomIntegerContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Integer(self):
            return self.getToken(ExprParser.Integer, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomInteger" ):
                listener.enterAtomInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomInteger" ):
                listener.exitAtomInteger(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomInteger" ):
                return visitor.visitAtomInteger(self)
            else:
                return visitor.visitChildren(self)


    class AtomParenContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def Lparen(self):
            return self.getToken(ExprParser.Lparen, 0)
        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)

        def Rparen(self):
            return self.getToken(ExprParser.Rparen, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomParen" ):
                listener.enterAtomParen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomParen" ):
                listener.exitAtomParen(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomParen" ):
                return visitor.visitAtomParen(self)
            else:
                return visitor.visitChildren(self)



    def atom(self):

        localctx = ExprParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_atom)
        try:
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExprParser.Lparen]:
                localctx = ExprParser.AtomParenContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.match(ExprParser.Lparen)
                self.state = 73
                self.expr()
                self.state = 74
                self.match(ExprParser.Rparen)
                pass
            elif token in [ExprParser.Integer]:
                localctx = ExprParser.AtomIntegerContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 76
                self.match(ExprParser.Integer)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MulOpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Mul(self):
            return self.getToken(ExprParser.Mul, 0)

        def Div(self):
            return self.getToken(ExprParser.Div, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_mulOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulOp" ):
                listener.enterMulOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulOp" ):
                listener.exitMulOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulOp" ):
                return visitor.visitMulOp(self)
            else:
                return visitor.visitChildren(self)




    def mulOp(self):

        localctx = ExprParser.MulOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_mulOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            _la = self._input.LA(1)
            if not(_la==ExprParser.Mul or _la==ExprParser.Div):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.add_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def add_sempred(self, localctx:AddContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




