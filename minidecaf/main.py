"""实例：真·main"""
import sys
import argparse
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
from .ExprLexer import ExprLexer
from .ExprParser import ExprParser
from .ExprVisitor import ExprVisitor
from .ir import IREmitter
from .ir.irgen import StackIRGen
from .asm import AsmEmitter
from .asm.riscv import RISCVAsmGen as AsmGen
class MyErrorListener(ErrorListener):
        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
                print(str(line) + ":" + str(column) + ": syntax ERROR, " + str(msg))
                print("Terminating Translation")
                sys.exit()

def parseArgs(argv):
    parser = argparse.ArgumentParser(description="MiniDecaf compiler")
    parser.add_argument("infile", type=str,
                       help="the input C file")
    parser.add_argument("outfile", type=str, nargs="?",
                       help="the output assembly file")
    parser.add_argument("-ir", action="store_true", help="emit ir rather than asm")
    return parser.parse_args()

def irGenerator(tree):
        irEmitter = IREmitter()
        StackIRGen(irEmitter).visit(tree)
        return irEmitter.getIR()
def asmGenerator(ir, outfile):
        asmEmitter = AsmEmitter(outfile)
        AsmGen(asmEmitter).gen(ir)
        asm = asmEmitter.getASM()
        asmEmitter.close()
        return asm
def main():
        args = parseArgs(sys.argv)
        input = FileStream(args.infile)
        # input = InputStream(sys.stdin.read())
        lexer = ExprLexer(input)
        tokens = CommonTokenStream(lexer)
        parser = ExprParser(tokens)
        parser._listeners = [MyErrorListener()]
        tree = parser.program()
        #print(tree.toStringTree(recog=parser))
        # print(tree.accept(visitor))
        ir = irGenerator(tree)
        
        asm = asmGenerator(ir, "lmao.txt")
        print(asm)
        # print(ir)
       
        
        
if __name__ == '__main__':
        main()
