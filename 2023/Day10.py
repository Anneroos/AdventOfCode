import math
import matplotlib.pyplot as plt
import matplotlib as mpl

with open("input10.txt") as f:
    full = f.read()
    startPointIdx = full.find('S')
    # Find starting point, marked with an S, and its coordinates
    lines = full.split("\n")
    startLine = math.floor(startPointIdx / (len(lines[0]) + 1))
    startColumn = startPointIdx - startLine * (len(lines[0]) + 1)

# We want to replace the S with the appropiate symbol, and choose a starting direction
inWhichDirectionAreNeighbors = {
'<':  lines[startLine][startColumn - 1] in ["-", "L", "F"],
'>': lines[startLine][startColumn + 1] in ["-", "J", "7"],
'^':  lines[startLine - 1][startColumn] in ["|", "7", "F"],
'v': lines[startLine + 1][startColumn] in ["|", "L", "J"]
}
possibilitiesForS = { '<': "J-7", '>' : "L-F", 'v': "F|7", '^': "L|J" }
twoDirs = [possibilitiesForS[direction] for direction in ["<", ">", "^", "v"] if inWhichDirectionAreNeighbors[direction]]
startSymbol = [i for i in twoDirs[0] if i in twoDirs[1]][0]
lines[startLine] = lines[startLine][0:startColumn] + startSymbol + lines[startLine][(startColumn+1):]
pointsToCheck = [(startLine, startColumn)]
startDirection = ">" if startSymbol in "-7J" else "^" 

# Store information about the points in the loop as we follow the pipes
loopPoints = {} 
# Store which points are to the left or to the right of the path, no matter what symbol is there
leftPoints = []
rightPoints = []
# We start with the starting position and follow the pipes, while updating the direction accordingly
currentDir = startDirection
while pointsToCheck:
    point = pointsToCheck.pop(0)
    char = lines[point[0]][point[1]] # What symbol is at this position
    combo = currentDir + char # For easy comparison
    neighbor = ()
    newDir = ""
    if combo in (">-", "vL", "^F"): # We end up going right in all these cases
        neighbor = (point[0], point[1] + 1)
        newDir = ">"
    elif combo in (">J", "^|", "<L" ): # up
        neighbor = (point[0] - 1, point[1])
        newDir = "^"
    elif combo in (">7", "v|", "<F"): # down
        neighbor = (point[0] + 1, point[1])
        newDir = "v"
    elif combo in ("<-", "vJ", "^7"): # left
        neighbor = (point[0], point[1] - 1)
        newDir = "<"
    else:
        print("Hmmm, something seems wrong...")
        break
    # Store the points to the left and the right of our path, for part 2 of the problem.
    if currentDir == ">" or newDir == ">":
        rightPoints.append((point[0] + 1, point[1]))
        leftPoints.append((point[0] - 1, point[1]))
    if currentDir == "v" or newDir == "v":
        rightPoints.append((point[0], point[1] - 1))
        leftPoints.append((point[0], point[1] + 1))
    if currentDir == "<" or newDir == "<":
        rightPoints.append((point[0] - 1, point[1]))
        leftPoints.append((point[0] + 1, point[1]))
    if currentDir == "^" or newDir == "^":
        rightPoints.append((point[0], point[1] + 1))
        leftPoints.append((point[0], point[1] - 1))
    # Add next point to the list, if we haven't considered it yet, and update the direction
    if neighbor not in loopPoints:
        loopPoints[neighbor] = {'distance': loopPoints.get(point, {}).get('distance',0) + 1, 'direction': newDir}
        pointsToCheck.append(neighbor)
    currentDir = newDir

print(f"Day 10:\n1) It takes {int((max([v['distance'] for k,v in loopPoints.items()]) ) /2)} steps along the loop to get from the starting position to the point farthest from the starting position.")

# Part 2 - Ok, we'll just use the points to the right of the path, that seems to be the correct side.
# We will use the points in rightPoints to find more points that are on the inside.
innerPointsToConsider = rightPoints.copy()
innerPoints = {}
for point in innerPointsToConsider:
    if point not in loopPoints: # It shouldn't be part of the main loop. Anything else is fine.
        innerPoints[point] = 1
        # Consider the four neighbors of the inner point, and add them to the consider-list, if not already there.
        for neighbor in [(point[0], point[1] + 1), (point[0], point[1] - 1), (point[0] + 1, point[1]), (point[0] - 1, point[1])]:
            if neighbor not in innerPoints and neighbor not in innerPointsToConsider:
                innerPointsToConsider.append(neighbor)

print(f"2) There are {sum(innerPoints.values())} tiles enclosed by the loop.")

# ------------ End of solution, now some fun plotting shenanigans! ----------------- #

print("Here is a visual representation of the loop, where its inner points are marked with 'x'.\r\n\r\n")

matrix = []
for lineIdx in range(len(lines)):
    newline = ""
    row = []
    rows = [[], [], []]
    for column in range(len(lines[lineIdx])):
        symbol = " "
        nr = 0
        if (lineIdx, column) in loopPoints:
            symbol = lines[lineIdx][column]
            nr = 2

        elif (lineIdx, column) in innerPoints:
            symbol = "x"
            nr = 5

        pipe = -13 if (lineIdx, column) == (startLine, startColumn) else -16
        inner = -10
        if symbol == "L":
            rows[0] += [0,pipe,0]
            rows[1] += [0,pipe,pipe]
            rows[2] += [0,0,0]
        elif symbol == "J":
            rows[0] += [0,pipe,0]
            rows[1] += [pipe,pipe,0]
            rows[2] += [0,0,0]
        elif symbol == "7":
            rows[0] += [0,0,0]
            rows[1] += [pipe,pipe,0]
            rows[2] += [0,pipe,0]
        elif symbol == "F":
            rows[0] += [0,0,0]
            rows[1] += [0,pipe,pipe]
            rows[2] += [0,pipe,0]
        elif symbol == "-":
            rows[0] += [0,0,0]
            rows[1] += [pipe,pipe,pipe]
            rows[2] += [0,0,0]
        elif symbol == "|":
            rows[0] += [0,pipe,0]
            rows[1] += [0,pipe,0]
            rows[2] += [0,pipe,0]
        elif symbol == "x":
            rows[0] += [inner, inner, inner]
            rows[1] += [inner, inner, inner]
            rows[2] += [inner, inner, inner]
        else:
            rows[0] += [0, 0, 0]
            rows[1] += [0, 0, 0]
            rows[2] += [0, 0, 0]
        newline += symbol
        row.append(nr)
    matrix.append(rows[0])
    matrix.append(rows[1])
    matrix.append(rows[2])
    print(newline)

print("Now there will be a popup with a colorful matrix!")
# To remove borders and axes from the picture
def full_frame(width=None, height=None):
    mpl.rcParams['savefig.pad_inches'] = 0
    figsize = None if width is None else (width, height)
    fig = plt.figure(figsize=figsize)
    ax = plt.axes([0, 0, 1, 1], frameon=False)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.autoscale(tight=True)
full_frame()

fig = plt.imshow(matrix)
fig.set_cmap('cubehelix')
fig.axes.get_xaxis().set_visible(False)
fig.axes.get_yaxis().set_visible(False)
plt.show()
