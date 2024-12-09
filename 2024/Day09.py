import math
with open("input09.txt") as f:
    diskmap1 = [int(i) for i in f.read()]
    diskmap2 = diskmap1.copy()

li = 0 # left index
ri = len(diskmap1) - 1  # right index
checksum = 0
positionFinal = 0  # final location
result = ""
while li <= ri:
    while diskmap1[li] == 0 and li < len(diskmap1):
        li += 1
    if li % 2 == 0:
        if diskmap1[li] > 0 and li < len(diskmap1):
            result += str(int(math.floor(li/2)))
            checksum += positionFinal * math.floor(li/2)
            diskmap1[li] -= 1
            positionFinal += 1
    else:  # li % 2 == 1
        while diskmap1[ri] == 0 and ri >= 0:
            ri -= 2
        if diskmap1[li] > 0:
            if ri >= 0 and diskmap1[ri] > 0:
                result += str(int(math.floor(ri / 2)))
                checksum += positionFinal * math.floor(ri/2)
                diskmap1[ri] -= 1
                diskmap1[li] -= 1
                positionFinal += 1

print(f"Day 09:\n  1) The resulting filesystem checksum is {checksum}.")

# -------------- PART 2 ---------------------------#

movedStuff = {}
movedFiles = []
ri = len(diskmap2) - 1
while ri >= 0:
    fileSize = diskmap2[ri]
    fileNumber = int(math.floor(ri/2))
    li = 1
    while li < ri:
        freeSpace = diskmap2[li] - movedStuff.get(li, {'used':0})['used']
        if freeSpace >= fileSize:
            if li not in movedStuff:
                movedStuff[li] = {'used':0, 'tenants':[]}
            movedStuff[li]["used"] += fileSize
            movedStuff[li]["tenants"] = movedStuff[li].get("tenants",[]) + [(fileNumber,diskmap2[ri])]
            movedFiles += [fileNumber]
            break
        li += 2
    ri -= 2

li = 0 # left index
checksum = 0
positionFinal = 0 # final location
result = ""
while li < len(diskmap2):
    if li % 2 == 0:
        fileNumber = int(math.floor(li/2))
        if fileNumber not in movedFiles:
            result += str(int(math.floor(li/2))) * diskmap2[li]
            for _ in range(diskmap2[li]):
                checksum += positionFinal * fileNumber
                positionFinal += 1
        else:
            result += "." * diskmap2[li]
            for _ in range(diskmap2[li]):
                positionFinal += 1
    else:  # li % 2 == 1
        if li in movedStuff:
            for tenant in movedStuff[li]["tenants"]:
                fileNumber = tenant[0]
                fileSize = tenant[1]
                result += str(fileNumber) * fileSize
                for _ in range(fileSize):
                    checksum += positionFinal * fileNumber
                    positionFinal += 1
        for _ in range(diskmap2[li] - movedStuff.get(li,{'used':0})['used']):
            result += "."
            positionFinal += 1
    li += 1

print(f"  2) The resulting filesystem checksum is now {checksum}.")