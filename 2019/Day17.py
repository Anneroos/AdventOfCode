import numpy as np
import matplotlib.pyplot as plt
input17 = [1,330,331,332,109,2608,1102,1182,1,16,1101,1399,0,24,102,1,0,570,1006,570,36,102,1,571,0,1001,570,-1,570,1001,24,1,24,1105,1,18,1008,571,0,571,1001,16,1,16,1008,16,1399,570,1006,570,14,21102,1,58,0,1105,1,786,1006,332,62,99,21102,333,1,1,21101,0,73,0,1106,0,579,1101,0,0,572,1101,0,0,573,3,574,101,1,573,573,1007,574,65,570,1005,570,151,107,67,574,570,1005,570,151,1001,574,-64,574,1002,574,-1,574,1001,572,1,572,1007,572,11,570,1006,570,165,101,1182,572,127,102,1,574,0,3,574,101,1,573,573,1008,574,10,570,1005,570,189,1008,574,44,570,1006,570,158,1106,0,81,21102,340,1,1,1105,1,177,21101,0,477,1,1106,0,177,21102,514,1,1,21101,0,176,0,1106,0,579,99,21101,184,0,0,1106,0,579,4,574,104,10,99,1007,573,22,570,1006,570,165,1001,572,0,1182,21101,375,0,1,21101,211,0,0,1106,0,579,21101,1182,11,1,21102,222,1,0,1105,1,979,21102,388,1,1,21101,0,233,0,1105,1,579,21101,1182,22,1,21101,0,244,0,1105,1,979,21101,401,0,1,21101,0,255,0,1105,1,579,21101,1182,33,1,21101,266,0,0,1105,1,979,21101,0,414,1,21101,0,277,0,1105,1,579,3,575,1008,575,89,570,1008,575,121,575,1,575,570,575,3,574,1008,574,10,570,1006,570,291,104,10,21101,1182,0,1,21102,313,1,0,1105,1,622,1005,575,327,1101,1,0,575,21102,327,1,0,1106,0,786,4,438,99,0,1,1,6,77,97,105,110,58,10,33,10,69,120,112,101,99,116,101,100,32,102,117,110,99,116,105,111,110,32,110,97,109,101,32,98,117,116,32,103,111,116,58,32,0,12,70,117,110,99,116,105,111,110,32,65,58,10,12,70,117,110,99,116,105,111,110,32,66,58,10,12,70,117,110,99,116,105,111,110,32,67,58,10,23,67,111,110,116,105,110,117,111,117,115,32,118,105,100,101,111,32,102,101,101,100,63,10,0,37,10,69,120,112,101,99,116,101,100,32,82,44,32,76,44,32,111,114,32,100,105,115,116,97,110,99,101,32,98,117,116,32,103,111,116,58,32,36,10,69,120,112,101,99,116,101,100,32,99,111,109,109,97,32,111,114,32,110,101,119,108,105,110,101,32,98,117,116,32,103,111,116,58,32,43,10,68,101,102,105,110,105,116,105,111,110,115,32,109,97,121,32,98,101,32,97,116,32,109,111,115,116,32,50,48,32,99,104,97,114,97,99,116,101,114,115,33,10,94,62,118,60,0,1,0,-1,-1,0,1,0,0,0,0,0,0,1,4,0,0,109,4,2101,0,-3,587,20101,0,0,-1,22101,1,-3,-3,21101,0,0,-2,2208,-2,-1,570,1005,570,617,2201,-3,-2,609,4,0,21201,-2,1,-2,1105,1,597,109,-4,2106,0,0,109,5,2101,0,-4,629,21002,0,1,-2,22101,1,-4,-4,21102,0,1,-3,2208,-3,-2,570,1005,570,781,2201,-4,-3,653,20101,0,0,-1,1208,-1,-4,570,1005,570,709,1208,-1,-5,570,1005,570,734,1207,-1,0,570,1005,570,759,1206,-1,774,1001,578,562,684,1,0,576,576,1001,578,566,692,1,0,577,577,21101,702,0,0,1105,1,786,21201,-1,-1,-1,1106,0,676,1001,578,1,578,1008,578,4,570,1006,570,724,1001,578,-4,578,21102,1,731,0,1105,1,786,1105,1,774,1001,578,-1,578,1008,578,-1,570,1006,570,749,1001,578,4,578,21101,756,0,0,1106,0,786,1105,1,774,21202,-1,-11,1,22101,1182,1,1,21101,0,774,0,1105,1,622,21201,-3,1,-3,1106,0,640,109,-5,2105,1,0,109,7,1005,575,802,21002,576,1,-6,21002,577,1,-5,1106,0,814,21101,0,0,-1,21102,1,0,-5,21101,0,0,-6,20208,-6,576,-2,208,-5,577,570,22002,570,-2,-2,21202,-5,39,-3,22201,-6,-3,-3,22101,1399,-3,-3,1202,-3,1,843,1005,0,863,21202,-2,42,-4,22101,46,-4,-4,1206,-2,924,21102,1,1,-1,1105,1,924,1205,-2,873,21102,35,1,-4,1105,1,924,1202,-3,1,878,1008,0,1,570,1006,570,916,1001,374,1,374,2101,0,-3,895,1101,2,0,0,2102,1,-3,902,1001,438,0,438,2202,-6,-5,570,1,570,374,570,1,570,438,438,1001,578,558,922,20101,0,0,-4,1006,575,959,204,-4,22101,1,-6,-6,1208,-6,39,570,1006,570,814,104,10,22101,1,-5,-5,1208,-5,31,570,1006,570,810,104,10,1206,-1,974,99,1206,-1,974,1101,0,1,575,21102,973,1,0,1105,1,786,99,109,-7,2105,1,0,109,6,21102,0,1,-4,21101,0,0,-3,203,-2,22101,1,-3,-3,21208,-2,82,-1,1205,-1,1030,21208,-2,76,-1,1205,-1,1037,21207,-2,48,-1,1205,-1,1124,22107,57,-2,-1,1205,-1,1124,21201,-2,-48,-2,1105,1,1041,21102,1,-4,-2,1105,1,1041,21102,-5,1,-2,21201,-4,1,-4,21207,-4,11,-1,1206,-1,1138,2201,-5,-4,1059,2101,0,-2,0,203,-2,22101,1,-3,-3,21207,-2,48,-1,1205,-1,1107,22107,57,-2,-1,1205,-1,1107,21201,-2,-48,-2,2201,-5,-4,1090,20102,10,0,-1,22201,-2,-1,-2,2201,-5,-4,1103,2101,0,-2,0,1106,0,1060,21208,-2,10,-1,1205,-1,1162,21208,-2,44,-1,1206,-1,1131,1106,0,989,21102,1,439,1,1105,1,1150,21102,1,477,1,1106,0,1150,21101,514,0,1,21102,1149,1,0,1105,1,579,99,21101,0,1157,0,1105,1,579,204,-2,104,10,99,21207,-3,22,-1,1206,-1,1138,2101,0,-5,1176,2101,0,-4,0,109,-6,2106,0,0,0,5,34,1,38,1,38,1,38,11,3,11,24,1,3,1,34,1,3,1,34,1,3,1,30,5,3,1,30,1,7,1,30,1,7,1,1,11,3,9,6,1,7,1,1,1,9,1,3,1,7,1,6,5,3,5,7,1,3,1,7,1,10,1,5,1,1,1,7,1,3,1,7,1,4,5,1,1,5,1,1,1,7,5,7,1,4,1,3,1,1,1,5,1,1,1,19,1,4,1,3,1,1,1,3,5,19,1,4,1,3,1,1,1,3,1,1,1,21,1,4,1,3,11,19,1,4,1,5,1,3,1,1,1,1,1,19,12,1,5,1,1,15,6,3,1,7,1,1,1,3,1,15,1,4,1,3,1,7,1,1,1,3,1,15,1,4,1,3,1,7,1,1,1,3,1,15,1,4,5,7,11,11,1,18,1,3,1,3,1,11,1,18,11,9,1,22,1,3,1,1,1,9,1,22,5,1,1,9,1,28,1,9,1,28,11,4]


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
        self.width = 0
        self.height = 0
        self.outputValue = ""



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
        self.height = int((len(self.outputValue)-1)/(self.width+1))
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
        if value == 10 and self.width == 0:
            self.width = len(self.outputValue)

        self.outputValue += chr(value)
        # print(self.outputValue)
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

ASCII = IntCodeComputer(input17.copy(), [], "ASCII")


ASCII.runProgram()
maze = ASCII.outputValue
width = ASCII.width
height = ASCII.height


array = np.zeros((height,width))

dict = {"#":1, ".":0 , "^" : 1, "<":1, ">":1, "v":1}

for x in range(width):
    for y in range(height):
        char = maze[y*(width+1) + x]

        array[y][x] = dict[char]
# plt.matshow(array)
# plt.show()


sumarray = array[1:(height-2+1),1:(width-2+1)]+array[2:(height-2+2),1:(width-2+1)]+array[0:(height-2+0),1:(width-2+1)]+array[1:(height-2+1),0:(width-2+0)]+array[1:(height-2+1),2:(width-2+2)]


alignment = 0
for i in range(width-2):
    for j in range(height - 2):
        if sumarray[j,i] == 5:
            alignment += (i+1)*(j+1)
print("Solution of puzzle 1 of day 17:",alignment)

######################################################
class IntCodeComputer2(IntCodeComputer):
    def output(self, value):
        if value > 10000:
            print(value)
        else:

            if value == 10 and self.width == 0:
                self.width = len(self.outputValue)

            if value == 10:
                print(self.outputValue)
                self.outputValue = ""
            else:
                self.outputValue += chr(value)
            # self.stop()
        return value


input17b = input17.copy()
input17b[0] = 2
ASCII2 = IntCodeComputer2(input17b, [], "ASCII")
main = "A,B,A,C,A,C,B,C,C,B"
A = "L,4,L,4,L,10,R,4"
B = "R,4,L,4,L,4,R,8,R,10"
C = "R,4,L,10,R,10"

def ASCIIinputter(stringInput):
    outputIntCodeInput = np.zeros((len(stringInput)+1))
    for x in range(len(stringInput)):
        char = stringInput[x]
        outputIntCodeInput[x] = ord(char)
    outputIntCodeInput[-1] = 10
    return outputIntCodeInput


ASCII2.addInputArray(ASCIIinputter(main))
ASCII2.addInputArray(ASCIIinputter(A))
ASCII2.addInputArray(ASCIIinputter(B))
ASCII2.addInputArray(ASCIIinputter(C))
ASCII2.addInputArray(ASCIIinputter(["n"]))
ASCII2.runProgram()

print(ASCII2.outputValue)
