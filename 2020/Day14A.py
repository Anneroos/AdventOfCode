import re
text_file = open("input14.txt", "r")
lines = text_file.read().split('\n')
text_file.close()

import time
start = time.time()
mask = "1X11X010X000X0X101X00100011X10100111"
memory = {}
for line in lines:
    # print(line[0:7])
    if line[0:3] == "mem":
        m = re.search("mem\[(\d+)\] = (\d+)$", line)
        address = int(m.group(1))
        value = int(m.group(2))
        binary = format(value,'036b')
        binaryList = list(binary)
        # print(f"address {address} and value {value}, which is {binary} in binary form.")
        for i in range(len(mask)):
            if mask[i] == "1" or mask[i] == "0":
                binaryList[i] = mask[i]
        binary = "".join(binaryList)
        memory[address] = binary
    elif line[0:7] == "mask = ":
        m = re.search("mask = ([X01]+)$", line)
        mask = m.group(1)
        # print(f"Mask is now set to {mask}")


print(memory)
sum = 0
for address in  memory.keys():
    sum += int(memory.get(address),2)
print(f"The answer to part 1 is {sum}.")



print('It took', time.time()-start, 'seconds.')

