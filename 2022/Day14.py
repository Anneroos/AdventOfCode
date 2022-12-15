with open("input14.txt") as f:
    inputpaths = [[[int(j) for j in i.split(",")] for i in x.split(" -> ")] for x in f.read().split("\n")]

class Rock():
    def __init__(self, paths, withBottom=False):
        self.withBottom = withBottom
        self.rocks = {}
        for path in paths:
            start = tuple(path[0])
            for pt in path[1:]:
                line = self.lineBetweenPoints(start,pt)
                for point in line:
                    self.rocks[point] = 1
                start = pt
        self.pouringPoint = (500, 0)
        self.floor = max([k[1] for k in self.rocks])+2

    def findThreeLowerPoints(self, pt):
        return [(pt[0], pt[1] + 1), (pt[0] - 1, pt[1] + 1), (pt[0] + 1, pt[1] + 1)]

    def lineBetweenPoints(self,pt1, pt2):
        dx = pt2[0] - pt1[0]
        dy = pt2[1] - pt1[1]
        d = max(abs(dx), abs(dy))
        dx = 0 if dx == 0 else dx // abs(dx)
        dy = 0 if dy == 0 else dy // abs(dy)
        line = [(pt1[0] + i * dx, pt1[1] + i * dy) for i in range(d + 1)]
        return line

    def pourSand(self):
        sandFalling = True
        while sandFalling:
            result = self.pourGrainOfSand()
            print(result)
            sandFalling = not(result == "infinite") and not (result==  "blocked")
        t = [k for k in self.rocks if self.rocks[k] == 2]
        print(len(t))

    def pourGrainOfSand(self):
        sand = (self.pouringPoint[0], self.pouringPoint[1])
        sandAtRest = False
        while not sandAtRest:
            destinations = self.findThreeLowerPoints(sand)
            sandAtRest = True
            for dest in destinations:
                if (not self.withBottom) or dest[1] < self.floor:
                    if dest not in self.rocks or self.rocks[dest] == "":
                        sand = dest
                        sandAtRest = False
                        break
            if sand[1] > self.floor:
                return "infinite"
        self.rocks[sand] = 2
        return "blocked" if sand == self.pouringPoint else "keepgoing"

rocks = Rock(inputpaths).pourSand()
rocks = Rock(inputpaths, withBottom=True).pourSand()
