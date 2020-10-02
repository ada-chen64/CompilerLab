grammar Expr;

import ExprLex;


program
    : function+ EOF
    ;
function 
    : typ Identifier Lparen Rparen Lbrace statement Rbrace
    ;
typ
    : Int #intType
    ;
statement
    : Return expression Semicolon #returnStmt
    ;
expression
    : Integer
    ;
expr
    : add
    ;
add
    : add op=('+'|'-') mul
    | mul
    ;
mul
    : atom (mulOp atom)*
    ;
atom
    : '(' expr ')'      # atomParen
    | Integer         # atomInteger
    ;
mulOp
    : '*' | '/' ;