from collections import defaultdict

with open("input20.txt", "r") as f:
    g = f.read().split("\n\n")
    enh = [1 if i == "#" else 0 for i in g[0]]
    startimage = g[1].split()

# Initialize dictionairy
imageDict = defaultdict(lambda: 0)
for i,row in enumerate(startimage):
    for j,char in enumerate(row):
        imageDict[(i,j)] = 1 if char == "#" else 0

def getNeighbors(point):
    x = point[0]
    y = point[1]
    return  [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y - 1), (x, y), (x, y + 1), (x + 1, y - 1), (x + 1, y),  (x + 1, y + 1)]

def imageEnchancementAlgorithm(image, enhanc, times):
    # image = im.copy()
    xs = [p[0] for p in image.keys()]
    minx = min(xs)
    maxx = max(xs)
    ys = [p[1] for p in image.keys()]
    miny = min(ys)
    maxy = max(ys)
    for i in range(times):
        if i % 2 == 0:
            newimage = defaultdict(lambda: enh[0] )
        else:
            newimage = defaultdict(lambda: 0)
        for j in range(minx - i - 1,maxx + i + 2):
            for k in range(miny - i - 1, maxy + i + 2):
                neighbors = getNeighbors((j,k))
                newimage[(j,k)] = enhanc[int("".join([str(image[n]) for n in neighbors]),2)]
        image = newimage
    return image

print(f"Part 1: After 2 iterations {sum(list(imageEnchancementAlgorithm(imageDict.copy(), enh, 2).values()))} pixels are lit.")
print(f"Part 2: After 50 iterations {sum(list(imageEnchancementAlgorithm(imageDict.copy(), enh, 50).values()))} pixels are lit.")



### I used this print function for debugging
#
# def printImage(d):
#     xs = [p[0] for p in d.keys()]
#     minx = min(xs)
#     maxx = max(xs)
#     ys = [p[1] for p in d.keys()]
#     miny = min(ys)
#     maxy = max(ys)
#     for i in range(minx - 1 , maxx + 2 ):
#         row = ""
#         for j in range(miny - 1, maxy + 2 ):
#             if (i,j) in d:
#                 row += "#" if d[(i,j)] == 1 else "."
#             else:
#                 row += "?"
#         print(row)