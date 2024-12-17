import math
with open("input17.txt") as f:
    a,b = f.read().split("\n\n")
    registers = [int(i.split(": ")[1]) for i in a.split("\n")]
    program = [int(i) for i in b.split(": ")[1].split(",")]


class Computer:
    def __init__(self, start_registers, program, mode):
        self.registers = start_registers
        self.program = program
        self.pointer = 0
        self.output = []
        self.couldBeSame = True # For part 2
        self.mode = mode
    def getComboOperand(self, n):
        if 0 <= n <= 3:
            return n
        elif n == 4:
            return self.registers[0]
        elif n == 5:
            return self.registers[1]
        elif n == 6:
            return self.registers[2]
        else:
            print("n >= 7 should not happen")
            return -1
    def movePointer(self, amount):
        self.pointer += amount
    def setPointer(self, amount):
        self.pointer = amount
    def adv(self, operand): #0
        self.registers[0] = math.floor(self.registers[0] / pow(2,self.getComboOperand(operand)))
        self.movePointer(2)
    def bxl(self, operand): #1
        self.registers[1] = self.registers[1] ^ operand
        self.movePointer(2)
    def bst(self, operand): #2
        self.registers[1] = self.getComboOperand(operand) % 8
        self.movePointer(2)
    def jnz(self, operand): #3
        if self.registers[0] == 0:
            self.movePointer(2)
        else:
            self.setPointer(operand)
    def bxc(self, operand): #4
        self.registers[1] = self.registers[1] ^ self.registers[2]
        self.movePointer(2)
    def out(self, operand): #5
        self.output.append(self.getComboOperand(operand) % 8)
        self.movePointer(2)
        if self.mode == 2:
            for i in range(min(len(self.output), len(self.program))):
                if self.output[i] != self.program[i]:
                    self.couldBeSame = False
                    break
    def bdv(self, operand): #6
        self.registers[1] = math.floor(self.registers[0] / pow(2, self.getComboOperand(operand)))
        self.movePointer(2)
    def cdv(self, operand):#7
        self.registers[2] = math.floor(self.registers[0] / pow(2, self.getComboOperand(operand)))
        self.movePointer(2)
    def giveOutput(self):
        return ",".join([str(i) for i in self.output])
    def runProgram(self):
        while self.pointer < len(self.program) and self.couldBeSame:
            opcode = self.program[self.pointer]
            operand = self.program[self.pointer + 1]
            funclist = [self.adv, self.bxl, self.bst, self.jnz, self.bxc, self.out, self.bdv, self.cdv]
            funclist[opcode](operand)

        if len(self.output) != len(self.program):
            self.couldBeSame = False

        return self.couldBeSame, self.giveOutput()

computer = Computer(registers, program, 1)
print(f"Day 17:\n  1) Output: {computer.runProgram()[1]}.")

# Let op: in het programma worden (up to) de laatste 10 digits van (binaire) A gebruikt.
# De laatste twee instructies halen de laatste 3 digits van A weg en slaan dat op in A, daarna herhalen we het programma tot A 0 is
# Aanpak: We starten met de getallen x in [0, ..., 1023], kijken of die iig het eerste outputcijfer goed hebben. Sla op in candidates.
# Voor alle c in candidates bekijken we de getallen y die je binair kan schrijven als een x in canidates met up to 3 extra digits ervoor.
# Voor deze ytjes checken we of ze de eerste twee outputcijfers correct hebben.
# Etc.

candidates = [i for i in range(0,pow(2,10))]
for x in range(len(program)):
    newcandidates = []
    for c in candidates:
        adjustedRegisters = [c, registers[1], registers[2]]
        computer = Computer(adjustedRegisters, program, 2)
        couldBeSame, output = computer.runProgram()
        output = [int(i) for i in output.split(",")]

        sameSoFar = True
        for i in range(x):
            if len(output) <= i or output[i] != program[i]:
                sameSoFar=False
        if sameSoFar:
            if x < len(program):
                for y in range(0, 8):
                    getal = c + y * pow(2, 3 * x + 10)
                    newcandidates.append(getal)
            else:
                newcandidates.append(c)
    candidates = newcandidates


for c in sorted(candidates):
    adjustedRegisters = [c, registers[1], registers[2]]
    computer = Computer(adjustedRegisters, program, 2)
    couldBeSame, output = computer.runProgram()
    output = [int(i) for i in output.split(",")]
    same = couldBeSame
    for i in range(len(program)):
        if len(output) > i and output[i] != program[i]:
            same = False
    if same and len(program) == len(output):
        print(f"  2) {c}.")
        break


