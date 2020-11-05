# Step 7

## 实验任务

作用域和块语句

对语法的改动：

```
function
	:type Identifier '(' ')' compound_statement
	;
compound_statement
	:'{' block_item* '}'
	;
statement
	: 'return' expression ';'
	| expression? ';'
	| 'if' '(' expression ')' statement ('else' statement)?
	| compound_statement
```

## 实验实现

实验指导说明该实验的目的是实现名称解析。在不同的作用域里可以用一样的变量名。同一个域里不能有同一个变量名。所以我们首先要解决的就是之前所设置的变量名冲定义的问题。我的想法是动态地建立一个区域栈，每遇到一个新的域就继承栈顶，也就是上一个域的所有变量，然后在这个域里添加新的变量或修改已存在变量，然后这个域结束的时候再把栈顶pop掉。我借鉴了参考代码的`stacked_dict`

```python
#utils.py
class stack_dict():
    def __init__(self):
        self._upp = [{}] #继承的变量
        self._cur = [{}] #当前域里声明的变量
    def __getitem__(self, key):
        return self._upp[-1][key]

    def __setitem__(self, key, value):
        self._cur[-1][key] = self._upp[-1][key] = value
        #print(self._upp)

    def __contains__(self, key):
        return key in self._upp[-1]

    def __len__(self):
        return len(self._upp[-1])

    def push(self):
        self._upp.append(deepcopy(self._upp[-1]))
        self._cur.append({})
        #print(self._upp)

    def pop(self):
        assert len(self._upp) > 1
        self._upp.pop()
        self._cur.pop()
        #print(self._upp)

    def peek(self, last=0):
        return self._cur[-1-last] #这个函数用于查看是否重定义
```

同时我也借鉴里参考代码里的Variables class：

```python
#ir.irgen.py
class Variables:
    _varcnt = {} #记录同名的变量有几个
    def __init__(self, ident:str, offset:int):
        incorInit(Variables._varcnt, ident) #如果存在，则Variables._varcnt[ident] +=1, 否则 Variables._varcnt[ident] = 0
        self.id = Variables._varcnt #为变量设置独特id
        self.ident = ident
        self.offset = offset #变量的frameAddr 
    def __eq__(self, other):
        return self.id == other.id and self.ident == other.ident and\
            self.offset == other.offset

    def __str__(self):
        return f"{self.ident}({self.id})"

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash((self.ident, self.id, self.offset))
```

我们在我们的IR栈中要维护一个stack_dict，我们称为_varstack。并且，由于我们需要记录每个域有多少变量，我们还需要一个列表和一个记录当前域的变量数的一个int。然后我们还需要加上对变量栈进行处理的函数：

```python
class StackIRGen(ExprVisitor):
    def __init__(self, emitter:IREmitter):
        self._E = emitter
        # self._offtable = {}
        # self._top = 0
        self._labelCounter = LabelCounter()
        self._frameSlots = [] #keeps track of frame slots used for each block
        self._curFrameSlot = 0 #frame slots used for THIS block
        self._varstack = stack_dict() #dict entry for each block
    def decVar(self, ctx, ident): #declare Variable
        self._curFrameSlot += 1 #当前域的变量数加一
        self._varstack[text(ident)] = Variables(text(ident), -INT_SIZE * self._curFrameSlot) #将新变量压如栈中
    def getVar(self, ctx, ident):
        return self._varstack[text(ident)]
    def newBlock(self, ctx):
        self._varstack.push() #战中增加新的域
        self._frameSlots.append(self._curFrameSlot) #当前使用的变量数压如列表，因为新域继承父域的变量数，当前变量数不变
    def popBlock(self, ctx):
        slots_to_release = self._curFrameSlot - self._frameSlots[-1] #当前变量数-父域的变量数=当前新增加的变量
        self._varstack.pop() 
        self._curFrameSlot = self._frameSlots[-1]
        self._frameSlots.pop()
        return slots_to_release
    def visitCompound_statement(self, ctx:ExprParser.Compound_statementContext):
        self._E(instr.Comment("new Block"))
        self.newBlock(ctx) #增加新的域
        self.visitChildren(ctx)
        pt = self.popBlock(ctx) #把该域弹出，记录需要释放的变量数
        #print("pop time",pt)
        for i in range(pt):
            self._E(instr.Comment("Pop"))
            self._E(instr.Pop())
```

思考提

1. 请将下述MiniDecaf代码中的`???`替换为一个32位整数，使得程序运行结束后返回0。

```c++
int main(){
    int x = ???; 
    if(x){
        return x;
    }else {
        int x = 2;
    }
    return x;
}
```

??? = 0，这样，`if(x)`为`false`，所以进入`else`，重新定义一个新的`x`，不影响原来的，然后跳出`else`之后返回最初设置的`x=0`。

2. 在实验指导中，我们提到“就MiniDecaf而言，名称解析的代码可以嵌入IR生成里”，但不是对于所有语言都可以把名称解析嵌入代码生成。试问被编译的语言有什么特征时，名称解析作为单独的一个阶段在IR生成之前会更好？


   当语言支持重定义时，名称解析作为单独的一个阶段比较好