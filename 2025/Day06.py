with open("2025/input06.txt") as f:
    rawlines =  f.read().splitlines()
    lines = [k.split() for k in rawlines]
    
nroflines = len(lines)
lenoflines = len(lines[0])
totalsum = 0
for i in range(lenoflines):

    if lines[nroflines-1][i] == "+":
        sum = 0
        for k in range(nroflines-1):
            sum += int(lines[k][i])
        totalsum += sum
    if lines[nroflines-1][i] == "*":
        product = 1
        for k in range(nroflines-1):
            product *= int(lines[k][i])
        totalsum += product

print(f"Day 6:\n  1) {totalsum}")

# Part 2
totalsum = 0
prevEmptyidx = -1
numbers = []
for idx in range(len(rawlines[0])):
    emptyIdx = True
    strN = ""
    for k in range(nroflines-1):
        strN += rawlines[k][idx]
        if rawlines[k][idx] != " ":
            emptyIdx = False
    if not  emptyIdx:
        numbers.append(int(strN)) 
    if emptyIdx or idx == len(rawlines[0]) -1:
        currentEmptyIdx = idx        

        if rawlines[nroflines-1][prevEmptyidx+1] == "+":
            sum = 0
            for n in numbers:
                sum += n
            totalsum += sum
        if rawlines[nroflines-1][prevEmptyidx+1] == "*":
            product = 1
            for n in numbers:
                product *= n
            totalsum += product
        
        prevEmptyidx  = currentEmptyIdx
        numbers = []

print(f"  2) {totalsum}")