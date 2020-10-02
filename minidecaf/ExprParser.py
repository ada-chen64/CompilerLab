# Generated from Expr.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("M\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\6\2\30\n\2\r\2\16\2")
        buf.write("\31\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\7\b\66\n\b\f\b\16\b9\13\b\3\t\3\t\3\t\3\t\7\t?\n\t\f")
        buf.write("\t\16\tB\13\t\3\n\3\n\3\n\3\n\3\n\5\nI\n\n\3\13\3\13\3")
        buf.write("\13\2\3\16\f\2\4\6\b\n\f\16\20\22\24\2\4\3\2\b\t\3\2\n")
        buf.write("\13\2F\2\27\3\2\2\2\4\35\3\2\2\2\6%\3\2\2\2\b\'\3\2\2")
        buf.write("\2\n+\3\2\2\2\f-\3\2\2\2\16/\3\2\2\2\20:\3\2\2\2\22H\3")
        buf.write("\2\2\2\24J\3\2\2\2\26\30\5\4\3\2\27\26\3\2\2\2\30\31\3")
        buf.write("\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2\32\33\3\2\2\2\33\34")
        buf.write("\7\2\2\3\34\3\3\2\2\2\35\36\5\6\4\2\36\37\7\20\2\2\37")
        buf.write(" \7\3\2\2 !\7\4\2\2!\"\7\5\2\2\"#\5\b\5\2#$\7\6\2\2$\5")
        buf.write("\3\2\2\2%&\7\16\2\2&\7\3\2\2\2\'(\7\17\2\2()\5\n\6\2)")
        buf.write("*\7\7\2\2*\t\3\2\2\2+,\7\f\2\2,\13\3\2\2\2-.\5\16\b\2")
        buf.write(".\r\3\2\2\2/\60\b\b\1\2\60\61\5\20\t\2\61\67\3\2\2\2\62")
        buf.write("\63\f\4\2\2\63\64\t\2\2\2\64\66\5\20\t\2\65\62\3\2\2\2")
        buf.write("\669\3\2\2\2\67\65\3\2\2\2\678\3\2\2\28\17\3\2\2\29\67")
        buf.write("\3\2\2\2:@\5\22\n\2;<\5\24\13\2<=\5\22\n\2=?\3\2\2\2>")
        buf.write(";\3\2\2\2?B\3\2\2\2@>\3\2\2\2@A\3\2\2\2A\21\3\2\2\2B@")
        buf.write("\3\2\2\2CD\7\3\2\2DE\5\f\7\2EF\7\4\2\2FI\3\2\2\2GI\7\f")
        buf.write("\2\2HC\3\2\2\2HG\3\2\2\2I\23\3\2\2\2JK\t\3\2\2K\25\3\2")
        buf.write("\2\2\6\31\67@H")
        return buf.getvalue()


class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "';'", "'+'", 
                     "'-'", "'*'", "'/'", "<INVALID>", "<INVALID>", "'int'", 
                     "'return'", "<INVALID>", "'.'" ]

    symbolicNames = [ "<INVALID>", "Lparen", "Rparen", "Lbrace", "Rbrace", 
                      "Semicolon", "Add", "Sub", "Mul", "Div", "Integer", 
                      "Whitespace", "Int", "Return", "Identifier", "Error" ]

    RULE_program = 0
    RULE_function = 1
    RULE_typ = 2
    RULE_statement = 3
    RULE_expression = 4
    RULE_expr = 5
    RULE_add = 6
    RULE_mul = 7
    RULE_atom = 8
    RULE_mulOp = 9

    ruleNames =  [ "program", "function", "typ", "statement", "expression", 
                   "expr", "add", "mul", "atom", "mulOp" ]

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
    Integer=10
    Whitespace=11
    Int=12
    Return=13
    Identifier=14
    Error=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
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
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.function()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ExprParser.Int):
                    break

            self.state = 25
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
            self.state = 27
            self.typ()
            self.state = 28
            self.match(ExprParser.Identifier)
            self.state = 29
            self.match(ExprParser.Lparen)
            self.state = 30
            self.match(ExprParser.Rparen)
            self.state = 31
            self.match(ExprParser.Lbrace)
            self.state = 32
            self.statement()
            self.state = 33
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
            self.state = 35
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
            self.state = 37
            self.match(ExprParser.Return)
            self.state = 38
            self.expression()
            self.state = 39
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

        def Integer(self):
            return self.getToken(ExprParser.Integer, 0)

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
            self.state = 41
            self.match(ExprParser.Integer)
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
        self.enterRule(localctx, 10, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
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
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_add, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.mul()
            self._ctx.stop = self._input.LT(-1)
            self.state = 53
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.AddContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add)
                    self.state = 48
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 49
                    localctx.op = self._input.LT(1)
                    _la = self._input.LA(1)
                    if not(_la==ExprParser.Add or _la==ExprParser.Sub):
                        localctx.op = self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 50
                    self.mul() 
                self.state = 55
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

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
        self.enterRule(localctx, 14, self.RULE_mul)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.atom()
            self.state = 62
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 57
                    self.mulOp()
                    self.state = 58
                    self.atom() 
                self.state = 64
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
        self.enterRule(localctx, 16, self.RULE_atom)
        try:
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExprParser.Lparen]:
                localctx = ExprParser.AtomParenContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 65
                self.match(ExprParser.Lparen)
                self.state = 66
                self.expr()
                self.state = 67
                self.match(ExprParser.Rparen)
                pass
            elif token in [ExprParser.Integer]:
                localctx = ExprParser.AtomIntegerContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 69
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
        self.enterRule(localctx, 18, self.RULE_mulOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
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
        self._predicates[6] = self.add_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def add_sempred(self, localctx:AddContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




