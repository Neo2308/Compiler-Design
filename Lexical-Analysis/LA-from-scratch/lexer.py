class lexer:
    keywords = ["if","else","int","char","return"]
    
    def __init__(self):
        self.state = 0
        self.word = ""
        self.curr = 0

    def is_keyword(self,word):
        return word in self.keywords
    
    def reset(self):
        if self.state == 100:
           pass
        elif self.state == 101:
            if(self.is_keyword(self.word)):
                print(self.word,"KEYWORD",sep='\t')
            else:
                print(self.word,"IDENTIFIER",sep='\t')
        elif self.state == 102:
            print(self.word,"NUMERICAL_CONSTANT",sep='\t')           
        elif self.state == 103:
            print(self.word,"CHAR_CONSTANT",sep='\t')           
        elif self.state == 104:
            print(self.word,"STRING_CONSTANT",sep='\t')           
        elif self.state == 105:
            print(self.word,"SEPERATOR",sep='\t')           
        else:
            print(self.word)
        self.state = 0       
        self.word = ""

    def readchar(self,c):    
        self.word = self.word + c 
        if self.state == 0:
            if c == ' ' or c == '\t' or c == '\n':
                self.state = 100
                self.reset()
            elif c.isalpha() or c == '_':
                self.state = 1
            elif c.isdigit():
                self.state = 2
            elif c == '\'':
                self.state = 8
            elif c == '\"':
                self.state = 12
            elif c == ',' or c == ';' or c == '(' or c == ')' or c == '{' or c == '}':
                self.state = 105
                self.reset()
            else:
                self.reset()
        elif self.state == 1:
            if c.isalpha() or c.isdigit() or c == '_':
                self.state = 1
            else:
                self.state = 101
                self.recant(1)
                self.reset()
        elif self.state == 2:
            if c.isdigit():
                self.state = 2
            elif c == '.':
                self.state = 3
            elif c == 'e' or c == 'E':
                self.state = 5
            else:
                self.state = 102
                self.recant(1)
                self.reset()
        elif self.state == 3:
            if c.isdigit():
                self.state = 4
            else:
                self.state = 102
                self.recant(2)
                self.reset()
        elif self.state == 4:
            if c.isdigit():
                self.state = 4
            elif c == 'e' or c == 'E':
                self.state = 5
            else:
                self.state = 102
                self.recant(1)
                self.reset()        
        elif self.state == 5:
            if c == '+' or c == '-':
                self.state = 6
            elif c.isdigit():
                self.state = 7
            else:
                self.state = 102
                self.recant(2)
                self.reset()
        elif self.state == 6:
            if c.isdigit():
                self.state = 7
            else:
                self.state = 102
                self.recant(3)
                self.reset()
        elif self.state == 7:
            if c.isdigit():
                self.state = 7
            else:
                self.state = 102
                self.recant(1)
                self.reset()
        elif self.state == 8:
            if c == '\\':
                self.state = 9
            elif c == '\'':    
                self.state = 103
                self.reset()
            else:
                self.state = 11
        elif self.state == 9:
            self.state = 10
        elif self.state == 10:
            if c == '\'':    
                self.state = 103
                self.reset()
            else:
                self.recant(3)
                self.reset()
        elif self.state == 11:
            if c == '\'':    
                self.state = 103
                self.reset()
            else:
                self.recant(2)
                self.reset()
        elif self.state == 12:
            if c == '\\':
                self.state = 13
            elif c == '\"':
                self.state = 104
                self.reset()
            else:
                self.state = 12
        elif self.state == 13:
            self.state = 12
                        
    def recant(self,n):
        self.word = self.word[:len(self.word)-n]
        self.curr-=n
    
    def parse(self,inp):
        while(self.curr!=len(inp)):
            self.readchar(inp[self.curr])
            self.curr+=1
        if len(self.word)!=0:
            self.reset()

with open('input.c','r') as f:
    data = f.read()
print(data)
mylexer = lexer()
mylexer.parse(data)
