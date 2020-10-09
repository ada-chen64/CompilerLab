MAX_INT = 2**31 - 1
MIN_INT = -2**31

binsymbols = {'+': 'add', '-': 'sub','*': 'mul', '/': 'div', '%': 'rem'}


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