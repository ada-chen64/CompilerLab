# Step 12

陈昱霏 2017080067

## 实验任务

数组

1. 数组的声明

   ```
   declaration
   	: typ Identifier('[' Integer ']')* ('=' expression)? ';'
   ```

   

2. 数组和指针的下表操作

   ```
   postfix
   	: atom #tPostFix
       | Identifier '(' expr_list ')' #cPostFix
       | postfix '[' expression ']' #aPostFix
       ;
   ```

   

3. 指针算数：语法不变，但允许：指针加/减整数，整数加指针，指针减指针了．

## 实验实现

本次实验也借鉴了参考代码．

首先我们要实现数组类，所以在Types中加了ArrayType．ArrayType类中要储存basetype和数组长度．

由于数组是多个整数，大小不再是４个byte，所以要在变量类中储存变量大小．

```python
class Variables:
    def __init__(self, ident:str, offset:int, size:INT_SIZE):
        incorInit(Variables._varcnt, ident)
        self.id = Variables._varcnt[ident]
        self.ident = ident
        self.offset = offset
        self.size = size
```

在名称解析中要计算变量的大小：

```python
def getVarsize(self, ctx:ExprParser.DeclarationContext):
        size = product([int(text(x)) for x in ctx.Integer()])　# a[6][2]的大小为6*2
        if size <= 0:
            raise ExprLocatedError(ctx, f"array size cannot be zero")
        if size > MAX_INT:
            raise ExprLocatedError(ctx, f"array size too big")
        return size
```

在类型检查中要检查类型规则．例如`a[n]`，检查a的类为`ArrayType`并且`n`的类为`IntType`，然后返回basetype．

对于地址查找的话，对于`a[n]`，地址为`a的起始地址+n*INT_SIZE`，所以我们的地址查找如下：

```python
    def visitAPostFix(self, ctx:ExprParser.APostFixContext):
        fixupMult = self.typeInfo[ctx.postfix()].basetype.sizeof()
        return [ctx.postfix(), ctx.expression(), instr.Const(fixupMult), 
            instr.Binaries('*'), instr.Binaries('+')]
```



## 思考题

１．设有以下几个函数，其中局部变量a的其实地址都是`0x1000(4096)`，请分别给出每个函数的返回值(用一个minidecaf表达式表示，例如函数A的返回值数`*(int*)(4096+ 23 * 4))`．

```c++
int A(){
    int a[100];
    return a[23];
}
// *(int*)(4096+23*4)

int B(){
    int *p = (int*) 4096;
    return p[23];
}
// *(int*)(4096+23*4)

int C(){
    int a[10][10];
    return a[2][3];
}
// *(int**)(4096 + (10*2 + 3)*4)

int D(){
    int *a[10];
    return a[2][3];
}
// *(int**)(4096 + (10*2 + 3)*4)

int E(){
    int **p = (int**) 4096;
    return p[2][3]
}
//*(int**)(4096 + (10*2 + 3)*4)
```

２．C语言规范规定，允许局部变量是可变长度的数组(Variable Length Aray, VLA)，在我们的实验中为了简化，选择了不支持它．请你简要回答，如果我们决定支持一维的可变长度的数组(即允许类似`int n = 5; int a[n];` 这种，但仍然不允许 `int n = ...; int m = ...; int a\[n\]\[m\];` 这种)，而且要求数组仍然保存在栈上(即不允许用堆上的动态内存申请，如malloc等来实现它)，应该在现在有的实现基础上左哪些改动？

首先是对语法的改变：

```
//原本的
declaration
	: typ Identifier('[' Integer ']')* ('=' expression)? ';'
//修改的
declaration
	: typ Identifier('[' Integer ']')* ('=' expression)? ';'
	| typ Identifier('[' Identifier ']') ('=' expression)? ';'
```

因为atom可以使整数或者变量名．

以我们现在实现的代码，我们是在名称解析的部分给数组类的变量分大小，因为现在值允许已定长度，所以直接通过得到的Integer来计算所需要的大小．如果我们要实现可变长度的话，最方便的办法是在我们的变量类Variables中记录该变量的值，并且每次对该变量进行赋值的时候修改Variables中的值的定义．

```python
#原本的代码
class Variables:
    _varcnt = {}
    def __init__(self, ident:str, offset:int, size:INT_SIZE):
        incorInit(Variables._varcnt, ident)
        self.id = Variables._varcnt[ident]
        self.ident = ident
        self.offset = offset
        self.size = size
#修改的
class Variables:
    _varcnt = {}
    def __init__(self, ident:str, offset:int, size:INT_SIZE, value=0):
        incorInit(Variables._varcnt, ident)
        self.id = Variables._varcnt[ident]
        self.ident = ident
        self.offset = offset
        self.size = size
        self.value = value　#加上对变量的赋值，每次重新赋值的时候修改这个单位
```

这样，假设代码为`int n = 5; int a[n];`，我们在生成数组a的时候要计算a所需要的大小：

```python
def getVarsize(self, ctx:ExprParser.DeclarationContext):
    	if ctx.Integer() is not None:
            size = product([int(text(x)) for x in ctx.Integer()])
            if size <= 0:
                raise ExprLocatedError(ctx, f"array size cannot be zero")
            if size > MAX_INT:
                raise ExprLocatedError(ctx, f"array size too big")
            return size
        else:
            var = self._varstack[text(ctx.Identifier())] #在这里Identifier为n
            return var.value　#5
```

