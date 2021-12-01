import numpy as np
import pandas as pd

lines = pd.read_csv("adventOfCodeInput7.txt", sep=' ', header=None, engine='python')
lines = lines[[1,7]]
# lines = lines.head(7)
# print(lines)

# define a node class
class Node:
    # Initializer / Instance Attributes
    children = np.array([])
    childrennames = np.array([])
    parents = np.array([])
    parentsnames = np.array([])
    secondsCompleted = 0
    done = False
    def __init__(self, name):
        self.name = name
        self.secondsNeeded = ord(name)-4



    def addChildNode(self, child):
        self.children = np.append(self.children, child)
        self.childrennames = np.append(self.childrennames, child.name)
        child.parents = np.append(child.parents, self)
        child.parentsnames = np.append(child.parentsnames,self.name)

    def workASecond(self):
        self.secondsCompleted += 1
        if(self.secondsCompleted == self.secondsNeeded):
            self.done = True


# read lines and make nodes and fill the nodes-dictionary
nodes = {}
for i in range(len(lines)):
    first = lines.loc[i][1]
    then = lines.loc[i][7]
    # print(first, then)
    if first not in nodes:
        nodes[first] = Node(first)
    if then not in nodes:
        nodes[then] = Node(then)
    nodes[first].addChildNode(nodes[then])


# find the nodes that have no parents, we can start with those!
nodesToVisit = np.array([])
for name in nodes:
    if len(nodes[name].parents)<1:
        nodesToVisit = np.append(nodesToVisit,name)

# let's go through the graph
nodesToVisit = np.sort(nodesToVisit)
route = ''
visited = np.array([])

while len(nodesToVisit) >= 1:
    goodnode = False
    index = 0
    # find first node that has all its parents visited
    while not goodnode:
        # print(index, "index")
        node = nodes[nodesToVisit[index]]
        goodnode = True
        for parent in node.parents:
            if parent.name not in visited:
                goodnode = False
                break
        if not goodnode:
            index += 1
    route += node.name
    # add this node to visited
    visited = np.append(visited, node.name)
    # slice!
    nodesToVisit = np.append(nodesToVisit[0:index],nodesToVisit[index+1:])
    # add children of this node to nodes that have to be visited
    nodesToVisit = np.append(nodesToVisit, np.array(node.childrennames))
    # remove duplicates
    nodesToVisit = np.unique(nodesToVisit)


print("The answer to puzzle 1 of Dy 7 is", route)


#############################
#                           #
#           PART 2          #
#                           #
#############################

maxWorkers = 5
secondsPassed = 0

# find the nodes that have no parents, we can start with those!
nodesToVisit = np.array([])
for name in nodes:
    if len(nodes[name].parents)<1:
        nodesToVisit = np.append(nodesToVisit,name)
# let's go through the graph
nodesToVisit = np.sort(nodesToVisit)

route = ''
visited = np.array([])
workingOn = nodesToVisit[0:maxWorkers]
while len(nodesToVisit) >= 1:
    secondsPassed += 1
    newWorkingOn = np.array([])
    # work a second on the parts we are working on
    for i in range(len(workingOn)):
        node = nodes[workingOn[i]]
        node.workASecond()
        if node.done:
            visited = np.append(visited, node.name)
            route += node.name
            nodesToVisit = nodesToVisit[nodesToVisit != node.name]
            nodesToVisit = np.append(nodesToVisit, np.array(node.childrennames))
            nodesToVisit = np.unique(nodesToVisit)
        else:
            # not finished? work again on this node next round
            newWorkingOn = np.append(newWorkingOn, node.name)

    index = 0
    while len(newWorkingOn) < maxWorkers and index < len(nodesToVisit):
        node = nodes[nodesToVisit[index]]
        goodnode = True
        if node.name in newWorkingOn:
            goodnode = False
        for parent in node.parents:
            if parent.name not in visited:
                goodnode = False
                break
        if goodnode:
           newWorkingOn = np.append(newWorkingOn, node.name)
        index += 1

    workingOn = newWorkingOn



print("The answer to puzzle 2 of day 7 is", secondsPassed, "seconds along the following route:", route)
