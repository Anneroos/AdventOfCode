#text_file = open("puzzleinput5.txt", "r")
#lines = text_file.read().split('\n')
#text_file.close()

from numpy import loadtxt
lines = loadtxt("puzzleinput5.txt", dtype=int, comments="#", delimiter=",", unpack=False)
lines = lines[:10]
idx = 0
steps = 0
while idx < len(lines):
    newidx = idx + lines[idx]
    if lines[idx] >= 3:
        lines[idx] -= 1
    else:
        lines[idx] += 1
    idx=newidx
    steps+=1


# this is the output for puzzle 2 actually ;)
print("we had ", steps, "steps")
