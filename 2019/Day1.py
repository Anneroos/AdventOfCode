import numpy as np
import math

text_file = open("input1a.txt", "r")
input = text_file.read().split('\n')
text_file.close()
lines = np.array(input)


def fuelCost(mass):
    return math.floor(mass/3) - 2

def fuelCost2(mass):

    if mass >= 7:
        cost = math.floor(mass/3) - 2

        return cost + fuelCost2(cost)
    else: return 0


array = np.array([fuelCost(int(s)) for s in lines])
print("answer puzzle 1 of day 1: ", array.sum())

array = np.array([fuelCost2(int(s)) for s in lines])
print("answer puzzle 2 of day 1: ", array.sum())