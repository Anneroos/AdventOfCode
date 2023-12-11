with open("input11.txt") as f:
    lines = f.read().split("\n")

def computeTotalGalaxyDistances(galaxies, emptyLines, emptyColumns, expansion):
    totalDist = 0
    for galaxyId1 in range(len(galaxies)):
        g1 = galaxies[galaxyId1]
        for galaxyId2 in range(galaxyId1+1, len(galaxies)):
            localDist = 0
            g2 = galaxies[galaxyId2]
            localDist += abs(g2[0] - g1[0]) + abs(g2[1] - g1[1])
            # check if the empty lines and columns are within this range. If so, add some extra steps to the distance.
            for col in emptyColumns:
                if g2[1] <= col <= g1[1] or g1[1] <= col <= g2[1]:
                    localDist += expansion - 1 # already counted the col itself
            for lineIdx in emptyLines:
                if g2[0] <= lineIdx <= g1[0] or g1[0] <= lineIdx <= g2[0]:
                    localDist += expansion - 1
            totalDist += localDist
    return totalDist

# find all galaxies in the input, and all empty lines and empty columns
myGalaxies = [(lineIdx, column) for lineIdx in range(len(lines)) for column in range(len(lines[lineIdx])) if lines[lineIdx][column] == "#"]
myEmptyLines = [lineIdx for lineIdx in range(len(lines)) if lineIdx not in [g[0] for g in myGalaxies]]
myEmptyColumns = [col for col in range(len(lines[0])) if col not in [g[1] for g in myGalaxies]]

print(f"Day 11:\n1) With a cosmic expansion of 2, the sum of the shortest path between every pair of galaxies is {computeTotalGalaxyDistances(myGalaxies, myEmptyLines, myEmptyColumns, 2)}.")
print(f"2) With a cosmic expansion of 1000000, the sum of the shortest path between every pair of galaxies is {computeTotalGalaxyDistances(myGalaxies, myEmptyLines, myEmptyColumns, 1000000)}.")


# ------------ End of solution, now some fun plotting shenanigans! ----------------- #
import matplotlib.pyplot as plt
import matplotlib as mpl

matrix = []
for lineIdx in range(len(lines)):
    newline = []
    for column in range(len(lines[lineIdx])):
        if (lineIdx, column) in myGalaxies:
            newline.append(2)
        elif lineIdx in myEmptyLines or column in myEmptyColumns:
            newline.append(.4)
        else:
            newline.append(0)
    matrix.append(newline)

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
