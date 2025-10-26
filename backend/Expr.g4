grammar Expr;

prog: stat+ | EOF;
stat: assignment | expr | assertStat | printStat;
assignment: ID '=' expr;
assertStat: ASSERT expr;
printStat: PRINT expr;

// Precedence ladder
expr: orExpr;
orExpr: andExpr (OR andExpr)*;
andExpr: notExpr (AND notExpr)*;
notExpr: NOT notExpr | cmpExpr;
cmpExpr: addSubExpr (COMPARE addSubExpr)*;
addSubExpr: mulDivExpr (ADD_SUB mulDivExpr)*;
mulDivExpr: unaryExpr (MUL_DIV unaryExpr)*;
unaryExpr: (ADD_SUB) unaryExpr | powExpr;
powExpr: atom (POW powExpr)?;

// Atoms
atom: numberExpr | scientificExpr | '(' expr ')' | ID;

// --- Custom number formats ---
numberExpr: NUMBER; // simple literal
scientificExpr:
	NUMBER 'x10^' expr; // custom exponent as expression

// Lexer
ASSERT: 'assert';
PRINT: 'print';
OR: 'or';
AND: 'and';
NOT: 'not';
POW: '^';
ADD_SUB: [+\-];
MUL_DIV: [*/%];
COMPARE: '==' | '!=' | '<=' | '>=' | '<' | '>';

ID: [a-zA-Z_][a-zA-Z_0-9]*;

// Numeric literal (no 'x10^' here — handled in parser)
NUMBER:
	[0-9]+ ('.' [0-9]+)? ([eE][+-]? [0-9]+)?
	| '.' [0-9]+ ([eE][+-]? [0-9]+)?;

// Comments and whitespace
COMMENT: '#' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;