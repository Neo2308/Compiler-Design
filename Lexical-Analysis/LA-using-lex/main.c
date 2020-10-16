#include<stdio.h>
#include<stdlib.h>
#include "lex.yy.c"
int main()
{
	FILE *fp;
	fp = fopen("input.c","r");
	if(!fp)
	{
		printf("Could not open file.\n");
		return 0;
	}
	yyin = fp;
	yylex();
	return 0;
}