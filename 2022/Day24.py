import copy
import math

with open("input24.txt") as f:
    valleyinput = f.read().split("\n")
shortestRoute = {"minminutes": math.inf}

class Blizzard():
    def __init__(self, x, y, dir, w, h):
        self.startx = x
        self.starty = y
        self.x = x
        self.y = y
        self.dir = dir
        self.spacew = w-2
        self.spaceh = h-2
        self.time = 0

    def locationAtCertainTime(self, time):
        dx = 0
        dy = 0
        if self.dir == "^":
            dy = -1
        elif self.dir == "v":
            dy = +1
        elif self.dir == "<":
            dx = -1
        elif self.dir == ">":
            dx = +1
        x = 1 + (self.startx + dx * (time ) - 1) % self.spacew
        y = 1 + (self.starty + dy * (time ) - 1) % self.spaceh
        return (x,y)

    def move(self):
        if self.dir == "^":
            self.y -= 1
            if self.y == 0:
                self.y = self.valleyH-2
        elif self.dir == "v":
            self.y += 1
            if self.y == self.valleyH-1:
                self.y = 1
        elif self.dir == "<":
            self.x -= 1
            if self.x == 0:
                self.x = self.valleyW-2
        elif self.dir == ">":
            self.x += 1
            if self.x == self.valleyW-1:
                self.x = 1
        return (self.x, self.y)

allBlizzards = []
allBlizzardTimePos = {0: {}}

# Read in all the blizzards
for y in range(len(valleyinput)):
    for x in range(len(valleyinput[y])):
        if valleyinput[y][x] in "><^v":
            b = Blizzard(x, y, valleyinput[y][x], len(valleyinput[0]), len(valleyinput))
            allBlizzards.append(b)
            allBlizzardTimePos[0][(x,y)] = 1

def computeNewBlizzardLocations(time):
    if time not in allBlizzardTimePos:
        allBlizzardTimePos[time] = {}
        for b in allBlizzards:
            pos = b.locationAtCertainTime(time)
            allBlizzardTimePos[time][pos] = 1

class Expedition():
    def __init__(self, vall,  starttime, startpoint, goal):
        self.valleyH = len(vall)
        self.valleyW = len(vall[0])
        self.period = math.lcm((self.valleyW - 2), (self.valleyH - 2))
        self.x = startpoint[0]
        self.y = startpoint[1]
        self.d = 1
        self.goal = goal
        self.minutes = starttime
        self.history = []

    def move(self,loc):
        self.history.append(loc)
        self.x = loc[0]
        self.y = loc[1]
        self.d = self.x+self.y

    def getPossibleMoveLocations(self, bliz):
        possibleLocs = []
        locs = [(self.x + 1, self.y), (self.x, self.y + 1), (self.x, self.y), (self.x, self.y - 1), (self.x - 1, self.y)]
        if self.goal == (1,0):
            locs.reverse()
        for loc in locs:
            if loc not in bliz[self.minutes] and ((1 <= loc[0] <= self.valleyW - 2 and 1 <= loc[1] <= self.valleyH - 2) or loc == (1, 0) or loc == self.goal):
                possibleLocs.append(loc)
        return possibleLocs

    def makeCopy(self, loc):
        newExpedition = copy.deepcopy(self)
        newExpedition.move(loc)
        return newExpedition

    def findBestRoute(self, sh, allstates, bliz):
        # drawValley(bliz, self.minutes, (self.x, self.y), self.goal)
        if (self.x, self.y) == self.goal:
            print("Found goal!", self.minutes, self.history)
            sh["minminutes"] = min(sh["minminutes"], self.minutes)
            return self.minutes, self.history
        # print("Minute", self.minutes, "Position", self.x, self.y, sh["minminutes"])
        self.minutes += 1
        state = (self.minutes % self.period, self.x, self.y)
        # Compute best possible score for this path and compare with shortestRoute
        if self.minutes + self.goal[0]-self.x + self.goal[1]-self.y >= sh["minminutes"]:
            # print("stop, this takes too long")
            return math.inf, self.history
        elif state in allstates:
            # print("been here before, in these circumstance, stop.", self.minutes)
            return math.inf, self.history
        else:
            allstates[state] = 1
            computeNewBlizzardLocations(self.minutes)

            # self.computeNextPositionBlizzards()
            locs = self.getPossibleMoveLocations(bliz)
            minTime = math.inf
            bestroute = [(self.x, self.y)]
            for loc in locs:
                newexp = self.makeCopy(loc)
                bestTimeNewExp, route = newexp.findBestRoute(sh, allstates, bliz)
                if bestTimeNewExp < minTime:
                    minTime = bestTimeNewExp
                    bestroute = route
            return minTime, bestroute

def drawValley(blizzardslocs, time, pos, goal):
    w = len(valleyinput[0])
    h = len(valleyinput)
    for y in range(h):
        line = ""
        for x in range(w):
            char = "."
            if (x,y) == pos:
                char = "E"
            elif (x,y) == (1, 0) or (x,y) == goal:
                char = "."
            elif x==0 or y==0 or x == w-1 or y == h-1:
                char = "#"
            elif (x,y) in blizzardslocs[time]:
                char = str(blizzardslocs[time][(x,y)])
            line += char
        print(line)

# states = {}
# shortestRoute = {"minminutes": math.inf}
# exp = Expedition(valleyinput,  0, (1,0), (len(valleyinput[0]) - 2, len(valleyinput) - 1))
# e = exp.findBestRoute(shortestRoute, states, allBlizzardTimePos)
# print(e)

# states = {}
# shortestRoute = {"minminutes": math.inf}
# exp = Expedition(valleyinput,  308, (len(valleyinput[0]) - 2, len(valleyinput) - 1), (1,0))
# e = exp.findBestRoute(shortestRoute, states, allBlizzardTimePos)
# print(e)

states = {}
shortestRoute = {"minminutes": math.inf}
exp = Expedition(valleyinput,  598, (1,0), (len(valleyinput[0]) - 2, len(valleyinput) - 1))
e = exp.findBestRoute(shortestRoute, states, allBlizzardTimePos)
print(e)

#308 # 598