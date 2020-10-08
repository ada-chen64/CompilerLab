# Generated from Expr.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#program.
    def enterProgram(self, ctx:ExprParser.ProgramContext):
        pass

    # Exit a parse tree produced by ExprParser#program.
    def exitProgram(self, ctx:ExprParser.ProgramContext):
        pass


    # Enter a parse tree produced by ExprParser#function.
    def enterFunction(self, ctx:ExprParser.FunctionContext):
        pass

    # Exit a parse tree produced by ExprParser#function.
    def exitFunction(self, ctx:ExprParser.FunctionContext):
        pass


    # Enter a parse tree produced by ExprParser#intType.
    def enterIntType(self, ctx:ExprParser.IntTypeContext):
        pass

    # Exit a parse tree produced by ExprParser#intType.
    def exitIntType(self, ctx:ExprParser.IntTypeContext):
        pass


    # Enter a parse tree produced by ExprParser#returnStmt.
    def enterReturnStmt(self, ctx:ExprParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#returnStmt.
    def exitReturnStmt(self, ctx:ExprParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#expression.
    def enterExpression(self, ctx:ExprParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#expression.
    def exitExpression(self, ctx:ExprParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#tUnary.
    def enterTUnary(self, ctx:ExprParser.TUnaryContext):
        pass

    # Exit a parse tree produced by ExprParser#tUnary.
    def exitTUnary(self, ctx:ExprParser.TUnaryContext):
        pass


    # Enter a parse tree produced by ExprParser#cUnary.
    def enterCUnary(self, ctx:ExprParser.CUnaryContext):
        pass

    # Exit a parse tree produced by ExprParser#cUnary.
    def exitCUnary(self, ctx:ExprParser.CUnaryContext):
        pass


    # Enter a parse tree produced by ExprParser#expr.
    def enterExpr(self, ctx:ExprParser.ExprContext):
        pass

    # Exit a parse tree produced by ExprParser#expr.
    def exitExpr(self, ctx:ExprParser.ExprContext):
        pass


    # Enter a parse tree produced by ExprParser#add.
    def enterAdd(self, ctx:ExprParser.AddContext):
        pass

    # Exit a parse tree produced by ExprParser#add.
    def exitAdd(self, ctx:ExprParser.AddContext):
        pass


    # Enter a parse tree produced by ExprParser#mul.
    def enterMul(self, ctx:ExprParser.MulContext):
        pass

    # Exit a parse tree produced by ExprParser#mul.
    def exitMul(self, ctx:ExprParser.MulContext):
        pass


    # Enter a parse tree produced by ExprParser#atomParen.
    def enterAtomParen(self, ctx:ExprParser.AtomParenContext):
        pass

    # Exit a parse tree produced by ExprParser#atomParen.
    def exitAtomParen(self, ctx:ExprParser.AtomParenContext):
        pass


    # Enter a parse tree produced by ExprParser#atomInteger.
    def enterAtomInteger(self, ctx:ExprParser.AtomIntegerContext):
        pass

    # Exit a parse tree produced by ExprParser#atomInteger.
    def exitAtomInteger(self, ctx:ExprParser.AtomIntegerContext):
        pass


    # Enter a parse tree produced by ExprParser#mulOp.
    def enterMulOp(self, ctx:ExprParser.MulOpContext):
        pass

    # Exit a parse tree produced by ExprParser#mulOp.
    def exitMulOp(self, ctx:ExprParser.MulOpContext):
        pass


