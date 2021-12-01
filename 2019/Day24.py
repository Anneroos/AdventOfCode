import numpy as np
import math

text_file = open("input24.txt", "r")
input = text_file.read().split('\n')
text_file.close()

lines = np.array(input)
width = len(lines[0])
height = len(lines)
print(lines)
dict = {'#':1, ".":0}
array = np.zeros((width,height))


bugDict = {}
for j in range(len(lines)):
    for i in range(len(lines[j])):
        array[i][j] = dict[lines[i][j]]
        bugDict[(i,j,0)] = {"bug": dict[lines[i][j]]}

print(array)

history = [array]
lastarray = array.copy()
Found = False
attempts = 0
while not Found and attempts < 1000:
    attempts += 1
    nextarray = lastarray.copy()
    for i in range(width):
        for j in range(height):
            nrOfBugs = 0
            if i > 0:
                nrOfBugs += lastarray[i-1][j]
            if i < width-1:
                nrOfBugs += lastarray[i+1][j]
            if j > 0:
                nrOfBugs += lastarray[i][j-1]
            if j < height - 1:
                nrOfBugs += lastarray[i][j+1]

            if lastarray[i][j] == 1 and nrOfBugs != 1:
                nextarray[i][j] = 0
            elif lastarray[i][j] == 0 and nrOfBugs in [1, 2]:
                nextarray[i][j] = 1
            else:
                pass # don't change current state


    # print(nextarray)
    for historicArray in history:
        if np.array_equal(historicArray, nextarray):
            print("FOOUUNNDD IITTT!")
            print(nextarray)
            Found = True
            break
    history.append(nextarray)
    lastarray = nextarray.copy()

# print(history)
diversity = 0
power2 = 1
for i in range(width):
    for j in range(height):
        diversity += nextarray[i][j]*power2
        power2 *= 2
print("Solution to puzzle 1 of day 24:", int(diversity))

minLevel = 0
maxLevel = 0

for minute in range(200):
    # create new layer of empty grids if necessary (if current lowest level has no bugs, no new one needed)
    minLevelBugs = 0
    maxLevelBugs = 0
    for location in bugDict.keys():
        minLevel = min(minLevel, location[2])
        maxLevel = max(maxLevel, location[2])
    print("Min level", minLevel, "max level", maxLevel)
    for location in bugDict.keys():
        if location[2] == minLevel:
            minLevelBugs += bugDict[location]["bug"]
        if location[2] == maxLevel:
            maxLevelBugs += bugDict[location]["bug"]
    if minLevelBugs > 0:
        print("Time for new min level")
        for i in range(5):
            for j in range(5):
                if j != 2 or i != 2:
                    bugDict[(i,j,minLevel-1)] = {"bug":0}
    if maxLevelBugs > 0:
        print("Time for new max level")
        for i in range(5):
            for j in range(5):
                if j != 2 or i != 2:
                    bugDict[(i,j,maxLevel+1)] = {"bug":0}
    # for each bug location, compute next bugsituation

    for location in bugDict.keys():
        # upper neighbors
        upperNeighbors = 0
        if location[0] == 0:
            upperNeighbors += bugDict.get((1,2,location[2]-1),{}).get("bug",0)
        elif location[0] == 3 and location[1] == 2:
            for k in range(5):
                upperNeighbors += bugDict.get((4,k,location[2]+1),{}).get("bug",0)
        else:
            upperNeighbors += bugDict.get((location[0]-1,location[1],location[2]),{}).get("bug",0)

        # lower neighbors

        lowerNeighbors = 0
        if location[0] == 4:
            lowerNeighbors += bugDict.get((3,2,location[2]-1),{}).get("bug",0)
        elif location[0] == 1 and location[1] == 2:
            for k in range(5):
                lowerNeighbors += bugDict.get((0,k,location[2]+1),{}).get("bug",0)
        else:
            lowerNeighbors += bugDict.get((location[0]+1,location[1],location[2]),{}).get("bug",0)

        # left neighbors

        leftNeighbors = 0
        if location[1] == 0:
            leftNeighbors += bugDict.get((2, 1, location[2] - 1),{}).get("bug", 0)
        elif location[0] == 2 and location[1] == 3 :
            for k in range(5):
                leftNeighbors += bugDict.get((k, 4, location[2] + 1),{}).get("bug", 0)
        else:
            leftNeighbors += bugDict.get((location[0], location[1]-1, location[2]),{}).get("bug", 0)


        # right neighbors

        rightNeighbors = 0
        if location[1] == 4:
            rightNeighbors += bugDict.get((2, 3, location[2] - 1),{}).get("bug", 0)
        elif location[0] == 2 and location[1] == 1 :
            for k in range(5):
                rightNeighbors += bugDict.get((k, 0, location[2] + 1),{}).get("bug", 0)
        else:
            rightNeighbors += bugDict.get((location[0], location[1] + 1, location[2]),{}).get("bug", 0)

        neighborBugs = upperNeighbors + lowerNeighbors + leftNeighbors + rightNeighbors
        if bugDict.get(location)["bug"] == 1 and neighborBugs != 1:
            bugDict[location]["nextbug"] = 0
        elif bugDict.get(location)["bug"] == 0 and neighborBugs in [1, 2]:
            bugDict[location]["nextbug"] = 1
        else:
            bugDict[location]["nextbug"] = bugDict[location]["bug"]
    # update each buglocation
    for location in bugDict.keys():
        bugDict[location]["bug"] = bugDict[location]["nextbug"]

totalBugsAfter200 = 0
for location in bugDict.keys():
    totalBugsAfter200 += bugDict[location]["bug"]


print("Total bugs, hopefully", totalBugsAfter200)

