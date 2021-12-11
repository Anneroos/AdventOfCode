import numpy as np
with open("input11.txt", "r") as f:
    octos = np.array([[int(i) for i in line] for line in f.read().splitlines()])

def computeNeighbors(octo):
    square = [[octo[0] + i,octo[1] + j] for i in [-1,0,1] for j in [-1,0,1]]
    return [k for k in square if k[0]in range(0,10) and k[1] in range(0,10) and k != octo]

def makeStep(grid):
    # First, increase all octopuses by 1
    grid[:,:] += 1
    flashed = []
    # Now, keep checking if we have some octopuses with value>9 that haven't flashed yet
    while sum(sum(grid>9)) > len(flashed):
        flashingOctos = [[i,j] for i in range(10) for j in range(10) if grid[i,j] > 9 and [i,j] not in flashed]
        for oc in flashingOctos:
            neighbors = computeNeighbors(oc)
            for n in neighbors:
                grid[n[0],n[1]] += 1
            flashed.append(oc)
    # count how many octopuses have value>9
    flashes = sum(sum(grid > 9))
    # reset all the octopuses that have a value > 9
    grid[grid > 9] = 0
    return grid, flashes

# Let's start
totalFlashes = 0
synchronized = False
steps = 0
while not synchronized:
    steps += 1
    octos, flashes = makeStep(octos)
    totalFlashes += flashes
    if steps == 100:
        print(f"Part 1: There were {totalFlashes} flashes after 100 steps.")
    if len(np.unique(octos)) == 1:
        synchronized = True
        print(f"Part 2: After {steps} steps is the first time that all the octopuses flash.")
