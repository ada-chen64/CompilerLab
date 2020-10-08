lexer grammar ExprLex;

// 括号
Lparen: '(';
Rparen: ')';
Lbrace: '{';
Rbrace: '}';

//符号
Semicolon: ';';

// 运算符
Add: '+';
Sub: '-';
Mul: '*';
Div: '/';
LNot: '!';
Not: '~';

// 整数
Integer: [0-9]+;

// 空白
fragment WhitespaceChar: [ \t\n\r];
Whitespace: WhitespaceChar+ -> skip;

//字符相关
Int: 'int';
Return: 'return';
Identifier: [a-zA-Z_][a-zA-Z0-9_]*;



//错
Error: '.';