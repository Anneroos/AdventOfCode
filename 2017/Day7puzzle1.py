import numpy as np

text_file = open("puzzleinput7.txt", "r")
input = text_file.read().split('\n')
text_file.close()
lines = np.array(input)



class Node:
    # Initializer / Instance Attributes
    children = np.array([])
    parent = None

    carryingWeight = 0
    def __init__(self, name, weight):
        self.name = name
        self.weight = int(weight)

    def addChildNode(self, child):
        self.children = np.append(self.children, child)
        child.parent = self

    def calculateCarryingWeight(self):
        if len(self.children)>0:
            for i in range(len(self.children)):
                child = self.children[i]
                self.carryingWeight += child.calculateCarryingWeight()
        return self.weight + self.carryingWeight

    def checkBalance(self):
        balanced = True
        if len(self.children)>0:
            # list the weights
            weights = np.zeros(len(self.children))
            for i in range(len(self.children)):
                weights[i] = self.children[i].weight + self.children[i].carryingWeight
            # print(self.name, "Children weights:", weights)
            balanced = np.all(weights == weights[0])

            # if the childrens carryingweights are not all the same, check their children
            if not balanced:
                # make empty array
                balancedChildren = np.zeros(len(self.children))
                for i in range(len(self.children)):
                    child = self.children[i]
                    balancedChildren[i] = child.checkBalance()


                # if node is unbalanced but all children are balanced, the problem is near
                if np.all(balancedChildren == True):
                    unbalancedNode = self
                    print(self.name, "is unbalanced but all children are balanced. ", weights)
                    for i in range(len(self.children)):
                        child = self.children[i]
                        print(child.name, child.weight, child.carryingWeight)

            else:
                return True
        # if no children, then balanced!
        return balanced


    # end of node class


# MAKING LIST OF ALL THE NODES
nodes = np.array([])
names = np.array([])
for i in range(len(lines)):
    splitted = np.array(lines[i].split(' '))
    programNode = Node(splitted[0],splitted[1][1:-1])
    nodes = np.append(nodes, programNode)
    names = np.append(names, splitted[0])


# GOING THROUGH AGAIN TO MAKE CONNECTIONS
for i in range(len(names)):

    splitted = np.array(lines[i].split(' '))
    # IF THIS NODE HAS CHILDREN:
    if len(splitted) > 2 :
        thisProgram = nodes[i]
        for j in range(len(splitted)-3):
            carriedProgramName = splitted[j+3].split(',')[0] # 0 name 1 weight 2 arrow 3 first carried

            if( np.any(names==str(carriedProgramName))):

                itemindex = np.where(names==carriedProgramName)
                carriedProgram = nodes[itemindex[0][0]]
                thisProgram.addChildNode(carriedProgram)
            else:
                print(carriedProgramName, "name doesnt exist")
                pass
                # NODE IS NOT CARRYING, ENDPOINT
                # I DONT HAVE TO DO SOMETHING WITH IT YET

# FIND WHICH NODE DOES NOT HAVE A PARENT
for i in range(len(lines)):
    if nodes[i].parent == None:
        base = nodes[i]
        print("The bottom program is called", nodes[i].name, "at index", i)
        break

base.calculateCarryingWeight()
print(base.carryingWeight)
base.checkBalance()
print(unbalancedNode)