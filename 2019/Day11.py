import matplotlib.pyplot as plt
import numpy as np

input11 = [3,8,1005,8,311,1106,0,11,0,0,0,104,1,104,0,3,8,1002,8,-1,10,101,1,10,10,4,10,108,0,8,10,4,10,1002,8,1,28,2,103,7,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,1001,8,0,55,2,3,6,10,1,101,5,10,1,6,7,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,0,10,4,10,1001,8,0,89,1,1108,11,10,2,1002,13,10,1006,0,92,1,2,13,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,0,10,4,10,101,0,8,126,3,8,1002,8,-1,10,101,1,10,10,4,10,108,1,8,10,4,10,1002,8,1,147,1,7,0,10,3,8,1002,8,-1,10,1001,10,1,10,4,10,108,0,8,10,4,10,101,0,8,173,1006,0,96,3,8,102,-1,8,10,101,1,10,10,4,10,108,0,8,10,4,10,1001,8,0,198,1,3,7,10,1006,0,94,2,1003,20,10,3,8,102,-1,8,10,1001,10,1,10,4,10,1008,8,1,10,4,10,102,1,8,232,3,8,102,-1,8,10,101,1,10,10,4,10,108,1,8,10,4,10,102,1,8,253,1006,0,63,1,109,16,10,3,8,1002,8,-1,10,101,1,10,10,4,10,1008,8,1,10,4,10,101,0,8,283,2,1107,14,10,1,105,11,10,101,1,9,9,1007,9,1098,10,1005,10,15,99,109,633,104,0,104,1,21102,837951005592,1,1,21101,328,0,0,1105,1,432,21101,0,847069840276,1,21101,0,339,0,1106,0,432,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,3,10,104,0,104,1,3,10,104,0,104,0,3,10,104,0,104,1,21102,179318123543,1,1,21102,386,1,0,1106,0,432,21102,1,29220688067,1,21102,1,397,0,1106,0,432,3,10,104,0,104,0,3,10,104,0,104,0,21102,709580567396,1,1,21102,1,420,0,1105,1,432,21102,1,868498694912,1,21102,431,1,0,1106,0,432,99,109,2,22101,0,-1,1,21101,40,0,2,21101,0,463,3,21101,0,453,0,1105,1,496,109,-2,2106,0,0,0,1,0,0,1,109,2,3,10,204,-1,1001,458,459,474,4,0,1001,458,1,458,108,4,458,10,1006,10,490,1102,1,0,458,109,-2,2105,1,0,0,109,4,1202,-1,1,495,1207,-3,0,10,1006,10,513,21102,0,1,-3,21201,-3,0,1,21202,-2,1,2,21101,0,1,3,21101,0,532,0,1106,0,537,109,-4,2106,0,0,109,5,1207,-3,1,10,1006,10,560,2207,-4,-2,10,1006,10,560,22102,1,-4,-4,1105,1,628,21201,-4,0,1,21201,-3,-1,2,21202,-2,2,3,21101,0,579,0,1105,1,537,22101,0,1,-4,21102,1,1,-1,2207,-4,-2,10,1006,10,598,21102,1,0,-1,22202,-2,-1,-2,2107,0,-3,10,1006,10,620,22102,1,-1,1,21101,0,620,0,106,0,495,21202,-2,-1,-2,22201,-4,-2,-4,109,-5,2106,0,0]

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
        self.paintedTiles = {}
        self.outputCounter = 0

    def start(self):
        # self.isFinished = False
        pass

    def stop(self):
        self.isFinished = True
        print(self.name, "stopped! At position", self.position)

    def defineNext(self, next):
        self.next = next

    def addInput(self,value):
        self.input.append(value)


    def output(self, value):
        self.outputCounter += 1
        if self.outputCounter == 1:
            current = self.grid.get(self.gridPosition, -1)
            # print("position",self.gridPosition,"has value", current, "output was ",value)
            if not current == value:
                self.paintedTiles[self.gridPosition] = 1
                self.grid[self.gridPosition] = value
                # print("applying paint to", self.gridPosition)
            # else:
                # print("It already ahs the right color")

        if self.outputCounter == 2:
            self.outputCounter = 0
            if value == 0: # turn left
                self.direction -= 1
            elif value == 1: # turn right
                self.direction += 1
            else:
                self.stop()
                print("Problem with output!")
            self.direction = (self.direction + 4) % 4
            # print("new direction", self.direction)
            # figure out what next tile is
            nextTile = list(self.gridPosition)
            if self.direction == 0: # upward
                nextTile[1] -= 1
            elif self.direction == 1: # right
                nextTile[0] += 1
            elif self.direction == 2: # down
                nextTile[1] += 1
            elif self.direction == 3: # left
                nextTile[0] -= 1
            self.gridPosition = tuple(nextTile)
            # print("Moving to tile ",self.gridPosition," which has color",self.grid.get(self.gridPosition,0))
            # feed color of that tile to input
            self.input.append(self.grid.get(self.gridPosition,0))

    def runProgram(self):
        while not self.isFinished:
            self.doAStep()


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
                self.intCode[position_a] = self.input.pop(0)
                self.position += 2
                pass
            elif opcode == 4:  # producing output
                self.position += 2
                # print("------------------------------------------------------>   Output:", value_a)
                self.output(value_a)
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



paintRobot = IntCodeComputer(input11.copy(),[0],"The Super Painting Robot")
paintRobot.runProgram()

# print(len(paintRobot.paintedTiles))
# minX=0
# maxX=0
# minY=0
# maxY=0
# for key in paintRobot.grid.keys():
#     minX = min(key[0],minX)
#     maxX = max(key[0], maxX)
#     minY = min(key[1], minY)
#     maxY = max(key[1], maxY)
# print(minX,maxX)
# print(minY,maxY)

print("---- day 11 puzzle 2 ----")
paintRobot2 = IntCodeComputer(input11.copy(),[1],"The Super Painting Robot")
paintRobot2.runProgram()

minX=0
maxX=0
minY=0
maxY=0
for key in paintRobot2.grid.keys():
    minX = min(key[0], minX)
    maxX = max(key[0], maxX)
    minY = min(key[1], minY)
    maxY = max(key[1], maxY)
print(minX,maxX)
print(minY,maxY)

surface = np.zeros((maxY-minY+1, maxX-minX+1))

for key in paintRobot2.grid.keys():
    print(key, "**", [key[0]-minX,key[1]-minY])
    value = paintRobot2.grid.get(key,-1)
    surface[key[1]-minY][key[0]-minX] = value

print(surface)
# Display matrix
plt.matshow(surface)

plt.show()