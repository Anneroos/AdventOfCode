with open("input02.txt") as f:
    lines = [[int(l) for l in k.split(" ")] for k in f.read().splitlines()]
nrOfSafeLines = 0

def checkReport(report):
        safe = True
        dir = report[1]-report[0]
        if dir == 0 or abs(dir) > 3:
            safe = False
        else:
            for i in range(2, len(report)):
                newdif = report[i] - report[i-1]
                if newdif * dir <= 0 or abs(newdif) > 3:
                    safe = False
                    break
        return safe

for line in lines:
    if checkReport(line):
        nrOfSafeLines += 1
print(nrOfSafeLines)


nrOfSafeLines = 0
for line in lines:
    if checkReport(line):
        nrOfSafeLines += 1
    else:
        for i in range(len(line)):
            if checkReport(line[0:i] + line[i+1:]):
                nrOfSafeLines += 1
                break

print(nrOfSafeLines)
