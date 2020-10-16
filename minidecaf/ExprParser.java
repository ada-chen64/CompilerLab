// Generated from Expr.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class ExprParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		MulOp=1, EqOp=2, InEqOp=3, Lparen=4, Rparen=5, Lbrace=6, Rbrace=7, Semicolon=8, 
		Add=9, Sub=10, Mul=11, Div=12, Mod=13, LNot=14, Not=15, LOr=16, Land=17, 
		Integer=18, Whitespace=19, Int=20, Return=21, Identifier=22, Error=23;
	public static final int
		RULE_program = 0, RULE_function = 1, RULE_typ = 2, RULE_statement = 3, 
		RULE_expression = 4, RULE_add = 5, RULE_mult = 6, RULE_unary = 7, RULE_atom = 8, 
		RULE_logical_or = 9, RULE_logical_and = 10, RULE_equality = 11, RULE_relational = 12;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "function", "typ", "statement", "expression", "add", "mult", 
			"unary", "atom", "logical_or", "logical_and", "equality", "relational"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, null, null, "'('", "')'", "'{'", "'}'", "';'", "'+'", "'-'", 
			"'*'", "'/'", "'%'", "'!'", "'~'", "'||'", "'&&'", null, null, "'int'", 
			"'return'", null, "'.'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "MulOp", "EqOp", "InEqOp", "Lparen", "Rparen", "Lbrace", "Rbrace", 
			"Semicolon", "Add", "Sub", "Mul", "Div", "Mod", "LNot", "Not", "LOr", 
			"Land", "Integer", "Whitespace", "Int", "Return", "Identifier", "Error"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Expr.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ExprParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(ExprParser.EOF, 0); }
		public List<FunctionContext> function() {
			return getRuleContexts(FunctionContext.class);
		}
		public FunctionContext function(int i) {
			return getRuleContext(FunctionContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).enterProgram(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).exitProgram(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExprVisitor ) return ((ExprVisitor<? extends T>)visitor).visitProgram(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(27); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(26);
				function();
				}
				}
				setState(29); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==Int );
			setState(31);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionContext extends ParserRuleContext {
		public TypContext typ() {
			return getRuleContext(TypContext.class,0);
		}
		public TerminalNode Identifier() { return getToken(ExprParser.Identifier, 0); }
		public TerminalNode Lparen() { return getToken(ExprParser.Lparen, 0); }
		public TerminalNode Rparen() { return getToken(ExprParser.Rparen, 0); }
		public TerminalNode Lbrace() { return getToken(ExprParser.Lbrace, 0); }
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public TerminalNode Rbrace() { return getToken(ExprParser.Rbrace, 0); }
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).enterFunction(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).exitFunction(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExprVisitor ) return ((ExprVisitor<? extends T>)visitor).visitFunction(this);
			else return visitor.visitChildren(this);
		}
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_function);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(33);
			typ();
			setState(34);
			match(Identifier);
			setState(35);
			match(Lparen);
			setState(36);
			match(Rparen);
			setState(37);
			match(Lbrace);
			setState(38);
			statement();
			setState(39);
			match(Rbrace);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypContext extends ParserRuleContext {
		public TypContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typ; }
	 
		public TypContext() { }
		public void copyFrom(TypContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class IntTypeContext extends TypContext {
		public TerminalNode Int() { return getToken(ExprParser.Int, 0); }
		public IntTypeContext(TypContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).enterIntType(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).exitIntType(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExprVisitor ) return ((ExprVisitor<? extends T>)visitor).visitIntType(this);
			else return visitor.visitChildren(this);
		}
	}

	public final TypContext typ() throws RecognitionException {
		TypContext _localctx = new TypContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_typ);
		try {
			_localctx = new IntTypeContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(41);
			match(Int);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	 
		public StatementContext() { }
		public void copyFrom(StatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class ReturnStmtContext extends StatementContext {
		public TerminalNode Return() { return getToken(ExprParser.Return, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode Semicolon() { return getToken(ExprParser.Semicolon, 0); }
		public ReturnStmtContext(StatementContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).enterReturnStmt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).exitReturnStmt(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExprVisitor ) return ((ExprVisitor<? extends T>)visitor).visitReturnStmt(this);
			else return visitor.visitChildren(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_statement);
		try {
			_localctx = new ReturnStmtContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(43);
			match(Return);
			setState(44);
			expression();
			setState(45);
			match(Semicolon);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public Logical_orContext logical_or() {
			return getRuleContext(Logical_orContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).enterExpression(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).exitExpression(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExprVisitor ) return ((ExprVisitor<? extends T>)visitor).visitExpression(this);
			else return visitor.visitChildren(this);
		}
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(47);
			logical_or(0);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AddContext extends ParserRuleContext {
		public AddContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_add; }
	 
		public AddContext() { }
		public void copyFrom(AddContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class AddOpMultContext extends AddContext {
		public AddContext add() {
			return getRuleContext(AddContext.class,0);
		}
		public MultContext mult() {
			return getRuleContext(MultContext.class,0);
		}
		public TerminalNode Add() { return getToken(ExprParser.Add, 0); }
		public TerminalNode Sub() { return getToken(ExprParser.Sub, 0); }
		public AddOpMultContext(AddContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).enterAddOpMult(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).exitAddOpMult(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExprVisitor ) return ((ExprVisitor<? extends T>)visitor).visitAddOpMult(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class AddMultContext extends AddContext {
		public MultContext mult() {
			return getRuleContext(MultContext.class,0);
		}
		public AddMultContext(AddContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).enterAddMult(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).exitAddMult(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExprVisitor ) return ((ExprVisitor<? extends T>)visitor).visitAddMult(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AddContext add() throws RecognitionException {
		return add(0);
	}

	private AddContext add(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		AddContext _localctx = new AddContext(_ctx, _parentState);
		AddContext _prevctx = _localctx;
		int _startState = 10;
		enterRecursionRule(_localctx, 10, RULE_add, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			_localctx = new AddMultContext(_localctx);
			_ctx = _localctx;
			_prevctx = _localctx;

			setState(50);
			mult(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(57);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new AddOpMultContext(new AddContext(_parentctx, _parentState));
					pushNewRecursionContext(_localctx, _startState, RULE_add);
					setState(52);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(53);
					_la = _input.LA(1);
					if ( !(_la==Add || _la==Sub) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(54);
					mult(0);
					}
					} 
				}
				setState(59);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,1,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class MultContext extends ParserRuleContext {
		public MultContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mult; }
	 
		public MultContext() { }
		public void copyFrom(MultContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class MultOpUnaryContext extends MultContext {
		public MultContext mult() {
			return getRuleContext(MultContext.class,0);
		}
		public UnaryContext unary() {
			return getRuleContext(UnaryContext.class,0);
		}
		public TerminalNode MulOp() { return getToken(ExprParser.MulOp, 0); }
		public MultOpUnaryContext(MultContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).enterMultOpUnary(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).exitMultOpUnary(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExprVisitor ) return ((ExprVisitor<? extends T>)visitor).visitMultOpUnary(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class MultUnaryContext extends MultContext {
		public UnaryContext unary() {
			return getRuleContext(UnaryContext.class,0);
		}
		public MultUnaryContext(MultContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).enterMultUnary(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).exitMultUnary(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExprVisitor ) return ((ExprVisitor<? extends T>)visitor).visitMultUnary(this);
			else return visitor.visitChildren(this);
		}
	}

	public final MultContext mult() throws RecognitionException {
		return mult(0);
	}

	private MultContext mult(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		MultContext _localctx = new MultContext(_ctx, _parentState);
		MultContext _prevctx = _localctx;
		int _startState = 12;
		enterRecursionRule(_localctx, 12, RULE_mult, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			_localctx = new MultUnaryContext(_localctx);
			_ctx = _localctx;
			_prevctx = _localctx;

			setState(61);
			unary();
			}
			_ctx.stop = _input.LT(-1);
			setState(68);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new MultOpUnaryContext(new MultContext(_parentctx, _parentState));
					pushNewRecursionContext(_localctx, _startState, RULE_mult);
					setState(63);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					{
					setState(64);
					match(MulOp);
					}
					setState(65);
					unary();
					}
					} 
				}
				setState(70);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class UnaryContext extends ParserRuleContext {
		public UnaryContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unary; }
	 
		public UnaryContext() { }
		public void copyFrom(UnaryContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class TUnaryContext extends UnaryContext {
		public AtomContext atom() {
			return getRuleContext(AtomContext.class,0);
		}
		public TUnaryContext(UnaryContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).enterTUnary(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).exitTUnary(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExprVisitor ) return ((ExprVisitor<? extends T>)visitor).visitTUnary(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class CUnaryContext extends UnaryContext {
		public UnaryContext unary() {
			return getRuleContext(UnaryContext.class,0);
		}
		public TerminalNode Sub() { return getToken(ExprParser.Sub, 0); }
		public TerminalNode LNot() { return getToken(ExprParser.LNot, 0); }
		public TerminalNode Not() { return getToken(ExprParser.Not, 0); }
		public CUnaryContext(UnaryContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).enterCUnary(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).exitCUnary(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExprVisitor ) return ((ExprVisitor<? extends T>)visitor).visitCUnary(this);
			else return visitor.visitChildren(this);
		}
	}

	public final UnaryContext unary() throws RecognitionException {
		UnaryContext _localctx = new UnaryContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_unary);
		int _la;
		try {
			setState(74);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Lparen:
			case Integer:
				_localctx = new TUnaryContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(71);
				atom();
				}
				break;
			case Sub:
			case LNot:
			case Not:
				_localctx = new CUnaryContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(72);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << Sub) | (1L << LNot) | (1L << Not))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(73);
				unary();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AtomContext extends ParserRuleContext {
		public AtomContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atom; }
	 
		public AtomContext() { }
		public void copyFrom(AtomContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class AtomIntegerContext extends AtomContext {
		public TerminalNode Integer() { return getToken(ExprParser.Integer, 0); }
		public AtomIntegerContext(AtomContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).enterAtomInteger(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).exitAtomInteger(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExprVisitor ) return ((ExprVisitor<? extends T>)visitor).visitAtomInteger(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class AtomParenContext extends AtomContext {
		public TerminalNode Lparen() { return getToken(ExprParser.Lparen, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode Rparen() { return getToken(ExprParser.Rparen, 0); }
		public AtomParenContext(AtomContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).enterAtomParen(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).exitAtomParen(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExprVisitor ) return ((ExprVisitor<? extends T>)visitor).visitAtomParen(this);
			else return visitor.visitChildren(this);
		}
	}

	public final AtomContext atom() throws RecognitionException {
		AtomContext _localctx = new AtomContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_atom);
		try {
			setState(81);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case Integer:
				_localctx = new AtomIntegerContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(76);
				match(Integer);
				}
				break;
			case Lparen:
				_localctx = new AtomParenContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(77);
				match(Lparen);
				setState(78);
				expression();
				setState(79);
				match(Rparen);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Logical_orContext extends ParserRuleContext {
		public Logical_orContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logical_or; }
	 
		public Logical_orContext() { }
		public void copyFrom(Logical_orContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class CLog_orContext extends Logical_orContext {
		public Logical_andContext logical_and() {
			return getRuleContext(Logical_andContext.class,0);
		}
		public CLog_orContext(Logical_orContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).enterCLog_or(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).exitCLog_or(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExprVisitor ) return ((ExprVisitor<? extends T>)visitor).visitCLog_or(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class TLog_orContext extends Logical_orContext {
		public Logical_orContext logical_or() {
			return getRuleContext(Logical_orContext.class,0);
		}
		public TerminalNode LOr() { return getToken(ExprParser.LOr, 0); }
		public Logical_andContext logical_and() {
			return getRuleContext(Logical_andContext.class,0);
		}
		public TLog_orContext(Logical_orContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).enterTLog_or(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).exitTLog_or(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExprVisitor ) return ((ExprVisitor<? extends T>)visitor).visitTLog_or(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Logical_orContext logical_or() throws RecognitionException {
		return logical_or(0);
	}

	private Logical_orContext logical_or(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Logical_orContext _localctx = new Logical_orContext(_ctx, _parentState);
		Logical_orContext _prevctx = _localctx;
		int _startState = 18;
		enterRecursionRule(_localctx, 18, RULE_logical_or, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			_localctx = new CLog_orContext(_localctx);
			_ctx = _localctx;
			_prevctx = _localctx;

			setState(84);
			logical_and(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(91);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new TLog_orContext(new Logical_orContext(_parentctx, _parentState));
					pushNewRecursionContext(_localctx, _startState, RULE_logical_or);
					setState(86);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(87);
					match(LOr);
					setState(88);
					logical_and(0);
					}
					} 
				}
				setState(93);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Logical_andContext extends ParserRuleContext {
		public Logical_andContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logical_and; }
	 
		public Logical_andContext() { }
		public void copyFrom(Logical_andContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class CLog_andContext extends Logical_andContext {
		public EqualityContext equality() {
			return getRuleContext(EqualityContext.class,0);
		}
		public CLog_andContext(Logical_andContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).enterCLog_and(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).exitCLog_and(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExprVisitor ) return ((ExprVisitor<? extends T>)visitor).visitCLog_and(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class TLog_andContext extends Logical_andContext {
		public Logical_andContext logical_and() {
			return getRuleContext(Logical_andContext.class,0);
		}
		public TerminalNode Land() { return getToken(ExprParser.Land, 0); }
		public EqualityContext equality() {
			return getRuleContext(EqualityContext.class,0);
		}
		public TLog_andContext(Logical_andContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).enterTLog_and(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).exitTLog_and(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExprVisitor ) return ((ExprVisitor<? extends T>)visitor).visitTLog_and(this);
			else return visitor.visitChildren(this);
		}
	}

	public final Logical_andContext logical_and() throws RecognitionException {
		return logical_and(0);
	}

	private Logical_andContext logical_and(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Logical_andContext _localctx = new Logical_andContext(_ctx, _parentState);
		Logical_andContext _prevctx = _localctx;
		int _startState = 20;
		enterRecursionRule(_localctx, 20, RULE_logical_and, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			_localctx = new CLog_andContext(_localctx);
			_ctx = _localctx;
			_prevctx = _localctx;

			setState(95);
			equality(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(102);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new TLog_andContext(new Logical_andContext(_parentctx, _parentState));
					pushNewRecursionContext(_localctx, _startState, RULE_logical_and);
					setState(97);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					setState(98);
					match(Land);
					setState(99);
					equality(0);
					}
					} 
				}
				setState(104);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class EqualityContext extends ParserRuleContext {
		public EqualityContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_equality; }
	 
		public EqualityContext() { }
		public void copyFrom(EqualityContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class CEqualityContext extends EqualityContext {
		public RelationalContext relational() {
			return getRuleContext(RelationalContext.class,0);
		}
		public CEqualityContext(EqualityContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).enterCEquality(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).exitCEquality(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExprVisitor ) return ((ExprVisitor<? extends T>)visitor).visitCEquality(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class TEqualityContext extends EqualityContext {
		public EqualityContext equality() {
			return getRuleContext(EqualityContext.class,0);
		}
		public RelationalContext relational() {
			return getRuleContext(RelationalContext.class,0);
		}
		public TerminalNode EqOp() { return getToken(ExprParser.EqOp, 0); }
		public TEqualityContext(EqualityContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).enterTEquality(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).exitTEquality(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExprVisitor ) return ((ExprVisitor<? extends T>)visitor).visitTEquality(this);
			else return visitor.visitChildren(this);
		}
	}

	public final EqualityContext equality() throws RecognitionException {
		return equality(0);
	}

	private EqualityContext equality(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		EqualityContext _localctx = new EqualityContext(_ctx, _parentState);
		EqualityContext _prevctx = _localctx;
		int _startState = 22;
		enterRecursionRule(_localctx, 22, RULE_equality, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			_localctx = new CEqualityContext(_localctx);
			_ctx = _localctx;
			_prevctx = _localctx;

			setState(106);
			relational(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(113);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new TEqualityContext(new EqualityContext(_parentctx, _parentState));
					pushNewRecursionContext(_localctx, _startState, RULE_equality);
					setState(108);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					{
					setState(109);
					match(EqOp);
					}
					setState(110);
					relational(0);
					}
					} 
				}
				setState(115);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class RelationalContext extends ParserRuleContext {
		public RelationalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relational; }
	 
		public RelationalContext() { }
		public void copyFrom(RelationalContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class CRelationalContext extends RelationalContext {
		public AddContext add() {
			return getRuleContext(AddContext.class,0);
		}
		public CRelationalContext(RelationalContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).enterCRelational(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).exitCRelational(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExprVisitor ) return ((ExprVisitor<? extends T>)visitor).visitCRelational(this);
			else return visitor.visitChildren(this);
		}
	}
	public static class TRelationalContext extends RelationalContext {
		public RelationalContext relational() {
			return getRuleContext(RelationalContext.class,0);
		}
		public AddContext add() {
			return getRuleContext(AddContext.class,0);
		}
		public TerminalNode InEqOp() { return getToken(ExprParser.InEqOp, 0); }
		public TRelationalContext(RelationalContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).enterTRelational(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof ExprListener ) ((ExprListener)listener).exitTRelational(this);
		}
		@Override
		public <T> T accept(ParseTreeVisitor<? extends T> visitor) {
			if ( visitor instanceof ExprVisitor ) return ((ExprVisitor<? extends T>)visitor).visitTRelational(this);
			else return visitor.visitChildren(this);
		}
	}

	public final RelationalContext relational() throws RecognitionException {
		return relational(0);
	}

	private RelationalContext relational(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		RelationalContext _localctx = new RelationalContext(_ctx, _parentState);
		RelationalContext _prevctx = _localctx;
		int _startState = 24;
		enterRecursionRule(_localctx, 24, RULE_relational, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			_localctx = new CRelationalContext(_localctx);
			_ctx = _localctx;
			_prevctx = _localctx;

			setState(117);
			add(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(124);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new TRelationalContext(new RelationalContext(_parentctx, _parentState));
					pushNewRecursionContext(_localctx, _startState, RULE_relational);
					setState(119);
					if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
					{
					setState(120);
					match(InEqOp);
					}
					setState(121);
					add(0);
					}
					} 
				}
				setState(126);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,8,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 5:
			return add_sempred((AddContext)_localctx, predIndex);
		case 6:
			return mult_sempred((MultContext)_localctx, predIndex);
		case 9:
			return logical_or_sempred((Logical_orContext)_localctx, predIndex);
		case 10:
			return logical_and_sempred((Logical_andContext)_localctx, predIndex);
		case 11:
			return equality_sempred((EqualityContext)_localctx, predIndex);
		case 12:
			return relational_sempred((RelationalContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean add_sempred(AddContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean mult_sempred(MultContext _localctx, int predIndex) {
		switch (predIndex) {
		case 1:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean logical_or_sempred(Logical_orContext _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean logical_and_sempred(Logical_andContext _localctx, int predIndex) {
		switch (predIndex) {
		case 3:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean equality_sempred(EqualityContext _localctx, int predIndex) {
		switch (predIndex) {
		case 4:
			return precpred(_ctx, 1);
		}
		return true;
	}
	private boolean relational_sempred(RelationalContext _localctx, int predIndex) {
		switch (predIndex) {
		case 5:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\31\u0082\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\3\2\6\2\36\n\2\r\2\16\2\37\3\2\3\2\3\3"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3"+
		"\7\3\7\3\7\3\7\7\7:\n\7\f\7\16\7=\13\7\3\b\3\b\3\b\3\b\3\b\3\b\7\bE\n"+
		"\b\f\b\16\bH\13\b\3\t\3\t\3\t\5\tM\n\t\3\n\3\n\3\n\3\n\3\n\5\nT\n\n\3"+
		"\13\3\13\3\13\3\13\3\13\3\13\7\13\\\n\13\f\13\16\13_\13\13\3\f\3\f\3\f"+
		"\3\f\3\f\3\f\7\fg\n\f\f\f\16\fj\13\f\3\r\3\r\3\r\3\r\3\r\3\r\7\rr\n\r"+
		"\f\r\16\ru\13\r\3\16\3\16\3\16\3\16\3\16\3\16\7\16}\n\16\f\16\16\16\u0080"+
		"\13\16\3\16\2\b\f\16\24\26\30\32\17\2\4\6\b\n\f\16\20\22\24\26\30\32\2"+
		"\4\3\2\13\f\4\2\f\f\20\21\2}\2\35\3\2\2\2\4#\3\2\2\2\6+\3\2\2\2\b-\3\2"+
		"\2\2\n\61\3\2\2\2\f\63\3\2\2\2\16>\3\2\2\2\20L\3\2\2\2\22S\3\2\2\2\24"+
		"U\3\2\2\2\26`\3\2\2\2\30k\3\2\2\2\32v\3\2\2\2\34\36\5\4\3\2\35\34\3\2"+
		"\2\2\36\37\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 !\3\2\2\2!\"\7\2\2\3\"\3"+
		"\3\2\2\2#$\5\6\4\2$%\7\30\2\2%&\7\6\2\2&\'\7\7\2\2\'(\7\b\2\2()\5\b\5"+
		"\2)*\7\t\2\2*\5\3\2\2\2+,\7\26\2\2,\7\3\2\2\2-.\7\27\2\2./\5\n\6\2/\60"+
		"\7\n\2\2\60\t\3\2\2\2\61\62\5\24\13\2\62\13\3\2\2\2\63\64\b\7\1\2\64\65"+
		"\5\16\b\2\65;\3\2\2\2\66\67\f\3\2\2\678\t\2\2\28:\5\16\b\29\66\3\2\2\2"+
		":=\3\2\2\2;9\3\2\2\2;<\3\2\2\2<\r\3\2\2\2=;\3\2\2\2>?\b\b\1\2?@\5\20\t"+
		"\2@F\3\2\2\2AB\f\3\2\2BC\7\3\2\2CE\5\20\t\2DA\3\2\2\2EH\3\2\2\2FD\3\2"+
		"\2\2FG\3\2\2\2G\17\3\2\2\2HF\3\2\2\2IM\5\22\n\2JK\t\3\2\2KM\5\20\t\2L"+
		"I\3\2\2\2LJ\3\2\2\2M\21\3\2\2\2NT\7\24\2\2OP\7\6\2\2PQ\5\n\6\2QR\7\7\2"+
		"\2RT\3\2\2\2SN\3\2\2\2SO\3\2\2\2T\23\3\2\2\2UV\b\13\1\2VW\5\26\f\2W]\3"+
		"\2\2\2XY\f\3\2\2YZ\7\22\2\2Z\\\5\26\f\2[X\3\2\2\2\\_\3\2\2\2][\3\2\2\2"+
		"]^\3\2\2\2^\25\3\2\2\2_]\3\2\2\2`a\b\f\1\2ab\5\30\r\2bh\3\2\2\2cd\f\3"+
		"\2\2de\7\23\2\2eg\5\30\r\2fc\3\2\2\2gj\3\2\2\2hf\3\2\2\2hi\3\2\2\2i\27"+
		"\3\2\2\2jh\3\2\2\2kl\b\r\1\2lm\5\32\16\2ms\3\2\2\2no\f\3\2\2op\7\4\2\2"+
		"pr\5\32\16\2qn\3\2\2\2ru\3\2\2\2sq\3\2\2\2st\3\2\2\2t\31\3\2\2\2us\3\2"+
		"\2\2vw\b\16\1\2wx\5\f\7\2x~\3\2\2\2yz\f\3\2\2z{\7\5\2\2{}\5\f\7\2|y\3"+
		"\2\2\2}\u0080\3\2\2\2~|\3\2\2\2~\177\3\2\2\2\177\33\3\2\2\2\u0080~\3\2"+
		"\2\2\13\37;FLS]hs~";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}