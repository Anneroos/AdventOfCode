with open("input16.txt", "r") as f:
    input = f.read()
from functools import reduce
import operator

def hexToBin(string): # van internet
    return format(int(string, 16), f"0{len(string)*4}b")
packets = hexToBin(input)
levelInfo = {0: {"typeID": 0, "lengthTypeID" : "1", "packetsLeft": 1, "values": []} }
sumOfVersion = 0
level = 0
index = 0
functions = {0: lambda x: sum(x), 1: lambda x: reduce(operator.mul, x, 1) , 2: lambda x : min(x), 3: lambda x : max(x),
             5: lambda x: 1 if x[0] > x[1] else 0, 6: lambda x: 1 if x[0] < x[1] else 0, 7: lambda x: 1 if x[0]==x[1] else 0 }

while level >= 0 and not index >= len(packets):
    # Check if we finished the level
    if  levelInfo[level].get("packetsLeft",1) == 0 or (levelInfo[level].get("lengthTypeID","?") == "0" and index - levelInfo[level].get("endOfHeaderIndex",-1) >= levelInfo[level].get("packetsLeft",10000000000)):
        if level > 0:
            # For part 2: combine the list of values with the correct function, and dump the value in the higher level
            levelInfo[level-1]["values"].append(functions[levelInfo[level]["typeID"]](levelInfo[level]["values"]))
        level -= 1
        if level>=0 and levelInfo[level]["lengthTypeID"] == "1":
            levelInfo[level]["packetsLeft"] -= 1
        continue

    # Start parsing the current packet
    version = int(packets[index:index+3],2)
    typeID = int(packets[index+3:index+6],2)
    # For Part 1:
    sumOfVersion += version

    if typeID == 4: # Literal packet - we will read the bits that belong to this packet, in steps of 5 bits
        i = 0
        num = ""
        while True:
            bits = packets[index+6+5*i:index+6+5*i+5]
            num += bits[1:5]
            i += 1
            if bits[0] == "0": # last chunk of bits
                break
        # move index to end of packet
        packetlength = 6 + i*5
        if levelInfo[level]["lengthTypeID"] == "1":
            levelInfo[level]["packetsLeft"] -= 1
        levelInfo[level]["values"].append(int(num,2))
    else: # Operator packet
        lengthTypeID = packets[index+6]
        levelInfo[level+1] = {"typeID": typeID, "lengthTypeID": lengthTypeID, "values":[]}
        if lengthTypeID == "0":
            length = int(packets[index+7:index+7+15],2)
            levelInfo[level+1]["packetsLeft"] = length
            packetlength = 6 + 1 + 15
            # I use endOfHeaderIndex to see where this package ends, so I can compare it with the index later on to see if we are donw with this package
            levelInfo[level+1]["endOfHeaderIndex"] = index + packetlength
        else:
            nr = int(packets[index + 7:index + 7 + 11], 2)
            packetlength = 6 + 1 + 11
            levelInfo[level+1]["packetsLeft"] = nr
        # An operator packet has subpackets, so let's go a level deeper
        level += 1
    # move index to the end of this packet, so that we can continue reading
    index += packetlength

print(f"Part 1: The sum of the versions of the packets is {sumOfVersion}.")
print(f"Part 2: The expression evaluates to {levelInfo[0]['values'][0]}.")
