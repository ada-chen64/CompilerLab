from copy import deepcopy
MAX_INT = 2**31 - 1
MIN_INT = -2**31
INT_SIZE = 8
binsymbols = {'+': 'add', '-': 'sub','*': 'mul', '/': 'div', '%': 'rem'}
eqsymbols = {'==' : 'eq', '!=' :'ne'}
relatesymbols = {'<=' : 'le', '>=' : 'ge', '<' :'lt', '>':'gt'}
logicsymbols = {'&&' : 'land', '||' : 'lor'}
branchOp =['beqz', 'bnez', 'br', 'beq']



class ExprError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, *kwargs)

class ExprLocatedError(ExprError):
    def __init__(self, ctx, msg:str):
        self.msg = f"input:{ctx.start.line},{ctx.start.column}: {msg}"

    def __str__(self):
        return self.msg

class ExprTypesError(ExprError):
    pass

def text(x):
    if x is not None:
        return str(x.getText())

def flatten(l):
    newlist = []
    for i in l:
        if type(i) is list:
            newlist += flatten(i)
        else:
            newlist += [i]
    return newlist

def incorInit(d:dict, key, init=0):
    if key in d:
        d[key] += 1
    else:
        d[key] = init
def noOp(*args, **kwargs):
    pass

def expandIterableKey(d:list):
    d2 = {}
    for (keys, val) in d:
        for key in keys:
            d2[key] = val
    return d2

class stack_dict():
    def __init__(self):
        self._upp = [{}]
        self._cur = [{}]
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
        return self._cur[-1-last]