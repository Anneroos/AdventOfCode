with open("input25.txt") as f:
    input = f.read().split("\n\n")
locks = []
keys = []
for t in input:
    lines = t.split("\n")
    heights = [0,0,0,0,0]
    for line in lines:
        for i in range(len(line)):
            heights[i] += 1 if line[i] == "#" else 0
    type = "lock" if lines[0][0] == "#" else "key"
    if type == "lock":
        locks.append(heights)
    else:
        keys.append(heights)
possibilities = 0
for key in keys:
    for lock in locks:
        sums = [key[i] + lock[i] for i in range(5)]
        fits = True if sum([1 if k <= 7 else 0 for k in sums]) == 5 else False
        if fits:
            possibilities += 1

print(possibilities)