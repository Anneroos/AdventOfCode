# Made: 03-12-2021
with open("input3.txt", "r") as f:
    lines=f.read().split("\n")
lines = [line.split() for line in lines]
#
def checkTriangle(a,b,c):
    isTriangle = True
    if a + b <= c or a + c <= b or b + c <= a:
        isTriangle = False
    return isTriangle

totalTriangles = 0
for line in lines:
    a,b,c = [int(i) for i in line]
    if checkTriangle(a,b,c):
        totalTriangles += 1
print(f"Part 1: There are {totalTriangles} triangles possible.")

totalTriangles = 0
for i in range(int(len(lines)/3)):
    for j in range(3):
        a,b,c = [int(lines[i*3][j]), int(lines[i*3+1][j]), int(lines[i*3 + 2][j])] # Gosh, that's quite unreadible
        if checkTriangle(a, b, c):
            totalTriangles += 1


print(f"Part 2: There are {totalTriangles} triangles possible.")


