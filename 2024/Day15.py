with open("input15.txt") as f:
    warehouse_input, dirs = f.read().split("\n\n")
    warehouse_input = warehouse_input.split("\n")
    dirs = "".join(dirs.split("\n"))

h = len(warehouse_input)
w = len(warehouse_input[0])
warehouse = {}
warehouseWide = {}
robotPos = (0,0)
robotPosWide = (0,0)

for lineIdx in range(len(warehouse_input)):
    line= warehouse_input[lineIdx]
    for colIdx in range(len(line)):
        char = line[colIdx]
        if char == "#":
            warehouse[(colIdx, lineIdx)] = char
            warehouseWide[(2 * colIdx, lineIdx)] = "#"
            warehouseWide[(2 * colIdx + 1, lineIdx)] = "#"
        elif char == "O":
            warehouse[(colIdx, lineIdx)] = char
            warehouseWide[(2*colIdx, lineIdx)] = "["
            warehouseWide[(2 * colIdx + 1, lineIdx)] =  "]"
        elif char == "@":
            robotPos = (colIdx, lineIdx)
            robotPosWide = (2 * colIdx, lineIdx)


def printWarehouse(wh, w, h, robotPos):
    for y in range(h):
        line = ""
        for x in range(w):
            if (x,y) == robotPos:
                line += "@"
            elif (x,y) in wh:
                line += wh[(x,y)]
            else:
                line += "."
        print(line)

def getNextLocation(loc,dir):
    if dir == "^":
        return (loc[0], loc[1]-1)
    elif dir == ">":
        return (loc[0]+1, loc[1])
    elif dir == "v":
        return (loc[0], loc[1]+1)
    elif dir == "<":
        return (loc[0]-1, loc[1])
    else:
        return (-1,-1)

def lookForEmptySpace(warehouse, pos, dir):
    loc = pos
    next = getNextLocation(loc,dir)
    while next in warehouse and warehouse[next] != "#":
        next = getNextLocation(next,dir)
    if next not in warehouse:
        return True, next
    elif warehouse[next] == "#":
        return False, next


for dir in dirs:
    nextLoc = getNextLocation(robotPos, dir)
    b, p = lookForEmptySpace(warehouse, robotPos, dir)

    if not b:
        pass
    elif p == nextLoc: # neighboring space is just empty
        robotPos = nextLoc
    elif b: # if there is an empty space ahead, but some boxes in the way
        robotPos = nextLoc
        warehouse[p] = warehouse[nextLoc]
        warehouse.pop(nextLoc)

def computeScore(wh):
    score = 0
    for pos in wh:
        if wh[pos] in "O[":
            score += pos[0] + 100 * pos[1]
    return score

print(f"Day 15:\n  1) The sum of all boxes' final GPS coordinates is {computeScore(warehouse)}.")

# --------- PART 2 --------


def findBoxesToBeMoved(wh, originalPos, dir):
    positionsToMove = []
    positionsToCheck = [originalPos]
    positionsChecked = []
    possibleToMove = True
    while len(positionsToCheck) > 0 :
        pos = positionsToCheck.pop(0)
        positionsChecked += [pos]
        if pos not in wh:
            pass
        else:
            if wh[pos] == "[":
                positionsToMove += [pos]
                otherside = (pos[0]+1, pos[1])
                if otherside not in positionsToCheck and otherside not in positionsChecked:
                    positionsToCheck += [otherside]
            elif wh[pos] == "]":
                positionsToMove += [pos]
                otherside = (pos[0] - 1, pos[1])
                if otherside not in positionsToCheck and otherside not in positionsChecked:
                    positionsToCheck += [otherside]
            elif wh[pos] == "#":
                possibleToMove = False
                break
            if dir == "^":
                above = (pos[0], pos[1] - 1)
                if above not in positionsToCheck and above not in positionsChecked:
                    positionsToCheck += [above]
            elif dir == "v":
                below = (pos[0], pos[1] + 1)
                if below not in positionsToCheck and below not in positionsChecked:
                    positionsToCheck += [below]
    return possibleToMove, positionsToMove



for dir in dirs:
    nextLoc = getNextLocation(robotPosWide, dir)
    b, p = lookForEmptySpace(warehouseWide, robotPosWide, dir)
    # print(b,p)
    if not b:
        pass
    elif p == nextLoc: # neighboring space is just empty
        robotPosWide = nextLoc
    elif b: # if there is an empty space ahead, but some boxes in the way
        if dir in "<>":
            plusminus = -1 if dir == ">" else +1
            for x in range(p[0], nextLoc[0], plusminus):
                warehouseWide[(x,p[1])] = warehouseWide[(x + plusminus, p[1])]
            warehouseWide.pop(nextLoc)
            robotPosWide = nextLoc
        else:
            possibleToMove, boxesToBeMoved = findBoxesToBeMoved(warehouseWide, nextLoc, dir)
            if possibleToMove:
                temp = {p:warehouseWide[p] for p in boxesToBeMoved}
                for p in boxesToBeMoved:
                    warehouseWide.pop(p)
                for p in boxesToBeMoved:
                    movedP = getNextLocation(p, dir)
                    warehouseWide[movedP] = temp[p]
                robotPosWide = nextLoc

print(f"  2) The sum of all boxes' final GPS coordinates in the wide warehouse is {computeScore(warehouseWide)}.")

