with open("2025/input10.txt") as f:
    lines = f.read().splitlines()
import math


def findShortestButtons1(lights, buttonsarray):
    nroflights = len(lights)
    start = tuple([0]*nroflights)
    end = tuple([0 if i=="." else 1 for i in lights])
    distances = {start: 0}
    pointsToCheck = [start]
    for round in range(len(buttonsarray)):
        # print(f"Round { round}!")
        newPointsToCheck = []
        for configuration in pointsToCheck:
            for buttons in buttonsarray:

                result = tuple([(configuration[i] + (1 if i in buttons else 0) )%2 for i in range(nroflights)])
                # print(f"Configuration: {configuration}")
                # print(f"Buttons:       {buttons}")
                # print(f"Result:        {result}")
                if result not in distances or distances[result] > distances[configuration] + 1:
                    newPointsToCheck.append(result)
                    distances[result] = distances[configuration] + 1
        if end in distances:
            return distances[end]            
            break
        pointsToCheck = newPointsToCheck

def findShortestButtons2(joltages, buttonsarray):
    nrofjoltages = len(joltages)
    start = tuple([0]*nrofjoltages)
    end = tuple(joltages)
    distances = {start: 0}
    pointsToCheck = [start]
    round = 0
    while end not in distances:
        round += 1
        print(f"Round { round}!")
        newPointsToCheck = []
        for configuration in pointsToCheck:
            for buttons in buttonsarray:
                result = tuple([configuration[i] + (1 if i in buttons else 0) for i in range(nrofjoltages)])
                # print(f"Configuration: {configuration}")
                # print(f"Buttons:       {buttons}")
                # print(f"Result:        {result}")
                if result not in distances or distances[result] > distances[configuration] + 1:
                    if min([result[i] <= end[i] for i in range(nrofjoltages)]):
                        newPointsToCheck.append(result)
                        distances[result] = distances[configuration] + 1
        if end in distances:
            return distances[end]            
            break
        pointsToCheck = newPointsToCheck
        
## PART 1
# totalButtonsPressed = 0
# for line in lines:
#     linesplit = line.split(" ")
#     lights = linesplit[0][1:len(linesplit[0])-1]
#     switches = [[int(i) for i in k[1:len(k)-1].split(",")] for k in linesplit[1:len(linesplit)-1]]
#     print(line)
#     distance = findShortestButtons1(lights, switches)
#     print(distance)
#     totalButtonsPressed += distance

# print(totalButtonsPressed)
    
## PART 2
totalButtonsPressed2 = 0
for line in lines:
    linesplit = line.split(" ")
    lights = linesplit[0][1:len(linesplit[0])-1]
    joltages = [int(i) for i in linesplit[-1][1:len(linesplit[-1])-1].split(",")]    
    switches = [[int(i) for i in k[1:len(k)-1].split(",")] for k in linesplit[1:len(linesplit)-1]]
    print(line)
    distance = findShortestButtons2(joltages, switches)
    print(distance)
    totalButtonsPressed2 += distance

print(totalButtonsPressed2)