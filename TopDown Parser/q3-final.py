term = ['a','+','*','(',')','$']
nonTerm = ['A','B','C','D','E']
pTable = {
    'A':{'a':'CB', '+':'', '*':'', '(':'CB', ')':'', '$':''},
    'B':{'a':'', '+':'+CB', '*':'', '(':'', ')':'eps', '$':'eps'},
    'C':{'a':'ED', '+':'', '*':'', '(':'ED', ')':'', '$':''},
    'D':{'a':'', '+':'eps', '*':'*ED', '(':'', ')':'eps', '$':'eps'},
    'E':{'a':'a', '+':'', '*':'', '(':'(A)', ')':'', '$':''}
}
class Tree:
    def __init__(self,start=''):
        self.root = Node('ROOT')
        if start!='':
            self.root.applyG([start,'$'])
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
    
    def applyG(self,nxt):
        self.current.applyG(nxt)
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

    def applyG(self,nxt):
        for i in nxt:
            child = Node(i,self)            
            self.children.append(child)
    
    def isDone(self):
        return self.done or self.activeChild >= len(self.children)

inp = input().strip()
inp+='$'
curr = 0
tree = Tree('A')
matched = ''
action = ''
row = "{:<15}\t{:<20}\t{:<15}\t{:<15}"
print(row.format("Current","Action Taken","Matched","Remaining"))
while tree.isDone() == False:
    x = tree.current
    w = inp[curr]
    if w==x.ch:
        matched +=x.ch
        action = "Match {}".format(x.ch)
        tree.matchCurrent()
        curr+=1
    elif x.isterm():
        print("Wrong Terminal Error")
        print("Needed {} got {}".format(x.ch,w))
        break
    elif pTable[x.ch][w]=='':
        print("Parsing Table Error")
        print("Cannot transition from {} for {}".format(x.ch,w))
        break
    else:
        action = "Applied "+x.ch+" -> "+pTable[x.ch][w]
        nxt = pTable[x.ch][w] 
        if nxt == 'eps':
            tree.matchCurrent()
        else:
            tree.applyG(nxt)
    print(row.format(x.ch,action,matched,inp[curr:]))

print('\nResult:')
if tree.isDone() and curr==len(inp):
    print("INPUT WAS A MATCH")   
else:
    print("INPUT WAS NOT A MATCH")   