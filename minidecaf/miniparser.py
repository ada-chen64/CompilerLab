import minilexer


# 大写字母。parser 语法里面，首字母大写的是终结符，小写的是非终结符。
BIG_LETTERS = { chr(x) for x in range(65, 91) }


class ASTNode:
    """语法树结点。叶子结点是终结符、内部结点是非终结符。"""
    def __init__(self, label:str, text:str=None, children:list=[]):
        """如果是叶子结点（即 token），那 text 是这个 token 的字符串，并且 children 为空。
        如果是内部结点，那 text 为 None，children 是它的产生式的右手边。"""
        self.label = label
        self.text = text
        self.children = children

    def __str__(self):
        if self.text is None:
            return f"{self.label}({', '.join([str(x) for x in self.children])})"
        if len(self.text) == 0: # 终结符没文字，没必要加括号
            return f"{self.label}"
        return f"{self.label}({self.text})"


class Parser:
    def __init__(self, rules:dict):
        self.rules = rules # str 产生式左手边 -> list 右手边

    def setInput(self, lexer):
        self.lex = lexer.lex()

    def parse(self, sym:str):
        """sym 是一个非终结符的名字。
        你不必看懂这个算法，虽然它不是很难。"""
        children = []
        for child in self.rules[sym]:
            #print(child)
            if child[0] in BIG_LETTERS: # 终结符
                #print("BIG LETTERS")
                # 按需返回 token
                tok = next(self.lex)
                if tok.kind.name != child:
                    raise Exception(f"syntax error, {child} expected but {tok.kind.name} found")
                children.append(ASTNode(tok.kind.name, text=tok.text))
            else: # 非终结符
                #print("no big letters")
                children.append(self.parse(child))
        return ASTNode(sym, children=children)

    def fromRules(s):
        rules = [line.split() for line in s.strip().split('\n')]
        rules = { r[0] : r[2:] for r in rules } # r[1] 是 ':'
        return Parser(rules)


def default():
    # 描述我们 step1 的语法
    rules = """
program    : function
function   : type Identifier Lparen Rparen Lbrace statement Rbrace
type       : Int
statement  : Return expression Semicolon
expression : Integer
    """

    parser = Parser.fromRules(rules)
    # lexer 的输出喂给 parser 当输入
    parser.setInput(minilexer.default())
    return parser


if __name__ == "__main__":
    print(default().parse("program"))