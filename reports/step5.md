# Step 5

陈昱霏 2017080067

## 实验任务

局部变量和赋值

```
function
    : typ Identifier '(' ')' '{' statement* '}'
	;
statement
    : Return expression ';' #returnStmt
    | expression? ';' #exprStmt
    | declaration	#delcarStmt
	;
declaration
    : typ Identifier ('=' expression)? ';' 
	;
expression
    : assignment
	;
assignment
    : logical_or #cAssign
    | Identifier '=' expression #tAssign
    ;
atom
    : Integer #atomInteger
    | '(' expression ')' #atomParen
    | Identifier #atomIdentifier
```

## 实验实现

该实验要增加栈帧布局，所以在要先为IR指令添加一下的指令：

```python
#ir.instr.py
class FrameAddr(IRInstr):
    def __init__(self, fpOffset:int):
        assert fpOffset<0
        self.offset = fpOffset
    def __str__(self):
        return f"frameaddr {self.offset}"
class Load(IRInstr):
    def __str__(self):
        return f"load"
class Store(IRInstr):
    def __str(self):
        return f"store"
class Pop(IRInstr):
    def __str__(self)：
    	return f"pop"
```

然后对新加的语法进行处理来生成以上的IR。由minidecaf-tutorial中的实验指导得知：

- 遇到读取变量`atom: Identifier`的时候，查符号表确定变量是第几个，然后生成`frameaddr`和`load`。

  - 如果查不到同名变量，应当报错：变量未定义

- 遇到变量赋值的时候，先生成等号右手边的 IR，同上对等号左手边查符号表，生成`frameaddr`和`store`。

  > 注意赋值表达式是有值的，执行完它的 IR 后栈顶还保留着赋值表达式的值。这就是为什么 `store` 只弹栈一次。

- 遇到表达式语句时，生成完表达式的 IR 以后记得再生成一个 `pop`，保证栈帧要满足的第 1. 条性质

- 遇到声明时，除了记录新变量，还要初始化变量。

  > 为了计算 prologue 中分配栈帧的大小，IR 除了一个指令列表，还要包含一个信息：局部变量的个数。

- `main` 有多条语句了，它的 IR 是其中语句的 IR 顺序拼接。

首先在生成IR的时候同时要在栈中加上符号表。我在StackIRGen中直接加上一个`self._offtable` 和 `self._top` 来分别记录符号表和栈顶的offset。

```python
#ir.irgen.py
class StackIRGen(ExprVisitor):
    def __init__(self, emitter:IREmitter):
        self._E = emitter
        self._offtable = {}
        self._top = 0
    def addVar(self, var:None):
        assert var not in self._offtable #确认变量不存在
        self._top -= INT_SIZE 
        if var is not None:
            self._offtable[var] = self._top
        return self._top
#...
def visitDeclaration(self, ctx:ExprParser.DeclarationContext):
    var = text(ctx.Identifier())
    if ctx.expression() is not None: #如果有赋值的话
        ctx.expression().accept(self)
    else:
        self._E(instr.Const(0)) #没有赋值就赋值为0
    self.addVar(var) #把新变量加到符号表
def visitAtomIdentifier(self, ctx:ExprParser.AtomIdentifierContext):
    var = text(ctx.Idetifier())
    off = self._offtable[var]
    self._E(instr.FrameAddr(off)) #frameaddr offset
    self._E(instr.Load()) #load
def visitTAssign(self, ctx:ExprParser.TAssignContext):
    self.visitChildren(ctx)
    var = text(ctx.Identifier())
    off = self._offtable[var]
    self._E(instr.FrameAddr(off))
    self._E(instr.Store())
#...
```

最后汇编的生成对新增加的IR进行汇编对应：

| IR               | 汇编                                                         | 工作原理                                                     |
| ---------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| frameaddr offset | push("fp", offset) + pop("t1", "t2") + add t1, t2, t1 + push("t1") | 由于fp存的是栈帧底部地址，而变量的地址往往存在fp-offset的位置，所以要做一个加法来把要求的变量的地址存至t1 |
| load             | pop("t1") + lw t1, 0(t1) + push("t1")                        | t1原本存的是一个地址，将该地址存的东西存进t1里               |
| store            | pop("t2", "t1") + sw t1, 0(t2) + push("t1")                  | 将t1存的东西存到t2保存的这个地址中                           |
| pop              | addi sp, sp, 8                                               | 减少栈空间                                                   |

最后，prologue和epilogue主要借鉴了参考代码，因为minidecaf-tutorial的列子不对。

## 思考题

1. 描述程序运行过程中函数栈帧的构成，分成哪几个部分？每个部分所用空间最少是多少？
   栈帧分成三个部分：栈顶是计算表达式用的运算栈，这个部分可能为空，然后存放当前可用的局部变量的地方也可能为空，最后是返回值和老的栈帧基地址，占空间为INT_SIZE *2

2. 有些语言允许在同一个作用域中多次定义同名的变量，例如这是一段合法的 Rust 代码（你不需要精确了解它的含义，大致理解即可）：

   ```rust
   fn main() {
     let a = 0;
     let a = f(a);
     let a = g(a);
   }
   ```

   其中`f(a)`中的`a`是上一行的`let a = 0;`定义的，`g(a)`中的`a`是上一行的`let a = f(a);`。

   如果 MiniDecaf 也允许多次定义同名变量，并规定新的定义会覆盖之前的同名定义，请问在你的实现中，需要对定义变量和查找变量的逻辑做怎样的修改？

   如果可以重定义的话，则要对minidecaf做以下的改变：

   ```python
   #原代码
   def addVar(self, var:None):
           assert var not in self._offtable #确认变量不存在
           self._top -= INT_SIZE 
           if var is not None:
               self._offtable[var] = self._top
           return self._top
   #新代码
   def addVar(self, var:None):
           if var is not None:
               if var not in self._offtable:
                   self._top -= INT_SIZE 
               	self._offtable[var] = self._top
                   return self._top
               else:
                   return self._offtable[var]
   ```

   