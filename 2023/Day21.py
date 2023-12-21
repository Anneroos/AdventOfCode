import math

with open("input21.txt") as f:
    lines = f.read().split("\n")
w = len(lines[0])
h = len(lines)
garden = {}  # 1 means you can walk there, 0 is you can't walk there
startPoint = (0,0)
for rowIdx, line in enumerate(lines):
    line = lines[rowIdx]
    for colIdx in range(len(line)):
        if line[colIdx] == ".":
            garden[(rowIdx, colIdx)] = 1
        elif line[colIdx] == "S":
            startPoint = (rowIdx, colIdx)
            garden[(rowIdx, colIdx)] = 1

def getNeighbors1(point):
    possibleNeighbors = [(point[0] + 1, point[1]), (point[0] - 1, point[1]), (point[0], point[1] + 1), (point[0], point[1] - 1)]
    return [p for p in possibleNeighbors if p in garden and 0 <= p[0] < h and 0 <= p[1] < w]

def getNrOfPointsFromStartPoint(start, steps):
    reachable = {} # (x,y) : 1 if reachable in odd nr of steps, 0 in even number of steps
    step = 0
    pointsToCheck = [start]
    while step <= steps:
        newPointsToCheck = []
        while pointsToCheck:
            point = pointsToCheck.pop(0)
            reachable[point] = step % 2
            neighbors = getNeighbors1(point)
            newPointsToCheck = newPointsToCheck + [n for n in neighbors if n not in newPointsToCheck and n not in reachable]
        step += 1
        pointsToCheck = newPointsToCheck
    return len([k for k,v in reachable.items() if v == (steps % 2)])

print(f"Day 21:\n1) The Elf can reach {getNrOfPointsFromStartPoint(startPoint,64)} garden plots in 64 steps.")

# Part 2

# On a closer look in the data, from the S going horizontally and vertically, there are just straight paths to the edges!
# This helps going around, since now we sort of have a Manhattan distance from one copy to another copy of the garden.
# Also, around the perimeter there is complete empty path. :)
# Also some spots you can only reach after an even number of steps, and some only after an odd number of steps.
# But the width and length of the garden are both odd. So in copies of gardens next to each other, you can
# reach alternatingly the 'even' set or the 'odd' set.

# Note: stepsToTake is odd. So in the first starting garden, you can ultimately only reach 'odd' points.
# In the 4 gardens surrounding it, you can reach only 'even' points. Etc.

# Note: stepsToTake = 202300 * 131 + 65. Suspicous!

# Note: after 131 steps you can reach all the (odd) points in the garden, and in 130 steps all the 'even' points.
# How many

fullEven = getNrOfPointsFromStartPoint(startPoint,w-1) # 7406
fullOdd = getNrOfPointsFromStartPoint(startPoint,w) # 7282

# Oh, there are 14697 '.'s in the garden, which is more than 7406+7282, but that's because some are completely surrounded by rocks.
# Also, after 131 steps you can be in the middle of new garden-copy!
# The centers you can reach form a sort of diamond shape <>

# stepsToTake is an odd number, so you can reach all 'odd' points in the original
# garden. In the 'diamond ring' around that garden (4 gardens), the elf can reach all the 'even' points. In the next
# diamond ring around that (consisting of 8 gardens) the elf can reach all 'odd' points again, and then a ring of 12
# gardens with 'even' points again. Etc.
# But in the end then there are some 'incomplete' gardens. Sort of 3 types, in 4 directions. Figure it out yourself. ;)
# Check my beautiful picture :P

# How many full ones?
# aantal keer fullOdd   = 1 + 8 + 16 + 24 + .. = 1 + 8*(1+2+3+....+ 101149) = 1 + (101149*101150 ) * 4
#                       = 202299^2
# aantal keer fullEven  = 4 + 12 + 20 + 28 + ... = (1 + 3 + 5 + 7 + ... + 202300-1) * 4 = (202300/2)^2 * 2^2
#                       = 202300^2
stepsToTake = 26501365

timesGarden = int(math.floor(stepsToTake/w))
rest = stepsToTake % w

top130 = getNrOfPointsFromStartPoint((0,(w-1)/2),w-1)
bottom130 = getNrOfPointsFromStartPoint((w-1,(w-1)/2),w-1)
left130 = getNrOfPointsFromStartPoint(((w-1)/2,0),w-1)
right130 = getNrOfPointsFromStartPoint(((w-1)/2,w-1),w-1)

bottomleft195 = getNrOfPointsFromStartPoint((w-1,0),w + rest - 1)
bottomright195 = getNrOfPointsFromStartPoint((w-1,w-1),w + rest - 1)
topleft195 = getNrOfPointsFromStartPoint((0,0),w + rest - 1)
topright195 = getNrOfPointsFromStartPoint((0,w-1),w + rest - 1)

bottomleft64 = getNrOfPointsFromStartPoint((w-1,0),rest - 1)
bottomright64 = getNrOfPointsFromStartPoint((w-1,w-1),rest - 1)
topleft64 = getNrOfPointsFromStartPoint((0,0),rest - 1)
topright64 = getNrOfPointsFromStartPoint((0,w-1),rest - 1)

total = fullOdd * (timesGarden - 1) * (timesGarden - 1) + fullEven * timesGarden * timesGarden + top130 + bottom130 + left130 + right130
total += (bottomleft195 + bottomright195 + topleft195 + topright195) * (timesGarden - 1)
total += (bottomleft64 + bottomright64 + topleft64 + topright64) * timesGarden

print(f"2) The Elf can reach {total} garden plots in {stepsToTake} steps.")
# 601113643448699