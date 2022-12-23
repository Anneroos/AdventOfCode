with open("input23.txt") as f:
    grove = f.read().split("\n")

# x runs from left to right
# Y runs from top to bottom
# North is where y gets smaller

class Elf():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.directions = ["N", "S", "W", "E"]
        self.firstdirectionIdx = 3 # will go to 0 when we start
        self.proposedLocation = (self.x, self.y)

    def neighborsToCheck(self, dir):
        if dir == "N":
            return [(self.x - 1, self.y - 1), (self.x, self.y - 1), (self.x + 1, self.y - 1)]
        elif dir == "S":
            return [(self.x - 1, self.y + 1), (self.x, self.y + 1), (self.x + 1, self.y + 1)]
        elif dir == "W":
            return [(self.x - 1, self.y - 1), (self.x - 1, self.y), (self.x - 1, self.y + 1)]
        elif dir == "E":
            return [(self.x + 1, self.y - 1), (self.x + 1, self.y), (self.x + 1, self.y + 1)]

    def allNeighbors(self):
        return [(self.x - 1, self.y - 1), (self.x, self.y - 1), (self.x + 1, self.y - 1), (self.x - 1, self.y + 1),
                (self.x, self.y + 1), (self.x + 1, self.y + 1), (self.x - 1, self.y), (self.x + 1, self.y)]

    def getNewPositionFromDir(self,dir):
        if dir == "N":
            return (self.x, self.y-1)
        elif dir == "S":
            return (self.x, self.y+1)
        elif dir == "W":
            return (self.x-1, self.y)
        elif dir == "E":
            return (self.x+1, self.y)

    def moveToProposedLocation(self):
        self.x = self.proposedLocation[0]
        self.y = self.proposedLocation[1]

    def stayPut(self):
        self.proposedLocation = (self.x, self.y)

    def lookAround(self,allelves):
        allNeighs = self.allNeighbors()
        presence = {}
        for n in allNeighs:
            if n in allelves:
                presence[n]= 1
        self.firstdirectionIdx = (self.firstdirectionIdx+1) % 4
        if len(presence.keys()) == 0:
            return (self.x, self.y)
        else:
            for i in range(4):
                dir = self.directions[(self.firstdirectionIdx + i) % 4]
                empty = True
                for n in self.neighborsToCheck(dir):
                    if n in presence:
                        empty = False
                        break
                if empty:
                    self.proposedLocation = self.getNewPositionFromDir(dir)
                    return self.proposedLocation
            # if none of the directions worked, also stay where you are
            return self.proposedLocation

def printElves(elfDict): # Doubles as counting the number of empty spaces
    minx = min([e[0] for e in elfDict])
    maxx = max([e[0] for e in elfDict])
    miny = min([e[1] for e in elfDict])
    maxy = max([e[1] for e in elfDict])
    emptySpots = 0
    lines = []
    for y in range(miny,maxy+1):
        line = ""
        for x in range(minx, maxx +1):
            elfPresent = (x,y) in elfDict
            line += "#" if (x,y) in elfDict else "."
            if not elfPresent:
                emptySpots += 1
        lines.append(line)
    return lines, emptySpots

# Initialize all the elves
elvesList = []
elvesDict = {}
for y in range(len(grove)):
    line = grove[y]
    for x in range(len(line)):
        char = line[x]
        if char == "#":
            e = Elf(x, y)
            elvesDict[(x,y)] = e
            elvesList.append(e)

# Part 1 and 2
elvesMoved = True
round = 0
while elvesMoved:
    round += 1
    elvesMoved = False
    newElvesDict = {}
    proposedLocations = {}
    for location in elvesDict:
        elf = elvesDict[location]
        proposedLoc = elf.lookAround(elvesDict)
        proposedLocations[proposedLoc] = proposedLocations.get(proposedLoc, 0) + 1

    for location in elvesDict:
        elf = elvesDict[location]
        if proposedLocations[elf.proposedLocation] == 1:
            if elf.proposedLocation != (elf.x, elf.y):
                elvesMoved = True
            elf.moveToProposedLocation()
        else:
            elf.stayPut()
        newloc = (elf.x, elf.y)
        newElvesDict[newloc] = elf

    elvesDict = newElvesDict
    if round == 10:
        lines1, emptySpots1 = printElves(elvesDict)

lines2, emptySpots2 = printElves(elvesDict)
for line in lines2:
    print(line)
print(f"Day 23:\n1) After 10 rounds, the smallest rectangle that contains all the elves has \033[1m{emptySpots1}\033[0m empty spots.")
print(f"2) After \033[1m{round}\033[0m rounds, all the elves stopped moving. Then there were {emptySpots2} empty spots in the smallest rectangle that contains all the elves.\nAlso, see above for a picture where the elves ended up.")



