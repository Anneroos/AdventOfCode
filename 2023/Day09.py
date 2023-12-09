with open("input09.txt") as f:
    lines = [[int(i) for i in line.split()] for line in f.read().split("\n")]

def computeDifferences(myArray):
    return [myArray[i]-myArray[i-1] for i in range(1,len(myArray))]

total1 = 0
total2 = 0
for line in lines:
    history = [line]
    start = line
    allZeros = False
    while not allZeros:
        diff = computeDifferences(history[-1])
        history.append(     diff)
        allZeros = True
        for i in range(1, len(diff)):
            if diff[i] - diff[0] != 0:
                allZeros = False
                break
    lastValues = [diff[-1] for diff in history]
    firstValues = [diff[0] for diff in history]
    total1 += sum(lastValues)
    total2 += sum([firstValues[i] * (-1 if (i %2) == 1 else 1) for i in range(len(firstValues))])

print(f"Day 9:\n1) The sum of the extrapolated values is {total1}.")
print(f"2) The sum of the extrapolated values is {total2}.")

