lexer grammar ExprLex;

// 括号
Lparen: '(';
Rparen: ')';
Lbrace: '{';
Rbrace: '}';

//符号
Semicolon: ';';
Ques: '?';
Colon: ':';
// 运算符
Add: '+';
Sub: '-';
Mul: '*';
Div: '/';
Mod: '%';
LNot: '!';
Not: '~';
LOr: '||';
Land: '&&'; 



// 整数
Integer: [0-9]+;

// 空白
fragment WhitespaceChar: [ \t\n\r];
Whitespace: WhitespaceChar+ -> skip;

//字符相关
Int: 'int';
Return: 'return';
Identifier: [a-zA-Z_][a-zA-Z0-9_]*;

//keywords
If: 'if';
Else: 'else';

//错
Error: '.';