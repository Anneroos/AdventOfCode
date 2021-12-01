
import numpy as np

listOfNumbers = np.loadtxt("adventOfCodeInput8.txt", dtype=int,  delimiter=" ")
# listOfNumbers = np.array([2 ,3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99 ,2, 1, 1, 2])
print(listOfNumbers)







# listOfNumbers = np.array([2, 2,0,1,3 ,0,5,2,2,2,3,4,3, 4])
print(listOfNumbers)

def findnodes(index):
    metadatasum = 0
    value =0
    lengthchildren = 0
    nrOfChildren = listOfNumbers[index]
    nrMetaData = listOfNumbers[index + 1]
    children = np.array([])
    if(nrOfChildren >0):
        print("Node at index", index, "has", nrOfChildren,  "children")
        for i in range(nrOfChildren):
            [lengthchildren1,nrMetaData1, metadatasum1 , value1] = findnodes(index + 2+ lengthchildren)
            # print("output van child:",lengthchildren1,nrMetaData1,metadatasum1)
            lengthchildren += lengthchildren1 + nrMetaData1 + 2
            metadatasum += metadatasum1
            children = np.append(children, value1)

    # if(nrOfChildren == 0):
    #     shift = nrMetaData + 2
    ownmetadata = listOfNumbers[index+lengthchildren+2:index+lengthchildren+2+nrMetaData]
    metadatasum += np.sum(ownmetadata)

    if nrOfChildren ==0:
       value =  metadatasum
    else:
        for child in ownmetadata:
            if child <= len(children):
                value += children[child -1]
    print("Node at index", index, ', total length children',lengthchildren, ', my metadata:', ownmetadata, ', my value', value)

    return lengthchildren, nrMetaData, metadatasum, value

answers =  findnodes(0)
print("The answer to puzzle 1 of Day 8 is ", answers[2])
print("The answer to puzzle 2 of Day 8 is ", int(answers[3]))