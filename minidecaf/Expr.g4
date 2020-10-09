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
    : add
    ;
add
    : mult #addMult
    | add ('+' | '-') mult #addOpMult
    ;
mult
    : unary #multUnary
    | mult (MulOp) unary #multOpUnary
    ;
unary
    : atom #tUnary
    | ('-'|'!'|'~') unary #cUnary
    ;
atom
    : Integer         # atomInteger
    | '(' expression ')'      # atomParen
    ;
MulOp
    : '*' | '/' | '%';

