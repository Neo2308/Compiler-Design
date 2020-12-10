%code{
	#include<bits/stdc++.h>
  int yyerror (const char *error);
  int yylex(void);
  std::map<std::string,std::pair<int,std::pair<int,std::pair<int,int>>>>SYM_TABLE;
  int MEM_PTR=0;
  int MAX_MEMORY = 10000;
  std::vector<int> memory(MAX_MEMORY,0);
}
%union{
  char* name;
  int number;
}
%token<name> ID
%token<number> NUM
%token DT OB CB EQ EOL END
%type lines line DECL ASSIGN PRINT
%type<number> ACC IND M1 M2 M3

%% 

start : lines     {
                      std::cout<<"Completed! Exiting..."<<std::endl;
                      exit(0);
                  }
  ;
lines : line EOL lines 
  | END 
  ;
line : DECL       {
                      std::cout<<std::endl;
                  }
  | ASSIGN        {
                      std::cout<<std::endl;
                  }
  | PRINT         {
                      std::cout<<std::endl;
                  }
  ;
DECL : DT ID IND IND IND {
                      std::cout<<"Identifier: "<<$2<<std::endl;
                      std::cout<<"Size 1: "<<$3<<std::endl;
                      std::cout<<"Size 2: "<<$4<<std::endl;
                      std::cout<<"Size 3: "<<$5<<std::endl;
                      int loc = MEM_PTR;
                      SYM_TABLE[$2] = {MEM_PTR,{$3,{$4,$5}}};
                      MEM_PTR+=$3*$4*$5;
                      if(MEM_PTR>MAX_MEMORY)
                      {
                          std::cout<<"Ran out of memory!"<<std::endl;
                          std::cout<<"Terminating..."<<std::endl;
                          exit(1);
                      }
                      else
                      {
                          std::cout<<"Memory for "<<$2<<" allocated starting from "<<loc<<" upto "<<MEM_PTR-1<<"."<<std::endl;
                      }
                  }
 ;
ASSIGN : ACC EQ NUM {
                      std::cout<<"Value to be assigned: "<<$3<<std::endl;
                      std::cout<<"Accessing "<<$1<<std::endl;
                      std::cout<<"Value at "<<$1<<" was previously "<<memory[$1]<<std::endl;
                      memory[$1] = $3;
                      std::cout<<"Value at "<<$1<<" is now "<<memory[$1]<<std::endl;
                  }
 ;
PRINT : ACC       {
                      std::cout<<"Accessing "<<$1<<std::endl;
                      std::cout<<"Value at "<<$1<<" is "<<memory[$1]<<std::endl;
                  } 
ACC : ID M1 IND M2 IND M3 IND {
                      std::cout<<"Index 3: "<<$7<<std::endl;
                      std::pair<int,std::pair<int,std::pair<int,int>>> val = SYM_TABLE[$1];
                      if($7 < val.second.second.second)
                      {
                          int loc = $6;
                          loc = loc + $7 * 1;
                          std::cout<<$1<<"["<<$3<<"]"<<"["<<$5<<"]"<<"["<<$7<<"]"<<" is at: "<<loc<<std::endl;
                          $$ = loc;
                      }
                      else
                      {
                          std::cout<<"Index "<<$7<<" out of range!"<<std::endl;
                          std::cout<<"Terminating..."<<std::endl;
                          exit(1);
                      }
                  }
 ;
IND : OB NUM CB   {
                      $$ = $2;
                  }
 ;
M1 :              {
                      std::cout<<"Identifier: "<<$<name>0<<std::endl;
                      if(SYM_TABLE.find($<name>0)!=SYM_TABLE.end())
                      {
                          std::pair<int,std::pair<int,std::pair<int,int>>> val = SYM_TABLE[$<name>0];
                          std::cout<<"Found identifier "<<$<name>0<<" in symbol table."<<std::endl;
                          int loc = val.first;
                          std::cout<<$<name>0<<" starts at: "<<loc<<std::endl;
                          $$ = loc;
                      }
                      else
                      {
                          std::cout<<$<name>0<<" accessed before declaration!"<<std::endl;
                          std::cout<<"Terminating..."<<std::endl;
                          exit(1);
                      }   
                  }
 ;
M2 :              {
                      std::cout<<"Index 1: "<<$<number>0<<std::endl;
                      std::pair<int,std::pair<int,std::pair<int,int>>> val = SYM_TABLE[$<name>-2];
                      if($<number>0 < val.second.first)
                      {
                          int loc = $<number>-1;
                          loc = loc + $<number>0 * val.second.second.first * val.second.second.second;
                          std::cout<<$<name>-2<<"["<<$<number>0<<"]"<<" starts at: "<<loc<<std::endl;
                          $$ = loc;
                      }
                      else
                      {
                          std::cout<<"Index "<<$<number>0<<" out of range!"<<std::endl;
                          std::cout<<"Terminating..."<<std::endl;
                          exit(1);
                      }
                  }
 ;
M3 :              {
                      std::cout<<"Index 2: "<<$<number>0<<std::endl;
                      std::pair<int,std::pair<int,std::pair<int,int>>> val = SYM_TABLE[$<name>-4];
                      if($<number>0 < val.second.second.first)
                      {
                          int loc = $<number>-1;
                          loc = loc + $<number>0 * val.second.second.second;
                          std::cout<<$<name>-4<<"["<<$<number>-2<<"]"<<"["<<$<number>0<<"]"<<" starts at: "<<loc<<std::endl;
                          $$ = loc;
                      }
                      else
                      {
                          std::cout<<"Index "<<$<number>0<<" out of range!"<<std::endl;
                          std::cout<<"Terminating..."<<std::endl;
                          exit(1);
                      }
                  }
 ;

%%

int yyerror(const char *s)
{
    std::cout<<std::endl;
    std::cout<<"Parser ran into an error: "<<s<<std::endl;
    std::cout<<"Input has been rejected!"<<std::endl;
    exit(1);
    return 1;
}
int main()
{
  yyparse();
  return 1;
}