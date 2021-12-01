from itertools import chain, combinations
input = sorted([11, 30, 47, 31 , 32,36,3,1,5,3,32,36,15,11,46,26,28,1,19,3])
eggnog = 150

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

count = 0
minimumNrOfBoxes = len(input)
minimumCombos = 0
for combination in powerset(input):
    if sum(combination) == eggnog:
        count += 1
        if len(combination) < minimumNrOfBoxes:
            minimumNrOfBoxes = len(combination)
            minimumCombos = 1
        elif len(combination) == minimumNrOfBoxes:
            minimumCombos += 1
print(f"Day 17 part 1: {count}.")
print(f"Day 17 part 2: we need at least {minimumNrOfBoxes} to store the {eggnog} liter eggnog. There are {minimumCombos} ways of doing that.")