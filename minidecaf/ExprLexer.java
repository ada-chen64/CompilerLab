// Generated from Expr.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class ExprLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		MulOp=1, EqOp=2, InEqOp=3, Lparen=4, Rparen=5, Lbrace=6, Rbrace=7, Semicolon=8, 
		Add=9, Sub=10, Mul=11, Div=12, Mod=13, LNot=14, Not=15, LOr=16, Land=17, 
		Integer=18, Whitespace=19, Int=20, Return=21, Identifier=22, Error=23;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"MulOp", "EqOp", "InEqOp", "Lparen", "Rparen", "Lbrace", "Rbrace", "Semicolon", 
			"Add", "Sub", "Mul", "Div", "Mod", "LNot", "Not", "LOr", "Land", "Integer", 
			"WhitespaceChar", "Whitespace", "Int", "Return", "Identifier", "Error"
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


	public ExprLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Expr.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\31\u0082\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31"+
		"\t\31\3\2\3\2\3\3\3\3\3\3\3\3\5\3:\n\3\3\4\3\4\3\4\3\4\3\4\5\4A\n\4\3"+
		"\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3"+
		"\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\22\3\23\6"+
		"\23b\n\23\r\23\16\23c\3\24\3\24\3\25\6\25i\n\25\r\25\16\25j\3\25\3\25"+
		"\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\7\30"+
		"|\n\30\f\30\16\30\177\13\30\3\31\3\31\2\2\32\3\3\5\4\7\5\t\6\13\7\r\b"+
		"\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\2)\25"+
		"+\26-\27/\30\61\31\3\2\b\5\2\'\',,\61\61\4\2>>@@\3\2\62;\5\2\13\f\17\17"+
		"\"\"\5\2C\\aac|\6\2\62;C\\aac|\2\u0086\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2"+
		"\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2"+
		"\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3"+
		"\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2)\3\2\2\2\2+\3\2"+
		"\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\3\63\3\2\2\2\59\3\2\2\2\7@\3\2"+
		"\2\2\tB\3\2\2\2\13D\3\2\2\2\rF\3\2\2\2\17H\3\2\2\2\21J\3\2\2\2\23L\3\2"+
		"\2\2\25N\3\2\2\2\27P\3\2\2\2\31R\3\2\2\2\33T\3\2\2\2\35V\3\2\2\2\37X\3"+
		"\2\2\2!Z\3\2\2\2#]\3\2\2\2%a\3\2\2\2\'e\3\2\2\2)h\3\2\2\2+n\3\2\2\2-r"+
		"\3\2\2\2/y\3\2\2\2\61\u0080\3\2\2\2\63\64\t\2\2\2\64\4\3\2\2\2\65\66\7"+
		"?\2\2\66:\7?\2\2\678\7#\2\28:\7?\2\29\65\3\2\2\29\67\3\2\2\2:\6\3\2\2"+
		"\2;A\t\3\2\2<=\7>\2\2=A\7?\2\2>?\7@\2\2?A\7?\2\2@;\3\2\2\2@<\3\2\2\2@"+
		">\3\2\2\2A\b\3\2\2\2BC\7*\2\2C\n\3\2\2\2DE\7+\2\2E\f\3\2\2\2FG\7}\2\2"+
		"G\16\3\2\2\2HI\7\177\2\2I\20\3\2\2\2JK\7=\2\2K\22\3\2\2\2LM\7-\2\2M\24"+
		"\3\2\2\2NO\7/\2\2O\26\3\2\2\2PQ\7,\2\2Q\30\3\2\2\2RS\7\61\2\2S\32\3\2"+
		"\2\2TU\7\'\2\2U\34\3\2\2\2VW\7#\2\2W\36\3\2\2\2XY\7\u0080\2\2Y \3\2\2"+
		"\2Z[\7~\2\2[\\\7~\2\2\\\"\3\2\2\2]^\7(\2\2^_\7(\2\2_$\3\2\2\2`b\t\4\2"+
		"\2a`\3\2\2\2bc\3\2\2\2ca\3\2\2\2cd\3\2\2\2d&\3\2\2\2ef\t\5\2\2f(\3\2\2"+
		"\2gi\5\'\24\2hg\3\2\2\2ij\3\2\2\2jh\3\2\2\2jk\3\2\2\2kl\3\2\2\2lm\b\25"+
		"\2\2m*\3\2\2\2no\7k\2\2op\7p\2\2pq\7v\2\2q,\3\2\2\2rs\7t\2\2st\7g\2\2"+
		"tu\7v\2\2uv\7w\2\2vw\7t\2\2wx\7p\2\2x.\3\2\2\2y}\t\6\2\2z|\t\7\2\2{z\3"+
		"\2\2\2|\177\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\60\3\2\2\2\177}\3\2\2\2\u0080"+
		"\u0081\7\60\2\2\u0081\62\3\2\2\2\b\29@cj}\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}