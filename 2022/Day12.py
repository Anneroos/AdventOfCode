with open("input12.txt") as f:
    lines =  f.read().split("\n")
h = len(lines)
w = len(lines[0])

# Find S and E
S = (0,0)
E = (0, 0)
for lineIdx in range(len(lines)):
    if "S" in lines[lineIdx]:
        S = (lineIdx, lines[lineIdx].index("S"))
    if "E" in lines[lineIdx]:
        E = (lineIdx, lines[lineIdx].index("E"))
# Translate letters a-z to numbers 0-25
area = [[ord(t)-97 for t in y] for y in lines]
# Also fill in the correct value for the starting point and the end point
area[S[0]][S[1]] = 0
area[E[0]][E[1]] = 25

def getNeighbors(point,max1, max2):
    # Every point has four neighbors: right, left, down and up.
    n = [(point[0] + 1, point[1]), (point[0] - 1, point[1]), (point[0], point[1] + 1), (point[0], point[1] - 1)]
    # Only return those neighbors that are within the grid
    return [x for x in n if 0 <= x[0] < max1 and 0 <= x[1] < max2 ]

def getShortestDistance(startPoint, endPoint):
    distances = {startPoint:0}
    U = [startPoint]
    while len(U)>0:
        point = U.pop(0)
        height = area[point[0]][point[1]]
        neighbors = getNeighbors(point, h, w)
        for n in neighbors:
            height_n = area[n[0]][n[1]]
            if height_n <= height + 1:
                if n not in distances or distances[n] > distances[point] + 1:
                    U.append(n)
                    distances[n] = distances[point] + 1
    if endPoint in distances:
        return distances[endPoint]
    else:
        return -1
# Part 1: compute the shortest distance from S to E
print(f"Day 12:\n1) The fewest steps required to move from my current position to the location that should get the best signal is {getShortestDistance(S,E)}.")

# Part 2: Find a starting point x for which the route from x to E is the shortest
minDist = h*w
winningStartPoint = (0,0)
for i in range(h):
    for j in range(w):
        if area[i][j] == 0:
            newDist = getShortestDistance((i,j),E)
            if newDist != -1 and newDist < minDist:
                minDist = newDist
                winningStartPoint = (i,j)
print(f"2) The fewest steps required to move starting from any square with elevation a to the location that should get the best signal is {minDist}.")

