# 08-12-2021
favoriteNumber = 1352
def checkIfWall(x,y):
    t = x*x + 3*x + 2*x*y + y*y + y + favoriteNumber
    return list(bin(t))[2:].count("1")%2
distances = {(1,1):0}
pointsToCheck = [(1,1)]
while len(pointsToCheck)>0 and not ((31,39) in distances.keys() and 51 in distances.values()):
    point = pointsToCheck.pop(0)
    for buurbouwer in [[-1,0],[0,1],[1,0],[0,-1]]:
        x = point[0] + buurbouwer[0]
        y = point[1] + buurbouwer[1]
        if x >= 0 and y >= 0:
            if (x,y) not in distances.keys():
                if not checkIfWall(x,y):
                    distances[(x,y)] = distances[point] + 1
                    pointsToCheck.append((x,y))
                else:
                    distances[(x, y)] = -1
print(f"Part 1: Point (31,39) is at distance {distances[(31,39)]} from (1,1).")
print(f"Part 2: There are {sum([1 for d in distances.values() if d <= 50 and d >= 0])} reachable points within a distance of 50 of (1,1).")