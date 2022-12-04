with open("input03.txt") as f:
    rucksacks = f.read().split()
sumOfRucksackPriorities = sum(map(lambda x: ord(x) - 96 if x == x.lower() else ord(x) - 38,[list(set(rucksack[0:int(len(rucksack) / 2)]).intersection(set(rucksack[int(len(rucksack) / 2):])))[0] for rucksack in rucksacks]))
sumOfGroupPriorities = sum(map(lambda x: ord(x) - 96 if x == x.lower() else ord(x) - 38,[list(groupRucksacks[0].intersection(groupRucksacks[1],groupRucksacks[2]))[0] for groupRucksacks in [[set(rucksack) for rucksack in rucksacks[3*grp:3*grp+3]] for grp in range(int(len(rucksacks)/3))]]))

print(f"Day 3:\n1) The sum of the priorities of the item type in each rucksack that appears in both compartments is {sumOfRucksackPriorities}.")
print(f"2) The sum of the priorities of the item type that corresponds to each three-Elf group is  {sumOfGroupPriorities}.")
