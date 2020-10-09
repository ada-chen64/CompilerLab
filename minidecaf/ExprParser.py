# Generated from Expr.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\25")
        buf.write("N\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\6\2\26\n\2\r\2\16\2\27\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\7\7\62\n\7\f\7\16")
        buf.write("\7\65\13\7\3\b\3\b\3\b\3\b\3\b\3\b\7\b=\n\b\f\b\16\b@")
        buf.write("\13\b\3\t\3\t\3\t\5\tE\n\t\3\n\3\n\3\n\3\n\3\n\5\nL\n")
        buf.write("\n\3\n\2\4\f\16\13\2\4\6\b\n\f\16\20\22\2\4\3\2\t\n\4")
        buf.write("\2\n\n\16\17\2I\2\25\3\2\2\2\4\33\3\2\2\2\6#\3\2\2\2\b")
        buf.write("%\3\2\2\2\n)\3\2\2\2\f+\3\2\2\2\16\66\3\2\2\2\20D\3\2")
        buf.write("\2\2\22K\3\2\2\2\24\26\5\4\3\2\25\24\3\2\2\2\26\27\3\2")
        buf.write("\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\31\3\2\2\2\31\32\7")
        buf.write("\2\2\3\32\3\3\2\2\2\33\34\5\6\4\2\34\35\7\24\2\2\35\36")
        buf.write("\7\4\2\2\36\37\7\5\2\2\37 \7\6\2\2 !\5\b\5\2!\"\7\7\2")
        buf.write("\2\"\5\3\2\2\2#$\7\22\2\2$\7\3\2\2\2%&\7\23\2\2&\'\5\n")
        buf.write("\6\2\'(\7\b\2\2(\t\3\2\2\2)*\5\f\7\2*\13\3\2\2\2+,\b\7")
        buf.write("\1\2,-\5\16\b\2-\63\3\2\2\2./\f\3\2\2/\60\t\2\2\2\60\62")
        buf.write("\5\16\b\2\61.\3\2\2\2\62\65\3\2\2\2\63\61\3\2\2\2\63\64")
        buf.write("\3\2\2\2\64\r\3\2\2\2\65\63\3\2\2\2\66\67\b\b\1\2\678")
        buf.write("\5\20\t\28>\3\2\2\29:\f\3\2\2:;\7\3\2\2;=\5\20\t\2<9\3")
        buf.write("\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2\2\2?\17\3\2\2\2@>\3\2")
        buf.write("\2\2AE\5\22\n\2BC\t\3\2\2CE\5\20\t\2DA\3\2\2\2DB\3\2\2")
        buf.write("\2E\21\3\2\2\2FL\7\20\2\2GH\7\4\2\2HI\5\n\6\2IJ\7\5\2")
        buf.write("\2JL\3\2\2\2KF\3\2\2\2KG\3\2\2\2L\23\3\2\2\2\7\27\63>")
        buf.write("DK")
        return buf.getvalue()


class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'('", "')'", "'{'", "'}'", 
                     "';'", "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'~'", 
                     "<INVALID>", "<INVALID>", "'int'", "'return'", "<INVALID>", 
                     "'.'" ]

    symbolicNames = [ "<INVALID>", "MulOp", "Lparen", "Rparen", "Lbrace", 
                      "Rbrace", "Semicolon", "Add", "Sub", "Mul", "Div", 
                      "Mod", "LNot", "Not", "Integer", "Whitespace", "Int", 
                      "Return", "Identifier", "Error" ]

    RULE_program = 0
    RULE_function = 1
    RULE_typ = 2
    RULE_statement = 3
    RULE_expression = 4
    RULE_add = 5
    RULE_mult = 6
    RULE_unary = 7
    RULE_atom = 8

    ruleNames =  [ "program", "function", "typ", "statement", "expression", 
                   "add", "mult", "unary", "atom" ]

    EOF = Token.EOF
    MulOp=1
    Lparen=2
    Rparen=3
    Lbrace=4
    Rbrace=5
    Semicolon=6
    Add=7
    Sub=8
    Mul=9
    Div=10
    Mod=11
    LNot=12
    Not=13
    Integer=14
    Whitespace=15
    Int=16
    Return=17
    Identifier=18
    Error=19

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
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.function()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ExprParser.Int):
                    break

            self.state = 23
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
            self.state = 25
            self.typ()
            self.state = 26
            self.match(ExprParser.Identifier)
            self.state = 27
            self.match(ExprParser.Lparen)
            self.state = 28
            self.match(ExprParser.Rparen)
            self.state = 29
            self.match(ExprParser.Lbrace)
            self.state = 30
            self.statement()
            self.state = 31
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
            self.state = 33
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
            self.state = 35
            self.match(ExprParser.Return)
            self.state = 36
            self.expression()
            self.state = 37
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

        def add(self):
            return self.getTypedRuleContext(ExprParser.AddContext,0)


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
            self.state = 39
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


        def getRuleIndex(self):
            return ExprParser.RULE_add

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AddOpMultContext(AddContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.AddContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def add(self):
            return self.getTypedRuleContext(ExprParser.AddContext,0)

        def mult(self):
            return self.getTypedRuleContext(ExprParser.MultContext,0)

        def Add(self):
            return self.getToken(ExprParser.Add, 0)
        def Sub(self):
            return self.getToken(ExprParser.Sub, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddOpMult" ):
                listener.enterAddOpMult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddOpMult" ):
                listener.exitAddOpMult(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddOpMult" ):
                return visitor.visitAddOpMult(self)
            else:
                return visitor.visitChildren(self)


    class AddMultContext(AddContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.AddContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def mult(self):
            return self.getTypedRuleContext(ExprParser.MultContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddMult" ):
                listener.enterAddMult(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddMult" ):
                listener.exitAddMult(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddMult" ):
                return visitor.visitAddMult(self)
            else:
                return visitor.visitChildren(self)



    def add(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.AddContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_add, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = ExprParser.AddMultContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 42
            self.mult(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 49
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.AddOpMultContext(self, ExprParser.AddContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_add)
                    self.state = 44
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 45
                    _la = self._input.LA(1)
                    if not(_la==ExprParser.Add or _la==ExprParser.Sub):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 46
                    self.mult(0) 
                self.state = 51
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class MultContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ExprParser.RULE_mult

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MultOpUnaryContext(MultContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.MultContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def mult(self):
            return self.getTypedRuleContext(ExprParser.MultContext,0)

        def unary(self):
            return self.getTypedRuleContext(ExprParser.UnaryContext,0)

        def MulOp(self):
            return self.getToken(ExprParser.MulOp, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultOpUnary" ):
                listener.enterMultOpUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultOpUnary" ):
                listener.exitMultOpUnary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultOpUnary" ):
                return visitor.visitMultOpUnary(self)
            else:
                return visitor.visitChildren(self)


    class MultUnaryContext(MultContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ExprParser.MultContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unary(self):
            return self.getTypedRuleContext(ExprParser.UnaryContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultUnary" ):
                listener.enterMultUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultUnary" ):
                listener.exitMultUnary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultUnary" ):
                return visitor.visitMultUnary(self)
            else:
                return visitor.visitChildren(self)



    def mult(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.MultContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_mult, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = ExprParser.MultUnaryContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 53
            self.unary()
            self._ctx.stop = self._input.LT(-1)
            self.state = 60
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ExprParser.MultOpUnaryContext(self, ExprParser.MultContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_mult)
                    self.state = 55
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")

                    self.state = 56
                    self.match(ExprParser.MulOp)
                    self.state = 57
                    self.unary() 
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
        self.enterRule(localctx, 14, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExprParser.Lparen, ExprParser.Integer]:
                localctx = ExprParser.TUnaryContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.atom()
                pass
            elif token in [ExprParser.Sub, ExprParser.LNot, ExprParser.Not]:
                localctx = ExprParser.CUnaryContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.Sub) | (1 << ExprParser.LNot) | (1 << ExprParser.Not))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 65
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
        def expression(self):
            return self.getTypedRuleContext(ExprParser.ExpressionContext,0)

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
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ExprParser.Integer]:
                localctx = ExprParser.AtomIntegerContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.match(ExprParser.Integer)
                pass
            elif token in [ExprParser.Lparen]:
                localctx = ExprParser.AtomParenContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.match(ExprParser.Lparen)
                self.state = 70
                self.expression()
                self.state = 71
                self.match(ExprParser.Rparen)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.add_sempred
        self._predicates[6] = self.mult_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def add_sempred(self, localctx:AddContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def mult_sempred(self, localctx:MultContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 1)
         




