with open("input13.txt", "r") as f:
    inputlines = f.read().split("\n\n")
    dots = [tuple([int(i) for i in j.split(",")]) for j in inputlines[0].splitlines()]
    instr = inputlines[1].splitlines()

for i,line in enumerate(instr):
    axis,fold = line.split(" ")[2].split("=")
    fold = int(fold)
    if axis == "x":
        dots = list(set([(2 * fold - p[0], p[1]) if p[0] > fold else p for p in dots]))
    else:
        dots = list(set([(p[0], 2 * fold - p[1]) if p[1] > fold else p for p in dots]))
    if i == 0:
        print(f"Part 1: There are {len(dots)} dots after 1 step.")

# Now let's show the final image
import numpy as np
maxx = max([p[0] for p in dots])
maxy = max([p[1] for p in dots])
matrix = np.zeros([maxy+1, maxx+1])
for dot in dots:
    matrix[dot[1], dot[0]] = 1
from matplotlib import pyplot as plt
plt.imshow(matrix)
plt.show()