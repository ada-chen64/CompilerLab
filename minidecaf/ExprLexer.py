# Generated from Expr.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25")
        buf.write("g\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3")
        buf.write("\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3")
        buf.write("\f\3\r\3\r\3\16\3\16\3\17\6\17G\n\17\r\17\16\17H\3\20")
        buf.write("\3\20\3\21\6\21N\n\21\r\21\16\21O\3\21\3\21\3\22\3\22")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\7\24a\n\24\f\24\16\24d\13\24\3\25\3\25\2\2\26\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\2!\21#\22%\23\'\24)\25\3\2\7\5\2\'\',,\61\61")
        buf.write("\3\2\62;\5\2\13\f\17\17\"\"\5\2C\\aac|\6\2\62;C\\aac|")
        buf.write("\2h\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2")
        buf.write("\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23")
        buf.write("\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3")
        buf.write("\2\2\2\2\35\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\3+\3\2\2\2\5-\3\2\2\2\7/\3\2\2\2")
        buf.write("\t\61\3\2\2\2\13\63\3\2\2\2\r\65\3\2\2\2\17\67\3\2\2\2")
        buf.write("\219\3\2\2\2\23;\3\2\2\2\25=\3\2\2\2\27?\3\2\2\2\31A\3")
        buf.write("\2\2\2\33C\3\2\2\2\35F\3\2\2\2\37J\3\2\2\2!M\3\2\2\2#")
        buf.write("S\3\2\2\2%W\3\2\2\2\'^\3\2\2\2)e\3\2\2\2+,\t\2\2\2,\4")
        buf.write("\3\2\2\2-.\7*\2\2.\6\3\2\2\2/\60\7+\2\2\60\b\3\2\2\2\61")
        buf.write("\62\7}\2\2\62\n\3\2\2\2\63\64\7\177\2\2\64\f\3\2\2\2\65")
        buf.write("\66\7=\2\2\66\16\3\2\2\2\678\7-\2\28\20\3\2\2\29:\7/\2")
        buf.write("\2:\22\3\2\2\2;<\7,\2\2<\24\3\2\2\2=>\7\61\2\2>\26\3\2")
        buf.write("\2\2?@\7\'\2\2@\30\3\2\2\2AB\7#\2\2B\32\3\2\2\2CD\7\u0080")
        buf.write("\2\2D\34\3\2\2\2EG\t\3\2\2FE\3\2\2\2GH\3\2\2\2HF\3\2\2")
        buf.write("\2HI\3\2\2\2I\36\3\2\2\2JK\t\4\2\2K \3\2\2\2LN\5\37\20")
        buf.write("\2ML\3\2\2\2NO\3\2\2\2OM\3\2\2\2OP\3\2\2\2PQ\3\2\2\2Q")
        buf.write("R\b\21\2\2R\"\3\2\2\2ST\7k\2\2TU\7p\2\2UV\7v\2\2V$\3\2")
        buf.write("\2\2WX\7t\2\2XY\7g\2\2YZ\7v\2\2Z[\7w\2\2[\\\7t\2\2\\]")
        buf.write("\7p\2\2]&\3\2\2\2^b\t\5\2\2_a\t\6\2\2`_\3\2\2\2ad\3\2")
        buf.write("\2\2b`\3\2\2\2bc\3\2\2\2c(\3\2\2\2db\3\2\2\2ef\7\60\2")
        buf.write("\2f*\3\2\2\2\6\2HOb\3\b\2\2")
        return buf.getvalue()


class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    MulOp = 1
    Lparen = 2
    Rparen = 3
    Lbrace = 4
    Rbrace = 5
    Semicolon = 6
    Add = 7
    Sub = 8
    Mul = 9
    Div = 10
    Mod = 11
    LNot = 12
    Not = 13
    Integer = 14
    Whitespace = 15
    Int = 16
    Return = 17
    Identifier = 18
    Error = 19

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'{'", "'}'", "';'", "'+'", "'-'", "'*'", "'/'", 
            "'%'", "'!'", "'~'", "'int'", "'return'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "MulOp", "Lparen", "Rparen", "Lbrace", "Rbrace", "Semicolon", 
            "Add", "Sub", "Mul", "Div", "Mod", "LNot", "Not", "Integer", 
            "Whitespace", "Int", "Return", "Identifier", "Error" ]

    ruleNames = [ "MulOp", "Lparen", "Rparen", "Lbrace", "Rbrace", "Semicolon", 
                  "Add", "Sub", "Mul", "Div", "Mod", "LNot", "Not", "Integer", 
                  "WhitespaceChar", "Whitespace", "Int", "Return", "Identifier", 
                  "Error" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


