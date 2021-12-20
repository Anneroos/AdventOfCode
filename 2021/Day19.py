import time
st = time.time()
import numpy as np
with open("input19.txt", "r") as f:
    scanners = [np.array([[int(k) for k in j.split(",")] for j in i.splitlines()[1:]]) for i in f.read().split("\n\n")]

mat1 = np.array([[0,1,0],[0,0,1],[1,0,0]])
mat2 = np.array([[1,0,0],[0,0,1],[0,-1,0]])
mat3 = np.array([[-1,0,0],[0,-1,0],[0,0,1]])
def rotateMatrix(vec,f,g,h):
    for i in range(f%3):
        vec = mat1.dot(vec)
    for j in range(g%4):
        vec = mat2.dot(vec)
    if h%2 == 1:
        vec = mat3.dot(vec)
    return vec

rotations = [[np.apply_along_axis(lambda x: rotateMatrix(x,a,b,c), 1, scanner.copy()) for a in range(3) for b in range(4) for c in range(2) ] for scanner in scanners]
scannersFound = []
scannersToVisit = [0]
finalScanners = {0: scanners[0]}
translations = {0: np.array([0,0,0])}
while len(scannersFound) < len(scanners):
    scannerIdx = scannersToVisit.pop(0)
    scanner = finalScanners[scannerIdx]
    scannerToList = [tuple(i) for i in scanner.tolist()]
    len1 = len(scanner)
    scannersFound.append(scannerIdx)
    print(f"Looking at scanner {scannerIdx}. Scanners found so far: {len(scannersToVisit + scannersFound)}.")
    for scannerIdx2 in range(len(scanners)):
        if scannerIdx2 not in scannersFound and scannerIdx2 not in scannersToVisit:
            len2 = len(scanners[scannerIdx2])
            for r,scanner2 in enumerate(rotations[scannerIdx2]):
                foundOverlap = False
                for i1, row1 in enumerate(scanner):
                    for i2, row2 in enumerate(scanner2):
                        diff = np.subtract(row1,row2) # how much to translate
                        sum = len1+len2 - len(set( scannerToList + [tuple(np.add(row,diff)) for row in scanner2]))
                        if sum>= 12:
                            scannersToVisit.append(scannerIdx2)
                            finalScanners[scannerIdx2] = np.apply_along_axis(lambda x: x+diff, 1, scanner2.copy())
                            translations[scannerIdx2] = diff
                            print(f"Scanner {scannerIdx} and scanner {scannerIdx2} overlap for rotation {r}! Sum {sum}. We mapped {i1} on {i2}.")
                            foundOverlap = True
                            break
                    if foundOverlap:
                        break
                if foundOverlap:
                    break

g = []
for k in range(len(finalScanners)):
    g += [tuple(i) for i in finalScanners[k]]
print(f"Part 1: There are {len(set(g))} beacons. ")

maxdist = 0
for i in range(len(translations)):
    for j in range(i,len(translations)):
        d = np.subtract(translations[i],translations[j])
        dist = abs(d[0])+abs(d[1]) + abs(d[2])
        maxdist = max(dist,maxdist)
print(f"Part 2: The maximum Manhattan distance between two scanners is {maxdist}.")

et = time.time()
print(f"Time that it took: {et-st} seconds.")