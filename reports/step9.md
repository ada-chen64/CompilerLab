# Step 9

陈昱霏 2017080067

## 实验任务

实现函数的声明和定义：

```
program
	: function+ EOF 
    ;
function 
    : typ Identifier '('param_list ')' '{' temp_stmt '}'  #funcDef
    | typ Identifier '('param_list ')' ';' #funcDecl
    ;
param_list
    : (declaration (',' declaration)*)?
    ;
temp_stmt
    : compound_statement
    | block_item*
    ;

```

实现函数调用：

```
expr_list
    : (expression (',' expression)*)?
    ;
unary
    : postfix #tUnary
    | ('-'|'!'|'~') unary #cUnary
    ;
postfix
    : atom #tPostFix
    | Identifier '(' expr_list ')' #cPostFix
    ;
```

## 实验实现

由于之前我们整个代码只支持一个函数，IRProg里存放的是IRInstr的序列，但是我们现在要实现多个函数，所以一个IRProg里不能只是指令的序列，而必须是函数的序列，其函数里包含的是指令序列。所以我们设一个新的类为IRFunc，里面存放函数名，参数信息，以及指令序列。

```python
class IRFunc:
    def __init__(self, name:str, param:ParamInfo, instrs:[IRInstr]):
        self.name = name
        self.param = param
        self.instrs = instrs
    def __str__(self):
        def f(i):
            if type(i) is instr.Comment:
                return f"\t\t\t\t{i}"
            if type(i) is instr.Label:
                return f"{i}" #函数名字
            return f"\t{i}" #正常指令
        body = '\n'.join(map(f, self.instrs))
        return f"{self.name}({self.param}):\n{body}"
#原本的IRProg的self.instrs 改为 self.funcs
class IRProg:
    def __init__(self, funcs:IRFunc):
        self.funcs = funcs

    def __str__(self):
        return "\n\n".join(map(str, self.funcs))
#IREmitter
class IREmitter:
    def __init__(self):
        self.funcs = [] #函数序列
        #self.instrs = []
        self.cur_func = None
        self.cur_param = None
        self.cur_instrs = [] #当前函数的指令序列
    def enterfunction(self, func_name: str, paramInfo:ParamInfo):
        self.cur_func = func_name
        self.cur_param = paramInfo
        self.cur_instrs = [] #每次进入新的函数的时候将当前函数指令序列清零
    def exitfunction(self):
        self.funcs.append(IRFunc(self.cur_func,self.cur_param, self.cur_instrs))
		#函数结束的时候生成IRFunc，压如函数序列
    def emit(self, ir:IRInstr):
        self.cur_instrs.append(ir)
        #print(self.instrs)
    def getIR(self):
        #return IRProg(self.instrs)
        return IRProg(self.funcs)

    def __call__(self, ir:IRInstr):
        #print("emitter called")
        #print(ir)
        self.emit(ir)
```

在StackIRGen中需要构造管理函数的类，所以我创建里一个新的类叫FunctionManager，其中函数管理中要做到参数管理，参数信息类参考了参考代码：

```python
class ParamInfo:
    def __init__(self, vars:[Variables]):
        self.vars = vars
        self.param_num = len(vars)
    def __str__(self):
        return f"{self.param_num}"
    def compatible(self, other):
        return self.param_num == other.param_num
class FunctionManager:
    def __init__(self):
        self.paramInfos = {}
        self.functions = [] #记录被定义过的函数
    def enterfunction(self, func_name: str,paramInfo: ParamInfo):
        self.paramInfos[func_name] = paramInfo #记录每个声明过的函数的参数信息
        self.functions.append(func_name)
```

对于函数的声明，主要需要查看该函数之前有没有声明，如果有声明，则查看参数数量符不符合，如果参数量不一样的话则报错，如果没有声明过，则在函数管理中增加该函数的参数信息。对于函数定义，不仅要查看函数的参数信息，还要查看该函数之前定义过没有，如果定义过则应该在函数管理中的function序列中有该函数的名字，并且报错。如果没有定义过，则需要进入函数定义：

```python
#irgen.py
    def visitFuncDef(self, ctx:ExprParser.FuncDefContext):
        func_name = text(ctx.Identifier())
        if func_name in self._functionManager.functions:
            raise ExprLocatedError(f"redefinition of function {func}")
        self.newBlock(ctx)
        paramInfo = ParamInfo(ctx.param_list().accept(self))
        if func_name in self._functionManager.paramInfos:
            if not self._functionManager.paramInfos[func_name].compatible(paramInfo):
                raise ExprLocatedError(f"conflicting types for {func}")
        self._functionManager.enterfunction(func_name, paramInfo)
        self._E.enterfunction(func_name, paramInfo)
        ctx.temp_stmt().accept(self)
        self.popBlock(ctx)
        self._E.exitfunction()
    def visitFuncDecl(self, ctx:ExprParser.FuncDeclContext):
        func_name = text(ctx.Identifier())
        self.newBlock(ctx)
        paramInfo = ParamInfo(ctx.param_list().accept(self))
        if func_name in self._functionManager.paramInfos:
            if not self._functionManager.paramInfos[func_name].compatible(paramInfo):
                raise ExprLocatedError(f"conflicting types for {func}")
        elif func_name not in self._functionManager.paramInfos:
            self._functionManager.paramInfos[func_name] = paramInfo
        self.popBlock(ctx)
```

函数调用中主要就是先执行参数计算，再生成call指令。要注意的是计算参数量和参数信息里存的量符不符。

```python
def visitCPostFix(self, ctx:ExprParser.CPostFixContext):
        func_name = text(ctx.Identifier())
        args = ctx.expr_list().expression()
        # print(func_name)
        # for key, value in self._functionManager.paramInfos.items():
        #     print(key)
        #     print(self._functionManager.paramInfos)
        if len(args) != self._functionManager.paramInfos[func_name].param_num:
            raise ExprLocatedError(ctx, f"wrong argument number")
        for arg in reversed(args):
            arg.accept(self)
        self._E(instr.Call(func_name))
```

## 思考题

1. MiniDecaf的函数调用时参数求值的顺序数未定义行为。试写出一段MiniDecaf代码，使得不同的参数求值顺序会导致不同的返回结果。

   ```c++
   int fun(int a, int b, int c)
   {
       return a + b + c;
   }
   int main()
   {
       int a = 1, b = 2;
       return fun(a++, b, a+5);
   }
   
   ```

   如果函数调用时参数求值数从左到右，fun的返回值是 `2+2+7` 也就是`11`，但如果数从右到左，返回值是`2+2+6`也就是`10`。

