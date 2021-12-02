#01-12-2021
with open("input1.txt","r") as f:
    n=f.read().split(', ')

directions=[[0,1],[1,0],[0,-1],[-1,0]]
currentX = 0
currentY = 0
currentDirection = 0
visitedPositions = [(0,0)]
firstRepeatedPostion = []
for instruction in n:
    if instruction[0] == "L":
        currentDirection = (currentDirection + 3) % 4
    else:
        currentDirection = (currentDirection + 1) % 4
    blocksToWalk = int(instruction[1:])
    for i in range(1,blocksToWalk+1):
        if (currentX+i*directions[currentDirection][0],currentY+i*directions[currentDirection][1]) in visitedPositions and len(firstRepeatedPostion) == 0:
            firstRepeatedPostion = [currentX+i*directions[currentDirection][0],currentY+i*directions[currentDirection][1]]
        else:
            visitedPositions += [(currentX+i*directions[currentDirection][0],currentY+i*directions[currentDirection][1])]
    currentX += blocksToWalk * directions[currentDirection][0]
    currentY += blocksToWalk * directions[currentDirection][1]

print(f"Solution Day 1 part A: Easter Bunny HQ is located at ({currentX},{currentY}), which is {abs(currentX) + abs(currentY)} blocks away.")
print(f"Solution Day 1 part B: Easter Bunny HQ is located at {firstRepeatedPostion}, which is {abs(firstRepeatedPostion[0]) + abs(firstRepeatedPostion[1])} blocks away.")
