// Generated from Expr.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link ExprParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface ExprVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link ExprParser#program}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProgram(ExprParser.ProgramContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExprParser#function}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunction(ExprParser.FunctionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code intType}
	 * labeled alternative in {@link ExprParser#typ}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIntType(ExprParser.IntTypeContext ctx);
	/**
	 * Visit a parse tree produced by the {@code returnStmt}
	 * labeled alternative in {@link ExprParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReturnStmt(ExprParser.ReturnStmtContext ctx);
	/**
	 * Visit a parse tree produced by {@link ExprParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression(ExprParser.ExpressionContext ctx);
	/**
	 * Visit a parse tree produced by the {@code addOpMult}
	 * labeled alternative in {@link ExprParser#add}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAddOpMult(ExprParser.AddOpMultContext ctx);
	/**
	 * Visit a parse tree produced by the {@code addMult}
	 * labeled alternative in {@link ExprParser#add}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAddMult(ExprParser.AddMultContext ctx);
	/**
	 * Visit a parse tree produced by the {@code multOpUnary}
	 * labeled alternative in {@link ExprParser#mult}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMultOpUnary(ExprParser.MultOpUnaryContext ctx);
	/**
	 * Visit a parse tree produced by the {@code multUnary}
	 * labeled alternative in {@link ExprParser#mult}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMultUnary(ExprParser.MultUnaryContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tUnary}
	 * labeled alternative in {@link ExprParser#unary}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTUnary(ExprParser.TUnaryContext ctx);
	/**
	 * Visit a parse tree produced by the {@code cUnary}
	 * labeled alternative in {@link ExprParser#unary}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCUnary(ExprParser.CUnaryContext ctx);
	/**
	 * Visit a parse tree produced by the {@code atomInteger}
	 * labeled alternative in {@link ExprParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAtomInteger(ExprParser.AtomIntegerContext ctx);
	/**
	 * Visit a parse tree produced by the {@code atomParen}
	 * labeled alternative in {@link ExprParser#atom}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAtomParen(ExprParser.AtomParenContext ctx);
	/**
	 * Visit a parse tree produced by the {@code cLog_or}
	 * labeled alternative in {@link ExprParser#logical_or}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCLog_or(ExprParser.CLog_orContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tLog_or}
	 * labeled alternative in {@link ExprParser#logical_or}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTLog_or(ExprParser.TLog_orContext ctx);
	/**
	 * Visit a parse tree produced by the {@code cLog_and}
	 * labeled alternative in {@link ExprParser#logical_and}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCLog_and(ExprParser.CLog_andContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tLog_and}
	 * labeled alternative in {@link ExprParser#logical_and}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTLog_and(ExprParser.TLog_andContext ctx);
	/**
	 * Visit a parse tree produced by the {@code cEquality}
	 * labeled alternative in {@link ExprParser#equality}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCEquality(ExprParser.CEqualityContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tEquality}
	 * labeled alternative in {@link ExprParser#equality}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTEquality(ExprParser.TEqualityContext ctx);
	/**
	 * Visit a parse tree produced by the {@code cRelational}
	 * labeled alternative in {@link ExprParser#relational}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCRelational(ExprParser.CRelationalContext ctx);
	/**
	 * Visit a parse tree produced by the {@code tRelational}
	 * labeled alternative in {@link ExprParser#relational}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTRelational(ExprParser.TRelationalContext ctx);
}