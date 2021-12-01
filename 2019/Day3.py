import math

text_file = open("input3a.txt", "r")
wires = text_file.read().split('\n')
wires[0] = wires[0].split(',')
wires[1] = wires[1].split(',')
print(wires)

wireDict = {}
minDistance2 = 100000000000
startPos = [0,0]
for wireindex in range(2):
    currentPosition = startPos.copy()
    wire=wires[wireindex]
    stepsCount = 0
    for step in range(len(wire)):
        instruction = wire[step]
        direction = instruction[0]
        nrOfSteps = int(instruction[1:])
        if direction == "R":
            dx = 1
            dy = 0
        elif direction == "L":
            dx = -1
            dy = 0
        elif direction == "U":
            dx = 0
            dy = 1
        elif direction == "D":
            dx = 0
            dy = -1
        for a in range(nrOfSteps):
            stepsCount += 1
            currentPosition[0] += dx
            currentPosition[1] += dy
            checkDict = wireDict.get((currentPosition[0], currentPosition[1]),["none",-1])
            if checkDict[0] == "none":
                wireDict[currentPosition[0], currentPosition[1]] = [wireindex, stepsCount]
            elif checkDict[0] == wireindex:
                pass
            elif checkDict[0] == 2:
                pass
            else:
                distance = checkDict[1] + stepsCount
                # for puzzle 2 we need this other distance
                wireDict[currentPosition[0], currentPosition[1]] = [2, distance]

                if distance < minDistance2:
                    minDistance2 = distance
                    winner2 = currentPosition

# puzzle 1
crossings = [[k,v] for k,v in wireDict.items() if v[0] == 2]
minDistance1 = 100000000000
for crossing in crossings:
    position = crossing[0]
    distance = abs(position[0]) + abs(position[1])
    if distance < minDistance1:
        minDistance1 = distance
        winner1 = position

print("Solution puzzle 1 of day 1", winner1, "with distance", minDistance1)
print("Solution puzzle 2 of day 1", winner2, "with distance", minDistance2)