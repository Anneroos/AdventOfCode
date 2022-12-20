with open(    "input18.txt") as f:
    cubes = [tuple([int(i) for i in x.split(",")]) for x in f.read().split("\n")]

cubesDict = {}
for cube in cubes:
    cubesDict[cube] = 1

def neighbors(c):
    return [(c[0]+1,c[1],c[2]),(c[0]-1,c[1],c[2]),(c[0],c[1]-1,c[2]),(c[0],c[1]+1,c[2]), (c[0],c[1],c[2]-1), (c[0],c[1],c[2]+1)]

def computeSurface(d):
    s = 0
    for cube in d:
        for n in neighbors(cube):
            if n in d:
                s+=1
    return len(d)*6-s
print(computeSurface(cubesDict))
# print(len(cubes)*6-s)

minx = min([k[0] for k in cubesDict])-1
maxx = max([k[0] for k in cubesDict])+1
miny = min([k[1] for k in cubesDict])-1
maxy = max([k[1] for k in cubesDict])+1
minz = min([k[2] for k in cubesDict])-1
maxz = max([k[2] for k in cubesDict])+1

outside = {}
points = [(minx,miny,minz)]

while len(points) > 0:
    pt = points.pop(0)
    outside[pt] = 1
    for n in neighbors(pt):
        if n not in cubesDict and n not in outside and n not in points:
            if minx<=n[0]<=maxx and miny<=n[1]<=maxy and minz<=n[2]<=maxz:
                points.append(n)
print(computeSurface(outside) - 2*((maxx-minx+1)*(maxy-miny+1) + (maxy-miny+1)*(maxz-minz+1) + (maxz-minz+1)*(maxy-miny+1)))