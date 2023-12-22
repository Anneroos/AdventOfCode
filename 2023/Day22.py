from copy import deepcopy
with open("input22.txt") as f:
    lines = f.read().split("\n")
# Read input
bricks = [[[int(j) for j in i.split(",")] for i in line.split("~")] for line in lines]
bricks.sort(key=lambda b: b[0][2])

class Brick():
    def __init__(self, definition):
        self.definition = definition
        self.cubes = getAllCubesOfBrick(self.definition)
        self.supporting = []
        self.leaningOn = []
    def fallDistance(self, d):
        self.cubes = [[c[0], c[1], c[2] - d] for c in self.cubes]

def getAllCubesOfBrick(brick):
    length = max(abs(brick[1][0] - brick[0][0]), abs(brick[1][1] - brick[0][1]), abs(brick[1][2] - brick[0][2]))
    return [[brick[0][0] + (i if brick[1][0] != brick[0][0] else 0),
            brick[0][1] + (i if brick[1][1] != brick[0][1] else 0),
            brick[0][2] + (i if brick[1][2] != brick[0][2] else 0)] for i in range(length + 1)]

def checkOverlap(brick1, brick2):
    overlapping = False
    for piece in brick1.cubes:
        if piece in brick2.cubes:
            overlapping = True
            break
    return overlapping

def checkHowFarBrickCanFall(stack, br): #, exclude=[]):
    keepFalling = True
    distance = 0
    brick = deepcopy(br)
    leaningOn = []
    while keepFalling:
        brick.cubes = [[cube[0], cube[1], cube[2] - 1] for cube in brick.cubes]
        distance += 1
        collision = False
        for stablebrick in stack:
            if checkOverlap(stablebrick, brick):
                collision = True
                leaningOn.append(stablebrick)

        if collision or brick.definition[0][2] - distance < 1:
            distance -= 1
            keepFalling = False
    return distance, leaningOn

landedBricks = []
print("Settling bricks...")
for brick in bricks:
    newbrick = Brick(brick)
    d, leaningOn = checkHowFarBrickCanFall(landedBricks, newbrick)
    newbrick.leaningOn = leaningOn
    newbrick.fallDistance(d)
    landedBricks.append(newbrick)

print("Check which bricks leans on which brick...")
for br in landedBricks:
    for brick in br.leaningOn:
        brick.supporting.append(br)

print("Calculating...")
nrSafeToDisintegrate = 0 # part 1
totalFallen = 0 # part 2
for idx, br in enumerate(landedBricks):
    bricksToConsider = br.supporting
    fallenWithMe = 0
    disappeared = [br]
    while bricksToConsider:
        b = bricksToConsider.pop(0)
        falling = True
        for bsbs in b.leaningOn:
            if bsbs not in disappeared:
                falling = False
        if falling:
            disappeared.append(b)
            fallenWithMe += 1
            bricksToConsider += [t for t in b.supporting if t not in bricksToConsider]
    totalFallen += fallenWithMe
    if fallenWithMe == 0:
        nrSafeToDisintegrate += 1
print(f"Day 22:\n1) There are {nrSafeToDisintegrate} bricks that could be safely chosen as the one to get disintegrated.")
print(f"2) The sum of the number of other bricks that would fall is {totalFallen}.")