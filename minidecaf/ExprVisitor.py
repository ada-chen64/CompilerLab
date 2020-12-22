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


    # Visit a parse tree produced by ExprParser#globFunc.
    def visitGlobFunc(self, ctx:ExprParser.GlobFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#globDecl.
    def visitGlobDecl(self, ctx:ExprParser.GlobDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#funcDef.
    def visitFuncDef(self, ctx:ExprParser.FuncDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#funcDecl.
    def visitFuncDecl(self, ctx:ExprParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ptrType.
    def visitPtrType(self, ctx:ExprParser.PtrTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#intType.
    def visitIntType(self, ctx:ExprParser.IntTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#param_list.
    def visitParam_list(self, ctx:ExprParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#temp_stmt.
    def visitTemp_stmt(self, ctx:ExprParser.Temp_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#compound_statement.
    def visitCompound_statement(self, ctx:ExprParser.Compound_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#block_item.
    def visitBlock_item(self, ctx:ExprParser.Block_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#returnStmt.
    def visitReturnStmt(self, ctx:ExprParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#exprStmt.
    def visitExprStmt(self, ctx:ExprParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#condStmt.
    def visitCondStmt(self, ctx:ExprParser.CondStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#cmpdStmt.
    def visitCmpdStmt(self, ctx:ExprParser.CmpdStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#forStmt.
    def visitForStmt(self, ctx:ExprParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#forDeclStmt.
    def visitForDeclStmt(self, ctx:ExprParser.ForDeclStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#whileStmt.
    def visitWhileStmt(self, ctx:ExprParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#doStmt.
    def visitDoStmt(self, ctx:ExprParser.DoStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#breakStmt.
    def visitBreakStmt(self, ctx:ExprParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#contStmt.
    def visitContStmt(self, ctx:ExprParser.ContStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#declaration.
    def visitDeclaration(self, ctx:ExprParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expr_list.
    def visitExpr_list(self, ctx:ExprParser.Expr_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expression.
    def visitExpression(self, ctx:ExprParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#cAssign.
    def visitCAssign(self, ctx:ExprParser.CAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#tAssign.
    def visitTAssign(self, ctx:ExprParser.TAssignContext):
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


    # Visit a parse tree produced by ExprParser#typUnary.
    def visitTypUnary(self, ctx:ExprParser.TypUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#cPostFix.
    def visitCPostFix(self, ctx:ExprParser.CPostFixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#aPostFix.
    def visitAPostFix(self, ctx:ExprParser.APostFixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#tPostFix.
    def visitTPostFix(self, ctx:ExprParser.TPostFixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#atomInteger.
    def visitAtomInteger(self, ctx:ExprParser.AtomIntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#atomParen.
    def visitAtomParen(self, ctx:ExprParser.AtomParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#atomIdentifier.
    def visitAtomIdentifier(self, ctx:ExprParser.AtomIdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#cCond.
    def visitCCond(self, ctx:ExprParser.CCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#tCond.
    def visitTCond(self, ctx:ExprParser.TCondContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#cLog_or.
    def visitCLog_or(self, ctx:ExprParser.CLog_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#tLog_or.
    def visitTLog_or(self, ctx:ExprParser.TLog_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#cLog_and.
    def visitCLog_and(self, ctx:ExprParser.CLog_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#tLog_and.
    def visitTLog_and(self, ctx:ExprParser.TLog_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#cEquality.
    def visitCEquality(self, ctx:ExprParser.CEqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#tEquality.
    def visitTEquality(self, ctx:ExprParser.TEqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#cRelational.
    def visitCRelational(self, ctx:ExprParser.CRelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#tRelational.
    def visitTRelational(self, ctx:ExprParser.TRelationalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#mulOp.
    def visitMulOp(self, ctx:ExprParser.MulOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#unaryOp.
    def visitUnaryOp(self, ctx:ExprParser.UnaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#addOp.
    def visitAddOp(self, ctx:ExprParser.AddOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#asgnOp.
    def visitAsgnOp(self, ctx:ExprParser.AsgnOpContext):
        return self.visitChildren(ctx)



del ExprParser