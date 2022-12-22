with open("input22.txt") as f:
    inputmaze, inputinstructions = f.read().split("\n\n")
    inputmaze = inputmaze.split("\n")

class Maze():
    def __init__(self, mz, ins, part):
        self.blockSize = 50 if len(mz) > 12 else 4
        self.nrBlocksRow = 3 if len(mz) > 12 else 4
        self.part = part
        self.maze = {}
        for y in range(1,len(mz) + 1):

            line = mz[y-1]
            for x in range(1, len(line) + 1):
                if x < len(line) + 1:
                    if line[x-1] != " ":
                        self.maze[(x,y)] = line[x-1]

        self.currentPosition = (min([k[0] for k in self.maze if k[1]==1]),1)
        self.currentDirection = 0 # Right=0, Down = 1, Left = 2, Up = 3
        self.instructions = []
        idx=0
        while idx < len(ins):
            r=1
            while idx + r < len(ins) and ins[idx].isnumeric() == ins[idx+r].isnumeric():
               r+=1
            self.instructions.append(ins[idx:idx+r])
            idx = idx + r
        self.instructionsIdx = 0

        self.pointWrap = {}
        self.blockWrap = {}
        if self.part == 2:#Hardcoded how we wrap around the faces of the cube
            # BLocknr, direction : destination blocknr, destination direction, reverse order of points
            if len(mz) > 12: # for my input, of shape [[0,1,1],[0,1,0],[1,1,0],[1,0,0]]
                self.blockWraps = {(2,2):(7,0,1), (2,3): (10,0, 0),
                              (3,3):(10,3,0), (3,0):(8,2,1), (3,1):(5,2,0),
                              (5,2):(7,1,0), (5,0):(3,3,0),
                              (7,2):(2,0,1), (7,3):(5,0,0),
                              (8,0):(3,2,1), (8,1):(10,2,0),
                              (10,2):(2,1,0), (10,1):(3,1,0), (10,0):(8,3,0)}
            else: # for testinput, with shape [[0,0,1,0],[1,1,1,0],[0,0,1,1]]
                self.blockWraps = {(3, 2): (6, 1, 0), (3, 3): (5, 1, 1), (3, 0): (12, 2, 1),
                                   (5, 3): (3, 1, 1), (5, 2): (12, 3, 1), (5, 1): (11, 3, 1),
                                   (6, 3): (3, 0, 0), (6, 1): (11, 0, 1),
                                   (7, 0): (12, 1, 1),
                                   (11, 2): (6, 3, 1), (11, 1): (5, 3, 1),
                                   (12, 3): (7, 2, 1), (12, 0): (3, 2, 1), (12, 1): (5, 0, 1)}

            for blockDir in self.blockWraps:
                block, dir = blockDir
                destBlock, destdir, shouldReverse = self.blockWraps[blockDir]
                fromPoints = self.getSideOfBlock(block,dir)
                toPoints = self.getSideOfBlock(destBlock, (destdir + 2 ) % 4)
                if shouldReverse == 1: # points are generated from left to right, or top to bottom, so sometimes we have to reverse this
                    toPoints.reverse()
                for idx in range(len(toPoints)):
                    self.pointWrap[(fromPoints[idx],dir)] = (toPoints[idx], destdir)

    def getSideOfBlock(self, blockidx, side):
        points = []
        startx = 1 + ((blockidx - 1) % self.nrBlocksRow) * self.blockSize
        starty = 1 + ((blockidx - 1) // self.nrBlocksRow) * self.blockSize
        dx = 0
        dy = 0
        if side == 0 or side == 2: # x constant, y runs
            dy = 1
            if side == 0:  # right side
                startx += self.blockSize-1
        elif side == 1 or side == 3: # y constant, x runs
            dx = 1
            if side == 1:  # bottom
                starty += self.blockSize-1
        for i in range(self.blockSize):

            point = (startx+i*dx, starty+i*dy)
            points.append(point)
        return points

    def doAStep(self):
        dir = self.currentDirection
        newdir = dir
        x = self.currentPosition[0]
        y = self.currentPosition[1]
        newx = x
        newy = y
        if dir == 0: #"Right"
            newx += 1
            if (newx,newy) not in self.maze:
                if self.part == 1:
                    newx = min([k[0] for k in self.maze if k[1] == newy])
                elif self.part == 2:
                    ((newx, newy), newdir) = self.pointWrap[((x,y),dir)]
        elif dir == 2: #"Left"
            newx -= 1
            if (newx,newy) not in self.maze:
                if self.part == 1:
                    newx = max([k[0] for k in self.maze if k[1] == newy])
                elif self.part == 2:
                    ((newx, newy), newdir) = self.pointWrap[((x,y),dir)]
        elif dir == 1: #"Down"
            newy += 1
            if (newx,newy) not in self.maze:
                if self.part == 1:
                    newy = min([k[1] for k in self.maze if k[0] == newx])
                elif self.part == 2:
                    ((newx, newy), newdir) = self.pointWrap[((x,y),dir)]
        elif dir == 3: #"Up"
            newy -= 1
            if (newx,newy) not in self.maze:
                if self.part == 1:
                    newy = max([k[1] for k in self.maze if k[0] == newx])
                elif self.part == 2:
                    ((newx, newy), newdir) = self.pointWrap[((x,y),dir)]
        # Now that we have the goal position, check if we can actually go there
        if self.maze[(newx,newy)] == ".":
            self.currentPosition = (newx, newy)
            if self.part == 2:
                self.currentDirection = newdir

    def turn(self, turndir):
        if turndir == "L":
            self.currentDirection = (self.currentDirection + 3) % 4
        elif turndir == "R":
            self.currentDirection = (self.currentDirection + 1) % 4

    def takeStep(self):
        instruction = self.instructions[self.instructionsIdx]
        if instruction.isnumeric():
            for i in range(int(instruction)):
                self.doAStep()
        else:
            self.turn(instruction)
        self.instructionsIdx += 1

    def takeSteps(self):
        for i in range(len(self.instructions)):
            self.takeStep()
        return self.currentPosition[1]*1000 + 4*self.currentPosition[0] + self.currentDirection

maze1 = Maze(inputmaze, inputinstructions, 1)
print(f"Day 22:\n1) The final password is {maze1.takeSteps()}.")

maze2 = Maze(inputmaze, inputinstructions, 2)
print(f"2) The final password is {maze2.takeSteps()}.")
