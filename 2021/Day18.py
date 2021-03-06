#### SECOND SOLUTION - with dictionairies
import time
import ast
import math
import copy

with open("input18.txt", "r") as f:
    lines = [ast.literal_eval(line) for line in f.read().splitlines()]

st= time.time()
def get_element(lst, index):
    if (len(index) == 1):
        return lst[index[0]]
    else:
        return get_element(lst[index[0]], index[1:])

def snailNrToDict(lst):
    indexes = [[0], [1]]
    d = {}
    while len(indexes) > 0:
        pt = indexes.pop(0)
        v = get_element(lst, pt)
        if type(v) == int:
            d[tuple(pt)] = v
        else:
            indexes.append(pt + [0])
            indexes.append(pt + [1])
    return d

def findLeftRightNeighbors(snrDict, index):
    idxtuple = tuple(index)
    integersIndices = [k for k in snrDict if type(snrDict[k]) == int]
    integersIndices.append(idxtuple)  # so that we know that idxtuple is findable, and can find neighbors
    t = sorted(set(integersIndices))
    s = t.index(idxtuple)
    left = t[s - 1] if s - 1 >= 0 else []
    right = t[s + 1] if s + 1 < len(t) else []
    return left, right

def explode(snailNr):
    exploding = False
    explodingIndices = sorted([k  for k in snailNr if len(k) >= 5])
    if explodingIndices:
        exploding = True
        v = [snailNr[explodingIndices[0]], snailNr[explodingIndices[1]]]
        index = tuple(list(explodingIndices[0])[:4])
        snailNr.pop(explodingIndices[0], None)
        snailNr.pop(explodingIndices[1], None)
        snailNr[index] = 0
        left, right = findLeftRightNeighbors(snailNr, index)
        if left != []:
            snailNr[left] +=  v[0]
        if right != []:
            snailNr[right] += v[1]
    return snailNr, exploding

def checkSplit(snailNr):
    d = sorted([k for k, v in snailNr.items() if type(v) == int and v >= 10])
    return d[0] if len(d) > 0 else []

def computeMagnitude(snailNr, index=()):
    if index:
        if index in snailNr:
            return snailNr[index]
        else:
            return 3 * computeMagnitude(snailNr, tuple(list(index) + [0])) + 2 * computeMagnitude(snailNr, tuple(list(index) + [1]))
    else:
        return 3 * computeMagnitude(snailNr,(0,)) + 2 * computeMagnitude(snailNr, (1,))

def computeSum(nr1, nr2):
    snr = {}
    for k,v in nr1.items():
        snr[tuple([0] + list(k))] = v
    for k,v in nr2.items():
        snr[tuple([1] + list(k))] = v
    action = True
    while action:
        action = False
        snr, exploding = explode(snr)
        if exploding:
            action = True
        else:
            i2 = checkSplit(snr)
            if i2:
                action = True
                snr[tuple(list(i2) + [0])] = math.floor(snr[i2] / 2)
                snr[tuple(list(i2) + [1])] = math.ceil(snr[i2] / 2)
                snr.pop(i2,None)
    return snr

snr = snailNrToDict(copy.deepcopy(lines[0]))
for idx,line in enumerate(lines[1:]):
    snr = computeSum(snr, snailNrToDict(copy.deepcopy(line)))
print(f"Part 1: {computeMagnitude(snr)}.")

maxMag = 0
linesAsDict = [snailNrToDict(line) for line in lines]
for idx1, line1 in enumerate(linesAsDict):
    for idx2, line2 in enumerate(linesAsDict[idx1 + 1:]):
        v1 = computeMagnitude(computeSum(copy.deepcopy(line1), copy.deepcopy(line2)))
        v2 = computeMagnitude(computeSum(copy.deepcopy(line2), copy.deepcopy(line1)))
        maxMag = max(v1, v2, maxMag)
print(f"Part 2: {maxMag}.")


et = time.time()
print(f"That took {et-st} seconds.")


#### My first solution, a mix between nested lists and dictionairies
print("That was my updated solution. Now my original solution:")
import ast
import math
import copy
with open("input18.txt", "r") as f:
    lines = [ast.literal_eval(line) for line in f.read().splitlines()]

st = time.time()
def snailNrToDict(lst):
    indexes = [[0],[1]]
    d = {}
    while len(indexes) > 0:
        pt = indexes.pop(0)
        v = get_element(lst,pt)
        d[tuple(pt)] = v
        if type(v) != int:
            indexes.append(pt + [0])
            indexes.append(pt + [1])
    return d

def findLeftRightNeighbors(snailNr,index):
    snrDict = snailNrToDict(snailNr)
    idxtuple = tuple(index)
    integersIndices = [k for k in snrDict if type(snrDict[k]) == int]
    integersIndices.append(idxtuple) # so that we know that idxtuple is findable, and can find neighbors
    t = sorted(set(integersIndices))
    s = t.index(idxtuple)
    left = t[s-1] if s-1>=0 else []
    right = t[s+1] if s+1 < len(t) else []
    return left, right

def checkExplode(snailNr, level=0):
    index = []
    for idx in range(2):
        if type(snailNr[idx]) == int:
            if level >= 4:
                return True, []
        else:
            b,i = checkExplode(snailNr[idx], level + 1)
            if b:
                index += [idx]
                index += i
                return b,index
    return False, index

def get_element(lst, index):
    if(len(index) == 1):
        return lst[index[0]]
    else:
        return get_element(lst[index[0]],index[1:])

def set_element(lst, index, value):
    if(len(index)==1):
        lst[index[0]] = value
    else:
        set_element(lst[index[0]],index[1:],value)
    return lst

def explode(snailNr, index):
    v = get_element(snailNr, index)
    snr = snailNr
    set_element(snr,index,0)
    left, right = findLeftRightNeighbors(snr, index)
    if left != []:
        set_element(snr, left, get_element(snr, left) + v[0])
    if right != []:
        set_element(snr,right,get_element(snr,right) + v[1])
    return snr

def checkSplit(snailNr):
    d = sorted([k for k,v in snailNrToDict(snailNr).items() if type(v) == int and v >= 10])
    return d[0] if len(d) > 0 else []

def computeMagnitude(snailNr):
    if type(snailNr) == int:
        return snailNr
    else:
        return computeMagnitude(snailNr[0])*3 + computeMagnitude(snailNr[1])*2

def computeSum(nr1,nr2):
    snr = [copy.deepcopy(nr1), copy.deepcopy(nr2)]
    action = True
    while action:
        action = False
        b,i = checkExplode(snr)
        if b:
            action = True
            snr = explode(snr, i)
        else:
            i2 = checkSplit(snr)
            if i2:
                action = True

                v = get_element(snr, i2)
                snr = set_element(snr, i2, [math.floor(v/2), math.ceil(v/2)])
    return snr

snr = copy.deepcopy(lines[0])
for line in lines[1:]:
    snr = computeSum(snr, copy.deepcopy(line))
print(f"Part 1: {computeMagnitude(snr)}.")

maxMag = 0
for idx1, line1 in enumerate(lines):
    for idx2, line2 in enumerate(lines[idx1+1:]):
        v1 = computeMagnitude(computeSum(line1.copy(),line2.copy()))
        v2 = computeMagnitude(computeSum(line2.copy(), line1.copy()))
        maxMag = max(v1,v2,maxMag)
print(f"Part 2: {maxMag}.")

et = time.time()
print(f"That took {et-st} seconds.")
