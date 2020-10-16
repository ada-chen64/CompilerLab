# Step 4

陈昱霏 2017080067

## 实验任务

比较和逻辑表达式

比较大小和相等的二元操作：`<`、`<=`、`>=`, `>`, `==`, `!=` 和逻辑与 `&&`、逻辑或 `||`

```
expression
     : logical_or

 logical_or
     : logical_and #cLog_or
     | logical_or '||' logical_and #tLog_or

 logical_and
     : equality #cLog_and
     | logical_and '&&' equality #tLog_and
 equality
     : relational #c
     | equality ('=='|'!=') relational

 relational
     : additive
     | relational ('<'|'>'|'<='|'>=') additive
```

## 实验实现

更改Expr.g4文件后，从新生成parser，lexer，visitor。并且修改以下的文件，添加比较操作和逻辑运算的处理生成IR。

```python
#instr.py
class Equalities(IRInstr):
    def __init__(self, op:str):
        self.op = op
    def __str__(self):
        return eqsymbols[self.op]
class Relational(IRInstr):
    def __init__(self, op:str):
        self.op = op
    def __str__(self):
        return relatesymbols[self.op]
class Logical(IRInstr):
    def __init__(self, op:str):
        self.op = op
    def __str__(self):
        return logicsymbols[self.op]

#irgen.py
def visitTLog_or(self, ctx:ExprParser.TLog_orContext):
    self.visitChildren(ctx)
    op = text(ctx.LOr())
    self._E(instr.Logical(op))
#剩下的运算处理和上面的函数一样

```

汇编的生成方法如下：

| IR   | 汇编                                                         | 含义                                                 |
| ---- | ------------------------------------------------------------ | ---------------------------------------------------- |
| eq   | pop("t1", "t2")  seqz t1, t2, t1  push("t1")                 | 弹出栈顶两个元素，如果相等，压入1，否则压入0         |
| ne   | pop("t1", "t2")  snez t1, t2, t1  push("t1")                 | 弹出栈顶两个元素，如果相等，压入0，否则压入1         |
| le   | pop("t1", "t2") sgt t1, t2, t1 push("t1") pop ("t1") seqz t1, t1 push("t1") | <= 和 !>是一样的，所以先实现是否大于，在非一下该结果 |
| ge   | pop("t1", "t2") slt t1, t2, t1 push("t1") pop ("t1") seqz t1, t1 push("t1") | <= 和 !<是一样的，所以先实现是否小于，在非一下该结果 |
| lt   | pop("t1", "t2") slt t1, t2, t1 push("t1")                    | 弹出栈顶两个元素，如果t2小于t1压入1，否则压入0       |
| gt   | pop("t1", "t2") sgt t1, t2, t1 push("t1")                    | 弹出栈顶两个元素，如果t2大于于t1压入1，否则压入0     |
| land | pop("t1","t2") snez t1, t1 snez t2, t2 and t1, t2, t1 push("t1") | 弹出栈顶两个元素，将其逻辑或与入栈                   |
| lor  | pop("t1","t2") or t1, t2, t1 snez t1, t1  push("t1")         | 弹出栈顶两个元素，将其逻辑或压入栈                   |

## 思考题

1. 在表达式计算时，对于某一步运算，是否一定要先计算出所有的操作数的结果才能进行运算？
   是的

2. 在 MiniDecaf 中，我们对于短路求值未做要求，但在包括 C 语言的大多数流行的语言中，短路求值都是被支持的。为何这一特性广受欢迎？你认为短路求值这一特性会给程序员带来怎样的好处？
   这种特性受欢迎是因为快。比如下面的一段代码：

   ```c++
   if (a == b || c == d || e == f) {
       // Do something
   }
   ```

   如果`a==b`满足了，那就不用再检查`c==d`或者`e==f`，直接进入大括号里的代码。这样会在执行代码时省略一些运行时间。