import re
with open("input16.txt") as f:
    auntLines = f.read().split("\n")


AuntSue = {"children": 3, "cats": 7, "samoyeds": 2,  "pomeranians": 3, "akitas": 0, "vizslas": 0, "goldfish": 5, "trees": 3, "cars": 2, "perfumes": 1 }
# Part 1
for auntLine in auntLines:
    m = re.search("Sue (\d+): ", auntLine)
    auntNr = m.group(1)
    x = re.findall( "(\w+): (\d+),?", auntLine)
    couldBeThisAuntie = True
    for property in x:

        if AuntSue[property[0]] is not int(property[1]):
            couldBeThisAuntie = False
            break
    if couldBeThisAuntie:
        print(f"Day 16 part 1: The real auntie Sue is auntie Sue number {auntNr}."  )

for auntLine in auntLines:
    m = re.search("Sue (\d+): ", auntLine)
    auntNr = m.group(1)
    x = re.findall( "(\w+): (\d+),?", auntLine)
    couldBeThisAuntie = True
    for property in x:
        # print(property)
        if property[0] in ["cats", "trees"] and AuntSue[property[0]] >=  int(property[1]):
            couldBeThisAuntie = False
        elif property[0] in ["pomeranians", "goldfish"] and AuntSue[property[0]] <= int(property[1]):
            couldBeThisAuntie = False
            break
        elif property[0] not in ["cats", "trees", "pomeranians", "goldfish"] and AuntSue[property[0]] is not int(property[1]):
            couldBeThisAuntie = False
            break
    if couldBeThisAuntie:
        print(f"Day 16 part 1: No no, the REAL auntie Sue is... auntie Sue number {auntNr}!")
