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


    # Enter a parse tree produced by ExprParser#globFunc.
    def enterGlobFunc(self, ctx:ExprParser.GlobFuncContext):
        pass

    # Exit a parse tree produced by ExprParser#globFunc.
    def exitGlobFunc(self, ctx:ExprParser.GlobFuncContext):
        pass


    # Enter a parse tree produced by ExprParser#globDecl.
    def enterGlobDecl(self, ctx:ExprParser.GlobDeclContext):
        pass

    # Exit a parse tree produced by ExprParser#globDecl.
    def exitGlobDecl(self, ctx:ExprParser.GlobDeclContext):
        pass


    # Enter a parse tree produced by ExprParser#funcDef.
    def enterFuncDef(self, ctx:ExprParser.FuncDefContext):
        pass

    # Exit a parse tree produced by ExprParser#funcDef.
    def exitFuncDef(self, ctx:ExprParser.FuncDefContext):
        pass


    # Enter a parse tree produced by ExprParser#funcDecl.
    def enterFuncDecl(self, ctx:ExprParser.FuncDeclContext):
        pass

    # Exit a parse tree produced by ExprParser#funcDecl.
    def exitFuncDecl(self, ctx:ExprParser.FuncDeclContext):
        pass


    # Enter a parse tree produced by ExprParser#ptrType.
    def enterPtrType(self, ctx:ExprParser.PtrTypeContext):
        pass

    # Exit a parse tree produced by ExprParser#ptrType.
    def exitPtrType(self, ctx:ExprParser.PtrTypeContext):
        pass


    # Enter a parse tree produced by ExprParser#intType.
    def enterIntType(self, ctx:ExprParser.IntTypeContext):
        pass

    # Exit a parse tree produced by ExprParser#intType.
    def exitIntType(self, ctx:ExprParser.IntTypeContext):
        pass


    # Enter a parse tree produced by ExprParser#param_list.
    def enterParam_list(self, ctx:ExprParser.Param_listContext):
        pass

    # Exit a parse tree produced by ExprParser#param_list.
    def exitParam_list(self, ctx:ExprParser.Param_listContext):
        pass


    # Enter a parse tree produced by ExprParser#temp_stmt.
    def enterTemp_stmt(self, ctx:ExprParser.Temp_stmtContext):
        pass

    # Exit a parse tree produced by ExprParser#temp_stmt.
    def exitTemp_stmt(self, ctx:ExprParser.Temp_stmtContext):
        pass


    # Enter a parse tree produced by ExprParser#compound_statement.
    def enterCompound_statement(self, ctx:ExprParser.Compound_statementContext):
        pass

    # Exit a parse tree produced by ExprParser#compound_statement.
    def exitCompound_statement(self, ctx:ExprParser.Compound_statementContext):
        pass


    # Enter a parse tree produced by ExprParser#block_item.
    def enterBlock_item(self, ctx:ExprParser.Block_itemContext):
        pass

    # Exit a parse tree produced by ExprParser#block_item.
    def exitBlock_item(self, ctx:ExprParser.Block_itemContext):
        pass


    # Enter a parse tree produced by ExprParser#returnStmt.
    def enterReturnStmt(self, ctx:ExprParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#returnStmt.
    def exitReturnStmt(self, ctx:ExprParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#exprStmt.
    def enterExprStmt(self, ctx:ExprParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#exprStmt.
    def exitExprStmt(self, ctx:ExprParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#condStmt.
    def enterCondStmt(self, ctx:ExprParser.CondStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#condStmt.
    def exitCondStmt(self, ctx:ExprParser.CondStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#cmpdStmt.
    def enterCmpdStmt(self, ctx:ExprParser.CmpdStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#cmpdStmt.
    def exitCmpdStmt(self, ctx:ExprParser.CmpdStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#forStmt.
    def enterForStmt(self, ctx:ExprParser.ForStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#forStmt.
    def exitForStmt(self, ctx:ExprParser.ForStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#forDeclStmt.
    def enterForDeclStmt(self, ctx:ExprParser.ForDeclStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#forDeclStmt.
    def exitForDeclStmt(self, ctx:ExprParser.ForDeclStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#whileStmt.
    def enterWhileStmt(self, ctx:ExprParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#whileStmt.
    def exitWhileStmt(self, ctx:ExprParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#doStmt.
    def enterDoStmt(self, ctx:ExprParser.DoStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#doStmt.
    def exitDoStmt(self, ctx:ExprParser.DoStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#breakStmt.
    def enterBreakStmt(self, ctx:ExprParser.BreakStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#breakStmt.
    def exitBreakStmt(self, ctx:ExprParser.BreakStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#contStmt.
    def enterContStmt(self, ctx:ExprParser.ContStmtContext):
        pass

    # Exit a parse tree produced by ExprParser#contStmt.
    def exitContStmt(self, ctx:ExprParser.ContStmtContext):
        pass


    # Enter a parse tree produced by ExprParser#declaration.
    def enterDeclaration(self, ctx:ExprParser.DeclarationContext):
        pass

    # Exit a parse tree produced by ExprParser#declaration.
    def exitDeclaration(self, ctx:ExprParser.DeclarationContext):
        pass


    # Enter a parse tree produced by ExprParser#expr_list.
    def enterExpr_list(self, ctx:ExprParser.Expr_listContext):
        pass

    # Exit a parse tree produced by ExprParser#expr_list.
    def exitExpr_list(self, ctx:ExprParser.Expr_listContext):
        pass


    # Enter a parse tree produced by ExprParser#expression.
    def enterExpression(self, ctx:ExprParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#expression.
    def exitExpression(self, ctx:ExprParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#cAssign.
    def enterCAssign(self, ctx:ExprParser.CAssignContext):
        pass

    # Exit a parse tree produced by ExprParser#cAssign.
    def exitCAssign(self, ctx:ExprParser.CAssignContext):
        pass


    # Enter a parse tree produced by ExprParser#tAssign.
    def enterTAssign(self, ctx:ExprParser.TAssignContext):
        pass

    # Exit a parse tree produced by ExprParser#tAssign.
    def exitTAssign(self, ctx:ExprParser.TAssignContext):
        pass


    # Enter a parse tree produced by ExprParser#addOpMult.
    def enterAddOpMult(self, ctx:ExprParser.AddOpMultContext):
        pass

    # Exit a parse tree produced by ExprParser#addOpMult.
    def exitAddOpMult(self, ctx:ExprParser.AddOpMultContext):
        pass


    # Enter a parse tree produced by ExprParser#addMult.
    def enterAddMult(self, ctx:ExprParser.AddMultContext):
        pass

    # Exit a parse tree produced by ExprParser#addMult.
    def exitAddMult(self, ctx:ExprParser.AddMultContext):
        pass


    # Enter a parse tree produced by ExprParser#multOpUnary.
    def enterMultOpUnary(self, ctx:ExprParser.MultOpUnaryContext):
        pass

    # Exit a parse tree produced by ExprParser#multOpUnary.
    def exitMultOpUnary(self, ctx:ExprParser.MultOpUnaryContext):
        pass


    # Enter a parse tree produced by ExprParser#multUnary.
    def enterMultUnary(self, ctx:ExprParser.MultUnaryContext):
        pass

    # Exit a parse tree produced by ExprParser#multUnary.
    def exitMultUnary(self, ctx:ExprParser.MultUnaryContext):
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


    # Enter a parse tree produced by ExprParser#typUnary.
    def enterTypUnary(self, ctx:ExprParser.TypUnaryContext):
        pass

    # Exit a parse tree produced by ExprParser#typUnary.
    def exitTypUnary(self, ctx:ExprParser.TypUnaryContext):
        pass


    # Enter a parse tree produced by ExprParser#tPostFix.
    def enterTPostFix(self, ctx:ExprParser.TPostFixContext):
        pass

    # Exit a parse tree produced by ExprParser#tPostFix.
    def exitTPostFix(self, ctx:ExprParser.TPostFixContext):
        pass


    # Enter a parse tree produced by ExprParser#cPostFix.
    def enterCPostFix(self, ctx:ExprParser.CPostFixContext):
        pass

    # Exit a parse tree produced by ExprParser#cPostFix.
    def exitCPostFix(self, ctx:ExprParser.CPostFixContext):
        pass


    # Enter a parse tree produced by ExprParser#atomInteger.
    def enterAtomInteger(self, ctx:ExprParser.AtomIntegerContext):
        pass

    # Exit a parse tree produced by ExprParser#atomInteger.
    def exitAtomInteger(self, ctx:ExprParser.AtomIntegerContext):
        pass


    # Enter a parse tree produced by ExprParser#atomParen.
    def enterAtomParen(self, ctx:ExprParser.AtomParenContext):
        pass

    # Exit a parse tree produced by ExprParser#atomParen.
    def exitAtomParen(self, ctx:ExprParser.AtomParenContext):
        pass


    # Enter a parse tree produced by ExprParser#atomIdentifier.
    def enterAtomIdentifier(self, ctx:ExprParser.AtomIdentifierContext):
        pass

    # Exit a parse tree produced by ExprParser#atomIdentifier.
    def exitAtomIdentifier(self, ctx:ExprParser.AtomIdentifierContext):
        pass


    # Enter a parse tree produced by ExprParser#cCond.
    def enterCCond(self, ctx:ExprParser.CCondContext):
        pass

    # Exit a parse tree produced by ExprParser#cCond.
    def exitCCond(self, ctx:ExprParser.CCondContext):
        pass


    # Enter a parse tree produced by ExprParser#tCond.
    def enterTCond(self, ctx:ExprParser.TCondContext):
        pass

    # Exit a parse tree produced by ExprParser#tCond.
    def exitTCond(self, ctx:ExprParser.TCondContext):
        pass


    # Enter a parse tree produced by ExprParser#cLog_or.
    def enterCLog_or(self, ctx:ExprParser.CLog_orContext):
        pass

    # Exit a parse tree produced by ExprParser#cLog_or.
    def exitCLog_or(self, ctx:ExprParser.CLog_orContext):
        pass


    # Enter a parse tree produced by ExprParser#tLog_or.
    def enterTLog_or(self, ctx:ExprParser.TLog_orContext):
        pass

    # Exit a parse tree produced by ExprParser#tLog_or.
    def exitTLog_or(self, ctx:ExprParser.TLog_orContext):
        pass


    # Enter a parse tree produced by ExprParser#cLog_and.
    def enterCLog_and(self, ctx:ExprParser.CLog_andContext):
        pass

    # Exit a parse tree produced by ExprParser#cLog_and.
    def exitCLog_and(self, ctx:ExprParser.CLog_andContext):
        pass


    # Enter a parse tree produced by ExprParser#tLog_and.
    def enterTLog_and(self, ctx:ExprParser.TLog_andContext):
        pass

    # Exit a parse tree produced by ExprParser#tLog_and.
    def exitTLog_and(self, ctx:ExprParser.TLog_andContext):
        pass


    # Enter a parse tree produced by ExprParser#cEquality.
    def enterCEquality(self, ctx:ExprParser.CEqualityContext):
        pass

    # Exit a parse tree produced by ExprParser#cEquality.
    def exitCEquality(self, ctx:ExprParser.CEqualityContext):
        pass


    # Enter a parse tree produced by ExprParser#tEquality.
    def enterTEquality(self, ctx:ExprParser.TEqualityContext):
        pass

    # Exit a parse tree produced by ExprParser#tEquality.
    def exitTEquality(self, ctx:ExprParser.TEqualityContext):
        pass


    # Enter a parse tree produced by ExprParser#cRelational.
    def enterCRelational(self, ctx:ExprParser.CRelationalContext):
        pass

    # Exit a parse tree produced by ExprParser#cRelational.
    def exitCRelational(self, ctx:ExprParser.CRelationalContext):
        pass


    # Enter a parse tree produced by ExprParser#tRelational.
    def enterTRelational(self, ctx:ExprParser.TRelationalContext):
        pass

    # Exit a parse tree produced by ExprParser#tRelational.
    def exitTRelational(self, ctx:ExprParser.TRelationalContext):
        pass


    # Enter a parse tree produced by ExprParser#mulOp.
    def enterMulOp(self, ctx:ExprParser.MulOpContext):
        pass

    # Exit a parse tree produced by ExprParser#mulOp.
    def exitMulOp(self, ctx:ExprParser.MulOpContext):
        pass


    # Enter a parse tree produced by ExprParser#unaryOp.
    def enterUnaryOp(self, ctx:ExprParser.UnaryOpContext):
        pass

    # Exit a parse tree produced by ExprParser#unaryOp.
    def exitUnaryOp(self, ctx:ExprParser.UnaryOpContext):
        pass


    # Enter a parse tree produced by ExprParser#addOp.
    def enterAddOp(self, ctx:ExprParser.AddOpContext):
        pass

    # Exit a parse tree produced by ExprParser#addOp.
    def exitAddOp(self, ctx:ExprParser.AddOpContext):
        pass


    # Enter a parse tree produced by ExprParser#asgnOp.
    def enterAsgnOp(self, ctx:ExprParser.AsgnOpContext):
        pass

    # Exit a parse tree produced by ExprParser#asgnOp.
    def exitAsgnOp(self, ctx:ExprParser.AsgnOpContext):
        pass


