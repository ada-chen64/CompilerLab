# Step1 

计73 陈昱霏 2017080067

# 任务

1. 在不同输入上，运行 minilexer, miniparser 和 minivisitor。
   已完成
   
2. 浏览它们的代码（不用完全看懂）
   已完成
   
3. 在实验报告中回答思考题。

4. **如果你选择使用工具**：按照你选择工具所需的格式，编写 step1 的 MiniDecaf 词法语法（可参考本章规范），以利用该工具进行解析。然后，从 AST 生成汇编。
这一步我先参考了minidecaf-tutorial的Expr.g4文件，学习了词法语法的编写格式，然后参考了本章的规范编写了能够处理函数的词法语法。
   
   ```
   grammar Expr;
import ExprLex;
   program
   	: function+ EOF
   	;
   function
   	: typ Identifier Lparen Rparen Lbrac statement Rbrace
   	;
   typ
   	: Int #intType
   	;
   statement
   	: Return expression Semicolon #returnStmt
   	;
   expression 
   	: Integer
   	;
   ```
   
   为了检测`syntaxError`，我在`main.py`里加了一个`MyErrorListener`。
   
5. （可选，推荐）改进你上一步的代码，先生成 IR，再从 IR 生成汇编

   IR和汇编的生成我用了minidecaf的参考代码，将`MiniDecafVisitor`改为我自己的`ExprVisitor`。本来是想自己写一个IR生成`class`的，但是在研究参考代码过程中发现参考代码的`IREmitter`和`ASMEmitter`的写法非常天才，所以最后决定用参考代码来为我的便一起的生成IR和ASM功能打底。对于以后的实验再自己对IR 和ASM的生成器进行修改和调试。我对参考点asm代码加了一个`getASM()`函数，将`asmGenerator`的形式改成和`irGenerator`一样，返回生成好的汇编，而不是在生成过程中打印。

# 思考题

1. 修改 minilexer 的输入（`lexer.setInput` 的参数），使得 lex 报错，给出一个简短的例子。

   唯一让lex报错的方法就是当前检测的token的action是"error"。所以将第一个输入设为TokenKind为"Error"的"."。

   ```Python
   lexer.setInput("""\
   	. int main() {
   		return 123;
   	}
   	""")
   ```

   

2. 修改 minilexer 的输入，使得 lex 不报错但 parse 报错，给出一个简短的例子。
   因为parse函数里预期的第一个终结符是Int，所以如果将int改成一个Integer的话就会导致parse报错。

   ```python
   lexer.setInput("""\
   	0 main() {
   		return 123;
   	}
   	""")
   ```

   

3. 在 riscv 中，哪个寄存器是用来存储函数返回值的？
   在riscv中x10-11寄存器是用来储存返回值的。