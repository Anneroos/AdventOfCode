import numpy as np
import math

text_file = open("input20.txt", "r")
input = text_file.read().split('\n')
text_file.close()

lines = np.array(input)

# print(lines)

portals = {}
maze = {}
for lineNr in range(len(lines)):
    line = lines[lineNr]
    for charNr in range(len(line)):
        char = line[charNr]

        if not char in [".", "#", " "]:
            isPortal = False
            portalName = "-"
            # print(charNr,len(line),lineNr,len(line))
            if charNr < len(line) - 1:
                nextChar = line[charNr+1]
                if nextChar not in [".", "#", " "]:
                    portalName = char + nextChar
                    isPortal = True
                    if charNr < len(line) - 2 and line[charNr+2] == ".":
                        portalCoord = (lineNr, charNr+2)
                    else:
                        portalCoord = (lineNr, charNr - 1)

            if lineNr < len(lines) - 1:
                nextLine = lines[lineNr+1]
                if charNr < len(nextLine):
                    nextChar = nextLine[charNr]
                    if nextChar not in [".", "#", " "]:
                        portalName = char + nextChar
                        isPortal = True
                        if lineNr > 0 and len(lines[lineNr-1])>charNr and lines[lineNr-1][charNr] == ".":
                            portalCoord = (lineNr -1 , charNr)
                        else:
                            portalCoord = (lineNr + 2, charNr)
            if isPortal:
                maze[portalCoord] = portalName
                if portalName in portals.keys():
                    portals[portalName].append(portalCoord)
                else:
                    portals[portalName] = [portalCoord]
        else:
            if (lineNr, charNr) not in maze.keys():
                maze[(lineNr,charNr)] = char

# Tijd voor Dijkstra
pointsToVisit = [portals["AA"][0]]
distancesDict = {portals["AA"][0] : 0}
while len(pointsToVisit) > 0:
    currentPoint = pointsToVisit.pop(0)
    neighbors = [(currentPoint[0]+1, currentPoint[1]), (currentPoint[0]-1,currentPoint[1]),(currentPoint[0],currentPoint[1]-1),(currentPoint[0],currentPoint[1]+1)]
    for neighbor in neighbors:
        if neighbor in maze.keys():
            valueNeighbor =  maze[neighbor]
            if valueNeighbor not in [" ", "#", "AA"]:
                if valueNeighbor in ["ZZ","."]:
                    if neighbor not in distancesDict.keys() or distancesDict.get(currentPoint)+1 < distancesDict.get(neighbor,1000000):
                        distancesDict[neighbor] = distancesDict[currentPoint] + 1
                        if maze[neighbor] != "ZZ":
                            pointsToVisit.append(neighbor)
                else: # then it is a portal!
                    nameOfPortal = maze[neighbor]
                    # print("Portal! Name: ", nameOfPortal)
                    locations = portals[nameOfPortal]
                    # print(locations)
                    if locations[0] == neighbor:
                        goToLocation = locations[1]
                    else:
                        goToLocation = locations[0]
                    if goToLocation not in distancesDict.keys() or distancesDict.get(currentPoint) + 2 < distancesDict.get(goToLocation, 1000000):
                        distancesDict[goToLocation] = distancesDict[currentPoint] + 2
                        if maze[neighbor] != "ZZ":
                            pointsToVisit.append(goToLocation)


print("Solution to puzzle 1 of day 20:" ,distancesDict[portals["ZZ"][0]])

################## PUZZLE 2 ############################################

portals = {}
maze = {}
for lineNr in range(len(lines)):
    line = lines[lineNr]
    for charNr in range(len(line)):
        char = line[charNr]

        if not char in [".", "#", " "]:
            isPortal = False
            portalName = "-"

            if charNr < len(line) - 1:
                nextChar = line[charNr+1]
                if nextChar not in [".", "#", " "]: # horizontal portal
                    portalName = char + nextChar
                    isPortal = True
                    if charNr < len(line) - 2 and line[charNr+2] == ".":
                        portalCoord = (lineNr, charNr+2)
                    else:
                        portalCoord = (lineNr, charNr - 1)

            if lineNr < len(lines) - 1:
                nextLine = lines[lineNr+1]
                if charNr < len(nextLine):
                    nextChar = nextLine[charNr]
                    if nextChar not in [".", "#", " "]: # vertical portal
                        portalName = char + nextChar
                        isPortal = True
                        if lineNr > 0 and len(lines[lineNr-1])>charNr and lines[lineNr-1][charNr] == ".":
                            portalCoord = (lineNr -1 , charNr)
                        else:
                            portalCoord = (lineNr + 2, charNr)
            if isPortal:
                if portalCoord[0] in [2, len(lines[2])-3] or portalCoord[1] in [2, len(lines)-1]:
                    portalType = "Outer"
                else:
                    portalType = "Inner"
                print(portalName, portalCoord,"Check",len(line)-3, len(lines)-1, portalType)
                maze[portalCoord] = portalName
                if portalName in portals.keys():
                    portals[portalName][portalType] = portalCoord
                else:
                    portals[portalName] = {portalType: portalCoord}
        else:
            if (lineNr, charNr) not in maze.keys():
                maze[(lineNr,charNr)] = char

print(portals)

# Tijd voor Dijkstra
pointsToVisit = [(portals["AA"]["Outer"][0],portals["AA"]["Outer"][1],0)]
distancesDict = {(portals["AA"]["Outer"][0],portals["AA"]["Outer"][1],0) : 0}
while len(pointsToVisit) > 0:
    currentPoint = pointsToVisit.pop(0)
    # print("****** current point   ***" , currentPoint)
    neighbors = [(currentPoint[0]+1, currentPoint[1]), (currentPoint[0]-1,currentPoint[1]),(currentPoint[0],currentPoint[1]-1),(currentPoint[0],currentPoint[1]+1)]
    for neighbor in neighbors:
        if currentPoint == (2,2,1):
            print(neighbor)
        if neighbor in maze.keys():
            valueNeighbor =  maze[(neighbor[0],neighbor[1])]
            if currentPoint == (2, 2, 1):
                print(valueNeighbor)
            if valueNeighbor not in [" ", "#", "AA"]:

                if valueNeighbor in ["ZZ","."]:
                    fullNeighbor = (neighbor[0], neighbor[1],currentPoint[2])
                    if fullNeighbor not in distancesDict.keys() or distancesDict.get(currentPoint)+1 < distancesDict.get(fullNeighbor,1000000):
                        distancesDict[fullNeighbor] = distancesDict[currentPoint] + 1
                        if maze[neighbor] != "ZZ":
                            pointsToVisit.append(fullNeighbor)
                        elif maze[neighbor] == "ZZ" and currentPoint[2] == 0:
                            print("FREEEDDOOMM")
                            pointsToVisit = []
                            break
                else: # then it is a portal!
                    nameOfPortal = maze[neighbor]
                    # print("Portal! Name: ", nameOfPortal)
                    portal = portals[nameOfPortal]
                    # print(locations)
                    if neighbor == portal["Inner"]:
                        # print("****** current point   ***", currentPoint)
                        goToLocation = (portal["Outer"][0],portal["Outer"][1],currentPoint[2] + 1)
                        # print("found inner poirta", currentPoint, goToLocation)
                        # print("**** go to location   ***", goToLocation)
                    elif neighbor == portal["Outer"] and currentPoint[2] != 0:
                        # print("****** current point   ***", currentPoint)
                        goToLocation = (portal["Inner"][0], portal["Inner"][1], currentPoint[2] - 1)
                        # print("Found outer portal", currentPoint, goToLocation)
                        # print("**** go to location   ***", goToLocation)
                    else:
                        continue
                    if goToLocation not in distancesDict.keys() or distancesDict.get(currentPoint) + 2 < distancesDict.get(goToLocation, 1000000):
                        distancesDict[goToLocation] = distancesDict[currentPoint] + 2
                        if maze[neighbor] != "ZZ":
                            pointsToVisit.append(goToLocation)
    # print(pointsToVisit)


print("Solution to puzzle 2 of day 20:" ,distancesDict[(portals["ZZ"]["Outer"][0],portals["ZZ"]["Outer"][1],0)])

###