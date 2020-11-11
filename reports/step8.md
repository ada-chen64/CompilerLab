# Step 8

陈昱霏 2017080067

## 实验任务：循环语句

在该实验中要对我们的编译器增加循环语句以及break/continue的支持：

```python
statement
    : 'return' expression ';'
    | expression? ';'
    | 'if' '(' expression ')' statement ('else' statement)?
    | compound_statement
    | 'for' '(' expression? ';' expression? ';' expression? ')' statement
    | 'for' '(' declaration expression? ';' expression? ')' statement
    | 'while' '(' expression ')' statement
    | 'do' statement 'while' '(' expression ')' ';'
    | 'break' ';'
    | 'continue' ';'
   	;
```

## 任务实现：

由实验指导所述，四种循环语句其实都大同小异。他们的结构都是以四个主要部分组成，可写为：Loop(init, cond, body, post)。该实验中不需要增加汇编语言的生成，主要的任务在于IR的生成。

对于循环语句，IR的构造如下：

1. `init` 的 `IR`
2. `label BEGINLOOP_LABEL`：开始下一轮迭代
3. `cond 的 IR`
4. `beqz BREAK_LABEL`：条件不满足就终止循环
5. `body 的 IR`
6. `label CONTINUE_LABEL`：continue 跳到这
7. `post 的 IR`
8. `br BEGINLOOP_LABEL`：本轮迭代完成
9. `label BREAK_LABEL`：条件不满足，或者 break 语句都会跳到这儿

其实对于四种不同循环语句基本上都采用上述结构，只不过对于`while`和`do while`而言，没有`init`这个设置。对于有`declaration`的`for`晕换，将`init`改为`declaration`。遇到`break`或者`continue`的时候，到`label`栈中找到最顶的`break`或`continue label`。

```python
#ir.irgen.py
def visitForStmt(self, ctx:ExprParser.ForStmtContext):
        #first do initialize expression
        self._E(instr.Comment("for Block"))
        self.newBlock(ctx)
        if ctx.init is not None:
            ctx.init.accept(self)
        begin_looplabel = self._labelCounter.addLabel("beginloop_Label")
        break_label = self._labelCounter.addLabel("breakloop_Label")
        cont_label = self._labelCounter.addLabel("continue_Label")
        self._E(instr.Label(begin_looplabel))
        if ctx.cond is not None:
            ctx.cond.accept(self)
            self._E(instr.Branch("beqz", break_label))
        ctx.statement().accept(self)
        self._E(instr.Label(cont_label))
        if ctx.incr is not None: #post
            ctx.incr.accept(self)
            self._E(instr.Pop())
        self._E(instr.Branch("br", begin_looplabel))
        self._E(instr.Label(break_label))
        pt = self.popBlock(ctx)
        #print("pop time",pt)
        self._E(instr.Comment("for Pop"))
        for i in range(pt):
            self._E(instr.Pop())
def visitForDeclStmt(self, ctx:ExprParser.ForDeclStmtContext):
        self._E(instr.Comment("for Block"))
        self.newBlock(ctx)
        ctx.declaration().accept(self)
        begin_looplabel = self._labelCounter.addLabel("beginloop_Label")
        break_label = self._labelCounter.addLabel("breakloop_Label")
        cont_label = self._labelCounter.addLabel("continue_Label")
        self._E(instr.Label(begin_looplabel))
        if ctx.cond is not None:
            ctx.cond.accept(self)
            self._E(instr.Branch("beqz", break_label))
        ctx.statement().accept(self)
        self._E(instr.Label(cont_label))
        if ctx.incr is not None:
            ctx.incr.accept(self)
            self._E(instr.Pop())
        self._E(instr.Branch("br", begin_looplabel))
        self._E(instr.Label(break_label))
        pt = self.popBlock(ctx)
        #print("pop time",pt)
        for i in range(pt):
            self._E(instr.Comment("Pop"))
            self._E(instr.Pop())
    def visitWhileStmt(self, ctx:ExprParser.WhileStmtContext):
        begin_looplabel = self._labelCounter.addLabel("beginloop_Label")
        break_label = self._labelCounter.addLabel("breakloop_Label")
        cont_label = self._labelCounter.addLabel("continue_Label")
        self._E(instr.Label(begin_looplabel))
        ctx.expression().accept(self)
        self._E(instr.Branch("beqz", break_label))
        ctx.statement().accept(self)
        self._E(instr.Label(cont_label))
        self._E(instr.Branch("br", begin_looplabel))
        self._E(instr.Label(break_label))


    def visitDoStmt(self, ctx:ExprParser.DoStmtContext):
        begin_looplabel = self._labelCounter.addLabel("beginloop_Label")
        break_label = self._labelCounter.addLabel("breakloop_Label")
        cont_label = self._labelCounter.addLabel("continue_Label")
        self._E(instr.Label(begin_looplabel))
        ctx.expression().accept(self)
        self._E(instr.Branch("beqz", break_label))
        ctx.statement().accept(self)
        self._E(instr.Label(cont_label))
        self._E(instr.Branch("br", begin_looplabel))
        self._E(instr.Label(break_label))

    
    def visitBreakStmt(self, ctx:ExprParser.BreakStmtContext):
        self._E(instr.Branch("br", self._labelCounter.getLabel("breakloop_Label")))

    def visitContStmt(self, ctx:ExprParser.ContStmtContext):
        self._E(instr.Branch("br", self._labelCounter.getLabel("continue_Label")))
```



## 思考题：

1. 将循环语句翻译成 IR 有许多可行的翻译方法，例如 while 循环可以有以下两种翻译方式：

第一种（即实验指导中的翻译方式）：

1. `label BEGINLOOP_LABEL`：开始下一轮迭代
2. `cond 的 IR`
3. `beqz BREAK_LABEL`：条件不满足就终止循环
4. `body 的 IR`
5. `label CONTINUE_LABEL`：continue 跳到这
6. `br BEGINLOOP_LABEL`：本轮迭代完成
7. `label BREAK_LABEL`：条件不满足，或者 break 语句都会跳到这儿

第二种：

1. `cond 的 IR`
2. `beqz BREAK_LABEL`：条件不满足就终止循环
3. `label BEGINLOOP_LABEL`：开始下一轮迭代
4. `body 的 IR`
5. `label CONTINUE_LABEL`：continue 跳到这
6. `cond 的 IR`
7. `bnez BEGINLOOP_LABEL`：本轮迭代完成，条件满足时进行下一次迭代
8. `label BREAK_LABEL`：条件不满足，或者 break 语句都会跳到这儿

从执行的指令的条数这个角度（`label` 指令不计算在内，假设循环体至少执行了一次），请评价这两种翻译方式哪一种更好？

从执行指令条数角度，第二种方法要比第一种更好，因为第二种方法其实执行的指令要比第一种方法少。假设两种方法都要至少循环一次，我们看看第一种方法要执行的指令，可以忽略`label`指令

```
label BEGIN_LABEL
cond IR #1
beqz BREAK_LABEL #2
body IR #3
label CONTINUE_LABEL
br BEGIN_LABEL #4
cond IR #5
beqz BREAK_LABEL #6
```

然后我们看一下第二种方法执行的指令：

```
cond IR #1
beqz BREAK_LABEL #2
label BEGIN_LABEL
body IR #3
label CONTINUE_LABEL
cond IR #4
bnez BEGIN_LABEL #5
```

第一种方法因为要`branch`到`begin`，执行了六条指令，而第二种值需要执行5条，所以从这可看出第二种方法要比第一种方法更高效。