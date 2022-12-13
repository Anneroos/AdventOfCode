with open("input13.txt") as f:
    pairs = [[eval(i) for i in x.split("\n")] for x in f.read().split("\n\n")]

def compareLeftRight(left, right):
    result = "?"
    if type(left) == int and type(right) == int:
        if left == right:
            result = 0
        else:
            result = 1 if left <= right else -1
    elif type(left) == list and type(right) == list:
        if len(left) > 0 and len(right) > 0:
            result = compareLeftRight(left[0],right[0])
            if result == 0:
                result = compareLeftRight(left[1:], right[1:])
        elif len(left) == 0 and len(right) == 0:
            result = 0
        else:
            result = 1 if len(left) == 0 else -1
    else:
        if type(left) == int:
            result = compareLeftRight([left],right)
        elif type(right) == int:
            result = compareLeftRight(left, [right])
    return result

# part 1
solution1 = sum([index+1 if compareLeftRight(pairs[index][0],pairs[index][1]) == 1 else 0 for index in range(len(pairs))])
print(f"Day 13:\n1) The sum of the indices of the pairs of packets that are already in the right order is {solution1}.")

# part 2 - not very efficient, I compare everything with everythin ;)
# Maybe I'll write a better version later
sumOfIndices = 0
packets = []
comparePackets = {}
dividerPackets = [[[2]],[[6]]]
pairsPlusDividers = pairs + [dividerPackets]

for index in range(len(pairsPlusDividers)):
    pair = pairsPlusDividers[index]
    for packet in pair:
        packetAsString = str(packet)
        for otherpacket in packets:
            otherPacketAsString = str(otherpacket)
            result = compareLeftRight(packet, otherpacket)
            comparePackets[packetAsString] = comparePackets.get(packetAsString,0) + result
            comparePackets[otherPacketAsString] = comparePackets.get(otherPacketAsString, 0) - result
        packets.append(packet)

sortPackets = list({k:v for k, v in sorted(comparePackets.items(), key=lambda item: item[1], reverse=True)})
k = [sortPackets.index(str(divider))+1  for divider in dividerPackets]
solution2 = k[0] * k[1]
print(f"2) The decoder key for the distress signal is {solution2}.")
