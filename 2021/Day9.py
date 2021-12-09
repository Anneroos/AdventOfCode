with open("input9.txt", "r") as f:
    input = f.read().splitlines()
cave = [[int(j) for j in i] for i in input]
m = len(cave)
n = len(cave[0])
flowDirection = {}

# Function to find the neighbors of a point, including the points itself, within the boundaries of the cave
def findNeighbors(point,minx, maxx, miny, maxy):
    neighbors = [point,[point[0]+1,point[1]],[point[0]-1,point[1]],[point[0],point[1]+1],[point[0],point[1]-1]]
    neighbors = [n for n in neighbors if n[0]>=minx and n[0] < maxx and n[1] >= miny and n[1]< maxy]
    return neighbors

# First determine the lowest neighbor for each point, and save that in the dictionairy flowDirection
for i in range(len(cave)):
    for j in range(len(cave[0])):
        localValue = cave[i][j]
        if localValue != 9:
            neighbors = findNeighbors([i,j],0,m,0,n)
            # The "lowest" neighbor(/itself) doesn't need to be unique! (check lower right corner of my input)
            # But I will just choose the first one, and trust that it will eventually flow to 1 point...
            lowestNeighbor = sorted(neighbors, key=lambda n: cave[n[0]][n[1]])[0]
            print([cave[n[0]][n[1]] for n in neighbors].count(cave[lowestNeighbor[0]][lowestNeighbor[1]]))
            print(i,j,[(n, cave[n[0]][n[1]]) for n in neighbors])
            flowDirection[(i, j)] = (lowestNeighbor[0],lowestNeighbor[1])

# Now follow the flow! Determine the final destination from each starting point
# By re-ordering the locations first, starting with the lowest heights, we only have to loop once through the locations
for key in sorted(flowDirection.keys(), key=lambda k: cave[k[0]][k[1]]):
    flowDirection[key] = flowDirection[flowDirection[key]]

lowPoints = set(flowDirection.values())
print(f"Part 1: The sum of the risk levels of all low points is {sum([cave[lowPoint[0]][lowPoint[1]] + 1 for lowPoint in lowPoints])}.")

basinSizes = sorted([list(flowDirection.values()).count(lowPoint) for lowPoint in lowPoints], reverse=True)
print(f"Part 2: The product of the sizes of the three largest basins is {basinSizes[0]*basinSizes[1]*basinSizes[2]}.")





# ORIGINAL UGLY SOLUTION
# with open("input9.txt", "r") as f:
#     input = f.read().splitlines()
# cave = [[int(j) for j in i] for i in input]
# m = len(cave)
# n = len(cave[0])
# totalRiskValue = 0
# lowPoints = []
# flowDirection = {}
#
#
# for i in range(len(cave)):
#     for j in range(len(cave[0])):
#         localValue = cave[i][j]
#         lowPoint=True
#         lowestNeighbor=(i,j)
#         for neighbor in [[-1,0],[1,0],[0,1],[0,-1]]:
#             x = i + neighbor[0]
#             y = j + neighbor[1]
#             if x>=0 and y>=0 and x < m and y < n:
#                 if cave[x][y] <= localValue:
#                     lowPoint = False
#                     if cave[x][y] < cave[lowestNeighbor[0]][ lowestNeighbor[1]]:
#                         lowestNeighbor = (x,y)
#                 flowDirection[(i,j)] = lowestNeighbor
#         if lowPoint:
#             totalRiskValue += localValue + 1
#             lowPoints.append([i,j])
# print(f"Part1: {totalRiskValue}.")
# print(flowDirection)
#
# for i in range(9):
#     for key in flowDirection.keys():
#         flowDirection[key] = flowDirection[flowDirection[key]]
# print(flowDirection)
# basins = {}
#
# for key in flowDirection.keys():
#     if cave[key[0]][key[1]] != 9:
#         basins[flowDirection[key]] = basins.get(flowDirection[key],0) + 1
# print(basins)
# basinValues = sorted(basins.values(), reverse=True)
# print(basinValues[0]*basinValues[1]*basinValues[2])