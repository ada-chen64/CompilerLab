# Step 6

陈昱霏 2017080067

## 实验任务

们要支持 if 语句和条件表达式（又称三元/三目表达式，ternary expression）。

语法改动：

```
function
    : type Identifier '(' ')' '{' block_item* '}'

block_item
    : statement
    | declaration
statement
    : 'return' expression ';'
    | expression? ';'
    | 'if' '(' expression ')' c_if=statement ('else' c_el=statement)?
assignment
    : conditional
    | Identifier '=' expression
conditional
    : logical_or
    | logical_or '?' expression ':' conditional

```

## 实验实现

由minidecaf-tutorial指示，我们需要做跳转和标号，所以首先要在IR里加上这两类指令。其`Branch`指令包含`beqz`, `bnez`, 和`br`。

```python
class Branch(IRInstr):
    def __init__(self, op:str, label:str):
        assert op in branchOp
        self.op = op
        self.label = label
    def __str__(self):
        return f"{self.op}"
class Label(IRInstr):
    def __init__(self, label:str):
        self.label = label
    def __str__(self):
        return f"label {self.label}"
```

有了这两类指令，就要进行从parse tree到IR的处理。我们先理一下逻辑：

对于`if (log_expr1) stmt1 else smt2`，我们先要计算`log_expr1`，然后对其进行判断。如果`log_expr1`的结果为0，则不成立，直接跳转到`else`，但是如果没有`else`的话，则直接跳转出`if`语句。

因此，处理代码如下：

```python
def visitCondStmt(self, ctx: ExprParser.CondStmtContext):
    ctx.expression().accept(self) #先计算log_expr1
    #生成label
    exit_label = self._labelCounter.addLabel("end_Label")
    else_label = self._labelCounter.addLabel("else_Label")
    if ctx.c_el() is not None: 
        #如果存在else则判断log_expr1是否为0，若为0，跳转至else_label
        self._E(instr.Branch("beqz", else_label))
        #没有跳转的情况下要对stmt1做处理
        ctx.c_if().accept(self) #c_if代表case if
        #stmt1处理完了不能执行else，所以要跳转至exit_label
        self._E(instr.Branch("br", exit_label))
        #最后嘉善exit_label 和stmt2的处理
        self._E(instr.Label(else_label))
        ctx.c_el().accept(self)
        #exit_label 放到最后
        self._E(instr.Label(exit_label))
def visitTCond(self, ctx:ExprParser.TCondContext):
    # logical_or '?' expr ':' conditional
    #如果logical_or=0，跳转到conditional，否则执行expression
    ctx.logical_or().accept(self)
    self._labelCounter.addLabel("end_Label")
    else_label = self._labelCounter.addLabel("else_Label")
    self._E(instr.Branch("beqz", else_label))
  	ctx.expression().accept(self)
    self._E(instr.Branch("br", exit_label))
    self._E(instr.Label(else_label))
    ctx.conditional().accept(self)
    #exit_label 放到最后
    self._E(instr.Label(exit_label))
```

汇编生成

| IR              | 汇编                                             | 意思                                                         |
| --------------- | ------------------------------------------------ | ------------------------------------------------------------ |
| label LABEL_STR | LABEL_STR:                                       | 直接生成Label，用的是command.py里的`AsmLabel`                |
| br LABEL_STR    | j LABEL_STR                                      | 直接跳转至LABEL_STR                                          |
| beqz LABEL_STR  | lw t1, 0(sp); addi sp, sp, 8; beqz t1, LABEL_STR | 从栈中pop掉最上面的，也就是`if`中的逻辑运算结果，然后执行beqz |
| bnez LABEL_STR  | lw t1, 0(sp); addi sp, sp, 8; bnez t1, LABEL_STR | 从栈中pop掉最上面的，也就是`if`中的逻辑运算结果，然后执行bnez |

## 思考题

1. Rust 和 Go 语言中的 if-else 语法与 C 语言中略有不同，它们都要求两个分支必须用大括号包裹起来，而且条件表达式不需要用括号包裹起来：

   ```Go
   if 条件表达式 {
     // 在条件为 true 时执行
   } else {
     // 在条件为 false 时执行
   }
   ```

   请问相比 C 的语法，这两种语言的语法有什么优点？

   用大括号将分支包裹寄来会完全解决c++里的悬吊问题。因为有语法的规定，不需要人为规定parser该怎么parse。