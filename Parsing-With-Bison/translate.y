%{
	#include <stdio.h>
	#include <stdlib.h>
%}

%token ID OP_ADD OP_MUL BR_OP BR_CL EOI
%% 
start : E EOI {
  							printf("\nInput has been accepted!\n");
  							exit(1);
  						}
 ;
E : T E_      {
                printf("Applied E -> T E'\n");
              }
 ;
E_ : OP_ADD T E_ {
                printf("Applied E' -> + T E'\n");
              }
  | 					{
                printf("Applied E' -> epsilon\n");
              }
 ;
T : F T_      {
                printf("Applied T -> F T'\n");
              }
 ;
T_ : OP_MUL F T_ {
                printf("Applied T' -> * F T'\n");
              }		
  |           {
                printf("Applied T' -> epsilon\n");
              } 					
 ;
F : BR_OP E BR_CL {
                printf("Applied F -> ( E )\n");
              }			
  |	ID				{
                printf("Applied F -> id\n");
              }	
 ;
%%
int yyerror(char *s)
{
    printf("\nError occurred while parsing: %s",s);
    printf("\nInput has been rejected!\n");
    exit(1);
    return 1;
}
int main()
{
  printf("Enter the input:\n");
  yyparse();
  return 1;
}