import math
with open("input20.txt") as f:
    input = f.read().split("\n")

# Parse input
h = len(input)
w = len(input[0])
paths = {}
start = (0,0)
end = (0,0)
for lineIdx in range(h):
    line = input[lineIdx]
    for colIdx in range(w):
        char = line[colIdx]
        if char in "SE.":
            paths[(colIdx, lineIdx)] = 1
        if char == "S":
            start = (colIdx, lineIdx)
        if char == "E":
            end = (colIdx, lineIdx)

#  Find shortest distance from start to each point on the path
pointsToCheck = [start]
distances = {start: 0}
while len(pointsToCheck) > 0:
    p = pointsToCheck.pop(0)
    ns = [(p[0] + 1, p[1]), (p[0] - 1, p[1]), (p[0], p[1] + 1), (p[0], p[1] - 1)]
    for n in ns:
        if n in paths:
            if distances.get(n, w*h) > distances[p]:
                distances[n] = distances[p] + 1
                pointsToCheck.append(n)

# Now we will check how much time we save by trying to cheat from each point on the path. Part 1 and 2 combined.
nrOfCheatsPart1 = 0
nrOfCheatsPart2 = 0
for x in range(1,w):
    for y in range(1,h):
        if (x,y) in paths:
            for dx in range(-20,21):
                for dy in range(-20+abs(dx), 20-abs(dx) + 1):
                    otherpoint = (x+dx, y + dy)
                    if otherpoint in paths:
                        cheatLength = distances[otherpoint] - distances[(x,y)] - abs(dx) - abs(dy)
                        if cheatLength >= 100:
                            nrOfCheatsPart2 += 1
                            if abs(dx) + abs(dy) == 2:
                                nrOfCheatsPart1 += 1

print(f"Day 20:\n  1) There are {nrOfCheatsPart1} cheats that would save me at least 100 picoseconds.")
print(f"  2) With the updated cheating rules, there are now {nrOfCheatsPart2} cheats that would save me at least 100 picoseconds.")