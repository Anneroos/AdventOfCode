import math

with open("input14.txt") as f:
    lines = f.read().split("\n")

h = len(lines)
w = len(lines[0])

cubes = {}
stones = {}
for col in range(len(lines[0])):
    for row in range(len(lines)):
        char = lines[row][col]
        if char == "#":
            cubes[(row, col)] = 1
        elif char == "O":
            stones[(row, col)] = 1

def totalLoadNorthSupportBeam(stones):
    total = 0
    for stone in stones: # stone = (row,col)
        total += h-stone[0]
    return total

def tilt(dir, stones, cubes):
    newStones = {}
    if dir == "N":
        for col in range(len(lines[0])):
            lastCube = -1
            for row in range(len(lines)):
                if (row, col) in cubes:
                    lastCube = row
                elif (row, col) in stones:
                    newStones[(lastCube + 1,col)] = 1
                    lastCube += 1
    elif dir == "S":
        for col in range(len(lines[0])):
            lastCube = h
            for row in range(len(lines)-1, -1, -1):
                if (row, col) in cubes:
                    lastCube = row
                elif (row, col) in stones:
                    newStones[(lastCube - 1,col)] = 1
                    lastCube -= 1
    elif dir == "W":
        for row in range(len(lines)):
            lastCube = -1
            for col in range(len(lines[0])):
                if (row, col) in cubes:
                    lastCube = col
                elif (row, col) in stones:
                    newStones[(row, lastCube + 1)] = 1
                    lastCube += 1
    elif dir == "E":
        for row in range(len(lines)):
            lastCube = w
            for col in range(len(lines[0]) - 1, -1, -1):
                if (row, col) in cubes:
                    lastCube = col
                elif (row, col) in stones:
                    newStones[(row, lastCube - 1)] = 1
                    lastCube -= 1
    return newStones

def tiltCycle(stones, cubes):
    newStones = stones
    for dir in "NWSE":
        newStones = tilt(dir, newStones, cubes)
    return newStones

def printStones(stones,cubes): # Used for debugging
    for rowIdx in range(h):
        line = ""
        for colIdx in range(w):
            char = "#" if (rowIdx, colIdx) in cubes else ("O" if (rowIdx, colIdx) in stones else ".")
            line += char

def runAmountOfCycles(stones, cubes, cycles):
    newStones = stones.copy()
    history = {}
    cycleCount = 0
    while cycleCount < cycles:
        cycleCount += 1
        newStones = tiltCycle(newStones, cubes)
        state = tuple(sorted(newStones.keys()))
        if state not in history:
            history[state] = cycleCount
        else:
            historicCycleCount = history[state]
            loopLength = cycleCount - historicCycleCount
            cycleToGo = cycles - cycleCount
            loopsLeft = math.floor(cycleToGo/loopLength)
            remainder = cycleToGo - loopsLeft*loopLength
            finalstate = [k for k,v in history.items() if v == historicCycleCount + remainder][0]
            finalStones = {stone:1 for stone in finalstate}
            result = totalLoadNorthSupportBeam(finalStones)
            return result

    return -1

# part 1
newStones = tilt("N", stones.copy(), cubes)
result1 = totalLoadNorthSupportBeam(newStones)
print(f"Day 14:\n1) After tilting the platform north, the total load on the north support beams is {result1}.")

# part 2
result2 = runAmountOfCycles(stones, cubes, 1000000000)
print(f"2) After running the spin cycle for 1000000000 cycles, the total load on the north support beams is {result2}.")