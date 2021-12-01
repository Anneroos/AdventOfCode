import numpy as np
with open("input17.txt") as file:
    lines = file.read().split("\n")

n = len(lines)
m = len(lines[0])
rounds = 6
xLayers = m + 2*rounds
yLayers = n + 2*rounds
zLayers = 2*6 + 1
wLayers = 2*6 + 1
print(m,n)
cubes = np.zeros([xLayers,yLayers,zLayers,wLayers])
start = np.zeros([m,n])

for i in range(len(lines)):
    start[i,:] = [1 if i == "#" else 0 for i in lines[i]]
cubes[6:m+6,6:n+6,6,6] = start
print(cubes.sum())

def computeNext(inputCubes):
    newCubes = np.zeros([xLayers,yLayers,zLayers,wLayers])
    for x in range(xLayers):
        for y in range(yLayers):
            for z in range(zLayers):
                for w in range(wLayers):

                    xmin = max(x-1,0)
                    xmax = min(x+1,xLayers)+1
                    ymin = max(y-1,0)
                    ymax = min(y+1,yLayers)+1
                    zmin = max(z-1,0)
                    zmax = min(z+1,zLayers)+1
                    wmin = max(w-1,0)
                    wmax = min(w+1,wLayers)+1

                    sumAround = inputCubes[xmin:xmax,ymin:ymax,zmin:zmax,wmin:wmax].sum() - inputCubes[x,y,z,w]
                    if inputCubes[x,y,z,w] == 1 and (sumAround == 2 or sumAround == 3):
                        newCubes[x,y,z,w] = 1
                    elif inputCubes[x,y,z,w] == 0 and sumAround == 3:
                        newCubes[x,y,z,w] = 1
    return newCubes



for i in range(6):
    cubes = computeNext(cubes)
    print(cubes.sum())
print(f"Part 2: {cubes.sum()}.")