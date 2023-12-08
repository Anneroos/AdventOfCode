from collections import defaultdict
import math

with open("input08.txt") as f:
    directions, graph = f.read().split("\n\n")
graph = {line.split(" = ")[0]: {"L": line.split(" = ")[1][1:4], "R" : line.split(" = ")[1][6:9]}  for line in graph.split("\n")}

startNodes = [node for node in graph if node[2] == "A"]
startNodes.sort()
endNodesPerNode = {}
for startNode in startNodes:
    dirIdx = 0
    node = startNode
    endNodes = {}
    history = defaultdict(list)
    while (dirIdx % len(directions)) not in history[node]:
        history[node].append(dirIdx % len(directions))
        node = graph[node][directions[dirIdx % len(directions)]]
        dirIdx += 1
        if (dirIdx % len(directions)) in history[node]:
            break
        if node[2] == "Z" and node not in endNodes:
            endNodes[node] = dirIdx
    endNodesPerNode[startNode] = endNodes

print(f"From each starting node, where do we end up after how many steps:\n{endNodesPerNode}")
stepsToEndNode = []
for v in endNodesPerNode.values():
    for w in v.values():
        stepsToEndNode.append(w)

print(f"Day 8:\n1) So for AAA, there are {endNodesPerNode['AAA']['ZZZ'] } steps required to reach ZZZ.")
print(f"2) Since every start node seems to have only one end node, we can just compute the least common multiple of the numbers above.\n   It takes {math.lcm(*stepsToEndNode)} steps to reach nodes that end with Z simultaneously for all starting nodes.")