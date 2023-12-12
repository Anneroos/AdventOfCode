with open("input12.txt") as f:
    lines = f.read().split("\n")

cache = {}

def findCombinations2(springs, groups):
    if (springs, groups) in cache:
        return cache[(springs, groups)]
    degreesOfFreedom = len(springs) - (sum(groups) + len(groups) - 1)
    if len(groups) == 0:
        if springs.find("#") >= 0:  # if no groups, but still there is a #, then not possible
            cache[(springs, groups)] = 0
            return 0
        else:
            cache[(springs, groups)] = 1
            return 1
    else:
        group = groups[0]
        total = 0
        for d in range(degreesOfFreedom + 1):
            isGoodChoice = False
            # Consider placing this group from index d up to index (d+group)
            # Then we first need d times a . or ?, then (d+group) times a # or ?
            # and then finish off with 1 . or ? (or all the way up to the end)
            if springs[0:d].find("#") < 0 and springs[d:(d + group)].find(".") < 0:
                if len(groups) == 1 and springs[(d + group):].find("#") < 0:
                    isGoodChoice = True
                elif len(groups) != 1 and springs[(d + group)] != "#":
                    isGoodChoice = True
            if isGoodChoice:  # It is possible!
                total += findCombinations2(springs[(d + group + 1):], groups[1:]) # +1, because there needs to be a '.'
        cache[(springs, groups)] = total
        return total

sumOfCounts1 = []
sumOfCounts2 = []

for line in lines:
    springs, groups = line.split(" ")
    groups = [int(i) for i in groups.split(",")]
    result1 = findCombinations2(springs,tuple(groups))
    sumOfCounts1.append(result1)

    springs2 = springs + "?" + springs + "?" + springs + "?" + springs + "?" + springs
    groups2 = tuple(groups + groups + groups + groups + groups)
    result2 = findCombinations2(springs2, tuple(groups2))
    sumOfCounts2.append(result2)

print(f"Day 12:\n1) The sum of the different arrangements of operational and broken springs that meet the given criteria is {sum(sumOfCounts1)}.")
print(f"2) After unfolding my condition records; the new sum of possible arrangement counts is {sum(sumOfCounts2)}.")

### Initial solution part 1 - with regex!
# import re
# import math
# import random
#
# def findCombinations(springs, regex):
#     if re.search(regex, springs):
#         idxs = [i for i in range(len(springs)) if springs[i] == "?"]
#         if len(idxs) > 0:
#             idx = idxs[random.randrange(len(idxs))]
#             newsprings1 = springs[:idx] + "." + springs[(idx + 1):]
#             newsprings2 = springs[:idx] + "#" + springs[(idx + 1):]
#             return findCombinations(newsprings1, regex) + findCombinations(newsprings2, regex)
#         else:
#             return 1
#     else:
#         return 0
#
# sum_of_counts = []
# for line in lines:
#     springs, groups = line.split(" ")
#     groups = [int(i) for i in groups.split(",")]
#     regex = "^[\.\?]*"
#     for i, group in enumerate(groups):
#         regex += "[#\?]{" + str(group) + "}"
#         if i < len(groups) - 1:
#             regex += "[\.\?]+"
#         else:
#             regex += "[\.\?]*$"
#     result = findCombinations(springs,regex)
#     sum_of_counts.append(result)
#
# print(sum(sum_of_counts))
