# Generated from Expr.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("W\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\3\2\3\2\3\3\3\3\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n")
        buf.write("\3\13\6\13\67\n\13\r\13\16\138\3\f\3\f\3\r\6\r>\n\r\r")
        buf.write("\r\16\r?\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\20\3\20\7\20Q\n\20\f\20\16\20T\13")
        buf.write("\20\3\21\3\21\2\2\22\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\2\31\r\33\16\35\17\37\20!\21\3\2\6\3")
        buf.write("\2\62;\5\2\13\f\17\17\"\"\5\2C\\aac|\6\2\62;C\\aac|\2")
        buf.write("X\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2")
        buf.write("\2\2\2\37\3\2\2\2\2!\3\2\2\2\3#\3\2\2\2\5%\3\2\2\2\7\'")
        buf.write("\3\2\2\2\t)\3\2\2\2\13+\3\2\2\2\r-\3\2\2\2\17/\3\2\2\2")
        buf.write("\21\61\3\2\2\2\23\63\3\2\2\2\25\66\3\2\2\2\27:\3\2\2\2")
        buf.write("\31=\3\2\2\2\33C\3\2\2\2\35G\3\2\2\2\37N\3\2\2\2!U\3\2")
        buf.write("\2\2#$\7*\2\2$\4\3\2\2\2%&\7+\2\2&\6\3\2\2\2\'(\7}\2\2")
        buf.write("(\b\3\2\2\2)*\7\177\2\2*\n\3\2\2\2+,\7=\2\2,\f\3\2\2\2")
        buf.write("-.\7-\2\2.\16\3\2\2\2/\60\7/\2\2\60\20\3\2\2\2\61\62\7")
        buf.write(",\2\2\62\22\3\2\2\2\63\64\7\61\2\2\64\24\3\2\2\2\65\67")
        buf.write("\t\2\2\2\66\65\3\2\2\2\678\3\2\2\28\66\3\2\2\289\3\2\2")
        buf.write("\29\26\3\2\2\2:;\t\3\2\2;\30\3\2\2\2<>\5\27\f\2=<\3\2")
        buf.write("\2\2>?\3\2\2\2?=\3\2\2\2?@\3\2\2\2@A\3\2\2\2AB\b\r\2\2")
        buf.write("B\32\3\2\2\2CD\7k\2\2DE\7p\2\2EF\7v\2\2F\34\3\2\2\2GH")
        buf.write("\7t\2\2HI\7g\2\2IJ\7v\2\2JK\7w\2\2KL\7t\2\2LM\7p\2\2M")
        buf.write("\36\3\2\2\2NR\t\4\2\2OQ\t\5\2\2PO\3\2\2\2QT\3\2\2\2RP")
        buf.write("\3\2\2\2RS\3\2\2\2S \3\2\2\2TR\3\2\2\2UV\7\60\2\2V\"\3")
        buf.write("\2\2\2\6\28?R\3\b\2\2")
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
    Integer = 10
    Whitespace = 11
    Int = 12
    Return = 13
    Identifier = 14
    Error = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'{'", "'}'", "';'", "'+'", "'-'", "'*'", "'/'", 
            "'int'", "'return'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "Lparen", "Rparen", "Lbrace", "Rbrace", "Semicolon", "Add", 
            "Sub", "Mul", "Div", "Integer", "Whitespace", "Int", "Return", 
            "Identifier", "Error" ]

    ruleNames = [ "Lparen", "Rparen", "Lbrace", "Rbrace", "Semicolon", "Add", 
                  "Sub", "Mul", "Div", "Integer", "WhitespaceChar", "Whitespace", 
                  "Int", "Return", "Identifier", "Error" ]

    grammarFileName = "Expr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


