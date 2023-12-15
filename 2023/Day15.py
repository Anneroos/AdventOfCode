from collections import defaultdict

with open("input15.txt") as f:
    steps = f.read().split(",")

def computeHash(string):
    s = 0
    for char in string:
        s = (s + ord(char)) * 17 % 256
    return s

# part 1
print(f"Day 15:\n1) After running the HASH algorithm on each step in the initialization sequence, the sum of the results is {sum([computeHash(step) for step in steps])}.")

# part 2
boxes = defaultdict(list)
for step in steps:
    label = "".join([i for i in step if i.isalpha()])
    symbol = step[len(label)]
    focalLength = -1 if symbol == "-" else int(step[len(label) + 1])
    boxNr = computeHash(label)
    if symbol == "=":
        labelsInBox = [lens[0] for lens in boxes[boxNr]]
        if label in labelsInBox: # Replace lens
            boxes[boxNr] = [[lens[0], lens[1] if lens[0] != label else focalLength] for lens in boxes[boxNr]]
        else: # Add lens
            boxes[boxNr].append([label, focalLength])
    else: # Remove lens
        boxes[boxNr] = [lens for lens in boxes[boxNr] if lens[0] != label]
print(f"2) The focusing power of the resulting lens configuration is {sum([sum([(1 + boxIdx) * (lensIdx + 1) * (lens[1]) for lensIdx, lens in enumerate(box)]) for boxIdx, box in boxes.items()])}.")