term = ['id','+','*','(',')','$']
nonTerm = ['E','E\'','T','T\'','F']
pTable = {
    'E':{'id':['T','E\''], '+':[], '*':[], '(':['T','E\''], ')':[], '$':[]},
    'E\'':{'id':[], '+':['+','T','E\''], '*':[], '(':[], ')':['epsilon'], '$':['epsilon']},
    'T':{'id':['F','T\''], '+':[], '*':[], '(':['F','T\''], ')':[], '$':[]},
    'T\'':{'id':[], '+':['epsilon'], '*':['*','F','T\''], '(':[], ')':['epsilon'], '$':['epsilon']},
    'F':{'id':['id'], '+':[], '*':[], '(':['(','E',')'], ')':[], '$':[]}
}
class Tree:
    def __init__(self,begin):
        self.root = Node('root')
        self.root.useRule([begin,'$'])
        self.current = self.root.children[0]

    def isDone(self):
        return self.root.isDone()

    def matchCurrent(self):
        self.current.done=True
        parent = self.current.parent
        while parent!=None:
            parent.activeChild+=1
            if parent.isDone():
                parent.done = True
                parent = parent.parent
            else:
                child = parent.children[parent.activeChild]
                while len(child.children)>0:
                    child = child.children[0]
                self.current = child
                break
        if parent is None:
            self.current = None
    
    def useRule(self,nxt):
        self.current.useRule(nxt)
        self.current = self.current.children[0]

class Node:
    def __init__(self,ch,parent=None):
        self.done=False
        self.ch = ch
        self.children = []
        self.parent = parent
        self.activeChild = 0
    
    def isterm(self):
        return self.ch in term

    def useRule(self,nxt):
        for i in nxt:
            child = Node(i,self)            
            self.children.append(child)
    
    def isDone(self):
        return self.done or self.activeChild >= len(self.children)

string = 'id * ( id * id ) + id'
inp = string.split()
inp.append('$')
print("Input Recieved:",inp)
print("\nParsing Steps:")
curr = 0
tree = Tree('E')
while tree.isDone() == False:
    x = tree.current
    w = inp[curr]
    if w==x.ch:
        print("Matched ",x.ch)
        tree.matchCurrent()
        curr+=1
    elif x.isterm():
        print("Error: Incorrect terminal")
        break
    elif len(pTable[x.ch][w])==0:
        print("Error: Missing Entry in Parsing Table")
        break
    else:
        print("Output "+x.ch+" -> "+''.join(pTable[x.ch][w]))
        nxt = pTable[x.ch][w] 
        if len(nxt) == 1 and nxt[0] == 'epsilon':
            tree.matchCurrent()
        else:
            tree.useRule(nxt)
print('')
if tree.isDone() and curr==len(inp):
    print("Valid Input")   
else:
    print("Invalid Input")   