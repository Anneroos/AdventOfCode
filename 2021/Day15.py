import numpy as np
with open("input15.txt") as f:
    d = np.array([[int(i) for i in line] for line in f.read().splitlines()])
w = d.shape[0]
h = d.shape[1]

def neighbors(point, w, h):
    return [tuple([x, y]) for x, y in [[point[0] + i, point[1] + j] for i, j in [[-1, 0], [1, 0], [0, 1], [0, -1]]]
            if x >= 0 and y >= 0 and x < w and y < h]

def findRoute(multiplier):
    goal = (w*multiplier - 1, h*multiplier - 1)
    distances = {(0,0) : 0}
    points = [(0,0)]
    visited = []
    while len(points)>0:
        pt = points.pop(0)
        visited.append(pt)
        dist = distances[pt]
        for n in neighbors(pt,w*multiplier,h*multiplier):
            bonus = n[0] // w + n[1]//h
            risk = (d[(n[0] % w, n[1] % h)] + bonus - 1) % 9 + 1
            nextdist = dist + risk
            if n not in distances or distances[n] > nextdist:
                distances[n] = nextdist
                points.append(n)
    return distances[goal]

print(f"Part 1: {findRoute(1)}.")
print(f"Part 2: {findRoute(5)}.")


