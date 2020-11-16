%{
		#include "translate.tab.h"
%}
%%
[ \t]       {}
"id"		return ID;
"+"	  		return OP_ADD;
"*"	  		return OP_MUL;
"("			return BR_OP;
")"			return BR_CL;
[\n]		return EOI;
%%
int yywrap()
{
	return 1;
}