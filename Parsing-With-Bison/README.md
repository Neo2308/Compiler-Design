Setup:

	bison -d translate.y
	lex token.l
	gcc lex.yy.c translate.tab.c -o parser

Usage:
	
	./parser

Made By:

	P. Radha Krishna
	17075040
	Part - IV
	CSE (B.Tech) 
	IIT (BHU) Varanasi
