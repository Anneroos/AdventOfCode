from copy import deepcopy
with open("input09.txt") as f:
    lines = [x.split(" ") for x in f.read().split("\n")]

class Point:
    def __init__(self, name):
        self.position = [0,0]
        self.name = name
        self.history = [(0,0)]
    def moveLetter(self, letter):
        if letter == "U":
            self.move([0,-1])
        elif letter == "D":
            self.move([0,1])
        elif letter == "L":
            self.move([-1,0])
        elif letter == "R":
            self.move([1,0])
        else:
            print("Unknown move")
    def move(self, direction):
        self.position[0] += direction[0]
        self.position[1] += direction[1]
        self.history.append(tuple(deepcopy(self.position)))
    def follow(self, otherpoint):
        otherpos = otherpoint.position
        dx = otherpos[0] - self.position[0]
        dy = otherpos[1] - self.position[1]
        if abs(dx) > 1 or abs(dy) > 1:
            newmove = [0, 0]
            if dx < 0:
                newmove[0] = -1
            elif dx > 0:
                newmove[0] = 1
            if dy < 0:
                newmove[1] = -1
            elif dy > 0:
                newmove[1] = 1
            self.move(newmove)

# part 1
head = Point("Head")
tail = Point( "Tail" )
for line in lines:
    letter = line[0]
    amount = int(line[1])
    for x in range(amount):
        head.moveLetter(letter)
        tail.follow(head)
print(len(set(tail.history)))

# part 2
length = 10
points = []
for i in range(length):
    points.append(Point(str(i)))

for line in lines:
    letter = line[0]
    amount = int(line[1])
    for x in range(amount):
        points[0].moveLetter(letter)
        for i in range(1,length):
            points[i].follow(points[i-1])
tail = points[-1]

print(len(set(tail.history)))