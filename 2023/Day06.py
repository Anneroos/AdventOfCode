from functools import reduce
import math

def computeWaysToWin(raceTime, distanceToBeat):
    D = raceTime * raceTime - 4 * distanceToBeat # Discrimant of this quadratic equation in b: - b*b + r*b - d = 0
    buttonTime1 = math.ceil((-raceTime - math.sqrt(D)) / 2)
    buttonTime2 = math.floor((-raceTime + math.sqrt(D)) / 2)
    return 1 + buttonTime2 - buttonTime1

with open("input06.txt", "r") as f:
    lines = [[j.strip() for j in line.split(":")] for line in f.read().split('\n')]

# part 1
times = [int(i) for i in lines[0][1].split()]
distances = [int(i) for i in lines[1][1].split()]
waysToWin = [computeWaysToWin(times[i], distances[i]) for i in range(len(times))]
print(f"The product of the ways to win these {len(times)} races is {reduce((lambda x, y: x * y), waysToWin)}.")

# part 2
raceTime2 = int("".join([i for i in lines[0][1].split()]))
distanceToBeat2 = int("".join([i for i in lines[1][1].split()]))
print(f"There are {computeWaysToWin(raceTime2, distanceToBeat2)} ways to beat this one much longer race.")
