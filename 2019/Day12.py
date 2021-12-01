import numpy as np
from math import gcd
import time
start_time = time.time()

class Moon:
    def __init__(self, position ,name="Moon"):
        self.position = np.array(position)
        self.name = name
        self.velocity = np.array([0,0,0])
        self.neighbors = []
        self.gravity = np.array([0,0,0])
    def whoAreMyNeighbors(self,neighbors):
        self.neighbors = neighbors
    def computeGravity(self):
        self.gravity = np.array([0, 0, 0])
        for other_moon in self.neighbors:
            self.gravity += np.sign(other_moon.position - self.position)
            # for dim in dimensionsToCheck:
            #     pass

    def applyGravity(self):
        self.velocity += self.gravity
    def move(self):
        self.position += self.velocity
    def computeEnergy(self):
        self.potentialEnergy = np.sum(np.abs(self.position))
        self.kineticEnergy = np.sum(np.abs(self.velocity))
        self.totalEnergy = self.potentialEnergy * self.kineticEnergy
        return self.totalEnergy


# Define the 4 moons - my input
Io = Moon([9,13,-8],"Io")
Europa = Moon([-3,16,-17],"Europa")
Ganymede = Moon([-4,11,-10],"Ganymede")
Callisto = Moon([0,-2,-2],"Callisto")
Moons = [Io,Europa,Ganymede,Callisto]

# Tell the moons who are their neighbors
Io.whoAreMyNeighbors([Europa,Ganymede,Callisto])
Europa.whoAreMyNeighbors([Io,Ganymede,Callisto])
Ganymede.whoAreMyNeighbors([Europa,Io,Callisto])
Callisto.whoAreMyNeighbors([Europa,Ganymede,Io])

# initalize - uggly stuff
positionVelocityX= (Io.position[0],Europa.position[0],Ganymede.position[0],Callisto.position[0],Io.velocity[0],Europa.velocity[0],Ganymede.velocity[0],Callisto.velocity[0])
positionVelocityY = (
Io.position[1], Europa.position[1], Ganymede.position[1], Callisto.position[1], Io.velocity[1], Europa.velocity[1],
Ganymede.velocity[1], Callisto.velocity[1])
positionVelocityZ = (
Io.position[2], Europa.position[2], Ganymede.position[2], Callisto.position[2], Io.velocity[2], Europa.velocity[2],
Ganymede.velocity[2], Callisto.velocity[2])

xDict = {positionVelocityX:0}
yDict = {positionVelocityY:0}
zDict = {positionVelocityZ:0}

xPeriod = [-1,-1]
yPeriod = [-1,-1]
zPeriod = [-1,-1]

# Let's get them mooooving
foundAll = [0,0,0]
for step in range(1,10000000000):
    # print("*** step",step)
    # print(" -- gravities")
    for moon in Moons:
        moon.computeGravity()
    for moon in Moons:
        moon.applyGravity()
    totalEnergy = 0
    for moon in Moons:
        moon.move()
        moon.computeEnergy()
        totalEnergy += moon.potentialEnergy + moon.kineticEnergy
    if foundAll[0] == 0:
        positionVelocityX = (Io.position[0],Europa.position[0],Ganymede.position[0],Callisto.position[0],Io.velocity[0],Europa.velocity[0],Ganymede.velocity[0],Callisto.velocity[0])
        testX = xDict.get(positionVelocityX, -1)
        if testX == -1:
            xDict[positionVelocityX] = step
        else:
            print("We've been here before! X", step, testX)
            foundAll[0] = 1
            xPeriod = [testX,step]
    if foundAll[1] == 0:
        positionVelocityY = (
            Io.position[1], Europa.position[1], Ganymede.position[1], Callisto.position[1], Io.velocity[1], Europa.velocity[1],
            Ganymede.velocity[1], Callisto.velocity[1])
        testY = yDict.get(positionVelocityY, -1)
        if testY == -1:
            yDict[positionVelocityY] = step
        else:
            print("We've been here before! Y", step,testY)
            foundAll[1] = 1
            yPeriod = [testY, step]
    if foundAll[2] == 0:
        positionVelocityZ = (
            Io.position[2], Europa.position[2], Ganymede.position[2], Callisto.position[2], Io.velocity[2],
            Europa.velocity[2],
            Ganymede.velocity[2], Callisto.velocity[2])
        testZ = zDict.get(positionVelocityZ, -1)
        if testZ == -1:
            zDict[positionVelocityZ] = step
        else:
            print("We've been here before! Z", step, testZ)
            foundAll[2] = 1
            zPeriod = [testZ, step]
    if foundAll == [1,1,1]:
        break
    if step == 1000:
        totalEnergy = 0
        for moon in Moons:
            totalEnergy += moon.computeEnergy()
        print("Solution part 1 of day 12:", totalEnergy)
        print("----------------")
print(xPeriod)
print(yPeriod)
print(zPeriod)

a = [xPeriod[1],yPeriod[1],zPeriod[1]]  #will work for an int array of any length
lcm = a[0]
for i in a[1:]:
    lcm = int(lcm * i / gcd(lcm, i))
print("Solution part 2 of day 12:", lcm)
print("--- Total time: %s seconds ---" % (time.time() - start_time))


start_time2 = time.time()
print("**** OTHER APPROACH")
startVecX = [9, -3, -4, 0]
startVecY = [13, 16, 11, -2]
startVecZ = [-8, -17, -10, -2]
startVecs = [startVecX, startVecY, startVecZ]
gravityMatrix = np.array([[-1,1,0,0],[0,-1,1,0],[0,0,-1,1],[1,0,0,-1],[-1,0,1,0],[0,-1,0,1]])
gravityMatrix2 = np.array([[1,0,0,-1,1,0],[-1,1,0,0,0,1],[0,-1,1,0,-1,0],[0,0,-1,1,0,-1]])
periods = []
for vec in startVecs:
    velocity = np.array([0,0,0,0])
    position = vec.copy()
    step =0
    while True:
        step += 1
        gravity = gravityMatrix2.dot(np.sign(gravityMatrix.dot(position)))
        velocity += gravity
        position += velocity
        if np.array_equal(position, vec) and np.array_equal(velocity, np.array([0,0,0,0])):
            print("Stop at step",step)
            periods.append(step)
            break
a = periods
lcm = a[0]
for i in a[1:]:
    lcm = int(lcm * i / gcd(lcm, i))
print("Numpy solution part 2 of day 12:", lcm)
print("--- Total time: %s seconds ---" % (time.time() - start_time2))

