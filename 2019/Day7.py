originalProgram = [3,8,1001,8,10,8,105,1,0,0,21,34,47,72,81,94,175,256,337,418,99999,3,9,102,3,9,9,1001,9,3,9,4,9,99,3,9,101,4,9,9,1002,9,5,9,4,9,99,3,9,1001,9,5,9,1002,9,5,9,1001,9,2,9,1002,9,5,9,101,5,9,9,4,9,99,3,9,102,2,9,9,4,9,99,3,9,1001,9,4,9,102,4,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,99]
# originalProgram = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
# originalProgram = [ 3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]

def runCode(intCode, input0, input1):
    inputCounter = 0
    position = 0
    attempts = 0
    output = -1

    while  attempts < 100000:
        instruction = intCode[position]
        opcode = instruction % 100
        if opcode == 99:
            break

        instructionLong = f'{instruction:05}'

        param1 = instructionLong[-3]
        param2 = instructionLong[-4]
        # print(intCode)
        # print("position", position)
        # print(instructionLong)


        # print(intCode)
        attempts += 1

        a = intCode[position + 1]
        if param1 == "0":
            value_a = intCode[a]
            # print("postion mode", a,value_a)
        else:
            value_a = a
            # print("immediate mode", a,value_a)

        if opcode == 1 or opcode == 2 or opcode == 5 or opcode == 6 or opcode == 7 or opcode == 8:
            b = intCode[position + 2]


            if param2 == "0":
                value_b = intCode[b]
                # print("postion mode", b, value_b)
            else:
                value_b = b
                # print("immediate mode",b, value_b)
        if opcode == 1 or opcode == 2 or opcode == 5 or opcode == 6 or opcode == 7 or opcode == 8:
            c = intCode[position + 3]

        if opcode == 1: # addition
            intCode[c] = value_a + value_b
            position += 4
        elif opcode == 2: # multiplication
            intCode[c] = value_a * value_b
            position += 4
        elif opcode == 3: # taking input
            if inputCounter == 0:
                intCode[a] = input0
                inputCounter += 1
            else:
                intCode[a] = input1
            position += 2
            pass
        elif opcode == 4: # producing output
            # print("Output:", value_a)
            output = value_a
            position += 2
            pass
        elif opcode == 5: # jump-if-true
            if value_a != 0:
                position = value_b
            else:
                position += 3
        elif opcode == 6: # jump-if-false

            if value_a == 0:
                position = value_b
            else:
                position += 3
        elif opcode == 7: # compare: less than
            if value_a < value_b:
                intCode[c] =1
            else:
                intCode[c] = 0
            position += 4
        elif opcode == 8: # compare : equal
            if value_a == value_b:
                intCode[c] = 1
            else:
                intCode[c] = 0
            position += 4
        else:
            print("Error! Position", position, "intCode[position]=",intCode[position])

            break


    return intCode, output

maxOutput = 0
config = [0,1,2,3,4]
#
# for A in range(5):
#     for B in range(5):
#         if B != A:
#             for C in range(5):
#                 if C!= A and C!= B:
#                     for D in range(5):
#                         if D!=C and D!= B and D!= A:
#                             for E in range(5):
#                                 if E not in [A,B,C,D]:
#                                     print("----",A,B,C,D,E)
#
#                                     amplifierA = runCode(originalProgram.copy(),A,0)
#                                     amplifierB = runCode(originalProgram.copy(), B, amplifierA[1])
#                                     amplifierC = runCode(originalProgram.copy(), C, amplifierB[1])
#                                     amplifierD = runCode(originalProgram.copy(), D, amplifierC[1])
#                                     amplifierE = runCode(originalProgram.copy(), E, amplifierD[1])
#                                     finalOutput = amplifierE[1]
#
#                                     print(finalOutput)
#                                     # finalOutput = faseAOutput
#                                     if finalOutput > maxOutput:
#                                         print("new winner")
#                                         maxOutput = finalOutput
#                                         config = [A,B,C,D,E]
#
# print("Winning configuration",config)
# print(maxOutput)



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
        self.latestOutput = -1

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
        self.latestOutput = value
        self.stop()
        self.next.addInput(value)
        self.next.runProgram()

    def runProgram(self):
        print(self.name, "at position", self.position)
        self.isFinished = False
        while not self.isFinished:
            self.doAStep()


    def doAStep(self):

        instruction = self.intCode.get(self.position, 0)
        opcode = instruction % 100
        # if not self.isFinished and opcode == 99:
        # print(self.name, "at position",self.position, "instruction",instruction)
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
                print(self.position)
                self.position += 2
                print(self.position)
                print("------------------------------------------------------>   Output:", value_a)
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
                print("Opcode 8!")
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



for A in range(5,10):
    for B in range(5,10):
        if B != A:
            for C in range(5,10):
                if C!= A and C!= B:
                    for D in range(5,10):
                        if D!=C and D!= B and D!= A:
                            for E in range(5,10):
                                if E not in [A,B,C,D]:
                                    print("----",A,B,C,D,E)
                                    finalOutput = -1
                                    amplifierA = IntCodeComputer(originalProgram.copy(),[A,0],"Ampy A")
                                    amplifierB = IntCodeComputer(originalProgram.copy(), [B], "Ampy B")
                                    amplifierC = IntCodeComputer(originalProgram.copy(), [C], "Ampy C")
                                    amplifierD = IntCodeComputer(originalProgram.copy(), [D], "Ampy D")
                                    amplifierE = IntCodeComputer(originalProgram.copy(), [E], "Ampy E")

                                    amplifierA.defineNext(amplifierB)
                                    amplifierB.defineNext(amplifierC)
                                    amplifierC.defineNext(amplifierD)
                                    amplifierD.defineNext(amplifierE)
                                    amplifierE.defineNext(amplifierA)
                                    amplifierA.runProgram()
                                    finalOutput = amplifierE.latestOutput

                                    print("FinalOuput this round: ", finalOutput)
                                    # finalOutput = faseAOutput
                                    if finalOutput > maxOutput:
                                        print("new winner")
                                        maxOutput = finalOutput
                                        config = [A,B,C,D,E]


print(maxOutput)
print(config)