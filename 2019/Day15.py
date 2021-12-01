import msvcrt
import time
import numpy as np
import matplotlib.pyplot as plt
start_time = time.time()
input15 = [3,1033,1008,1033,1,1032,1005,1032,31,1008,1033,2,1032,1005,1032,58,1008,1033,3,1032,1005,1032,81,1008,1033,4,1032,1005,1032,104,99,1002,1034,1,1039,1002,1036,1,1041,1001,1035,-1,1040,1008,1038,0,1043,102,-1,1043,1032,1,1037,1032,1042,1106,0,124,1001,1034,0,1039,1002,1036,1,1041,1001,1035,1,1040,1008,1038,0,1043,1,1037,1038,1042,1106,0,124,1001,1034,-1,1039,1008,1036,0,1041,1001,1035,0,1040,102,1,1038,1043,1002,1037,1,1042,1106,0,124,1001,1034,1,1039,1008,1036,0,1041,102,1,1035,1040,1001,1038,0,1043,1002,1037,1,1042,1006,1039,217,1006,1040,217,1008,1039,40,1032,1005,1032,217,1008,1040,40,1032,1005,1032,217,1008,1039,5,1032,1006,1032,165,1008,1040,35,1032,1006,1032,165,1102,1,2,1044,1106,0,224,2,1041,1043,1032,1006,1032,179,1102,1,1,1044,1106,0,224,1,1041,1043,1032,1006,1032,217,1,1042,1043,1032,1001,1032,-1,1032,1002,1032,39,1032,1,1032,1039,1032,101,-1,1032,1032,101,252,1032,211,1007,0,38,1044,1106,0,224,1101,0,0,1044,1106,0,224,1006,1044,247,1001,1039,0,1034,1001,1040,0,1035,101,0,1041,1036,102,1,1043,1038,1002,1042,1,1037,4,1044,1106,0,0,4,26,16,55,25,8,4,99,2,21,20,20,56,26,97,81,12,2,4,9,32,7,49,54,5,18,81,16,7,88,4,23,30,66,17,31,27,29,34,26,81,62,27,81,41,84,12,53,90,79,37,22,45,27,17,39,76,1,55,58,44,20,18,57,57,20,76,47,20,44,88,26,43,36,79,12,68,30,19,71,27,21,18,75,18,9,56,29,15,84,8,74,93,1,35,91,39,32,86,9,97,54,4,22,59,13,61,31,19,97,26,82,35,73,23,77,71,59,26,76,78,73,34,85,67,26,1,66,91,79,26,95,5,75,99,29,14,23,26,8,66,97,55,21,25,49,17,99,71,37,62,21,45,46,13,29,30,24,31,63,99,12,12,63,10,64,2,76,3,8,37,94,33,12,47,65,35,65,60,12,88,8,10,49,36,12,14,4,43,82,19,16,51,52,20,17,43,18,33,49,19,93,49,29,86,10,31,92,90,44,26,97,8,63,70,81,28,17,80,23,22,79,56,33,67,61,91,37,4,83,77,16,6,8,33,66,92,46,8,34,23,81,3,93,14,23,72,20,91,16,62,79,7,27,81,10,11,44,65,24,66,77,31,12,53,15,50,84,24,70,29,62,50,5,3,88,13,52,85,42,4,15,39,82,65,18,15,58,37,71,10,13,90,98,29,59,52,3,22,13,59,91,29,23,79,1,7,24,80,79,37,31,77,17,11,64,10,9,8,74,97,6,74,35,73,44,68,29,97,3,45,73,30,28,80,9,48,73,76,7,3,77,83,8,12,41,62,44,10,21,27,74,32,95,73,4,47,71,6,67,17,57,10,67,5,25,74,18,24,57,7,61,66,4,51,14,7,44,29,79,74,11,6,49,75,32,3,98,89,63,5,15,5,74,78,37,7,77,3,13,47,9,33,76,22,47,6,72,12,35,75,39,25,87,83,37,19,91,25,45,22,30,54,83,74,22,71,19,3,3,85,74,37,95,26,67,46,10,12,96,44,50,32,90,3,28,56,24,43,4,1,65,5,9,50,22,44,88,9,48,59,21,24,54,11,35,53,28,7,82,32,24,17,45,88,34,72,95,17,9,39,29,4,55,66,95,22,62,15,71,11,39,51,37,86,49,20,10,63,31,66,59,15,55,93,3,11,28,54,30,41,20,92,7,3,12,54,49,14,33,56,89,21,26,67,20,93,7,64,3,31,60,23,51,36,30,57,20,14,28,88,4,6,69,33,65,98,35,96,80,49,25,68,78,97,30,63,35,73,89,32,64,69,10,68,96,19,89,71,41,32,31,30,90,5,71,20,53,36,51,23,87,19,25,15,34,15,48,19,25,33,14,50,64,11,96,19,34,14,44,33,29,40,16,50,90,22,34,44,17,64,63,18,86,57,29,44,22,98,16,41,20,99,34,14,51,11,4,84,91,66,27,49,6,58,34,95,62,6,45,53,27,72,4,12,40,43,17,41,93,27,30,70,31,47,87,26,64,9,63,59,73,9,11,97,35,56,73,23,58,9,49,13,88,1,87,13,54,21,94,13,69,16,39,2,10,64,13,10,19,96,2,23,1,60,99,47,12,61,37,13,70,24,48,91,7,33,51,10,25,88,33,69,29,98,16,16,60,5,29,44,17,21,41,62,65,8,61,84,27,42,78,72,23,98,16,76,98,77,37,19,49,37,93,83,97,1,63,9,63,27,66,34,74,87,58,3,90,4,48,51,67,32,66,9,56,9,44,1,67,24,49,29,58,20,70,32,73,27,82,0,0,21,21,1,10,1,0,0,0,0,0,0]


def simplifyPath(list):
    path = list
    index = 0
    while index < len(path) - 1:
        if path[index] + path[index+1] == 3 or path[index] + path[index+1] == 7:
            path = path[:index] + path[(index+2):]
            index = max(index-1,0)
        else:
            index += 1
    return path




def printSurface(gridDict):
    minX = 0
    maxX = 0
    minY = 0
    maxY = 0
    for key in grid.keys():
        minX = min(key[0], minX)
        maxX = max(key[0], maxX)
        minY = min(key[1], minY)
        maxY = max(key[1], maxY)
    Y = maxY - minY + 1
    X = maxX - minX + 1
    surface = np.zeros((Y, X))
    for j in range(Y):
        for k in range(X):
            surface[j][k] = -1
    for key in grid.keys():
        value = grid.get(key, 0)
        surface[key[1] - minY][key[0] - minX] = value
    print(surface)
    return surface

def printmatrix(surfacematrix):


    plt.matshow(surfacematrix)

    plt.show()

class IntCodeComputer:
    def __init__(self, intCode, input, name="Computer zonder naam"):
        self.intCode =  { i : intCode[i] for i in range(0, len(intCode) ) }
        self.input = input
        self.position = 0
        self.relativebase = 0
        self.name = name
        self.grid = {(0,0):0}
        self.gridPosition = (0,0)
        self.direction = 0
        self.isFinished = False

        self.outputValue = -1



        self.tileTypes = {
            0: " ",
            1: "#",
            2: "x",
            3: "=",
            4: "o"}
        self.ball = [-1,-1]
        self.paddle = [-1, -1]
        self.score = 0

    def start(self):
        pass
        # self.isFinished = False

    def stop(self):
        self.isFinished = True
        # print("Stopped. Temporarily", self.name)
    #

    # def defineNext(self, next):
    #     self.next = next

    # def printScreen(self):
    #
    #     toprint = " \n \n          Score:   " +  str(self.score) + "\n \n "
    #     for i in range(len(self.gameScreen)):
    #
    #         for j in range(len(self.gameScreen[0])):
    #             value = self.gameScreen[i][j]
    #
    #             toprint += self.tileTypes.get(value,"?")
    #
    #         toprint += "\n"
    #
    #
    #     print(toprint)

    def addInput(self,value):
        self.input.append(value)
        # print(self.name, "got an input! It was",value," <-----------------------------------")




    def readInput(self,position):

        self.intCode[position] = self.input.pop(0)




    def output(self, value):
        self.outputValue = value
        self.stop()
        return value


    def runProgram(self):
        self.isFinished = False
        while not self.isFinished:
            self.doAStep()
        return self.outputValue

    def doAStep(self):

        instruction = self.intCode.get(self.position, 0)
        opcode = instruction % 100
        # if not self.isFinished and opcode == 99:
        # print("** Position",self.position, "instruction",instruction)
        if opcode == 99:
            self.stop()
        if not self.isFinished:
            # else:
            instructionLong = f'{instruction:05}'

            param1 = instructionLong[-3]
            param2 = instructionLong[-4]
            param3 = instructionLong[-5]

            a = self.intCode.get(self.position + 1, 0)

            if param1 == "0":  # postion mode
                position_a = a
                value_a = self.intCode.get(position_a, 0)
            elif param1 == "1":  # immediate mode
                value_a = a
            elif param1 == "2":  # relative mode
                position_a = self.relativebase + a
                value_a = self.intCode.get(position_a, 0)
            else:
                print("Oops")
                self.stop()
                return

            if opcode == 1 or opcode == 2 or opcode == 5 or opcode == 6 or opcode == 7 or opcode == 8:
                b = self.intCode.get(self.position + 2, 0)
                if param2 == "0":  # postion mode
                    position_b = b
                    value_b = self.intCode.get(position_b, 0)
                elif param2 == "1":  # immediate mode
                    value_b = b
                elif param2 == "2":  # relative mode
                    position_b = self.relativebase + b
                    value_b = self.intCode.get(position_b, 0)
                else:
                    print("Oops")
                    self.stop()
                    return
            if opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:
                c = self.intCode.get(self.position + 3, 0)
                if param3 == "0":  # postion mode
                    position_c = c
                    value_c = self.intCode.get(position_c, 0)

                elif param3 == "1":  # immediate mode
                    value_c = c
                    print("This should not happen")
                elif param3 == "2":  # relative mode
                    position_c = self.relativebase + c
                    value_c = self.intCode.get(position_c, 0)
                else:
                    print("Oops")
                    self.stop()
                    return
            # if not self.isFinished:
            if opcode == 1:  # addition
                self.intCode[position_c] = value_a + value_b
                self.position += 4
            elif opcode == 2:  # multiplication
                self.intCode[position_c] = value_a * value_b
                self.position += 4
            elif opcode == 3:  # taking input
                self.readInput(position_a)
                self.position += 2
                pass
            elif opcode == 4:  # producing output
                self.position += 2
                # print("------------------------------------------------------>   Output:", value_a)
                return self.output(value_a)
                # self.stop()
                return
            elif opcode == 5:  # jump-if-true
                if value_a != 0:
                    self.position = value_b
                else:
                    self.position += 3
            elif opcode == 6:  # jump-if-false
                if value_a == 0:
                    self.position = value_b
                else:
                    self.position += 3
            elif opcode == 7:  # compare: less than
                if value_a < value_b:
                    self.intCode[position_c] = 1
                else:
                    self.intCode[position_c] = 0
                self.position += 4
            elif opcode == 8:  # compare : equal

                if value_a == value_b:
                    self.intCode[position_c] = 1
                else:
                    self.intCode[position_c] = 0
                self.position += 4
            elif opcode == 9:  # adjust relative base... takes one input
                self.relativebase += value_a
                self.position += 2
            else:
                print("Error! Position", self.position, "intCode[position]=", self.intCode[self.position])
                self.stop()
                return

RepairDroid = IntCodeComputer(input15.copy(), [], "Repair Droid")

grid = {(0,0) : -5}
gridPosition = (0,0)
attempts = 0
# directions = [1,4,2,3] # N E S W
# directionIdx = 0
pathFromOrigin = { (0,0) : {"towards": [], "backToOrigin": [], "distance": 0}}

pointsToVisit = [(0,0),(0,0)]
oppositeDirections = {1:2, 2:1,3:4,4:3}


while len(pointsToVisit)> 0 and attempts < 1000:
    attempts += 1

    # walk back to origin...
    totalDistance = 0
    pathback = pathFromOrigin[gridPosition]["backToOrigin"]
    # new point
    gridPosition = pointsToVisit.pop(0)
    # path to get from origin to new point
    originToCurrentPoint = pathFromOrigin[gridPosition]["towards"]
    # total path:
    totalPath = simplifyPath(pathback + originToCurrentPoint)
    if len(totalPath) > 0:
        for i in totalPath:
            RepairDroid.addInput(i)

            RepairDroid.runProgram()


    print(attempts, "--------- New Grid position:", gridPosition)
    for direction in [1,2,3,4]:
        # print("Current direction: ",direction)
        if direction == 1:  # north
            potentialgridPosition = (gridPosition[0], gridPosition[1] + 1)
        elif direction == 2:  # south
            potentialgridPosition = (gridPosition[0], gridPosition[1] - 1)
        elif direction == 3:  # west
            potentialgridPosition = (gridPosition[0] - 1, gridPosition[1])
        elif direction == 4:  # east
            potentialgridPosition = (gridPosition[0] + 1, gridPosition[1])
        else:
            print("OMG")
            break

        RepairDroid.addInput(direction)
        droidOutput = RepairDroid.runProgram()
        # print("Scanning position ", potentialgridPosition, "output of droid   ---->", droidOutput)

        if droidOutput == 0:
            grid[potentialgridPosition] = 0
            # nextdirection
            # directionIdx = ( directionIdx + 1) % 4
            # print("wall")
        elif droidOutput == 1 or droidOutput == 2:
            if droidOutput == 2:
                print("****************************************************************FOOUNND IT! At ",potentialgridPosition)
                grid[potentialgridPosition] = 2
            # print("I can go there!", potentialgridPosition)
            otherDirection = oppositeDirections[direction]

            # print("otherDirection",otherDirection)

            # add to grid
            if potentialgridPosition not in grid.keys():
                # print("New point!")
                grid[potentialgridPosition] = 1
                pointsToVisit.append(potentialgridPosition)
            # print("key exists:", potentialgridPosition in pathFromOrigin.keys() )
            if not potentialgridPosition in pathFromOrigin.keys() or (pathFromOrigin[gridPosition].get("distance") + 1) < pathFromOrigin[potentialgridPosition].get("distance"):

                # print("distance smaller now?",  (pathFromOrigin[gridPosition].get("distance") + 1) < pathFromOrigin.get(potentialgridPosition,{}).get("distance",1000000))
                # print( pathFromOrigin[gridPosition].get("distance") + 1,  pathFromOrigin[potentialgridPosition].get("distance"))
                pathFromOrigin[potentialgridPosition] =  {"towards": pathFromOrigin[gridPosition]["towards"].copy()+[direction],
                                                          "backToOrigin": [otherDirection] + pathFromOrigin[gridPosition]["backToOrigin"],
                                                          "distance" : ( pathFromOrigin[gridPosition].get("distance") + 1 )}




            RepairDroid.addInput(otherDirection)
            droidOutput = RepairDroid.runProgram()
            # print("quick, walk back!",droidOutput)

            # break
        # 0: wall
        # 1: walk
        # 2: golllddd


    # printSurface(grid)





for position in grid.keys():

    if grid.get(position) == 2:
        oxygenPoint = position

print("Puzzle 1 day 15:",  pathFromOrigin[oxygenPoint].get("distance"))
print("--- Total time: %s seconds ---" % (time.time() - start_time))


start_time2 = time.time()
# printmatrix(printSurface(grid))
maxLength = 0
originToOxygen = pathFromOrigin[oxygenPoint]["towards"]
for position in grid.keys():
    if grid[position] == 1:
        pointToOrigin = pathFromOrigin[position]["backToOrigin"]
        totalPath = simplifyPath(pointToOrigin + originToOxygen)
        maxLength = max(maxLength,len(totalPath))

print("Puzzle 2 of Day 15:", maxLength)
print("--- Total time: %s seconds ---" % (time.time() - start_time2))