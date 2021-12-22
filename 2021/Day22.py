from collections import defaultdict
import time
st=time.time()
with open("input22.txt","r") as f:
    steps = f.read().splitlines()

# Original part 1
lights = defaultdict(int)
for step in steps:
    onOrOff, ranges = step.split(" ")
    ranges = [[int(j) for j in i[2:].split("..")] for i in ranges.split(",")]
    for x in range(max(ranges[0][0],-50),min(ranges[0][1],50)+1):
        for y in range(max(ranges[1][0], -50), min(ranges[1][1], 50) + 1):
            for z in range(max(ranges[2][0], -50), min(ranges[2][1], 50) + 1):
                if onOrOff == "on":
                    lights[(x,y,z)]=1
                else:
                    lights[(x,y,z)]=0
print(f"Part 1: {sum(lights.values())}.")

# Part 2 - time to this a little different. Computing overlapping cubes and dividing cubes into smaller pieces
def checkOverlap(range1,range2):
    # First check if they overlap at all: the x,y,z ranges all should overlap  (otherwise there is a plane between them)
    overlap = True
    for coord in range(len(range1)): # check for each axis
        r1 = range1[coord]
        r2 = range2[coord]
        if not ( r2[0] <= r1[0] <= r2[1] or r2[0] <= r1[1] <= r2[1] or r1[0] <= r2[0] <= r1[1] or r1[0] <= r2[1] <= r1[1] ):
            overlap = False
    result = []
    if overlap:
        for coord in range(len(range1)): # Consider each axis individually, they are cubes right!
            subresults = {}  # {  ( (x1,x2) : [b1,b2]}  # x1,x2: subrange for this axis # b1,b2: 0 or 1, included in (input)range for this axis?
            r1 = range1[coord]
            r2 = range2[coord]
            # left piece
            if r1[0] < r2[0]:
                subresults[(r1[0], min(r2[0] - 1, r1[1]))] = [1,0]
            if r1[0] > r2[0]:
                subresults[(r2[0], min(r1[0] - 1, r2[1]))] = [0, 1]
            # middle piece (overlap)
            subresults[( max(r1[0],r2[0]), min(r1[1],r2[1]))] = [1,1]
            # right piece
            if r1[1] < r2[1]:
                subresults[(max(r1[1]+1, r2[0]), r2[1])] = [0,1]
            if r1[1] > r2[1]:
                subresults[(max(r2[1]+1, r1[0]), r1[1])] = [1,0]
            result.append(subresults)
    return overlap, result

cubes = {} # This will be filled with cubes that are all mutually disjunct!
for step in steps:
    newcubes = {}
    onOrOff, ranges = step.split(" ")
    ranges = [[int(j) for j in i[2:].split("..")] for i in ranges.split(",")]
    onOrOff = 1 if onOrOff=="on" else 0
    cubesToCheck = {tuple([tuple(k) for k in ranges]): 1}

    # Compute overlap with cubes that we already found before
    overlap = False
    for oldcube in cubes:
        newCubesToCheck = cubesToCheck.copy()
        if not cubesToCheck: # This is the tiny thing that I missed...
            newcubes[oldcube] = 1
        for newcube in cubesToCheck:
            r,a = checkOverlap(oldcube,newcube)
            if r:
                if onOrOff: # If on: To keep "cubes" completely disjunct, we keep the old cube in there,
                    newcubes[oldcube] = 1
                    # but divide the newcube in small pieces that don't overlap with oldcube
                    # and continue with those pieces for the next oldcubes.
                    newCubesToCheck.pop(newcube)
                    for x,u in a[0].items():
                        for y,v in a[1].items():
                            for z,w in a[2].items():
                                if u[1] and v[1] and w[1] and not (u[0] and v[0] and w[0]):
                                    newCubesToCheck[(x,y,z)] = 1
                else:
                    # If off: In this case we divide the oldcube up into pieces, but keep the newcube intact.
                    newCubesToCheck[newcube] = 1
                    for x,u in a[0].items():
                        for y,v in a[1].items():
                            for z,w in a[2].items():
                                if (u[0] and v[0] and w[0]) and not ((u[1] and v[1] and w[1])):
                                    newcubes[(x,y,z)] = 1
                    pass
            else:
                newcubes[oldcube] = 1
        cubesToCheck = newCubesToCheck
    if onOrOff:
        for newcube in cubesToCheck:
            newcubes[newcube] = 1
    cubes=newcubes

sum = 0
sum1 = 0 # om deel 1 opnieuw te berekenen als sanity check

for cube in set(cubes):
    print(cube)
    if cube[0][1] >=-50 and cube[0][0]<=50 and cube[1][1] >=-50 and cube[1][0]<=50 and cube[2][1] >=-50 and cube[2][0]<=50:
        sum1 +=  (min(50,cube[0][1])-max(-50,cube[0][0]) + 1) * (min(50,cube[1][1])-max(-50,cube[1][0]) + 1) * (min(50,cube[2][1])-max(-50,cube[2][0]) + 1)
    sum += (cube[0][1]-cube[0][0] + 1) * (cube[1][1]-cube[1][0] + 1) * (cube[2][1]-cube[2][0] + 1)
print(f"Part 1: {sum1}.")
print(f"Part 2: {sum}.")
et=time.time()
print("This took a whopping {et-st} seconds.")
# IDEA
# dict d1 with cubes that are currently on, all disjunct
# for each new cube, make a new dictionairy d2  '
# for each cube in old d1: if no overlap, add this old cube to d2
# otherwise, compute overlap and add the correct subcubes of the old cube to d2
# and for the new cube, divide it up in subcubes, and consider all these subcubes on the rest of the cubes