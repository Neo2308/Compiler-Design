delim 	[ \t\n]
space	{delim}+
letter	[_a-zA-Z]
digit	[0-9]
all		[_a-zA-Z0-9] 
id		{letter}({letter}|digit)*
number	{digit}+([eE][\+\-]?{digit}+)?
decimal	{digit}+(\.{digit}+)?([eE][\+\-]?{digit}+)?
%%
{space}		{}
if 			{printf("%s\t%s\t%s\n",yytext,"KEYWORD","IF");}
else 		{printf("%s\t%s\t%s\n",yytext,"KEYWORD","ELSE");}
int			{printf("%s\t%s\t%s\n",yytext,"KEYWORD","INT");}
char		{printf("%s\t%s\t%s\n",yytext,"KEYWORD","CHAR");}
return 		{printf("%s\t%s\t%s\n",yytext,"KEYWORD","RETURN");}
{id}		{printf("%s\t%s\t%s\n",yytext,"IDENTIFIER",yytext);}
{number}	{printf("%s\t%s\t%d\n",yytext,"INTEGER_CONSTANT",atoi(yytext));}
{decimal}	{printf("%s\t%s\t%lf\n",yytext,"DECIMAL_CONSTANT",atof(yytext));}
\"[^\"]*\"	{printf("%s\t%s\t%s\n",yytext,"STRING_CONSTANT",yytext);}
\'.?\'		{printf("%s\t%s\t%s\n",yytext,"CHAR_CONSTANT",yytext);}
"=="		{printf("%s\t%s\t%s\n",yytext,"RELOP","EQ");}
"!="		{printf("%s\t%s\t%s\n",yytext,"RELOP","NE");}
"<"			{printf("%s\t%s\t%s\n",yytext,"RELOP","LT");}
"<="		{printf("%s\t%s\t%s\n",yytext,"RELOP","LE");}
">"			{printf("%s\t%s\t%s\n",yytext,"RELOP","GT");}
">="		{printf("%s\t%s\t%s\n",yytext,"RELOP","GE");}
"+="		{printf("%s\t%s\t%s\n",yytext,"OP","ADD_ASSIGN");}
"-="		{printf("%s\t%s\t%s\n",yytext,"OP","SUB_ASSIGN");}
"*="		{printf("%s\t%s\t%s\n",yytext,"OP","MUL_ASSIGN");}
"/="		{printf("%s\t%s\t%s\n",yytext,"OP","DIV_ASSIGN");}
"%="		{printf("%s\t%s\t%s\n",yytext,"OP","MOD_ASSIGN");}
"=" 		{printf("%s\t%s\t%s\n",yytext,"OP","ASSIGN");}
"+" 		{printf("%s\t%s\t%s\n",yytext,"OP","ADD");}
"-"			{printf("%s\t%s\t%s\n",yytext,"OP","SUB");}
"*"			{printf("%s\t%s\t%s\n",yytext,"OP","MUL");}
"/"			{printf("%s\t%s\t%s\n",yytext,"OP","DIV");}
"%"			{printf("%s\t%s\t%s\n",yytext,"OP","MOD");}
"(" 		{printf("%s\t%s\t%s\n",yytext,"SEP","OP_PAR");}
")"			{printf("%s\t%s\t%s\n",yytext,"SEP","CL_PAR");}
"["			{printf("%s\t%s\t%s\n",yytext,"SEP","OP_SQR");}
"]"			{printf("%s\t%s\t%s\n",yytext,"SEP","CL_SQR");}
"{"			{printf("%s\t%s\t%s\n",yytext,"SEP","OP_BRC");}
"}"			{printf("%s\t%s\t%s\n",yytext,"SEP","CL_BRC");}
","			{printf("%s\t%s\t%s\n",yytext,"SEP","COMMA");}
";"			{printf("%s\t%s\t%s\n",yytext,"SEP","SEMICOLON");}
%%
int yywrap()
{
	printf("****END OF LEXICAL ANALYSIS****\n");
	return(1);
}