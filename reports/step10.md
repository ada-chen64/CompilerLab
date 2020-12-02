# Step 10

陈昱霏 2017080067

## 实验任务

支持全局变量

```
program
    : glob_stuff+ EOF 
    ;
glob_stuff
    : function #globFunc
    | declaration ';' #globDecl
    ;
```

## 实验实现

全局变量主要存的信息：变量，大小，和初始值，如果没有初始化则设为None。类型结构主要参考了参考代码。

```python
class GlobalInfo:
    def __init__(self, size:int, var:Variables, init=None):
        self.var = var
        self.size = size
        self.init = init
    def __str__(self):
        return f"{self.var}, size={self.size}, init={self.initStr()}"
    def initStr(self):
        if init is None:
            return f"uninitialized"
        else:
            return f"{self.init}"
    def compatible(self, other):
        return True
```

由于全局变量要在汇编代码的最前面一起输出，所以不能记录在IR指令中，必须记录在程序中，也就是IRProg，所以我们必须设置一个新的IR类为IRGlobals，该类借鉴了参考代码的IRGlobs：

```python
class IRGlobals:
    def __init__(self, symbol:str, size:int, init, align=4):
        self.symbol = symbol #变量名
        self.size = size #大小
        self.init = init #初始化
        self.align = align #对齐
    #从GlobalInfo类生成
    def genfromGlobalInfo(globalInfo):
        assert globalInfo.var.offset is None
        return IRGlobals(globalInfo.var.ident, globalInfo.size, globalInfo.init)
    def __str__(self):
        return f"{self.symbol}:\n\tsize={self.size}, align={self.align}\n\t{self.initStr()}"
    def initStr(self):
        if self.init is None:
            return f"uninitialized"
        else:
            return f"initialized: {self.init}"
```

在生成IR的时候，每遇到一个全局变量都必须添加到程序中，使用以下函数：

```python
def emitGlobalInfo(self, globalInfo: GlobalInfo):
        self.globals.append(IRGlobals.genfromGlobalInfo(globalInfo))
```

最后在StackIRGen中对全局变量做处理就行。因为一旦进入declaration就会生成普通的变量，所以不能让程序进入`visitDeclaration`，则在`visitGlobDecl`的时候就不再往下访问。在生成全局变量时，主要做的数计算初始化值，可以通过`eval`来做到。之后就是查看该变量有没有声明过，声明过的话查看有没有定义过，避免重定义。如果每，没有定义过，修改该变量的初始值即可。然后将信息传给程序。

```python
def doGlobalInitializer(self, ctx:ExprParser.ExpressionContext):
        if ctx is None:
            return None
        try:
            init = eval(text(ctx), {}, {})
            return init
        except:
            raise ExprLocatedError(ctx, f"global variable must be constant")
    def visitGlobDecl(self, ctx:ExprParser.GlobDeclContext):
        #print("visitGlobDecl")
        ctx = ctx.declaration()
        init = self.doGlobalInitializer(ctx.expression())
        ident = text(ctx.Identifier())
        if ident in self._functionManager.paramInfos:
            raise ExprLocatedError(ctx, f"conflict global variable and function {func}")
        var = Variables(ident, None)
        globInfo = GlobalInfo(INT_SIZE, var, init)
        if ident in self._varstack.peek():
            prevVar = self._varstack[ident]
            prevGlobalInfo = self._functionManager.globalInfos[prevVar]
            if prevGlobalInfo.init is not None:
                if globInfo is not None:
                    raise ExprLocatedError(ctx, f"redefinition of variable {ident}")
            elif globInfo is not None:
                self._functionManager.globalInfos[preVar].init = init
        else:
            self._varstack[ident] = var
            self._functionManager.globalInfos[var] = globInfo
        self._E.emitGlobalInfo(globInfo)
```

对于全局变量的访问，再以下两处判断以下`offset`是否为`None`，就可以得知是否为全局变量。如果数全局变量，则生成IR指令`globaladdr SYMBOL`：

```python
def visitAtomIdentifier(self, ctx:ExprParser.AtomIdentifierContext):
        #print("AtomIdentifier")
        ident = ctx.Identifier()
        #print(f"ident: {ident}")
        var = self.getVar(ctx, ident)
        off = var.offset
        #off = self.offset.getVar(var)
        #off = self._offtable[var]
        self._E(instr.Comment("frameaddress load"))
        if off is None:
            self._E(instr.GlobalAddr(ident))
        else:
            self._E(instr.FrameAddr(off))
        self._E(instr.Load())
        self._E(instr.Comment("frameaddress load done"))
    
    def visitTAssign(self, ctx:ExprParser.TAssignContext):
        self.visitChildren(ctx)
        ident = ctx.Identifier()
        var = self.getVar(ctx, ident)
        off = var.offset
        #off = self._offtable[var]
        #off = self.offset.getVar(var)
        self._E(instr.Comment("frameaddress store"))
        if off is None:
            self._E(instr.GlobalAddr(ident))
        else:
            self._E(instr.FrameAddr(off))
        self._E(instr.Store())
        self._E(instr.Comment("frameaddress store done"))
```

全局变量的声明和定义在汇编代码中数放到最上面的，所以在汇编代码中我们首先把程序的所有全局变量先左声明和定义：

```python
def genGlobalInfo(self, glob):
        if glob.init is None:
            self._E([AsmDirective(f".comm {glob.symbol},{glob.size},{glob.align}")])
        else:
            self._E([
                AsmDirective(".data"),
                AsmDirective(f".globl {glob.symbol}"),
                AsmDirective(f".align {glob.align}"),
                AsmDirective(f".size {glob.symbol}, {glob.size}"),
                AsmLabel(f"{glob.symbol}"),
                AsmDirective(f".quad {glob.init}")])
```

访问全局变量用以下的汇编：

```python
@Instrs
def globaladdr(symbol:str):
    return [f"addi sp, sp, -8", f"la t1, {symbol}", f"sw t1, 0(sp)"]
```

## 思考题

1.请给出将全局变量`a`的值读到寄存器`t0`所需要的riscv指令序列。

la t0, a