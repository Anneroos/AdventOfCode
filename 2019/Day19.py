import numpy as np
import matplotlib.pyplot as plt
input19 = [109,424,203,1,21101,11,0,0,1106,0,282,21102,18,1,0,1106,0,259,2101,0,1,221,203,1,21101,31,0,0,1106,0,282,21102,1,38,0,1106,0,259,21002,23,1,2,22102,1,1,3,21102,1,1,1,21101,57,0,0,1106,0,303,2101,0,1,222,21002,221,1,3,21001,221,0,2,21102,259,1,1,21102,80,1,0,1106,0,225,21102,1,79,2,21101,0,91,0,1106,0,303,2102,1,1,223,21001,222,0,4,21102,259,1,3,21101,225,0,2,21102,1,225,1,21101,0,118,0,1105,1,225,21002,222,1,3,21101,118,0,2,21101,0,133,0,1106,0,303,21202,1,-1,1,22001,223,1,1,21102,1,148,0,1105,1,259,1202,1,1,223,20102,1,221,4,20101,0,222,3,21102,1,22,2,1001,132,-2,224,1002,224,2,224,1001,224,3,224,1002,132,-1,132,1,224,132,224,21001,224,1,1,21102,1,195,0,105,1,109,20207,1,223,2,21002,23,1,1,21101,-1,0,3,21102,214,1,0,1106,0,303,22101,1,1,1,204,1,99,0,0,0,0,109,5,2101,0,-4,249,22101,0,-3,1,22102,1,-2,2,21201,-1,0,3,21101,0,250,0,1105,1,225,22101,0,1,-4,109,-5,2105,1,0,109,3,22107,0,-2,-1,21202,-1,2,-1,21201,-1,-1,-1,22202,-1,-2,-2,109,-3,2106,0,0,109,3,21207,-2,0,-1,1206,-1,294,104,0,99,22102,1,-2,-2,109,-3,2106,0,0,109,5,22207,-3,-4,-1,1206,-1,346,22201,-4,-3,-4,21202,-3,-1,-1,22201,-4,-1,2,21202,2,-1,-1,22201,-4,-1,1,22102,1,-2,3,21102,343,1,0,1106,0,303,1105,1,415,22207,-2,-3,-1,1206,-1,387,22201,-3,-2,-3,21202,-2,-1,-1,22201,-3,-1,3,21202,3,-1,-1,22201,-3,-1,2,21201,-4,0,1,21102,384,1,0,1105,1,303,1106,0,415,21202,-4,-1,-4,22201,-4,-3,-4,22202,-3,-2,-2,22202,-2,-4,-4,22202,-3,-2,-3,21202,-4,-1,-2,22201,-3,-2,1,22101,0,1,-4,109,-5,2106,0,0]

class IntCodeComputer:
    def __init__(self, intCode, input, name="Computer zonder naam"):
        self.intCode =  { i : intCode[i] for i in range(0, len(intCode) ) }
        self.input = input
        self.position = 0
        self.relativebase = 0
        self.name = name
        self.isFinished = False
        self.outputValue = -1

    def start(self):
        pass
        # self.isFinished = False

    def stop(self):
        # self.height = int((len(self.outputValue)-1)/(self.width+1))
        # print(self.outputValue)
        # print(self.width, self.height)
        self.isFinished = True


    def addInput(self,value):
        self.input.append(value)
        # print(self.name, "got an input! It was",value," <-----------------------------------")


    def addInputArray(self,inputArray):
        for x in inputArray:
            self.addInput(x)

    def readInput(self,position):

        self.intCode[position] = self.input.pop(0)

    def output(self, value):

        self.outputValue = value

        # self.stop()
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
size = 50
array = np.zeros((size,size))
minY = 0
for i in range(size):
    yOnAndOff = 0
    for j in range(minY,size):
        TractorBeam = IntCodeComputer(input19.copy(),[i,j],"Tractor Beam")
        TractorBeam.runProgram()
        output = TractorBeam.outputValue
        array[i][j] = output
        if output == 1:
            yOnAndOff = 1
        if output == 0 and yOnAndOff == 1:
            break
        if output == 0 and yOnAndOff == 0 and i > 5:
            minY = j
plt.matshow(array)
plt.show()
print("Solution to puzzle 1 of day 19:", int(array.sum()))
############
spaceDict = {}
attempts = 0
x = 0
y = 0
minY = 0
maxY = 0
while attempts < 10000:
    spaceDict[x] = {"minY":-1, "maxY": -1}
    attempts += 1
    y = minY
    yOnAndOff = 0
    while yOnAndOff < 2 and y < maxY+10:
        TractorBeam = IntCodeComputer(input19.copy(), [x, y], "Tractor Beam")
        TractorBeam.runProgram()
        output = TractorBeam.outputValue
        if output == 1 and yOnAndOff == 0:
            yOnAndOff = 1
            spaceDict[x]["minY"] = y
            minY = max(0,y)
            y = max(minY+1, maxY,1)
        elif output == 0 and yOnAndOff == 1:
            yOnAndOff = 2
            maxY = y - 1
            spaceDict[x]["maxY"] = y - 1
        else:
            y += 1
    # check if it fits already
    if spaceDict[x]["minY"] + 99 <=    spaceDict.get(x-99,{}).get("maxY",0):
        print("Solution to puzzle 2 of day 19:", (x-99)*10000 + spaceDict[x]["minY"] )
        break
    x += 1
