import re
import time
t0 = time.time()
with open("input19.txt") as file:
    input = file.read().split("\n\n")

rules = input[0].split("\n")
messages = input[1].split("\n")


ruleDict = {}
for rule in rules:
    split = rule.split(": ")
    ruleIndex = split[0]
    subrules = split[1].split(" | ")
    subrules = [[index if index.isnumeric() else index[1] for index in subrule.split(" ")] for subrule in subrules]
    ruleDict[ruleIndex] = subrules


def makeRegex(ruleIdx):
    subrules = ruleDict[ruleIdx]  # bijv. [[4 5],[5 4] ]
    regexes = []
    for subrule in subrules:
        regex = ""
        for idx in subrule:
            if idx.isnumeric():
                regex += "(" + makeRegex(idx) + ")"
            else:
                regex += idx

        regexes.append((regex))
    regex =  "|".join(regexes)
    return regex

regex = "^" + makeRegex("0") + "$"
print(f"The regex that we made is of length {len(regex)} and looks like this:\n{regex}")

validMessages = sum([re.match(regex,m) is not None for m in messages])

print(f"Day 19 part 1: there are {validMessages} valid messages!")
t1 = time.time()
print(f"This took {t1-t0} seconds.")