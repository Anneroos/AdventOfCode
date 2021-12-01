import numpy as np
import math

text_file = open("input18", "r")
input = text_file.read().split('\n')
text_file.close()

lines = np.array(input)

# print(lines)

entrance = [-1,-1]
keys = {}
doors = {}
for lineNr in range(len(lines)):
    line = lines[lineNr]
    for charNr in range(len(line)):
        char = line[charNr]

        if not char in [".", "#"]:

            if char == "@":
                entrance = [lineNr, charNr]
            elif char.islower():
                keys[char] = [lineNr, charNr]
            elif char.isupper():
                doors[char] = [lineNr, charNr]

print("entrance", entrance)
print("keys", keys)
print("keys", len(keys))
print("doors", doors)

print("doors", len(doors))