# Step 2

陈昱霏 2017080067

## 实验任务

step2 中，我们要给整数常量增加一元运算：取负 `-`、按位取反 `~` 以及逻辑非 `!`。

## 实验步骤

### 修改Expr.g4文件

我在Expr.g4文件中的expression部分做了相应的改变：

```
expression
	: unary
	;
unary
	: atom #tUnary
	| ('-'|'!'|'~') unary #cUnary
atom
	: '(' expr ')' #atomParen
	| Integer #atomInteger
	;
```

利用atlr4从新生成Lexer，Parser，Visitor后，修改ir的生成。

```python
#ir.irgen.py
#StackIRGen(ExprVisitor)

def visitCUnary(self, ctx:ExprParser.UnaryContext):
    self.visitChildren(ctx) #先遍历子函数
    if(ctx.Not()): #如果符号是 '~'
        self._E(instr.Not())
    if(ctx.Sub()): #如果符号是 '-'
        self._E(instr.Neg())
    if(ctx.LNot()): #如果符号是 '!'
        self._E(instr.LNOT())
       
# ir.instr.py
#生成IR命令
class Neg(IRInstr):
    def __str__(self):
        return f"neg"
class Not(IRInstr):
    def __str__(self):
        return f"not"
class LNOT(IRInstr):
    def __str__(self):
        return f"lnot"
       
```

然后更改asm，加上三个汇编指令，该部分借鉴了参考代码：

```python
#asm.riscv.py

@Instrs
def NOT(reg):
    return pop(reg) + [f"not {reg}, {reg}"] + push(reg)
@Instrs
def neg(reg):
    return pop(reg) + [f"neg {reg}, {reg}"] + push(reg)
@Instrs
def LNot(reg)
	return pop(reg) + [f"seqz {reg}, {reg}"] + push(reg)
```

## 思考题

1. 我们在语义规范中规定整数运算越界是未定义行为，运算越界可以简单理解成理论上的运算结果没有办法保存在32位整数的空间中，必须截断高于32位的内容。请设计一个表达式，只使用`-~!`这三个单目运算符和 $[0, 2^{31} - 1]$ 范围内的非负整数，使得运算过程中发生越界。

   -~0x7FFFFFFF

   因为对0x7FFFFFFF取反可得0x80000000也就是−2,147,483,648，C++里的最小值，但是对该值取负，得到的数还是0x80000000。要取2,147,483,648的话，就超出了32位数。