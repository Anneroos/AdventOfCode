import math
with open("input18.txt") as f:
    input = [[int(k) for k in i.split(",")] for i in f.read().split("\n")]
bytes = []
for b in input:
    bytes.append(tuple(b))

def getNeighbors(p, size):
    ns = [(p[0]+1,p[1]), (p[0]-1,p[1]), (p[0],p[1]+1), (p[0],p[1]-1)]
    return [q for q in ns if 0<=q[0]<=size and 0<=q[1]<=size]

def findExit(bytesList, nrOfBytes, size):
    gridSize = size
    start = (0, 0)
    end = (gridSize, gridSize)
    distances = {start: 0}
    pointsToCheck = [start]
    while len(pointsToCheck) > 0:
        p = pointsToCheck.pop(0)
        if distances[p] + 1 <= distances.get(end, gridSize*gridSize):
            for n in getNeighbors(p, gridSize):
                if n not in bytesList[0:nrOfBytes]:
                    if distances.get(n, gridSize*gridSize) > distances[p] + 1:
                        pointsToCheck.append(n)
                        distances[n] = distances[p] + 1
    if end in distances:
        return True, distances[end]
    else:
        return False, -1


solution1 = findExit(bytes, 1024, 70)
print(f"Day 18:\n  1) The minimum number of steps needed to reach the exit is {solution1[1]}.")


# BINARY SEARCH
highestGood = 1024
lowestBad = len(bytes)

while lowestBad - highestGood > 1:
    n = math.floor((lowestBad + highestGood)/2)
    sol = findExit(bytes, n, 70)
    if sol[0] == True:
        highestGood = n
    elif sol[0] == False:
        lowestBad = n

print(f"  2) The coordinates of the first byte that will prevent the exit from being reachable from the starting position are {','.join([str(i) for i in bytes[highestGood]])}.")

