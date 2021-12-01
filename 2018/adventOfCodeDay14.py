import numpy as np
import time
t0 = time.time()

class Node:

    def __init__(self, value, nr):
        self.value = value
        self.number = nr
        self.prev = self
        self.next = self
    def setNext(self,next):
        self.next = next
        next.prev = self
    def setPrev(self, prev):
        self.prev = prev
        prev.next = self


def printNodeList(startNode, endNode, elf0, elf1):
    currentNode = startNode
    nodeList = ''
    recipe = str(currentNode.value)
    if currentNode == elf0:
        recipe = '(' + recipe + ')'
    elif currentNode == elf1:
        recipe = '[' + recipe + ']'
    nodeList += '  ' + recipe
    while currentNode != endNode:
        currentNode = currentNode.next
        recipe = str(currentNode.value)
        if currentNode == elf0:
            recipe = '(' + recipe + ')'
        elif currentNode == elf1:
            recipe = '[' + recipe + ']'
        nodeList += '  ' + recipe
    print(nodeList)

# printNodeList(startNode)

def printEndNodeList(node,number):
    currentNode = node
    while(currentNode.number > number+1):
        currentNode = currentNode.prev
    print("start at node ", currentNode.number)
    nodeList = currentNode.value * 10**9

    for i in range (1, 10):
        # print(nodeList)
        currentNode = currentNode.next
        nodeList += 10**(9-i) * currentNode.value
    print(nodeList)
    # print("{:09d}".format(nodeList))
    return("{:010d}".format(nodeList))


def computeRecipeList(maxNrOfRecipes):
    startNode = Node(3, 1)
    endNode = Node(7, 2)
    startNode.setNext(endNode)
    endNode.setNext(startNode)
    elf0 = startNode
    elf1 = endNode
    nrOfRecipes = 2
    while nrOfRecipes < maxNrOfRecipes + 10:

        score = elf0.value + elf1.value
        if score>=10:
            # print("score = " , score, "double digits!")
            newNode = Node(int(score/10),nrOfRecipes+1)
            newNode2 = Node(score%10,nrOfRecipes+2)

            endNode.setNext(newNode)
            endNode.next.setNext(newNode2)
            endNode = newNode2
            endNode.setNext(startNode)
            nrOfRecipes += 2
        else:
            # print("score = ", score, "one digit")
            newNode = Node(score,nrOfRecipes+1)
            endNode.setNext(newNode)
            endNode = newNode
            endNode.setNext(startNode)
            nrOfRecipes += 1

        for j in range(elf0.value+1):
            elf0 = elf0.next
        for j in range(elf1.value+1):
            elf1 = elf1.next
        # printNodeList(startNode,endNode, elf0,elf1)

    return printEndNodeList(endNode, maxNrOfRecipes)

def checkLastRecipes(endNode,recipeListToFind):
    currentNode = endNode
    rightList = True
    for i in range(1,len(recipeListToFind)+1):
        if currentNode.value != int(recipeListToFind[-i]):
            rightList = False
            break
        currentNode = currentNode.prev
    return rightList

def computeRecipeList2(recipeListToFind):
    startNode = Node(3, 1)
    endNode = Node(7, 2)
    startNode.setNext(endNode)
    endNode.setNext(startNode)
    elf0 = startNode
    elf1 = endNode
    nrOfRecipes = 2
    indexToMatch = 0

    timeToStop = False

    while not timeToStop :
        if nrOfRecipes %1000 == 0:
            print(nrOfRecipes)
        # print('indexToMatch: ', indexToMatch)

        score = elf0.value + elf1.value
        if score >= 10:
            # print("score = " , score, "double digits!")
            newNode = Node(int(score/10),nrOfRecipes+1)
            newNode2 = Node(score%10, nrOfRecipes+2)
            # print(newNode.value, newNode2.value)

            endNode.setNext(newNode)
            endNode = newNode
            nrOfRecipes += 1

            # print("2 recipes. 1: endnode.value", endNode.value, "int(recipeListToFind[indexToMatch])",int(recipeListToFind[indexToMatch])  )
            if endNode.value == int(recipeListToFind[indexToMatch]):
                # print(nrOfRecipes)
                indexToMatch += 1
                if indexToMatch == len(recipeListToFind):
                    timeToStop = True
            else:
                indexToMatch = 0
                if endNode.value == int(recipeListToFind[indexToMatch]):
                    indexToMatch += 1
            # print('indexToMatch: ', indexToMatch)

            endNode.setNext(newNode2)
            endNode = newNode2
            # print("2 recipes. 2: endnode.value", endNode.value, "int(recipeListToFind[indexToMatch])", int(recipeListToFind[indexToMatch]))

            endNode.setNext(startNode)
            nrOfRecipes += 1
            if (not timeToStop) and  endNode.value == int(recipeListToFind[indexToMatch]):
                indexToMatch += 1
                if indexToMatch == len(recipeListToFind):
                    timeToStop = True
            else:
                if  not timeToStop :
                    indexToMatch = 0
                if endNode.value == int(recipeListToFind[indexToMatch]):
                    indexToMatch += 1
            # print('indexToMatch: ', indexToMatch)
        else:
            # print("score = ", score, "one digit")
            newNode = Node(score,nrOfRecipes+1)
            endNode.setNext(newNode)
            endNode = newNode
            endNode.setNext(startNode)
            nrOfRecipes += 1
            # print("endnode.value", endNode.value, "int(recipeListToFind[indexToMatch])",
            #       int(recipeListToFind[indexToMatch]))
            if str(endNode.value) == recipeListToFind[indexToMatch]:
                indexToMatch += 1
            else:
                indexToMatch = 0
                if endNode.value == int(recipeListToFind[indexToMatch]):
                    indexToMatch += 1

        for j in range(elf0.value+1):
            elf0 = elf0.next
        for j in range(elf1.value+1):
            elf1 = elf1.next
        # printNodeList(startNode,endNode, elf0,elf1)
        if indexToMatch >= len(recipeListToFind):
            timeToStop = True

    return(nrOfRecipes - len(str(recipeListToFind)))


# print("The answer to puzzle 1 of day 1:", computeRecipeList(760221))

def computeRecipeList3(recipeListToFind):
    recipes = np.zeros(100000000).astype(int)
    recipes[0:2] = [3,7]
    # recipes = np.array([3,7])

    elf0 = 0
    elf1 = 1
    nrOfRecipes = 2
    indexToMatch = 0

    timeToStop = False

    while not timeToStop and nrOfRecipes < 10000000000:
        # if nrOfRecipes % 10 == 0:
        #     print(nrOfRecipes)
        # print(recipes[0:10])

        score = recipes[elf0] + recipes[elf1]
        if score >= 10:
            # print("score = " , score, "double digits!")
            # recipes = np.append(recipes,[int(score/10),score%10])
            recipes[nrOfRecipes] = int(score/10)
            recipes[nrOfRecipes+1] = score%10
            nrOfRecipes += 1

            if recipes[nrOfRecipes-1] == int(recipeListToFind[indexToMatch]):
                indexToMatch += 1
                if indexToMatch == len(recipeListToFind):
                    timeToStop = True
                    return (nrOfRecipes - len(str(recipeListToFind)))
            else:
                indexToMatch = 0
                if recipes[nrOfRecipes-1] == int(recipeListToFind[indexToMatch]):
                    indexToMatch += 1

            nrOfRecipes += 1
            if (not timeToStop) and  recipes[nrOfRecipes-1] == int(recipeListToFind[indexToMatch]):
                indexToMatch += 1
                if indexToMatch == len(recipeListToFind):
                    timeToStop = True
            else:
                if  not timeToStop :
                    indexToMatch = 0
                    if recipes[nrOfRecipes-1] == int(recipeListToFind[indexToMatch]):
                        indexToMatch += 1

        else:
            # print("score = ", score, "one digit")
            # recipes = np.append(recipes,score)
            recipes[nrOfRecipes] = score
            nrOfRecipes += 1
            # print("endnode.value", endNode.value, "int(recipeListToFind[indexToMatch])",
            #       int(recipeListToFind[indexToMatch]))
            if recipes[nrOfRecipes-1] == int(recipeListToFind[indexToMatch]):
                indexToMatch += 1
            else:
                indexToMatch = 0
                if recipes[nrOfRecipes-1] == int(recipeListToFind[indexToMatch]):
                    indexToMatch += 1

        elf0 = (elf0 + 1 + recipes[elf0]) % nrOfRecipes
        elf1 = (elf1 + 1 + recipes[elf1]) % nrOfRecipes
        # print(elf0,elf1,len(recipes),recipes)

        if indexToMatch >= len(recipeListToFind):
            timeToStop = True

    return(nrOfRecipes - len(str(recipeListToFind)))

# print("The answer to puzzle 2 of day 1:", computeRecipeList3('51589'))
# print("The answer to puzzle 2 of day 1:", computeRecipeList3('01245'))
# print("The answer to puzzle 2 of day 1:", computeRecipeList3('92510'))
# print("The answer to puzzle 2 of day 1:", computeRecipeList3('59414'))
print("The answer to puzzle 2 of day 1:", computeRecipeList3('760221'))
# print("The answer to puzzle 2 of day 1:", computeRecipeList3('101'))

t1 = time.time()

print("time: ", t1-t0)