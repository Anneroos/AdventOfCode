from collections import defaultdict
with open("input25.txt", "r") as f:
    lines = f.read().splitlines()
grid = {}
for lineIdx,line in enumerate(lines):
    for idx,char in enumerate(line):
        grid[(lineIdx,idx)] = char
n = len(lines)
m = len(lines[0])
thingsMoved = True

# Used for debugging
def printGrid(dic):
    print("*"*(m+2))
    for i in range(n):
        row = "*"
        for j in range(m):
            row += dic[(i,j)]
        row += "*"
        print(row)
    print("*" * (m + 2))

# Let's get started!
round=0
while thingsMoved:
    round += 1
    thingsMoved = False
    newgrid = defaultdict(lambda: ".")
    # First move the ">"
    for lineIdx in range(n):
        for idx in range(m):
            if grid[(lineIdx, idx)] == ">":
                nextIdx = (idx+1) % m
                if grid[(lineIdx,idx)] == ">"  and grid[(lineIdx,nextIdx)] == ".":
                    newgrid[(lineIdx,nextIdx)] = ">"
                    thingsMoved = True
                else:
                    newgrid[(lineIdx, idx)] = grid[(lineIdx,idx)]
            elif grid[(lineIdx, idx)] == "v":
                newgrid[(lineIdx, idx)] = grid[(lineIdx, idx)]

    grid=newgrid
    newgrid = defaultdict(lambda: ".")
    # Then move the "v"
    for lineIdx in range(n):
        for idx in range(m):
            if grid[(lineIdx,idx)] == "v":
                nextLineIdx = (lineIdx+1) % n
                if grid[(lineIdx,idx)] == "v"  and grid[(nextLineIdx,idx)] == ".":
                    newgrid[(nextLineIdx,idx)] = "v"
                    thingsMoved = True
                else:
                    newgrid[(lineIdx, idx)] = grid[(lineIdx,idx)]
            elif grid[(lineIdx,idx)] == ">":
                newgrid[(lineIdx, idx)] = grid[(lineIdx, idx)]
    grid = newgrid

print(f"Day 25! After {round} steps, no sea cucumber moves.")