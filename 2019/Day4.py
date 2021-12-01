lowerbound=402328
upperbound=864247
lowerboundAsArray = [int(x) for x in str(lowerbound)]
upperboundAsArray = [int(x) for x in str(upperbound)]

def initializeFirstNumber(array):

    for i in range(1,len(array)):
        if array[i] < array[i-1]:
            for k in range(i,len(array)):
                array[k] = array[k-1]
            break
    return array


def findNextNumber(array):
    length = len(array)
    for idx in range(length):
        if array[length-1-idx] < 9:
            array[length-1-idx] += 1
            break
        else: # als wel 9
            if array[length-2-idx] < 9:
                array[length - 1 - idx] = array[length-2-idx] + 1
            else:
                array[length - 1 - idx] = 0
    return array

def checkNumber(array):
    adjacency = False
    monotone = True
    for i in range(1,len(array)):
        if array[i] == array[i-1]:
            adjacency = True
        if array[i] < array[i-1]:
            monotone = False
    return  (adjacency and monotone)

def checkNumber2(array):
    adjacency = False
    monotone = True
    adjacencyDict = {}
    for i in range(1,len(array)):
        if array[i] == array[i-1]:

            adjacencyDict[array[i]] = 1
        if array[i] < array[i-1]:
            monotone = False
    for i in range(2,len(array)):
        if array[i] == array[i-1] and array[i] == array[i-2]:
            adjacencyDict[array[i]] = 0
    for value in adjacencyDict.values():
        if value == 1:
            adjacency = True
    return  (adjacency and monotone)

def checkRange(array):
    outOfRange = False
    currentNumber = int("".join(map(str, array)))
    if currentNumber > upperbound or currentNumber < lowerbound:
        outOfRange = True
    return not outOfRange




possiblePasswords1 = 0
possiblePasswords2 = 0
numberArray = initializeFirstNumber(lowerboundAsArray)

while checkRange(numberArray):
    print(numberArray)
    if checkNumber(numberArray):
        possiblePasswords1 +=1
    if checkNumber2(numberArray):
        possiblePasswords2 +=1
    numberArray = findNextNumber(numberArray)

print(possiblePasswords1)
print(possiblePasswords2)