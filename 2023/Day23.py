with open("input23.txt") as f:
    lines = f.read().split("\n")
w = len(lines[0])
h = len(lines)
startpoint = (0,1)
endpoint = (h-1, w-2)

def getNeighbors(p):
    poss = [(p[0] + 1, p[1]), (p[0] - 1, p[1]), (p[0], p[1] + 1), (p[0], p[1] - 1)]
    return [p for p in poss if 0 <= p[0] < h and 0 <= p[1] < w]

# Find all intersections, to reduce the problem to a simpler 'graph'
initialIntersections = {startpoint: {}, endpoint: {}}
for rowIdx, line in enumerate(lines):
    for colIdx, char in enumerate(line):
        if char == ".":
            t = [lines[n[0]][n[1]] for n in getNeighbors((rowIdx, colIdx)) if lines[n[0]][n[1]] != "#"]
            if len(t) > 2:
                initialIntersections[(rowIdx, colIdx)] = {}

def findDistancesBetweenIntersections(part, intersections):
    for intersection in intersections:
        pointsToCheck = [intersection]
        history = []
        neighboringIntersections = {}
        distances = {intersection: 0}
        while pointsToCheck:
            p = pointsToCheck.pop(0)
            history.append(p)
            neighbors = [n for n in getNeighbors(p) if lines[n[0]][n[1]] != "#"]
            for n in neighbors:
                if n not in history and n not in pointsToCheck:
                    distances[n] = distances[p] + 1
                    if part == 1:
                        nchar = lines[n[0]][n[1]]
                        if nchar == ".":
                            if n in intersections:
                                neighboringIntersections[n] = distances[n]
                            else:
                                pointsToCheck.append(n)
                        else:
                            if nchar == ">" and n[1] > p[1] or nchar == "<" and n[1] < p[1] or nchar == "v" and n[0] > p[0] or nchar == "^" and n[0] < p[0]:
                                pointsToCheck.append(n)
                    elif part == 2:
                        if lines[n[0]][n[1]] != "#":
                            if n in intersections:
                                neighboringIntersections[n] = distances[n]
                            else:
                                pointsToCheck.append(n)
        intersections[intersection] = neighboringIntersections
    return intersections

def findLongestRoute(part):
    intersections = findDistancesBetweenIntersections(part, initialIntersections)
    longestRoute = -1
    pathsToCheck = [[[(startpoint)], 0]]
    while pathsToCheck:
        path, distance = pathsToCheck.pop(-1) # This -1 was essential. The difference between neverending and few minutes.
        for p, pdist in intersections[path[-1]].items():
            if p not in path:
                newdist = distance + pdist
                if p == endpoint:
                    if newdist > longestRoute:
                        longestRoute = newdist
                else:
                    pathsToCheck.append([path + [p], newdist])
    return longestRoute

print(f"Day 23:")
print(f"1) The longest hike is {findLongestRoute(1)} steps long.")
print(f"2) The longest hike through the surprisingly dry hiking trails is {findLongestRoute(2)} steps long.")