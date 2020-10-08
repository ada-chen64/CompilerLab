# Generated from Expr.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\23")
        buf.write("_\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3")
        buf.write("\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3\r\6\r?\n\r\r\r")
        buf.write("\16\r@\3\16\3\16\3\17\6\17F\n\17\r\17\16\17G\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\22\3\22\7\22Y\n\22\f\22\16\22\\\13\22\3\23\3\23\2\2")
        buf.write("\24\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\2\35\17\37\20!\21#\22%\23\3\2\6\3\2\62;\5\2")
        buf.write("\13\f\17\17\"\"\5\2C\\aac|\6\2\62;C\\aac|\2`\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\3\'\3\2\2\2\5")
        buf.write(")\3\2\2\2\7+\3\2\2\2\t-\3\2\2\2\13/\3\2\2\2\r\61\3\2\2")
        buf.write("\2\17\63\3\2\2\2\21\65\3\2\2\2\23\67\3\2\2\2\259\3\2\2")
        buf.write("\2\27;\3\2\2\2\31>\3\2\2\2\33B\3\2\2\2\35E\3\2\2\2\37")
        buf.write("K\3\2\2\2!O\3\2\2\2#V\3\2\2\2%]\3\2\2\2\'(\7*\2\2(\4\3")
        buf.write("\2\2\2)*\7+\2\2*\6\3\2\2\2+,\7}\2\2,\b\3\2\2\2-.\7\177")
        buf.write("\2\2.\n\3\2\2\2/\60\7=\2\2\60\f\3\2\2\2\61\62\7-\2\2\62")
        buf.write("\16\3\2\2\2\63\64\7/\2\2\64\20\3\2\2\2\65\66\7,\2\2\66")
        buf.write("\22\3\2\2\2\678\7\61\2\28\24\3\2\2\29:\7#\2\2:\26\3\2")
        buf.write("\2\2;<\7\u0080\2\2<\30\3\2\2\2=?\t\2\2\2>=\3\2\2\2?@\3")
        buf.write("\2\2\2@>\3\2\2\2@A\3\2\2\2A\32\3\2\2\2BC\t\3\2\2C\34\3")
        buf.write("\2\2\2DF\5\33\16\2ED\3\2\2\2FG\3\2\2\2GE\3\2\2\2GH\3\2")
        buf.write("\2\2HI\3\2\2\2IJ\b\17\2\2J\36\3\2\2\2KL\7k\2\2LM\7p\2")
        buf.write("\2MN\7v\2\2N \3\2\2\2OP\7t\2\2PQ\7g\2\2QR\7v\2\2RS\7w")
        buf.write("\2\2ST\7t\2\2TU\7p\2\2U\"\3\2\2\2VZ\t\4\2\2WY\t\5\2\2")
        buf.write("XW\3\2\2\2Y\\\3\2\2\2ZX\3\2\2\2Z[\3\2\2\2[$\3\2\2\2\\")
        buf.write("Z\3\2\2\2]^\7\60\2\2^&\3\2\2\2\6\2@GZ\3\b\2\2")
        return buf.getvalue()


class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    Lparen = 1
    Rparen = 2
    Lbrace = 3
    Rbrace = 4
    Semicolon = 5
    Add = 6
    Sub = 7
    Mul = 8
    Div = 9
    LNot = 10
    Not = 11
    Integer = 12
    Whitespace = 13
    Int = 14
    Return = 15
    Identifier = 16
    Error = 17

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'{'", "'}'", "';'", "'+'", "'-'", "'*'", "'/'", 
            "'!'", "'~'", "'int'", "'return'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "Lparen", "Rparen", "Lbrace", "Rbrace", "Semicolon", "Add", 
            "Sub", "Mul", "Div", "LNot", "Not", "Integer", "Whitespace", 
            "Int", "Return", "Identifier", "Error" ]

    ruleNames = [ "Lparen", "Rparen", "Lbrace", "Rbrace", "Semicolon", "Add", 
                  "Sub", "Mul", "Div", "LNot", "Not", "Integer", "WhitespaceChar", 
                  "Whitespace", "Int", "Return", "Identifier", "Error" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


