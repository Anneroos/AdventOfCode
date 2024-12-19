with open("input19.txt") as f:
    input = f.read().split("\n\n")
    towels_available = input[0].split(", ")
    designs = input[1].split("\n")


def isDesignPossible(des, towels):
    longestTowel = max([len(towel) for towel in towels])
    remainingDesigns = {des:1}
    totalPossibilities = 0
    while len(remainingDesigns) > 0:
        d= list(remainingDesigns.keys())[0]
        for l in range(1,min(longestTowel, len(d)) + 1):
            if d[0:l] in towels:
                rest = d[l:]
                if rest == "":
                    totalPossibilities += remainingDesigns[d]
                else:
                    remainingDesigns[rest] = remainingDesigns.get(rest, 0) + remainingDesigns[d]
        remainingDesigns.pop(d)
    return totalPossibilities

total1 = 0
total2 = 0
for design in designs:
    result = isDesignPossible(design, towels_available)
    if result > 0:
        total1 += 1
        total2 += result

print(f"Day 19:\n  1) There are {total1} designs possible.")
print(f"  2) If we add up the number of different ways you could make each design, we get {total2}.")