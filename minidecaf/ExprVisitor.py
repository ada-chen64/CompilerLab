# Generated from Expr.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#program.
    def visitProgram(self, ctx:ExprParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#function.
    def visitFunction(self, ctx:ExprParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#intType.
    def visitIntType(self, ctx:ExprParser.IntTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#returnStmt.
    def visitReturnStmt(self, ctx:ExprParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expression.
    def visitExpression(self, ctx:ExprParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#addOpMult.
    def visitAddOpMult(self, ctx:ExprParser.AddOpMultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#addMult.
    def visitAddMult(self, ctx:ExprParser.AddMultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#multOpUnary.
    def visitMultOpUnary(self, ctx:ExprParser.MultOpUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#multUnary.
    def visitMultUnary(self, ctx:ExprParser.MultUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#tUnary.
    def visitTUnary(self, ctx:ExprParser.TUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#cUnary.
    def visitCUnary(self, ctx:ExprParser.CUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#atomInteger.
    def visitAtomInteger(self, ctx:ExprParser.AtomIntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#atomParen.
    def visitAtomParen(self, ctx:ExprParser.AtomParenContext):
        return self.visitChildren(ctx)



del ExprParser