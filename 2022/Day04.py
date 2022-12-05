with open("input04.txt") as f:
    inp = [[[int(i) for i in j.split("-")] for j in x.split(",")] for x in f.read().split()]
completeleyOverlappingPairs = 0
overlappingPairs = 0
for k in inp:
    elf1 = k[0]
    elf2 = k[1]
    if (elf1[0] <= elf2[0] and elf1[1] >= elf2[1]) or (elf1[0] >= elf2[0] and elf1[1] <= elf2[1]):
        completeleyOverlappingPairs += 1
    if not (elf1[1] < elf2[0] or elf1[0] > elf2[1]): # Equivalent: if (elf1[1] >= elf2[0] and elf1[0] <= elf2[1]):
        overlappingPairs += 1
print(f"Day 4:\n1) There are {completeleyOverlappingPairs} pairs that have completely overlapping ranges.")
print(f"2) There are {overlappingPairs} pairs with overlapping ranges.")
