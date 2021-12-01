import re
import time
t0 = time.time()
with open("input19.txt") as file:
    rules, messages = file.read().split("\n\n")

def parseRule(ruleString):
    return [[index if index.isnumeric() else index[1] for index in subrule.split(" ")] for subrule in ruleString.split(" | ")]

ruleDict = {}
for rule in rules.split("\n"):
    ruleIndex, subrules = rule.split(": ")
    ruleDict[ruleIndex] = parseRule(subrules)

maxLength = max([len(m) for m in messages.split("\n")])

# PART 2 TWIST
ruleDict["8"] = parseRule("42 | 42 8")
ruleDict["11"] = parseRule("42 31 | 42 11 31")

def makeRegex(ruleIdx, depth): # depth counts how deep we go in nesting rules
    subrules = ruleDict[ruleIdx]
    regexes = []
    for subrule in subrules:
        regex = ""
        for idx in subrule:
            if idx.isnumeric():
                if depth<maxLength/2:
                    regex += "(" + makeRegex(idx, depth + 1) + ")"
                else: # Surely, we don't need that much depth, with message of maximum length maxLength ;)
                    regex += "d"
            else:
                regex += idx
            # if (idx == "8" or idx == "11"):
            #     print(depth)
            #     if depth < 5:
            #         regex += "(" + makeRegex(idx, depth + 1) + ")"
            #     else:  # Surely, we don't need that much depth, with message of maximum length maxLength ;)
            #         regex += "d"
            # else:
            #     regex += "(" + makeRegex(idx, depth) + ")"
        regexes.append((regex))
    regex =  "|".join(regexes)
    return regex

pattern = "^" + makeRegex("0",0) + "$"
print(f"The regex that we made is of length {len(pattern)} and looks like this:\n{pattern}")
validMessages = sum([re.match(pattern,m) is not None for m in messages.split("\n")])
print(f"Day 19 part 2: there are {validMessages} valid messages!")
t1 = time.time()
print(f"This took {t1-t0} seconds.")