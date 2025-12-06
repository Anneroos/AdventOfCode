with open("2025/input04.txt") as f:
    grid = f.read().split("\n")
accessible = 0
width = len(grid[0])
height = len(grid)
for rowIdx in range(height):
    for colIdx in range(width):
        if grid[rowIdx][colIdx] == "@":
            rolls_around = 0
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    n = (rowIdx+dy, colIdx + dx)
                    if n != (rowIdx, colIdx) and n[0] in range(0,height) and n[1] in range(0, height):
                        if grid[n[0]][n[1]] != ".":
                            rolls_around += 1
            if rolls_around < 4:
                accessible += 1
                
print(f"Day 4:\n  1) {accessible}")


with open("2025/input04.txt") as f:
    grid = f.read().split("\n")

def removeAccessible(grid):
    accessible = 0
    width = len(grid[0])
    height = len(grid)
    for rowIdx in range(height):
        for colIdx in range(width):
            if grid[rowIdx][colIdx] == "@":
                rolls_around = 0
                for dx in [-1,0,1]:
                    for dy in [-1,0,1]:
                        n = (rowIdx+dy, colIdx + dx)
                        if n != (rowIdx, colIdx) and n[0] in range(0,height) and n[1] in range(0, height):
                            if grid[n[0]][n[1]] != ".":
                                rolls_around += 1
                if rolls_around < 4:
                    accessible += 1
                    grid[rowIdx] = grid[rowIdx][0:colIdx] + "." + grid[rowIdx][colIdx + 1:]
    return grid, accessible

totalAccessible = 0
while True:
    grid, accessible = removeAccessible(grid)
    totalAccessible += accessible
    if accessible == 0:
        break
print(f"  2) {totalAccessible}")