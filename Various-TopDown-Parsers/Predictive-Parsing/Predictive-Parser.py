class TopDownParser:
    def __init__(self):
        self.term = ['id','+','*','(',')','$']
        self.nonTerm = ['E','E\'','T','T\'','F']
        self.pTable = {
            'E':{'id':['T','E\''], '+':[], '*':[], '(':['T','E\''], ')':[], '$':[]},
            'E\'':{'id':[], '+':['+','T','E\''], '*':[], '(':[], ')':['epsilon'], '$':['epsilon']},
            'T':{'id':['F','T\''], '+':[], '*':[], '(':['F','T\''], ')':[], '$':[]},
            'T\'':{'id':[], '+':['epsilon'], '*':['*','F','T\''], '(':[], ')':['epsilon'], '$':['epsilon']},
            'F':{'id':['id'], '+':[], '*':[], '(':['(','E',')'], ')':[], '$':[]}
        }
    
    def displayParseTable(self):
        print("PARSE TABLE IN USE :")
        head = '{:^12}\t'
        cell = '{:^12}\t'
        print(head.format(''),end='')
        for i in self.term:
            print(head.format(i),end='')
        print('\n')
        for i in self.nonTerm:
            print(head.format(i),end = '')
            for j in self.term:
                if len(self.pTable[i][j])==0:
                    print(cell.format(''),end='')
                else:
                    print(cell.format(i+' -> '+''.join(self.pTable[i][j])),end = '')
            print('')
        print('')
    
    def isTerminal(self,x):
        return x in self.term

    def applyG(self,stack,nxt):
        stack.pop()
        for ch in nxt[::-1]:
            stack.append(ch)
        return stack
        
    def parse(self,inp,start):
        tokens = list(inp.split(' '))
        tokens.append('$')
        print('INPUT :')
        print(tokens)
        print('\n')
        curr = 0
        stack = ['$',start]
        matched = []
        action = ''
        head = "{:^25}\t{:^25}\t{:^25}\t{:^25}"
        row = "{:<25}\t{:<25}\t{:<25}\t{:>25}"
        print(head.format("ACTION TAKEN","MATCHED","STACK","REMAINING"))
        print(row.format(action,' '.join(matched),' '.join(stack),' '.join(tokens[curr:])))        
        while len(stack)>0:
            x = stack[-1]
            w = tokens[curr]
            if w == x:
                matched.append(x)
                action = "Matched {}".format(x)
                stack.pop()
                curr+=1
            elif self.isTerminal(x):
                print("\nERROR:")
                print("Wrong Terminal Error")
                print("Needed {} got {}".format(x,w))
                break
            elif len(self.pTable[x][w])==0:
                print("\nERROR:")
                print("Parsing Table Error")
                print("No transition for {} from {}".format(w,x))
                break
            else:
                action = "Applied {:<8}".format(x+' -> '+''.join(self.pTable[x][w]))
                nxt = self.pTable[x][w] 
                if len(nxt) == 1 and nxt[0] == 'epsilon':
                    stack.pop()
                else:
                    stack = self.applyG(stack,nxt)
            print(row.format(action,' '.join(matched),' '.join(stack),' '.join(tokens[curr:])))        
        print('\n')
        print('RESULT:')
        if len(stack)==0 and curr==len(tokens):
            print("INPUT WAS A MATCH")
        else:
            print("INPUT WAS NOT A MATCH")

parser = TopDownParser()
parser.displayParseTable()
parser.parse('id * ( id + id ) + id','E')