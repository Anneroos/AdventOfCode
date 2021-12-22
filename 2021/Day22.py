from collections import defaultdict

with open("input22.txt","r") as f:
    steps = f.read().splitlines()

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

# Part 2
def checkOverlap(range1,range2):
    # first check if they overlap at all: the x,y,z ranges all should overlap  (otherwise there is a plane between them)
    overlap = True
    for coord in range(len(range1)):
        r1 = range1[coord]
        r2 = range2[coord]
        if not ( r2[0] <= r1[0] <= r2[1] or r2[0] <= r1[1] <= r2[1] or r1[0] <= r2[0] <= r1[1] or r1[0] <= r2[1] <= r1[1] ):
            overlap = False
    result = []
    if overlap:
        for coord in range(len(range1)):
            subresults = {}
            r1 = range1[coord]
            r2 = range2[coord]
            # left piece ;)
            if r1[0] < r2[0]:
                subresults[(r1[0], min(r2[0] - 1, r1[1]))] = [1,0]
            if r1[0] > r2[0]:
                subresults[(r2[0], min(r1[0] - 1, r2[1]))] = [0, 1]
            # middle piece
            subresults[( max(r1[0],r2[0]), min(r1[1],r2[1]))] = [1,1]
            # right piece
            if r1[1] < r2[1]:
                subresults[(max(r1[1]+1, r2[0]), r2[1])] = [0,1]
            if r1[1] > r2[1]:
                subresults[(max(r2[1]+1, r1[0]), r1[1])] = [1,0]
            result.append(subresults)
    return overlap, result

cubes = {}
for step in steps:
    print("step:", step)
    newcubes = {}
    onOrOff, ranges = step.split(" ")
    ranges = [[int(j) for j in i[2:].split("..")] for i in ranges.split(",")]
    onOrOff = 1 if onOrOff=="on" else 0
    overlap = False
    cubesToCheck = {tuple([tuple(k) for k in ranges]):1}

    for oldcube in cubes:
        newCubesToCheck = cubesToCheck.copy()
        for newcube in cubesToCheck:
            r,a = checkOverlap(oldcube,newcube)
            if r:
                if onOrOff: # Beide zijn aan, dan kan de gehele oude cube blijven bestaan, maar delen we de nieuwe cube juist op in kleine stukjes, zodnerde ovelap
                    # print("1")
                    newCubesToCheck.pop(newcube)
                    newcubes[oldcube] = 1
                    for x,u in a[0].items():
                        for y,v in a[1].items():
                            for z,w in a[2].items():
                                if u[1] and v[1] and w[1] and not (u[0] and v[0] and w[0]):
                                    newCubesToCheck[(x,y,z)] = 1
                else:
                    # oude is aan, maar nieuwe is uit. dan kan nieuwe cube blijven bestaan, maar oude opdelen
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
    if cube[0][1] >=-50 and cube[0][0]<=50 and cube[1][1] >=-50 and cube[1][0]<=50 and cube[2][1] >=-50 and cube[2][0]<=50:
        sum1 +=  (min(50,cube[0][1])-max(-50,cube[0][0]) + 1) * (min(50,cube[1][1])-max(-50,cube[1][0]) + 1) * (min(50,cube[2][1])-max(-50,cube[2][0]) + 1)
    sum += (cube[0][1]-cube[0][0] + 1) * (cube[1][1]-cube[1][0] + 1) * (cube[2][1]-cube[2][0] + 1)
print(f"Part 1: {sum1}.")
print(f"Part 2: {sum}.")

# My answer: 743602878476639 TOO LOW


# IDEA
# dict d1 with cubes that are currently on, all disjunct
# for each new cube, make a new dictionairy d2  '
# for each cube in old d1: if no overlap, add this old cube to d2
# otherwise, compute overlap and add the correct subcubes of the old cube to d2
# and for the new cube, divide it up in subcubes, and consider all these subcubes on the rest of the cubes