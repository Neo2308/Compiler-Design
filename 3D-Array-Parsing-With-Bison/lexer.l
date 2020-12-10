%{
		#include<iostream>
		#include "parser.tab.hh"
%}
%%
[ \t]       				{}
"int"						return DT;
[a-zA-Z_][a-zA-Z_0-9]*		{
								yylval.name = strdup(yytext);
								return ID;
							};
[0-9]+						{
								yylval.number = atoi(yytext);
								return NUM;
							};
"["							return OB;
"]"							return CB;
"="							return EQ;
[\n]						return EOL;
"$$"						return END;
.							{
								std::cout<<"Unexpected symbol: "<<strdup(yytext)<<std::endl;
								std::cout<<"Terminating..."<<std::endl;
								exit(1);
							}
%%
int yywrap()
{
	return 1;
}