import re
from itertools import chain, combinations
text_file = open("input14.txt", "r")
lines = text_file.read().split('\n')
text_file.close()

import time
start = time.time()

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))



mask = "1X11X010X000X0X101X00100011X10100111"
memory = {}

for line in lines:
    # print(line[0:7])
    if line[0:3] == "mem":
        m = re.search("mem\[(\d+)\] = (\d+)$", line)
        address = int(m.group(1))
        value = int(m.group(2))
        binary = format(address,'036b')
        binaryList = list(binary)
        Xpositions = []
        for i in range(len(mask)):
            if mask[i] == "1":
                binaryList[i] = mask[i]
            elif mask[i] == "X":
                Xpositions.append(i)

        for set in list(powerset(Xpositions)):
            for position in Xpositions:
                binaryList[position] = "1" if  position in set else "0"

            binary = "".join(binaryList)
            memory[binary] = value
    elif line[0:7] == "mask = ":
        m = re.search("mask = ([X01]+)$", line)
        mask = m.group(1)
        # print(f"Mask is now set to {mask}")
        # print(f"Mask contains {mask.count('X')} X's.")

#

# print(memory)
sum = 0
for address in  memory.keys():
    sum += memory.get(address)
print(f"The answer to part 2 is {sum}.")

# # python 3
print('It took', time.time()-start, 'seconds.')

