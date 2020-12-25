# Step 11

陈昱霏 2017080067

## 实验任务

増加指针类型：

```
typ
    : 'int' #intType
    | typ '*' #ptrType
    ;

```

引入左值的概念，修改賦值：

```
assignment
    : conditional #cAssign
    | unary asgnOp expression #tAssign
    ;
```

支持取地址操作符`&`和解引用操作符`*`和类型转换

```
unary
    : postfix #tUnary
    | unaryOp unary #cUnary
    | '(' typ ')' unary #typUnary
    ;
unaryOp
    : '-' | '!' | '~' | '*' | '&';
```

## 实验实现

本次实验主要还是借鉴了参考代码, 但是由于之前的名称解析和IRStack是一起处理的, 我在左值分析和类型检查部分就得加上名称解析．

由于代码比较繁琐，我主要就解释以下类型检查要左的工作：

类型检查部分主要是给IR生成时提供快速的变量类信息．当我们声明和定义变量的时候，要把变量的类存储下来，然后每次用到该变量的时候，通过查看存储的类来记录当前的context是什么类．所以类信息TypeInfo中存了三个dictionary：

```python
class TypeInfo:
    def __init__(self):
        self._t = {} # ctx -> Type
        self.loc = {} # ctx -> (IRInstr|ctx)+
        self.funcs = {} # str -> FuncTypeInfo
        
```

第一个数基于context寻找记录类，第二个是基于context寻找地址，目的数为了访问指针的时候可以找到指针指向的值．第三个数存储函数的返回值类和参数类，以便保证正确的函数访问．

类型检查中除了存储每个变量context的类型以外，还要检查变量规则，比如对于某些操作的返回类：

```c++
1 + 2; //int + int = int
&a; //ptrtype
*a; //return basetype of pointer
&a + 2; // ptrtype
&a - &b; //return int type
```

将这些操作应该的得到的类和左值中定义的类左比较，如果不是同一类，则报错．

对于地址查询，如果数普通变量的话，在地址信息上存储GlobalAddr或FrameAddr指令，如果是指针的话，存储当前的context，这样IRStack在处理的时候，要么得到一个IR命令，要么沿着context继续往下走得到地址．在IRStack中还要注意对加减操作的处理，遇到指针加减指针或者指针加减整数要做一些特殊的处理．汇编代码并不需要任何的改变．

## 思考题

1. 为什么类型检查要放到名称解析之后？
   因为在访问以定义的变量时，需要通过之前存的信息来得知该变量是什么类型。所以，在左名称解析之后，可以更方便地将变量名称和类型保存到一起以便之后的访问。
2. MiniDecaf中一个值只能有一种类型，但在很多语言中并非如此，请举出一个反例。
   在C++中，(1+2)可以赋值给int也可以赋值给double或float．
3. 在本次实验中我们禁止进行指针的比大小运算。请问如果要实现指针大小比较需要注意什么问题？可以和原来整数比较方法一样吗？
   指针比大小和整数比大小不同。由于指针指向某个值的存储地址，指针比大小比的就是地址的大小。但因为那个指针变量里存的也算是一个数字（地址的值）所以应该可以和整数比较一样。

