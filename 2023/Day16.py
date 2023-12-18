with open("input16.txt") as f:
    lines = f.read().split("\n")

w = len(lines[0])
h = len(lines)

mirrors = {}
for row in range(h):
    for col in range(w):
        char = lines[row][col]
        if char in "|-\/":
            mirrors[(row, col)] = char

def nextPoint(point,dir):
    if dir == "E":
        return (point[0], point[1] + 1)
    if dir == "W":
        return (point[0], point[1] - 1)
    if dir == "N":
        return (point[0] - 1, point[1])
    if dir == "S":
        return (point[0] + 1, point[1])

def nextDir(dir, mirror):
    if mirror == "|":
        if dir in "EW":
            return ["S", "N"]
        elif dir in "NS":
            return dir
    elif mirror == "-":
        if dir in "NS":
            return ["E", "W"]
        elif dir in "EW":
            return dir
    elif mirror == "/":
        if dir == "W":
            return ["S"]
        elif dir == "E":
            return ["N"]
        elif dir == "S":
            return ["W"]
        elif dir == "N":
            return ["E"]
    elif mirror == "\\":
        if dir == "W":
            return ["N"]
        elif dir == "E":
            return ["S"]
        elif dir == "S":
            return ["E"]
        elif dir == "N":
            return ["W"]
    return []

def getNrOfEnergizedTiles(start):
    pointsToCheck = [start]
    energized = {}
    history = []
    while pointsToCheck:
        point = pointsToCheck.pop(0)
        history.append(point)
        if 0 <= point[0] < h and 0 <= point[1] < w:
            energized[(point[0], point[1])] = 1
        row = point[0]
        col = point[1]
        dir = point[2]
        nextPos = nextPoint((point[0],point[1]), dir)
        if not (0 <= nextPos[0] < h and 0 <= nextPos[1] < w):
            continue
        nextDirs = dir if nextPos not in mirrors.keys() else nextDir(dir, mirrors[nextPos])
        for nextD in nextDirs:
            nextP = (nextPos[0], nextPos[1], nextD)
            if nextP not in pointsToCheck and nextP not in history:
                pointsToCheck.append(nextP)
    return sum(energized.values())

print(f"Day 16:\n1) With the beam starting in the top-left heading right, {getNrOfEnergizedTiles((0,-1,'E'))} tiles end up being energized.")

# Part 2
startsE = [(row, -1, "E") for row in range(h)]
startsW = [(row, w, "W") for row in range(h)]
startsS = [(-1, col, "S") for col in range(w)]
startsN = [(h, col, "N") for col in range(w)]
allStarts = startsE + startsW + startsN + startsS
maxEnergized = 0
bestStartPos = ()
for start in allStarts:
    energized = getNrOfEnergizedTiles(start)
    if energized >= maxEnergized:
        maxEnergized = energized
        bestStartPos = start

print(f"2) The best initital beam configuration energizes {maxEnergized} tiles.")