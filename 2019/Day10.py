import numpy as np
import math

text_file = open("input10.txt", "r")
input = text_file.read().split('\n')
text_file.close()

lines = np.array(input)

width = len(lines[0])
height = len(lines)

asteroids = {}
for y in range(height):
    line = lines[y]
    for x in range(width):
        # print(x,y, line[x])
        if line[x] == "#":
            asteroids[x,y] = 1

maxSeeableAsteroids = 0
winner = (-1,-1)
for asteroid in asteroids.keys():
    asteroidsAbleToSee = 0
    for other_asteroid in asteroids.keys():
        if not asteroid == other_asteroid:
            dx = other_asteroid[0] - asteroid[0]
            dy = other_asteroid[1] - asteroid[1]
            gcd = math.gcd(dx,dy)
            ableToSee=True
            for step in range(1,gcd):
                result = asteroids.get((asteroid[0] + dx/gcd*step, asteroid[1] + dy/gcd*step),"none")
                if result == 1:
                    ableToSee = False
                    break
            if ableToSee:
                asteroidsAbleToSee += 1
    if maxSeeableAsteroids < asteroidsAbleToSee:
        maxSeeableAsteroids = asteroidsAbleToSee
        winner = asteroid

print("Day 10 puzzle 1:")
print(maxSeeableAsteroids,winner)
print("----------------")
print("Day 10 puzzle 2:")



laser = winner
angles = {}
for asteroid in asteroids.keys():
    if asteroid != laser:
        dx = asteroid[0] - laser[0]
        dy = asteroid[1] - laser[1]
        angle = (math.atan2(dy,dx)*180/math.pi + 90 + 360 )%360
        # print(dx,dy, angle)
        if angle in angles.keys():
            angles[angle].append(asteroid)
        else:
            angles[angle] = [asteroid]

# print(angles)

asteroidsToShoot = angles.copy()
# print(asteroidsToShoot)
sortedAngleList = sorted(angles.keys())
attempts = 0
asteroidsShot = 0
while len(asteroidsToShoot.keys())>0 and attempts<1000:
    attempts += 1
    for laserAngle in sortedAngleList:
        possibleAsteroids = asteroidsToShoot.get(laserAngle,[])
        if len(possibleAsteroids)>0:
            minDistance = 1000000
            asteroidToGetShot = "None"
            for asteroid in possibleAsteroids:
                dx = asteroid[0] - laser[0]
                dy = asteroid[1] - laser[1]
                distanceSqr = dx*dx + dy*dy
                if distanceSqr < minDistance:
                    minDistance = distanceSqr
                    asteroidToGetShot = asteroid
            asteroidsShot += 1
            if asteroidsShot == 200:

                print("200th asteroid to be vaporized is asteroid at location :", asteroidToGetShot, ", so the answer for puzzle 2 is", asteroidToGetShot[0]*100+asteroidToGetShot[1])
           
            asteroidsToShoot[laserAngle].remove(asteroidToGetShot)

            if len(asteroidsToShoot[laserAngle]) == 0:
                asteroidsToShoot.pop(laserAngle, None)





