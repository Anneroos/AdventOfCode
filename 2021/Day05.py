import math
with open("input5.txt", "r") as f:
    lines = f.read().split("\n")
lines = [[[int(k) for k in j.split(",")] for j in i.split(" -> ")] for i in lines]
vents_easy = {}
vents = {}

for line in lines:
    start = line[0]
    end = line[1]
    #For part 1: only hor and ver lines
    if start[0] == end[0]:
        for i in range(min(start[1],end[1]),max(start[1],end[1]) + 1):
            vents_easy[(start[0], i)] = vents_easy.get((start[0],i),0) + 1
    elif start[1] == end[1]:
        for i in range(min(start[0],end[0]),max(start[0],end[0]) + 1):
            vents_easy[(i, start[1])] = vents_easy.get((i, start[1]),0) + 1
    # For part 2: all lines
    dx = 0 if start[0]==end[0] else math.copysign(1,end[0]-start[0])
    dy = 0 if start[1]==end[1] else math.copysign(1,end[1]-start[1])
    r = max(abs(end[0]-start[0]), abs(end[1]-start[1]))
    for j in range(0,r+1):
        vents[(start[0]+j*dx, start[1]+j*dy)] = vents.get((start[0]+j*dx, start[1]+j*dy), 0) + 1

dangerPoints_easy = sum([1 for k in vents_easy.items() if k[1] > 1])
dangerPoints = sum([1 for k in vents.items() if k[1] > 1])

print(f"Part 1: There are {dangerPoints_easy} dangerous points to avoid!")
print(f"Part 2: There are {dangerPoints} dangerous points to avoid!")