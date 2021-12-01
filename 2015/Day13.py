import re
from itertools import chain, combinations, permutations

def volgordes(iterable):
    s = list(iterable)
    return permutations(s, len(s))

with open("input13.txt") as file:
    lines = file.read().split("\n")

# initialize names and happiness dictionairy
names = []
happinessDict = {}
for line in lines:
    m = re.search("(\w+) would (\w{4}) (\d+) happiness units by sitting next to (\w+).$",line)
    who = m.group(1)
    verb = m.group(2)
    number = int(m.group(3))
    other = m.group(4)
    if verb == "lose":
        number = - number
    happinessDict[(who, other)] = number
    if who not in names:
        names.append(who)

# add myself for part 2
for name in names:
    happinessDict[("me", name)] = 0
    happinessDict[(name, "me")] = 0

# part 1
seatingOptions = list(volgordes(names))
optimalHappiness = 0
for seating in seatingOptions:
    currentHappiness = 0
    for i in range(len(seating)-1):
        person = seating[i]
        other = seating[i+1]
        currentHappiness += happinessDict[(person, other)]
        currentHappiness += happinessDict[(other, person)]
    currentHappiness += happinessDict[(seating[len(seating)-1], seating[0])]
    currentHappiness += happinessDict[(seating[0],seating[len(seating)-1])]
    if currentHappiness > optimalHappiness:
        optimalHappiness = currentHappiness
print(f"Day 13 part 1: {optimalHappiness}")


# part 2
names.append("me")
seatingOptions = list(volgordes(names))
optimalHappiness = 0
for seating in seatingOptions:
    currentHappiness = 0
    for i in range(len(seating)-1):
        person = seating[i]
        other = seating[i+1]
        currentHappiness += happinessDict[(person, other)]
        currentHappiness += happinessDict[(other, person)]
    currentHappiness += happinessDict[(seating[len(seating)-1], seating[0])]
    currentHappiness += happinessDict[(seating[0],seating[len(seating)-1])]
    if currentHappiness > optimalHappiness:
        optimalHappiness = currentHappiness
print(f"Day 13 part 1: {optimalHappiness}")

