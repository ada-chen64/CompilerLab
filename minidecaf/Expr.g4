grammar Expr;

import ExprLex;


program
    : function+ EOF 
    ;
function 
    : typ Identifier '('param_list ')' '{' temp_stmt '}'  #funcDef
    | typ Identifier '('param_list ')' ';' #funcDecl
    ;
typ
    : Int #intType
    ;
param_list
    : (declaration (',' declaration)*)?
    ;
temp_stmt
    : compound_statement
    | block_item*
    ;
compound_statement
    :'{' block_item* '}'
    ;
block_item
    : statement
    | declaration ';'
    ;
statement
    : Return expression ';' #returnStmt
    | expression? ';' #exprStmt
    | 'if' '(' expression ')' c_if=statement ('else' c_el=statement)? #condStmt
    | compound_statement #cmpdStmt
    | 'for' '(' init=expression? ';' cond=expression? ';' incr=expression? ')' statement #forStmt
    | 'for' '(' declaration ';' cond=expression? ';' incr=expression?  ')' statement #forDeclStmt
    | 'while' '(' expression ')' statement #whileStmt
    | 'do' statement 'while' '(' expression ')' ';' #doStmt
    | 'break' ';' #breakStmt
    | 'continue' ';' #contStmt
    ;
declaration
    : typ Identifier ('=' expression)? 
    ;
expr_list
    : (expression (',' expression)*)?
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
    : postfix #tUnary
    | ('-'|'!'|'~') unary #cUnary
    ;
postfix
    : atom #tPostFix
    | Identifier '(' expr_list ')' #cPostFix
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

