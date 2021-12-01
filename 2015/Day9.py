# 16-12-2020 met Wouter
import re
import numpy as np
text_file = open("input9.txt", "r")
lines = text_file.read().split('\n')
text_file.close()
from itertools import chain, combinations, permutations
# print(lines)
places = {}
nrOfPlaces = 0

for line in lines:
    place = line.split(" ")[0]
    otherplace = line.split(" ")[2]
    if place not in places:
        places[place] = nrOfPlaces
        nrOfPlaces += 1
    if otherplace not in places:
        places[otherplace] = nrOfPlaces
        nrOfPlaces += 1
# print(places)

distances = np.zeros([nrOfPlaces,nrOfPlaces])


for line in lines:
    place = line.split(" ")[0]
    otherplace = line.split(" ")[2]
    distance = int(line.split(" ")[4])
    distances[places[place],places[otherplace]] = distance
    distances[places[otherplace], places[place]] = distance
# print(distances)



# places = ["Tristram","Arbre","Snowdin"]
def volgordes(iterable):
    s = list(iterable)
    return permutations(s, len(s))

routes = list(volgordes(places))

minDistance = 142*7
for route in routes:
    routeDistance = 0
    for i in range(len(route)-1):
        place = places[route[i]]
        otherplace = places[route[i+1]]
        routeDistance += distances[place,otherplace]
    minDistance = int(min(minDistance,routeDistance))
print(f"Day 9 part 1: Distance of shortest route: {minDistance}.")


maxDistance = 0
for route in routes:
    routeDistance = 0
    for i in range(len(route)-1):
        place = places[route[i]]
        otherplace = places[route[i+1]]
        routeDistance += distances[place,otherplace]
        maxDistance = int(max(maxDistance,routeDistance))
print(f"Day 9 part 2: Distance of longest route: {maxDistance}.")

