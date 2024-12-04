with open("input04.txt") as f:
    x = f.read().split("\n")
directions = {"W": (-1,0), "NW": (-1,-1), "N": (0,-1), "NE": (1,-1), "E": (1,0), "SE": (1,1), "S": (0,1), "SW": (-1,1)}
gridSize = (len(x), len(x[0]))

def getLetter(grid, lineIdx, colIdx, dir, dist):
    newLineIdx = lineIdx + dir[0]*dist
    newColIdx = colIdx + dir[1]*dist
    if 0 <= newLineIdx < gridSize[0] and 0 <= newColIdx < gridSize[1]:
        return grid[newLineIdx][newColIdx]
    else:
        return "-"

nrOfXMASfound = 0
for lineIdx in range(gridSize[0]):
    for colIdx in range(gridSize[1]):
        if x[lineIdx][colIdx] == "X":
            # print(f"Found X at {lineIdx,colIdx}")
            for dir in directions.values():
                if getLetter(x, lineIdx, colIdx, dir, 1) == "M":
                    if getLetter(x, lineIdx, colIdx, dir, 2) == "A":
                        if getLetter(x, lineIdx, colIdx, dir, 3) == "S":
                            nrOfXMASfound += 1
print(f"Day 4:\n  Found XMAS {nrOfXMASfound} times.")

nrOfXMASfound = 0
for lineIdx in range(1,gridSize[0]-1):
    for colIdx in range(1,gridSize[1]-1):
        if x[lineIdx][colIdx] == "A":
            # First check NW and SE
            a = getLetter(x, lineIdx, colIdx, directions["NW"], 1)
            b = getLetter(x, lineIdx, colIdx, directions["SE"], 1)
            if a+b in ["MS", "SM"]:
                # Then check NE and SW
                a = getLetter(x, lineIdx, colIdx, directions["NE"], 1)
                b = getLetter(x, lineIdx, colIdx, directions["SW"], 1)
                if a + b == "MS" or a+b == "SM":
                    nrOfXMASfound += 1
print(f"  Found X-MAS {nrOfXMASfound} times.")