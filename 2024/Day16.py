with open("input16.txt") as f:
    input = f.read().split("\n")
w=len(input[0])
h=len(input)
maze = {}
startPos = (0,0)
endPos = (0,0)
# Read the input and convert to maze to dictionary
for y in range(len(input)):
    line = input[y]
    for x in range(len(line)):
        char = line[x]
        if char in ".SE":
            maze[(x,y)] = w*h*1000
        if char == "S":
            startPos = (x,y)
        elif char == "E":
            endPos = (x,y)

# We'll Dijkstra our way through the graph
pointsToCheck = [(startPos,"E")]
scores = {(startPos, "E"):0}
endPointReached = False
endPointMin = w*h*1000
routes = {(startPos,"E"): [startPos]}

while len(pointsToCheck) > 0:
    pd = pointsToCheck.pop(0)
    p = pd[0]
    dir = pd[1]
    if p == endPos:
        endPointReached = True
        endPointMin = min(endPointMin, scores[pd])
    if endPointReached and scores[pd] > endPointMin:
        continue
    neighbors = (p[0]+1, p[1]), (p[0], p[1]+1), (p[0]-1, p[1]), (p[0], p[1]-1)
    dirs = "ESWN"
    for idx in [0,1,3]:
        n = neighbors[(dirs.index(dir) + idx) % 4]
        d = dirs[(dirs.index(dir) + idx) % 4]
        nd = (n, d)
        score = 1 if idx == 0 else 1001
        if n in maze and scores.get(nd, w*h*1000) >= scores.get(pd) + score:
            if nd not in routes:
                routes[nd] = routes[pd] + [n] if n not in routes[pd] else routes[pd]
                if nd not in pointsToCheck:
                    pointsToCheck.append(nd)
            else:
                if scores[nd] > scores.get(pd) + score:
                    routes[nd] = routes[pd] + [n] if n not in routes[pd] else routes[pd]
                    if nd not in pointsToCheck:
                        pointsToCheck.append(nd)
                elif scores[nd] == scores.get(pd) + score:
                    routes[nd] = routes[pd] + [point for point in routes[nd] if point not in routes[pd]]
            scores[nd] = scores.get(pd) + score

endScores = [scores.get((endPos, dir), w*h*1000) for dir in "ESWN"]
endDir = "ESWN"[endScores.index(min(endScores))]

print(f"Day 16:\n  1) The lowest score a Reindeer could possibly get is {min(endScores)}.")
print(f"  2) There are {len(routes[(endPos, endDir)])} tiles that are part of at least one of the best paths through the maze.")

