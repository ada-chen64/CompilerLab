import sys
sys.path.append('..')
from ..utils import *

class Type:
    def __repr__(self):
        return self.__str__()

    def sizeof(self):
        raise Exception("abstract type is unsized")

#types need initializers, where they just pass
# __str__ returns their type representation such as int, void, bool, etc.
# __eq__ checks if the object in comparison is of the same type
# sizeof returns the size of the type

class IntType(Type):
    def __init__(self):
        pass

    def __str__(self):
        return "int"

    def __eq__(self, other):
        return isinstance(other, IntType)

    def sizeof(self):
        return INT_SIZE

class PtrType(Type):
    def __init__(self, basetype:Type):
        self.basetype = basetype
    def __str__(self):
        return f"{self.basetype}*"
    def __eq__(self, other):
        if not isinstance(other, PtrType):
            return False
        return other.basetype == self.basetype
    def sizeof(self):
        return INT_SIZE

class ArrayType(Type):
    def __init__(self, base:Type, len:int):
        self.base = base
        self.len = len

    def __str__(self):
        return f"[{self.len}]{self.base}"

    def __eq__(self, other):
        if not isinstance(other, ArrayType):
            return False
        return self.base == other.base and self.len == other.len

    def make(base:Type, dims:list):
        for len in dims:
            base = ArrayType(base, len)
        return base

    def sizeof(self):
        return self.base.sizeof() * self.len

def TypeRule(f):
    """A type rule is a function: (ctx, *inputTypes) -> {outputType | errStr | None}.
    The ctx parameter is only used for error reporting."""
    def g(ctx, *inTy):
        res = f(ctx, *inTy)
        if type(res) is str:
            raise ExprLocatedError(ctx, f"{f.__name__}: {res}")
        if res is None:
            raise ExprLocatedError(ctx, f"{f.__name__}: type error")
        return res
    g.__name__ = f.__name__ # black magic
    return g

def tryEach(name="tryEach", *fs):
    """Combine multiple type rules `fs`, returns result the first that does not fail."""
    @TypeRule
    def g(ctx, *inTy):
        errs = []
        for f in fs:
            try:
                return f(ctx, *inTy)
            except ExprTypesError as e:
                errs += [e.msg]
        return f"{name}:\n\t" + '\n\t'.join(map(str, errs))
    g.__name__ = name # black magic
    return g

@TypeRule
def condRule(ctx, cond, tru_typ, fal_typ):
    if cond == IntType() and tru_typ == fal_typ:
        return tru_typ

@TypeRule
def intBinOpRule(ctx, lhs, rhs):
    if lhs == IntType() and rhs ==  IntType():
        return IntType()
    else:
        return f"expected IntType, got {lhs} and {rhs}"

@TypeRule
def intUnaopRule(ctx, ty):
    if ty == IntType():
        return IntType()
    return f"integer expected, got {ty}"

@TypeRule
def ptrArithRule(ctx, lhs, rhs):
    if lhs == IntType() and isinstance(rhs, PtrType):
        return rhs
    if rhs == IntType() and isinstance(lhs, PtrType):
        return lhs
    return f"pointer and integer, got {lhs} and {rhs}"

@TypeRule
def ptrDiffRule(ctx, lhs, rhs):
    if lhs == rhs and isinstance(rhs, PtrType):
        return IntType()
    return f"two pointers of the same type, got {lhs} and {rhs}"

@TypeRule
def eqRule(ctx, lhs, rhs):
    if lhs != rhs:
        return f"cannot equate or compare {lhs} to {rhs}"
    if lhs != IntType() and not isinstance(lhs, PtrType):
        return f"expected integer or pointer types, found {lhs}"
    return IntType()

@TypeRule
def relRule(ctx, lhs, rhs):
    if lhs != IntType():
        return f"int expected as relop lhs, found {lhs}"
    if rhs != IntType():
        return f"int expected as relop rhs, found {rhs}"
    return IntType()

@TypeRule
def asgnRule(ctx, lhs, rhs):
    if lhs != rhs:
        return f"cannot assign {rhs} to {lhs}"
    if isinstance(lhs, ArrayType):
        return f"cannot assign to array type {lhs}"
    return lhs

@TypeRule
def derefRule(ctx, ty):
    if isinstance(ty, PtrType):
        return ty.basetype
    return f"pointer expected, got {ty}"

@TypeRule
def addrofRule(ctx, ty):
    if isinstance(ty, ArrayType):
        return "cannot take address of array type"
    return PtrType(ty)

@TypeRule
def retRule(ctx, retType, typ):
    if retType != typ:
        return f"return {retType} expected, got {typ}"
    return retType

@TypeRule
def stmtCondRule(ctx, typ):
    if typ != IntType():
        return f"expected IntType, got {typ}"
    return IntType()