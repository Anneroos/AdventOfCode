import matplotlib.pyplot as plt
with open("input10.txt") as f:
    lines = [x.split(" ") for x in f.read().split("\n")]

class CRT():
    def __init__(self):
        self.signalStrengths = 0
        self.cycle = 0
        self.CRT = ["", "", "", "", "", ""]
        self.lineIdx = 0
        self.X = 1
    def addCycle(self):
        self.cycle += 1
        # for part 1:
        if self.cycle % 40 == 20:
            self.signalStrengths += self.X * self.cycle
        self.addPixel()
    def updateX(self, amount):
        self.X += amount
    def addPixel(self):
        pixelNr = len(self.CRT[self.lineIdx])
        char = "."
        if self.X - 1 <= pixelNr <= self.X + 1:
            char = "#"
        self.CRT[self.lineIdx] += char
        # if we reach end of line, go to next line
        if len(self.CRT[self.lineIdx]) == 40:
            self.lineIdx += 1
    def printCRT(self):
        # First just print the ASCII art:
        for line in self.CRT:
            print(line)
        # Now show as a matrix:
        CRTasMatrix = [[1 if i == "#" else 0 for i in x] for x in self.CRT]
        plt.imshow(CRTasMatrix)
        plt.colorbar()
        plt.show()
    def readLines(self, lines):
        for line in lines:
            self.addCycle()
            if line[0] == "addx":
                self.addCycle()
                self.updateX(int(line[1]))
        print(f"Day 10:\n1) The sum of the six signal strengths is {CRT.signalStrengths}.")
        print(f"2) The eight capital letters are:")
        self.printCRT()

CRT = CRT()
CRT.readLines(lines)