class TopDownParser:
    def __init__(self):
        self.term = ['id','+','*','(',')','$']
        self.nonTerm = ['E','E\'','T','T\'','F']
        self.grammar = {
            'E':[['T','E\'']],
            'E\'':[['+','T','E\''],['epsilon']],
            'T':[['F','T\'']],
            'T\'':[['*','F','T\''],['epsilon']],
            'F':[['(','E',')'],['id']]
        }
    
    def displayGrammar(self):
        print("GRAMMAR IN USE :")
        head = '{:^12}\t'
        cell = '{:^12}\t'
        for i in self.grammar.keys():
            print('{} -> {}'.format(i,''.join(self.grammar[i][0])),end='')
            for j in range(1,len(self.grammar[i])):
                print(' | {}'.format(''.join(self.grammar[i][j])),end = '')
            print('')
        print('')
    
    def isTerminal(self,x):
        return x in self.term

    def applyG(self,start,inp,tabs = 0):
        rules = self.grammar[start]
        match = []
        curr = 0
        message = '\t'*tabs+'{}'
        matchRowTerm = message.format('MATCHED \'{}\' WITH {}')
        matchRowNonTerm = message.format('MATCHED \"{}\" WITH {}')
        errorRow = message.format('ERROR: {}')
        delim = message.format('-'*20)
        print(message.format('Looking for {} in : \"{}\"'.format(start,' '.join(inp))))
        for rule in rules:
            print(delim)
            print(message.format('Trying {} -> {}'.format(start,''.join(rule))))
            match = []
            for ch in rule:
                if self.isTerminal(ch):
                    if curr not in range(len(inp)):
                        print(errorRow.format('Incorrect terminal (Needed \'{}\' got EOF)'.format(ch)))
                        match = None
                        break
                    elif inp[curr] == ch:
                        match.append(ch)
                        print(matchRowTerm.format(inp[curr],ch))
                        curr += 1
                    else:
                        print(errorRow.format('Incorrect terminal (needed \'{}\' got \'{}\')'.format(ch,inp[curr])))
                        match = None
                        break
                elif ch == 'epsilon':
                    print(matchRowTerm.format('',ch))
                    break
                else:
                    nonTermMatch = self.applyG(ch,inp[curr:],tabs+1)
                    if nonTermMatch is None:
                        print(errorRow.format('Could not resolve {}'.format(ch)))
                        match = None
                        break
                    else:
                        for a in nonTermMatch:
                            match.append(a)
                        curr += len(nonTermMatch)     
            if match is not None:
                print(message.format('Applied {} -> {}'.format(start,''.join(rule))))
                print(delim)
                print(matchRowNonTerm.format(' '.join(match),start))
                print('')
                return match
            else:
                print(message.format('{} -> {} failed.'.format(start,''.join(rule))))
                print(delim)
        print(message.format('Could not find {} in \"{}\"'.format(start,' '.join(inp))))
        return None

    def parse(self,inp,start):
        tokens = list(inp.split(' '))
        print('TOKENS :')
        print(tokens)
        print('\n')
        result = self.applyG(start,tokens)
        print('RESULT:')
        if len(tokens)==len(result):
            print("INPUT WAS A MATCH")
        else:
            print("INPUT WAS NOT A MATCH")

parser = TopDownParser()
parser.displayGrammar()
parser.parse('id * ( id + id ) + id','E')