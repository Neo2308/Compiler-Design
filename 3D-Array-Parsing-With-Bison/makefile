3darray: parser.tab.cc lex.yy.c
	g++ lex.yy.c parser.tab.cc -o 3darray

parser.tab.cc: parser.y
	bison -d parser.y -o parser.tab.cc

lex.yy.c: lexer.l
	lex lexer.l

clean:
	rm -f parser lex.yy.c parser.tab.cc parser.tab.hh parser.tab.[ch] stack.hh 3darray

test: 3darray
	cat test | ./3darray