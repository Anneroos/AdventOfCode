from functools import lru_cache
import re
import time

with open("input16.txt") as f:
    lines = f.read().split("\n")

class Valve():
    def __init__(self, name, flowrate, othervalves):
        self.name = name
        self.flowrate = flowrate
        self.opened = False
        self.otherValvesNames = othervalves
        self.allvalves = {}
        self.distances = {}
        self.bestMoves = {}
    def setAllValves(self, allvalves):
        self.allvalves = allvalves
    def computePotential(self, minutesLeft, distance):
        print(self.name, "potential",minutesLeft, distance, self.flowrate,(minutesLeft - distance)*self.flowrate)
        return (minutesLeft - distance)*self.flowrate
    def Dijkstra(self):
        toVisit = [self.name]
        self.distances[self.name] = 0
        while len(toVisit) > 0:
            currentName = toVisit.pop(0)
            current = self.allvalves[currentName]
            for neighborName in current.otherValvesNames:
                if neighborName not in self.distances or self.distances[currentName] + 1 < self.distances[neighborName]:
                    self.distances[neighborName] = self.distances[currentName] + 1
                    toVisit.append(neighborName)

    def cleanUpDistances(self):
        newdistances = {}
        for v in self.distances:
            if self.allvalves[v].flowrate > 0 or v == "AA":
                newdistances[v] = self.distances[v]
        self.distances = newdistances
    def cleanUpAllvalves(self, newallvalves):
        self.allvalves = newallvalves
    def computePotentialOfNeighbors(self, minutesLeft):
        potentials = {}
        for name,valve in self.allvalves.items():
            potentials[name] = valve.computePotential(minutesLeft,self.distances[name])
        return potentials

# part 1
allvalves = {}
for line in lines:
    matchObj = re.match(r'^Valve (\w+) has flow rate=(-?\d+); tunnels? leads? to valves? (.*)$', line)
    valvename = matchObj.group(1)
    flowrate = int(matchObj.group(2))
    othervalves = matchObj.group(3).split(", ")
    v = Valve(valvename, flowrate, othervalves)
    allvalves[valvename] = v

for valve in allvalves:
    allvalves[valve].setAllValves(allvalves)

for valve in allvalves:
    allvalves[valve].Dijkstra()

# Make tha graph smaller: only keep the valves that have a non-zero flowrate, and starting location "AA"
newallvalves = {}
for valve in allvalves:
    v = allvalves[valve]
    if v.flowrate >0 or v.name == "AA":
        v.cleanUpDistances()
        newallvalves[valve] = v
allvalves = newallvalves

for vname in allvalves:
    v = allvalves[vname]
    v.cleanUpAllvalves(allvalves)
    # print( f"My name is {v.name} my flowrate is {v.flowrate}, my neighbors are {v.otherValvesNames} and my distances to others are: {v.distances}.")

currentValve = allvalves["AA"]

minutesTotal = 30
currentMinute = 0
pressureReleased = 0

paths = {"AA": 0 }
pathsFinished = {}

@lru_cache(maxsize=None)
def findBestMove1(startvalvename, valvesopened, minutesLeft):
    v = allvalves[startvalvename]
    bestscore = 0
    winningmove = []
    winningbestmoves = []
    bestmoves = []

    if minutesLeft < 0:
        return 0, ""

    for othervalvename in [valvename for valvename in allvalves if valvename not in valvesopened and v.distances[valvename] < minutesLeft]:
        newvalvesopened = valvesopened + tuple([othervalvename])
        score, bestmoves = findBestMove1(othervalvename, newvalvesopened, minutesLeft - v.distances[othervalvename]-1)
        score += (minutesLeft - v.distances[othervalvename]-1)*allvalves[othervalvename].flowrate
        if score > bestscore:
            winningmove = [othervalvename]
            winningbestmoves = bestmoves
            bestscore = score
    return bestscore,  winningmove + winningbestmoves

score , moves = findBestMove1("AA", ("AA",), 30)
print(f"Day 16:\n1) The most pressure that I can release is {score}, by visiting these valves with non-zero flowrates: {moves}.")

## part 2!

@lru_cache(maxsize=1200)
def findBestMove2(destdist1, destdist2, valvesopened, minutesLeftTotal): #
    # As a test I changed the valves with the lowest flow rates so that they had 0 flowrate and computed the best route
    # Now I use this route to make sure that during the first steps, we follow this path... Cheaty?
    bestPlaces = ["CO","EU", "IJ", "QN",  "GJ", "NA", "SE", "AE",  "MN", "KF", "CS" ]
    bestPlaces = bestPlaces[:4]
    dest1 = destdist1[0]
    dist1 = destdist1[1]
    dest2 = destdist2[0]
    dist2 = destdist2[1]
    # open valves if I or the elephants reached their destination valve
    if dist1 == 0 and dest1 not in valvesopened:
        valvesopened = valvesopened + tuple([dest1])
    if dist2 == 0 and dest2 not in valvesopened:
        valvesopened = valvesopened + tuple([dest2])
    # Just to be sure :P
    valvesopened = tuple(sorted(valvesopened))
    # Score for this minute
    score = sum([allvalves[valve].flowrate for valve in valvesopened])
    # Consider all valves that are not opened yet and are not destinations of either of us
    valvesLeft = [vv for vv in allvalves if vv not in valvesopened and vv != dest1 and vv != dest2]

    # Initialize a list of destinations we would like to consider next
    newdestdists = []
    if minutesLeftTotal <= 1:
        # Don't consider opening any new valve
       pass
    elif len(valvesLeft) > 1:
        ## if two ore more valves left
        if dist1 == 0 and dist2 == 0:
            for newdest1 in valvesLeft:
                newdist1 = allvalves[dest1].distances[newdest1]

                for newdest2 in [k for k in valvesLeft if k != newdest1]:
                    # This is the cheaty part
                    if (minutesLeftTotal < 20) or (newdest1 in bestPlaces and newdest2 in bestPlaces):
                        newdist2 = allvalves[dest2].distances[newdest2]
                        destdists = ((newdest1, newdist1), (newdest2, newdist2))
                        newdestdists.append(destdists)
        elif dist1 == 0:
            for newdest1 in valvesLeft:
                if (minutesLeftTotal < 20) or newdest1 in bestPlaces:
                    newdist1 = allvalves[dest1].distances[newdest1]
                    destdists = ((newdest1, newdist1), (dest2, dist2 -1))
                    newdestdists.append(destdists)
        elif dist2 == 0:
            for newdest2 in valvesLeft:
                if (minutesLeftTotal < 20) or newdest2 in bestPlaces:
                    newdist2 = allvalves[dest2].distances[newdest2]
                    destdists = ((dest1, dist1-1), (newdest2, newdist2))
                    newdestdists.append(destdists)
        else:
            destdists = ((dest1, dist1 -1), (dest2, dist2 - 1))
            newdestdists.append(destdists)
    elif len(valvesLeft) == 0:
        destdists = ((dest1, dist1 - 1), (dest2, dist2 - 1))
        newdestdists.append(destdists)
    else: # exactly one valve left to close
        lastValve = valvesLeft[0]
        if dist1 == 0:
            m = (lastValve, allvalves[dest1].distances[lastValve])
            newdestdists.append( (m, (dest2, dist2-1)) )
        if dist2 == 0:
            m = (lastValve, allvalves[dest2].distances[lastValve])
            newdestdists.append( ((dest1, dist1-1), m))
        newdestdists.append(((dest1, dist1-1), (dest2, dist2-1)))

    # Now, for all the possible next moves, let's check which is the best one! Initialize some variables
    maxscore = 0
    # These are just for keeping track of the routes, not very readable.
    bestmoves1 = [str(dist1) + dest1+str(minutesLeftTotal)]
    bestmoves2 = [str(dist2) + dest2+str(minutesLeftTotal)]
    # To reduce the state space, I sort the values of destdist1 and destdist2
    newdestdists = list(set([tuple(sorted(d)) for d in newdestdists]))
    for combi in newdestdists:
        dd1 = combi[0]
        dd2 = combi[1]
        bestscore, moves1, moves2 = findBestMove2(dd1, dd2, valvesopened, minutesLeftTotal - 1)
        if bestscore > maxscore:
            maxscore = bestscore
            bestmoves1 = [str(dd1[1]) + dd1[0]+str(minutesLeftTotal)] + moves1
            bestmoves2 = [str(dd2[1]) + dd2[0]+str(minutesLeftTotal)] + moves2
    return maxscore + score, bestmoves1, bestmoves2

# Let's see how long this takes!
time1 = time.time()
score, moves1, moves2 = findBestMove2(("AA",0), ("AA",0),  ("AA",), 26)
time2 = time.time()
print(f"2) The best the elephants and I can do together is to release {score} pressure. The calculation took {time2-time1} seconds.")
