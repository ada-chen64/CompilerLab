# Step3

陈昱霏 2017080067

## 实验任务

增加的是：加 `+`、减 `-`、乘 `*`、整除 `/`、模 `%` 以及括号 `(` `)`。

## 实验实现

修改Expr.g4文件

```
...
expression:
	:add
	;
add
	: mult #addMult
	| add ('+' | '-') mult #addOpMult
	;
mult
	: unary #multUnary
	| mult (MulOp) unary #multOpUnary
	;
...
MulOp
	: '*' | '/' | '%';

```

其实本来想把加法符号也归并为一个AddOp的终结符集合，但是因为'-'在一元运算里也有用到，这样做会导致一元运算出错，所以我就将加和减分开处理。在下面的代码里可以看到加减法和乘除法的不同处理。

在代码中添加对加减乘除的处理：

```python
#ir.irgen.py
def visitAddOpMult(self, ctx:ExprParser.AddOpMultContext):
    self.visitChildren(ctx) #先访问优先级最高的地方
    if(ctx.Add()):
        op = text(ctx.Add()) #如果是加法
    if(ctx.Sub()):
        op = text(ctx.Sub()) #如果是减法
    self._E(instr.Binaries(op))
def visitMultOpUnary(self, ctx:ExprParser.MultOpUnaryContext):
    self.visitChildren(ctx)
    op = text(ctx.MulOp()) #提取乘除法的符号
    self._E(instr.Binaries(op))
```

由于二元运算的步骤其实都一样，就是汇编里的其中一行指令不一样，所以对其做统一处理更方便。上一步做一元运算的时候我就发现自己对每个指令做分开处理非常浪费时间也增加了不必要的代码行数。所以这次我将加减乘除指令统一成class Binaries，其中保存它的运算符：

```python
#ir.instr.py
class Binaries(IRInstr):
    def __init__(self, op:str):
        self.op = op
   	def __str__(self):
        return binsymbols[self.op] #我在utils.py里加了一个dictionary，将运算符和对应的指令保存起来
```

最后生成汇编的代码中，我借鉴了参考代码里的flatten函数，更尬了我的pop和push来处理多个寄存器。

```python
#utils.py
#flatten函数是将多个list连成一个
def flatten(l):
    newlist = []
    for i in l:
        if type(i) is list:
            newlist += flatten(i)
        else:
            newlist += [i]
     return newlist
#asm.riscv.py
#pop和push的修改如下
def _pop(reg):
    if reg is None:
        return [f"addi sp, sp, 8"]
    return [f"lw {reg}, 0(sp)"] +[f"addi sp, sp, 8"]
def pop(*regs):
    return flatten(map(_pop, regs))
def _push(val):
    if type(val) is int:
        return [f"addi sp, sp, -8", f"li t1, {val}", f"sw t1, 0(sp)"]
    else:
        return [f"addi sp, sp -8", f"sw {val}, 0(sp)"]
def push(*vals):
    return flatten(map(_push, vals))

#下面是对二元运算生成汇编
@Instrs
def binary(op):
    inst = binsymbols[op] #获取指令
    return pop("t1", "t2") + [f"{inst} t1, t2, t1"] + push("t1") #先从栈里获得之前压进去的两个数，存到t1 t2寄存器中，对这两个寄存器做加减乘除，保存至t1，将结果从新压入栈中

```

## 思考题

1. 请给出将寄存器 `t0` 中的数值压入栈中所需的 riscv 汇编指令序列；请给出将栈顶的数值弹出到寄存器 `t0` 中所需的 riscv 汇编指令序列。

   ```assembly
   addi sp, sp, -8
   sw t0, 0(sp) #store word （压入栈中）
   lw t0, 0(sp) #load word （将栈顶弹出存入t0）
   addi sp, sp, 8
   ```

   

2. 语义规范中规定“除以零、模零都是未定义行为”，但是即使除法的右操作数不是 0，仍然可能存在未定义行为。请问这时除法的左操作数和右操作数分别是什么？请将这时除法的左操作数和右操作数填入下面的代码中，分别在你的电脑（请标明你的电脑的架构，比如 x86-64 或 ARM）中和 RISCV-32 的 qemu 模拟器中编译运行下面的代码，并给出运行结果。（编译时请不要开启任何编译优化）

   ```c++
   #include <stdio.h>
   
   int main() {
     int a = -2147483648;
     int b = -1;
     printf("%d\n", a / b);
     return 0;
   }
   ```

   我的电脑是windows x86-64，我在命令行里用g++跑该程序没有结果，不会输出任何东西。在Visual Studio里编译会编译出错。

   在我的qemu模拟器中，我把代码放入test.c，并执行下面的指令：

   ```
   $ riscv64-unknown-elf-gcc -march=rv32im -mabi=ilp32 -O3 test.c
   $ qemu-riscv32 a.out
   -2147483648
   ```

   

