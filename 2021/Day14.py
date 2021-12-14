with open("input14.txt", "r") as f:
    inputlines = f.read().split("\n\n")
    start = inputlines[0]
    instr = [[i for i in line.split(" -> ")] for line in inputlines[1].splitlines()]
rules = dict(instr)

def computePolymerLength(string, steps):
    # We don't need to remember the full string, just how often each pair occurs
    pairs = {}
    for i in range(len(string)-1):
        pairs[string[i:i+2]] = pairs.get(string[i:i+2],0) + 1
    # pairs = dict([[string[i:i+2],1] for i in range(len(string)-1)])  <-- this worked for part 1, but not for part 2... d'oh! Took me 90 minutes to find that...
    for step in range(steps):
        newpairs = {}
        for pair,n in pairs.items():
            if pair in rules: # if the pair is in the rules, replace it by the two resulting pairs
                middle = rules.get(pair)
                newpairs[pair[0]+middle] = newpairs.get(pair[0]+middle,0) + n
                newpairs[middle + pair[1]] = newpairs.get(middle + pair[1],0) + n
            else: # If this pair is not in the rules, keep the pair (but this doesn't happen apparently)
                newpairs[pair] = n
        pairs = newpairs
    # Count the characters by considering the first char of each pair
    charCounts = {}
    for pair in pairs:
        charCounts[pair[0]] = charCounts.get(pair[0],0) + pairs[pair]
    # Don't forget the last char
    charCounts[string[-1]] =  charCounts.get(string[-1],0) + 1
    return max(charCounts.values()) - min(charCounts.values())

print(f"Part 1: {computePolymerLength(start,10)}.")
print(f"Part 2: {computePolymerLength(start,40)}.")