class BottomUpParser:
    def __init__(self):
        self.term = ['id','+','*','(',')','$']
        self.nonTerm = ['E','E\'','T','T\'','F']
        self.actionTable = {
            '0':{'id':['s','5'], '+':[], '*':[], '(':['s','4'], ')':[], '$':[]},
            '1':{'id':[], '+':[], '*':[], '(':[], ')':[], '$':['acc']},
            '2':{'id':[], '+':['s','7'], '*':[], '(':[], ')':['r','3'], '$':['r','3']},
            '3':{'id':[], '+':['r','6'], '*':['s','9'], '(':[], ')':['r','6'], '$':['r','6']},
            '4':{'id':['s','5'], '+':[], '*':[], '(':['s','4'], ')':[], '$':[]},
            '5':{'id':[], '+':['r','8'], '*':['r','8'], '(':[], ')':['r','8'], '$':['r','8']},
            '6':{'id':[], '+':[], '*':[], '(':[], ')':['r','1'], '$':['r','1']},
            '7':{'id':['s','5'], '+':[], '*':[], '(':['s','4'], ')':[], '$':[]},
            '8':{'id':[], '+':['r','4'], '*':[], '(':[], ')':['r','4'], '$':['r','4']},
            '9':{'id':['s','5'], '+':[], '*':[], '(':['s','4'], ')':[], '$':[]},
            '10':{'id':[], '+':[], '*':[], '(':[], ')':['s','13'], '$':[]},
            '11':{'id':[], '+':['s','7'], '*':[], '(':[], ')':['r','3'], '$':['r','3']},
            '12':{'id':[], '+':['r','6'], '*':['s','9'], '(':[], ')':['r','6'], '$':['r','6']},
            '13':{'id':[], '+':['r','7'], '*':['r','7'], '(':[], ')':['r','7'], '$':['r','7']},
            '14':{'id':[], '+':[], '*':[], '(':[], ')':['r','2'], '$':['r','2']},
            '15':{'id':[], '+':['r','5'], '*':[], '(':[], ')':['r','5'], '$':['r','5']},
        }
        self.gotoTable = {
            '0':{'E':'1','E\'':None,'T':'2','T\'':None,'F':'3'},
            '1':{'E':None,'E\'':None,'T':None,'T\'':None,'F':None},
            '2':{'E':None,'E\'':'6','T':None,'T\'':None,'F':None},
            '3':{'E':None,'E\'':None,'T':None,'T\'':'8','F':None},
            '4':{'E':'10','E\'':None,'T':'2','T\'':None,'F':'3'},
            '5':{'E':None,'E\'':None,'T':None,'T\'':None,'F':None},
            '6':{'E':None,'E\'':None,'T':None,'T\'':None,'F':None},
            '7':{'E':None,'E\'':None,'T':'11','T\'':None,'F':'3'},
            '8':{'E':None,'E\'':None,'T':None,'T\'':None,'F':None},
            '9':{'E':None,'E\'':None,'T':None,'T\'':None,'F':'12'},
            '10':{'E':None,'E\'':None,'T':None,'T\'':None,'F':None},
            '11':{'E':None,'E\'':'14','T':None,'T\'':None,'F':None},
            '12':{'E':None,'E\'':None,'T':None,'T\'':'15','F':None},
            '13':{'E':None,'E\'':None,'T':None,'T\'':None,'F':None},
            '14':{'E':None,'E\'':None,'T':None,'T\'':None,'F':None},
            '15':{'E':None,'E\'':None,'T':None,'T\'':None,'F':None},
        }
        self.productions = {
            '0':('S',['E']),
            '1':('E',['T','E\'']),
            '2':('E\'',['+','T','E\'']),
            '3':('E\'',['eps']),
            '4':('T',['F','T\'']),
            '5':('T\'',['*','F','T\'']),
            '6':('T\'',['eps']),
            '7':('F',['(','E',')']),
            '8':('F',['id'])
        }
    
    def displayActionTable(self):
        print("ACTION TABLE IN USE :")
        head = '{:^12}\t'
        cell = '{:^12}\t'
        print(head.format(''),end='')
        for i in self.term:
            print(head.format(i),end='')
        print('\n')
        for i in self.actionTable.keys():
            print(head.format(i),end = '')
            for j in self.term:
                if len(self.actionTable[i][j])==0:
                    print(cell.format(''),end='')
                else:
                    print(cell.format(' '.join(self.actionTable[i][j])),end = '')
            print('')
        print('')

    def displayGotoTable(self):
        print("GOTO TABLE IN USE :")
        head = '{:^12}\t'
        cell = '{:^12}\t'
        print(head.format(''),end='')
        for i in ['E','T','F']:
            print(head.format(i),end='')
        print('\n')
        for i in self.gotoTable.keys():
            print(head.format(i),end = '')
            for j in ['E','T','F']:
                if self.gotoTable[i][j]==None:
                    print(cell.format(''),end='')
                else:
                    print(cell.format(str(self.gotoTable[i][j])),end = '')
            print('')
        print('')
    
    def displayProductions(self):
        print('Grammar Rules:')
        prod = '{}) {} --> {}'
        for key,val in self.productions.items():
            print(prod.format(key,val[0],' '.join(val[1])))
    
    def parse(self,inp,start):
        accepted = False
        tokens = list(inp.split(' '))
        tokens.append('$')
        print('\nINPUT :')
        print(tokens)
        print('\n')
        curr = 0
        stack = ['$',start]
        symbols = []
        action = ''
        head = "{:^25}\t{:^25}\t{:^25}\t{:^25}"
        row = "{:<25}\t{:<25}\t{:<25}\t{:>25}"
        print(head.format("ACTION TAKEN","STACK","SYMBOLS","REMAINING"))
        print(row.format(action,' '.join(stack),' '.join(symbols),' '.join(tokens[curr:])))        
        while len(stack)>0:
            x = stack[-1]
            w = tokens[curr]
            if len(self.actionTable[x][w])==0:
                print("\nERROR:")
                print("Parsing Table Error")
                print("No transition for {} from {}".format(w,x))
                break
            if self.actionTable[x][w][0]=='acc':
                accepted = True
                break
            if self.actionTable[x][w][0]=='s':
                symbols.append(w)
                nextState = self.actionTable[x][w][1]
                stack.append(nextState)
                action = "Shifted to {}".format(nextState)
                curr+=1
            else:
                rno = self.actionTable[x][w][1]
                rule = self.productions[rno]
                action = "Applied {:<8}".format(rule[0]+' -> '+''.join(rule[1]))
                if rule[1][0]!='eps':
                    stack = stack[:-len(rule[1])]
                    symbols = symbols[:-len(rule[1])]
                x = stack[-1]
                stack.append(self.gotoTable[x][rule[0]])
                symbols.append(rule[0])
            print(row.format(action,' '.join(stack),' '.join(symbols),' '.join(tokens[curr:])))        
        print('\n')
        print('RESULT:')
        if accepted:
            print("INPUT WAS A MATCH")
        else:
            print("INPUT WAS NOT A MATCH")

parser = BottomUpParser()
parser.displayActionTable()
parser.displayGotoTable()
parser.displayProductions()
parser.parse('( id + id ) * id','0')
