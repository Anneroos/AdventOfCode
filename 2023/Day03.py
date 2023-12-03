with open("input03.txt", "r") as f:
    engine = f.read().split('\n')


def findSymbolsAndGears(lineNr, startindex, endindex, engineSchema):
    symbols = []
    gears = []
    lineMin = max(0,lineNr - 1)
    lineMax = min(len(engineSchema) - 1, lineNr + 1)
    indexMin = max(0,startindex-1)
    indexMax = min(endindex + 1, len(engineSchema[0]) - 1)
    for lineIdx in range(lineMin, lineMax + 1):
        for index in range(indexMin, indexMax + 1):
            char = engineSchema[lineIdx][index]
            if char != "." and not char.isnumeric():
                symbols.append(char)
                if char == "*":                    
                    gears.append((lineIdx,index))
    return list(set(symbols)), gears

totalEngineParts = 0 # part 1
gearsDict = {} # part 2

for lineIdx in range(len(engine)):
    # First find a number
    line = engine[lineIdx]
    foundDigit = False
    endOfNumber = False
    numberAtEndOfLine = False
    number = ""
    for i in range(len(line)):
        char = line[i]
        if char.isnumeric():
            foundDigit = True
            number += char
        else:
            if foundDigit: # so if previously found a digit, but now not
                foundDigit = False
                endOfNumber = True
        if (i == len(line)-1 and foundDigit):
            numberAtEndOfLine = True
        if endOfNumber or numberAtEndOfLine:
            startindex = i - len(number)
            endindex = i - 1
            if numberAtEndOfLine:
                startindex += 1
                endindex += 1
            symbols, gears = findSymbolsAndGears(lineIdx, startindex, endindex, engine)
            if len(symbols) > 0: # Part 1
                totalEngineParts += int(number)
            for gear in gears: # Part 2
                gearsDict[gear] = gearsDict.get(gear,[]) + [int(number)]
            number = ""
            endOfNumber = False
            numberAtEndOfLine = False

print(f"Day 3:\n1) The sum of all of the part numbers in the engine schematic is {totalEngineParts}.")

gearSum = 0
for gear, numbers in gearsDict.items():
    if len(numbers) == 2:
        gearSum += numbers[0] * numbers[1]

print(f"2) The sum of all the gear ratios in the engine schematic is {gearSum}.")

