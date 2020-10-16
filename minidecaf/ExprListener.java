// Generated from Expr.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ExprParser}.
 */
public interface ExprListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ExprParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(ExprParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(ExprParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#function}.
	 * @param ctx the parse tree
	 */
	void enterFunction(ExprParser.FunctionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#function}.
	 * @param ctx the parse tree
	 */
	void exitFunction(ExprParser.FunctionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code intType}
	 * labeled alternative in {@link ExprParser#typ}.
	 * @param ctx the parse tree
	 */
	void enterIntType(ExprParser.IntTypeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code intType}
	 * labeled alternative in {@link ExprParser#typ}.
	 * @param ctx the parse tree
	 */
	void exitIntType(ExprParser.IntTypeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code returnStmt}
	 * labeled alternative in {@link ExprParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterReturnStmt(ExprParser.ReturnStmtContext ctx);
	/**
	 * Exit a parse tree produced by the {@code returnStmt}
	 * labeled alternative in {@link ExprParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitReturnStmt(ExprParser.ReturnStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(ExprParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(ExprParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code addOpMult}
	 * labeled alternative in {@link ExprParser#add}.
	 * @param ctx the parse tree
	 */
	void enterAddOpMult(ExprParser.AddOpMultContext ctx);
	/**
	 * Exit a parse tree produced by the {@code addOpMult}
	 * labeled alternative in {@link ExprParser#add}.
	 * @param ctx the parse tree
	 */
	void exitAddOpMult(ExprParser.AddOpMultContext ctx);
	/**
	 * Enter a parse tree produced by the {@code addMult}
	 * labeled alternative in {@link ExprParser#add}.
	 * @param ctx the parse tree
	 */
	void enterAddMult(ExprParser.AddMultContext ctx);
	/**
	 * Exit a parse tree produced by the {@code addMult}
	 * labeled alternative in {@link ExprParser#add}.
	 * @param ctx the parse tree
	 */
	void exitAddMult(ExprParser.AddMultContext ctx);
	/**
	 * Enter a parse tree produced by the {@code multOpUnary}
	 * labeled alternative in {@link ExprParser#mult}.
	 * @param ctx the parse tree
	 */
	void enterMultOpUnary(ExprParser.MultOpUnaryContext ctx);
	/**
	 * Exit a parse tree produced by the {@code multOpUnary}
	 * labeled alternative in {@link ExprParser#mult}.
	 * @param ctx the parse tree
	 */
	void exitMultOpUnary(ExprParser.MultOpUnaryContext ctx);
	/**
	 * Enter a parse tree produced by the {@code multUnary}
	 * labeled alternative in {@link ExprParser#mult}.
	 * @param ctx the parse tree
	 */
	void enterMultUnary(ExprParser.MultUnaryContext ctx);
	/**
	 * Exit a parse tree produced by the {@code multUnary}
	 * labeled alternative in {@link ExprParser#mult}.
	 * @param ctx the parse tree
	 */
	void exitMultUnary(ExprParser.MultUnaryContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tUnary}
	 * labeled alternative in {@link ExprParser#unary}.
	 * @param ctx the parse tree
	 */
	void enterTUnary(ExprParser.TUnaryContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tUnary}
	 * labeled alternative in {@link ExprParser#unary}.
	 * @param ctx the parse tree
	 */
	void exitTUnary(ExprParser.TUnaryContext ctx);
	/**
	 * Enter a parse tree produced by the {@code cUnary}
	 * labeled alternative in {@link ExprParser#unary}.
	 * @param ctx the parse tree
	 */
	void enterCUnary(ExprParser.CUnaryContext ctx);
	/**
	 * Exit a parse tree produced by the {@code cUnary}
	 * labeled alternative in {@link ExprParser#unary}.
	 * @param ctx the parse tree
	 */
	void exitCUnary(ExprParser.CUnaryContext ctx);
	/**
	 * Enter a parse tree produced by the {@code atomInteger}
	 * labeled alternative in {@link ExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterAtomInteger(ExprParser.AtomIntegerContext ctx);
	/**
	 * Exit a parse tree produced by the {@code atomInteger}
	 * labeled alternative in {@link ExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitAtomInteger(ExprParser.AtomIntegerContext ctx);
	/**
	 * Enter a parse tree produced by the {@code atomParen}
	 * labeled alternative in {@link ExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void enterAtomParen(ExprParser.AtomParenContext ctx);
	/**
	 * Exit a parse tree produced by the {@code atomParen}
	 * labeled alternative in {@link ExprParser#atom}.
	 * @param ctx the parse tree
	 */
	void exitAtomParen(ExprParser.AtomParenContext ctx);
	/**
	 * Enter a parse tree produced by the {@code cLog_or}
	 * labeled alternative in {@link ExprParser#logical_or}.
	 * @param ctx the parse tree
	 */
	void enterCLog_or(ExprParser.CLog_orContext ctx);
	/**
	 * Exit a parse tree produced by the {@code cLog_or}
	 * labeled alternative in {@link ExprParser#logical_or}.
	 * @param ctx the parse tree
	 */
	void exitCLog_or(ExprParser.CLog_orContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tLog_or}
	 * labeled alternative in {@link ExprParser#logical_or}.
	 * @param ctx the parse tree
	 */
	void enterTLog_or(ExprParser.TLog_orContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tLog_or}
	 * labeled alternative in {@link ExprParser#logical_or}.
	 * @param ctx the parse tree
	 */
	void exitTLog_or(ExprParser.TLog_orContext ctx);
	/**
	 * Enter a parse tree produced by the {@code cLog_and}
	 * labeled alternative in {@link ExprParser#logical_and}.
	 * @param ctx the parse tree
	 */
	void enterCLog_and(ExprParser.CLog_andContext ctx);
	/**
	 * Exit a parse tree produced by the {@code cLog_and}
	 * labeled alternative in {@link ExprParser#logical_and}.
	 * @param ctx the parse tree
	 */
	void exitCLog_and(ExprParser.CLog_andContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tLog_and}
	 * labeled alternative in {@link ExprParser#logical_and}.
	 * @param ctx the parse tree
	 */
	void enterTLog_and(ExprParser.TLog_andContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tLog_and}
	 * labeled alternative in {@link ExprParser#logical_and}.
	 * @param ctx the parse tree
	 */
	void exitTLog_and(ExprParser.TLog_andContext ctx);
	/**
	 * Enter a parse tree produced by the {@code cEquality}
	 * labeled alternative in {@link ExprParser#equality}.
	 * @param ctx the parse tree
	 */
	void enterCEquality(ExprParser.CEqualityContext ctx);
	/**
	 * Exit a parse tree produced by the {@code cEquality}
	 * labeled alternative in {@link ExprParser#equality}.
	 * @param ctx the parse tree
	 */
	void exitCEquality(ExprParser.CEqualityContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tEquality}
	 * labeled alternative in {@link ExprParser#equality}.
	 * @param ctx the parse tree
	 */
	void enterTEquality(ExprParser.TEqualityContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tEquality}
	 * labeled alternative in {@link ExprParser#equality}.
	 * @param ctx the parse tree
	 */
	void exitTEquality(ExprParser.TEqualityContext ctx);
	/**
	 * Enter a parse tree produced by the {@code cRelational}
	 * labeled alternative in {@link ExprParser#relational}.
	 * @param ctx the parse tree
	 */
	void enterCRelational(ExprParser.CRelationalContext ctx);
	/**
	 * Exit a parse tree produced by the {@code cRelational}
	 * labeled alternative in {@link ExprParser#relational}.
	 * @param ctx the parse tree
	 */
	void exitCRelational(ExprParser.CRelationalContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tRelational}
	 * labeled alternative in {@link ExprParser#relational}.
	 * @param ctx the parse tree
	 */
	void enterTRelational(ExprParser.TRelationalContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tRelational}
	 * labeled alternative in {@link ExprParser#relational}.
	 * @param ctx the parse tree
	 */
	void exitTRelational(ExprParser.TRelationalContext ctx);
}