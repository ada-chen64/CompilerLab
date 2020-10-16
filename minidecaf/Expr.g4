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
    : logical_or
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
logical_or
    : logical_and #cLog_or
    | logical_or '||' logical_and #tLog_or
    ;
logical_and
    : equality #cLog_and
    | logical_and '&&' equality #tLog_and
    ;
equality
    : relational #cEquality
    | equality (EqOp) relational #tEquality
    ;
relational
    : add #cRelational
    | relational (InEqOp) add #tRelational
    ;
MulOp
    : '*' | '/' | '%';

EqOp
    : '==' | '!=' ;
InEqOp 
    : '<' | '>' |'<=' | '>=';

