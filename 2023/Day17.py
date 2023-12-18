import numpy as np

with open("input17.txt") as f:
    lines = [[int(i) for i in line] for line in f.read().split("\n")]
w = len(lines[0])
h = len(lines)

matrix = np.array(lines)
goal = [h - 1, w - 1]

def computeBestRoute(minstep, maxstep):
    goalDist = (w + h - 2) * 9  # Just wiggling around a fields of 9's should give an upper bound
    pointsToCheck = [(0, 0, "vert"), (0, 0, "hor")]
    shortestDistances = {(0, 0, "vert"): 0, (0, 0, "hor"): 0}
    while pointsToCheck:
        point = pointsToCheck.pop(0)
        direction = point[2]
        nextdir = "vert" if direction == "hor" else "hor"
        nextpoints = []
        heatLoss = 0
        # positive directions
        for step in range(1, maxstep + 1):
            possibleNextPoints = []
            if nextdir == "vert":
                possibleNextPoints.append((point[0] + step, point[1], "vert"))
            elif nextdir == "hor":
                possibleNextPoints.append((point[0], point[1] + step, "hor"))
            for nextpoint in possibleNextPoints:
                if 0 <= nextpoint[0] < h and 0 <= nextpoint[1] < w: # should be in the grid
                    heatLoss += matrix[nextpoint[0], nextpoint[1]]
                    if minstep <= step <= maxstep:
                        nextpoints.append([nextpoint, heatLoss])
        # same for negative directions
        heatLoss = 0
        for step in range(1, maxstep + 1):
            possibleNextPoints = []
            if nextdir == "vert":
                possibleNextPoints.append((point[0] - step, point[1], "vert"))
            elif nextdir == "hor":
                possibleNextPoints.append((point[0], point[1] - step, "hor"))
            for nextpoint in possibleNextPoints:
                if 0 <= nextpoint[0] < h and 0 <= nextpoint[1] < w:  # should be in the grid
                    heatLoss += matrix[nextpoint[0], nextpoint[1]]
                    if minstep <= step <= maxstep:
                        nextpoints.append([nextpoint, heatLoss])
        # Add to pointsToCheck and shortestDistances if applicable
        for nextpointpair in nextpoints:
            nextpoint = nextpointpair[0]
            heatLoss = nextpointpair[1]
            if nextpoint not in shortestDistances or shortestDistances[point] + heatLoss < shortestDistances[nextpoint]:
                if shortestDistances[point] + heatLoss <= goalDist:
                    pointsToCheck.append(nextpoint)
                    shortestDistances[nextpoint] = shortestDistances[point] + heatLoss
                    if nextpoint[0] == goal[0] and nextpoint[1] == goal[1]:
                        goalDist = min(goalDist, shortestDistances[point] + heatLoss)

    return min([v for k, v in shortestDistances.items() if k[0] == goal[0] and k[1] == goal[1]])

print(f"Day 17:\n1) Directing the crucible from the lava pool to the machine parts factory, the least heat loss it can incur is {computeBestRoute(1, 3)}.")
print(f"2) Directing the ultra crucible from the lava pool to the machine parts factory, the least heat loss it can incur is {computeBestRoute(4, 10)}.")