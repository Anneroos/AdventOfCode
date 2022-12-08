from copy import deepcopy
import matplotlib.pyplot as plt
with open("input08.txt") as f:
    inp = [[int(i) for i in list(x)] for x in f.read().split()]
h = len(inp)
w = len(inp[0])

# ---------- PART 1 ----------
visible = [[0 for i in x] for x in deepcopy(inp)]

# Horizontal
for i in range(h):
    # left to right
    max = -1
    for j in range(w):
        if inp[i][j] > max:
            max = inp[i][j]
            visible[i][j] = 1
    # right to left
    max = -1
    for j in reversed(range(w)):
        if inp[i][j] > max:
            max = inp[i][j]
            visible[i][j] = 1

# VERTICAL
for j in range(w):
    # top to bottom
    max = -1
    for i in range(h):
        if inp[i][j] > max:
            max = inp[i][j]
            visible[i][j] = 1
    # bottom to top
    max = -1
    for i in reversed(range(h)):
        if inp[i][j] > max:
            max = inp[i][j]
            visible[i][j] = 1
print(f"Day 8:\n1) There are {sum([sum(x) for x in visible])} trees visible from outside the grid.")

# --------- PART 2 ----------
maxScenicScore = 0
for i in range(h):
    for j in range(w):
        # for each tree, checkthe current height and then look in the four directions
        currentHeight = inp[i][j]
        # look up
        up = 0
        for u in reversed(range(i)):
            if inp[u][j] < currentHeight:
                up += 1
            else:
                up += 1
                break
        # look down
        down = 0
        for u in range(i+1,h):
            if inp[u][j] < currentHeight:
                down += 1
            else:
                down += 1
                break
        # look left
        left = 0
        for u in reversed(range(j)):
            if inp[i][u] < currentHeight:
                left += 1
            else:
                left += 1
                break
        # look right
        right = 0
        for u in range(j+1,w):
            if inp[i][u] < currentHeight:
                right += 1
            else:
                right += 1
                break
        # Check the scenic score and if it's a new highscore
        scenicScore = up*down*left*right
        if scenicScore > maxScenicScore:
            maxScenicScore = up*down*left*right
            directions = [up, down, left, right] # for plotting
            treeSpot = [i,j] # for plotting
print(f"2) The highest possible scenic score is {maxScenicScore} at position {treeSpot}.")

#   ----- PLOTTING PART 1 and PART 2 together -----
for i in range(treeSpot[0]-directions[0], treeSpot[0]+directions[1]+1):
    visible[i][treeSpot[1]] += 0.5
for j in range(treeSpot[1]-directions[2], treeSpot[1]+directions[3]+1):
    visible[treeSpot[0]][j] += 0.5
visible[treeSpot[0]][treeSpot[1]] += 1
plt.imshow(visible)
plt.colorbar()
plt.show()