grammar Expr;

import ExprLex;


program
    : function+ EOF
    ;
function 
    : typ Identifier '(' ')' compound_statement
    ;
typ
    : Int #intType
    ;
compound_statement
    :'{' block_item* '}'
    ;
block_item
    : statement
    | declaration
    ;
statement
    : Return expression ';' #returnStmt
    | expression? ';' #exprStmt
    | 'if' '(' expression ')' c_if=statement ('else' c_el=statement)? #condStmt
    | compound_statement #cmpdStmt
    ;
declaration
    : typ Identifier ('=' expression)? Semicolon
    ;
expression
    : assignment
    ;
assignment
    : conditional #cAssign
    | Identifier '=' expression #tAssign
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
    | Identifier #atomIdentifier
    ;
conditional
    : logical_or #cCond
    | logical_or '?' expression ':' conditional #tCond
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

