# 1-1-2021
with open("input18.txt") as f:
    input = f.read().split("\n")

import numpy as np
sizeX = len(input[0])
sizeY = len(input)
lighting = np.zeros([sizeX,sizeY])
for i in range(sizeY):
    line = list(input[i])
    for j in range(sizeX):
        if line[j] == "#":
            lighting[i,j] = 1
print(lighting)

def animation(nparray, part, steps):
    [w,h] = nparray.shape
    for step in range(steps):
        print(step)
        newarray = np.zeros([w,h])
        for i in range(w):
            for j in range(h):
                minX = max(0,i-1)
                maxX = min(w,i+1)+1
                minY = max(0, j - 1)
                maxY = min(h, j + 1) + 1
                neighbors = nparray[minX:maxX,minY:maxY].sum() - nparray[i,j]
                if nparray[i,j] == 1 and not (neighbors==2 or neighbors == 3):
                    newarray[i,j] = 1 - nparray[i,j]
                elif nparray[i, j] == 0 and neighbors == 3:
                    newarray[i, j] = 1 - nparray[i, j]
                else:
                    newarray[i, j] = nparray[i, j]
        nparray = newarray
        if part == 2:
            nparray[0,0] = 1
            nparray[0,h-1] = 1
            nparray[w-1,0] = 1
            nparray[w-1,h-1] = 1
    return nparray

# def animation(nparray, part, steps):
#     [w,h] = nparray.shape
#     for step in range(steps):
#         print(step)
#         indicesToChange = {}
#         for i in range(w):
#             for j in range(h):
#                 minX = max(0,i-1)
#                 maxX = min(w,i+1)+1
#                 minY = max(0, j - 1)
#                 maxY = min(h, j + 1) + 1
#                 neighbors = nparray[minX:maxX,minY:maxY].sum() - nparray[i,j]
#                 if (nparray[i, j] == 0 and neighbors == 3) or (nparray[i,j] == 1 and not (neighbors==2 or neighbors == 3)):
#
#                     indicesToChange[(i,j)] = 1 - nparray[i,j]
#         for key in indicesToChange.keys():
#             nparray[key[0],key[1]] = indicesToChange[key]
#
#         if part == 2:
#             nparray[0,0] = 1
#             nparray[0,h-1] = 1
#             nparray[w-1,0] = 1
#             nparray[w-1,h-1] = 1
#     return nparray



import time
t0 = time.time()
print(animation(lighting,1,100).sum())

t1 = time.time()

print("time: ", t1 - t0)
print(animation(lighting,2,100).sum())

t2 = time.time()

print("time: ", t2 - t1)
