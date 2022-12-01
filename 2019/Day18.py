# revisited 14-12-2021
import numpy as np
with open("input18", "r") as f:
    input = f.read().split('\n')
lines = np.array(input)

def neighbors(point,w,h):
    return [tuple([x,y]) for x,y in  [[point[0]+i,point[1]+j] for i,j in [[-1,0],[1,0],[0,1],[0,-1]]] if x>=0 and y>=0 and x<w and y<h]

charToNeighbors = {}
class mazePoint:
    def __init__(self,char,position):
        self.char=char
        self.position=position
        self.nearbyPoints = []
        self.nearbyDistances = []

        # self.findNearbyThings()
    def findNearbyThings(self):
        # print(f"---- find neighbors for point {self.char} at {self.position}")
        pointsToCheck = [self.position]
        w = len(input)
        h = len(input[0])
        visited = [self.position]
        distances = {self.position: 0}
        while len(pointsToCheck) > 0:
            point = pointsToCheck.pop(0)
            visited.append(point)

            for n in neighbors(point,w,h):
                if n in maze:
                    distances[n] = distances[point] + 1
                    if n in points and n not in visited and points[n].char not in self.nearbyPoints:
                        # print(f"current point {point} neighbor {n} with char {maze[n]}")
                        self.nearbyDistances.append([points[n],distances[n]])
                        self.nearbyPoints.append(points[n].char)
                    elif n not in pointsToCheck and n not in visited:
                        pointsToCheck.append(n)

        charToNeighbors[self.char] = self.nearbyPoints
        print(f"{self.char}  op plek {self.position} has neighbors { [self.nearbyPoints]}.")
        # print(self.nearbyKeys)


maze = {}
entrance = None
points = {}
charToPoint = {}
for lineNr,line in enumerate(lines):
    for charNr,char in enumerate(line):
        if not char in [".", "#"]:
            newpoint = mazePoint(char, (lineNr, charNr))
            points[(lineNr, charNr)] = newpoint
            charToPoint[char] = newpoint
            if char == "@":
                entrance = newpoint
        if char != "#":
            maze[(lineNr,charNr)] = char

keys=[p.char for p in points.values() if p.char in "abcdefghijklmnopqrstuvwxyz"]
print("All keys: ",keys)
for pos,point in points.items():
    point.findNearbyThings()
print(sorted("zxgda"))
# Soo, now we need to find feasible paths, and of them the shortest.
pathCheckDict = {"@":True}
pathToReachablePoints = { "": "@" }
print(pathToReachablePoints)
pathsToCheck = ["@"]
finalPaths = []
# fill pathToReachablePoints
count = 0
while len(pathsToCheck)>0:
    count+=1
    if(count%1000==0):
        print(count, path)
    path = pathsToCheck.pop(0) # Assume that the path minus last character is feasible
    # print("current path", path, len(pathToReachablePoints))
    if len(path) == len(keys)+1:
        finalPaths.append(path)
    sortedpath = "".join(sorted(path))
    if sortedpath not in pathToReachablePoints:
        # We have to compute reachable points, and then we can decide what next options we have
        sortedPathAlmost = "".join(sorted(path[:(len(path)-1)]))
        reachables = pathToReachablePoints[sortedPathAlmost] # reachables from previous step
        newreachables = reachables
        pointsToCheck = [path[-1]] + list(reachables)
        while len(pointsToCheck) > 0 :
            pt = pointsToCheck.pop(0)
            for char in charToNeighbors[pt]: #charToPoint[pt].nearbyPoints:
                if char not in pointsToCheck and char not in newreachables:
                    if char.islower() or char.lower() in path:
                        pointsToCheck.append(char)
                        newreachables += char
        # newreachables = list(set(newreachables))
        pathToReachablePoints[sortedpath] = "".join(newreachables)
    reachables = pathToReachablePoints[sortedpath]
    keysLeft = [k for k in keys if k not in path and k in reachables]
    # print(f"reachables {newreachables}")
    # print(f"keysLeft {keysLeft}")
    for key in keysLeft:
        pathsToCheck.append(path+key)
        # print(f"! {path+key} will be checked later!")
print(pathToReachablePoints)
print(finalPaths)

def computeLength(path):
    # TO DO
    return 0

print(min([computeLength(path) for paths in finalPaths]))


# What I had back then (not much)
# import numpy as np
# import math
#
# text_file = open("input18", "r")
# input = text_file.read().split('\n')
# text_file.close()
#
# lines = np.array(input)
#
# # print(lines)
#
# entrance = [-1,-1]
# keys = {}
# doors = {}
# for lineNr in range(len(lines)):
#     line = lines[lineNr]
#     for charNr in range(len(line)):
#         char = line[charNr]
#
#         if not char in [".", "#"]:
#
#             if char == "@":
#                 entrance = [lineNr, charNr]
#             elif char.islower():
#                 keys[char] = [lineNr, charNr]
#             elif char.isupper():
#                 doors[char] = [lineNr, charNr]
#
# print("entrance", entrance)
# print("keys", keys)
# print("keys", len(keys))
# print("doors", doors)
#
# print("doors", len(doors))