import math
with open("2025/input09.txt") as f:
    lines = [[int(i) for i in k.split(",")] for k in f.read().splitlines()]
maxArea = 0
for i in range(len(lines)):
    p = lines[i]
    for j in range(i+1,len(lines)):
        q = lines[j]
        area = abs(p[0]+1-q[0]) * abs(p[1]+1-q[1])
        if area > maxArea:
            maxArea = area

print(f"Day 9:\n  1) {maxArea}")

# --------------------------------- PART 2
# verticals = [[] for _ in range(len(maxlines[0]))]
# horizontals = [[] for _ in range(len(lines))]
# for i in range(len(lines)):
#     p = lines[i]
#     if i < len(lines)-1:
#         q = lines[i+1]
#     else:
#         q = lines[0]
#     if p[0] == q[0]:
#         print("verticaal lijn")
#         verticals[p[0]].append(sorted([p[1],q[1]]))
#     else:
#         print("horizontaal lijn")
#         horizontals[p[1]].append(sorted([p[0],q[0]]))
        
# print(horizontals)
# print(verticals)

points = {}
maxX = max([l[0] for l in lines])
maxY = max([l[1] for l in lines])
print(maxX, maxY)
for i in range(len(lines)):
    p = lines[i]
    if i < len(lines)-1:
        q = lines[i+1]
    else:
        q = lines[0]
    xrange = sorted([p[0], q[0]])
    yrange = sorted([p[1], q[1]])
    print(xrange, yrange)
    for x in range(xrange[0], xrange[1]+1):
        for y in range(yrange[0], yrange[1]+1):
            points[(x,y)] = 1

for y in range(maxY+1):
    row = ""
    prev = "."
    flip = 0
    for x in range(maxX+1):
        if (x,y) in points:
            char = "#"
        else:
            char = "."

        
        # if prev == "#" and char == ".":
        #     flip += 1
        #     if flip %2 == 1:
        #         char = 'x'
        # elif prev == "x" and char == ".":
        #     char = 'x'
        row += char
        prev = char
    print(row)