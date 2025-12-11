with open("2025/input07.txt") as f:
    lines = f.read().splitlines()
# print(lines)
beamlocations = {i:1 for i in range(len(lines[0])) if lines[0][i]=="S"}
print(beamlocations)
timesSplit = 0
for lineIdx in range(1,len(lines)):
    newbeamlocations = {}
    for i in beamlocations.keys():
        if lines[lineIdx][i]=="^":
            newbeamlocations[i-1] = newbeamlocations.get(i-1,0) + beamlocations[i]
            newbeamlocations[i+1] = newbeamlocations.get(i+1,0) + beamlocations[i]
            
            timesSplit += 1
        else:
            newbeamlocations[i] = newbeamlocations.get(i,0) + beamlocations[i]
    

    print(newbeamlocations)
    beamlocations = newbeamlocations
print(timesSplit)
totalPaths = 0
for k in beamlocations.keys():
    totalPaths += beamlocations[k]
print(totalPaths)