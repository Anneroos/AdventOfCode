with open("input06.txt") as f:
    area = [line for line in f.read().split("\n")]

directions = {"W": (-1,0), "N": (0,-1), "E": (1,0), "S": (0,1)}
directionsOrder = "WNES"
w = len(area[0])
h = len(area)

lab = {}
for rowIdx in range(h):
    for colIdx in range(w):
        if area[rowIdx][colIdx] == "#":
            lab[(colIdx, rowIdx)] = "#"
        elif area[rowIdx][colIdx] == "^":
            startPos = (colIdx, rowIdx)
            startDir = "N"


def findPathGuard(grid, startPos, startDir):
    placeVisited = {}
    guardPos = startPos
    guardDir = startDir
    stuckInLoop = False
    stepsTaken = 0
    while stepsTaken < w*h:
        nextPos = (guardPos[0] + directions[guardDir][0], guardPos[1] + directions[guardDir][1])
        while nextPos in grid:
            guardDir = directionsOrder[(directionsOrder.index(guardDir) + 1)%4]
            nextPos = (guardPos[0] + directions[guardDir][0], guardPos[1] + directions[guardDir][1])
        if nextPos[0] < 0 or nextPos[1] < 0 or nextPos[0] >= w or nextPos[1] >= h:
            break
        else:
            guardPos = nextPos
            if guardPos in placeVisited and guardDir in placeVisited[guardPos]:
                stuckInLoop = True
                break
            placeVisited[guardPos] = placeVisited.get(guardPos, []) + [guardDir]
            stepsTaken += 1
    return stuckInLoop, stepsTaken, len(placeVisited.keys()), placeVisited


result1 = findPathGuard(lab, startPos, startDir)
placeVistitedOriginal = result1[3]
print(f"Day 06:\n  The guard visits {result1[2]} distinct positions.")

nrOfGoodObstructions = 0
for pos in placeVistitedOriginal: # An obstruction only does something when it is in the original path of the guard
    if pos != startPos and pos not in lab:
        newlab = lab.copy()
        newlab[pos] = "#"
        loop, steps, places, places = findPathGuard(newlab, startPos, startDir)
        if loop:
            nrOfGoodObstructions += 1

print(f"  We can choose {nrOfGoodObstructions} different place for an obstruction.")

