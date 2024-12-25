with open("input21.txt") as f:
    codes = f.read().split("\n")

numpad = ["789","456","123",".0A"]
numpad2= {(0,0): "7", (1,0): "8", (2,0): "9", (0,1) :"4", (1,1): "5", (2,1): "6", (0,2): "1", (1,2): "2", (2,2): "3", (1,3): "0", (2,3) : "A"}
numpadRev = {v:k for (k,v) in numpad2.items()}

dirPad = [".^A", "<v>"]
dirPad2 = {(1,0): "^", (2,0): "A", (0,1): "<", (1,1):"v", (2,1): ">"}
dirPadRev = {v:k for (k,v) in dirPad2.items()}

def pointsForRoute(route):
    if route == "" :
        return 0
    else:
        dirs = {">": 4,  "^" :3,  "v" : 2, "<":1 }
        return int("".join([str(dirs[char]) for char in route]))

numpadRoutes = {}
for start in "0123456789A":
    pointsToCheck = [start]
    distancesAndRoutes = {start: {"d":0, "routes": [""]}}
    while len(pointsToCheck):
        point = pointsToCheck.pop(0)
        p = numpadRev[point]
        ns = [(p[0] + 1, p[1]), (p[0] - 1, p[1]), (p[0], p[1] + 1), (p[0], p[1] - 1)]
        dirs = "><v^"
        for nIdx in range(len(ns)):
            npoint = ns[nIdx]
            if npoint in numpad2:
                n = numpad2[ns[nIdx]]
                if n in numpadRev:
                    if n not in distancesAndRoutes or distancesAndRoutes[n]["d"] > distancesAndRoutes[point]["d"] + 1:
                        distancesAndRoutes[n] = { "d": distancesAndRoutes[point]["d"] + 1,  "routes": [k + dirs[nIdx] for k in distancesAndRoutes[point]["routes"] ]}
                        pointsToCheck.append(n)
                    elif distancesAndRoutes[n]["d"] == distancesAndRoutes[point]["d"] + 1:
                        distancesAndRoutes[n] = {"d": distancesAndRoutes[point]["d"] + 1,
                                                 "routes": [k + dirs[nIdx] for k in distancesAndRoutes[point]["routes"]] + distancesAndRoutes[n]["routes"]}
                        pointsToCheck.append(n)

    numpadRoutes[start] = {k:list(set(v["routes"])) for (k,v) in distancesAndRoutes.items()}
    # numpadRoutes[start] = {k: [sorted(list(set(v["routes"])), key=lambda x:pointsForRoute(x), reverse=True)[0]] for (k, v) in distancesAndRoutes.items()}
# print(numpadRoutes)
dirPadRoutes = {}
for start in "<>v^A":
    pointsToCheck = [start]
    distancesAndRoutes = {start: {"d":0, "routes": [""]}}
    while len(pointsToCheck):
        point = pointsToCheck.pop(0)
        p = dirPadRev[point]
        ns = [(p[0] + 1, p[1]), (p[0] - 1, p[1]), (p[0], p[1] + 1), (p[0], p[1] - 1)]
        dirs = "><v^"
        for nIdx in range(len(ns)):
            npoint  = ns[nIdx]
            if npoint in dirPad2:
                n = dirPad2[ns[nIdx]]
                if n in dirPadRev:
                    if n not in distancesAndRoutes or distancesAndRoutes[n]["d"] > distancesAndRoutes[point]["d"] + 1:
                        distancesAndRoutes[n] = { "d": distancesAndRoutes[point]["d"] + 1,  "routes": [k + dirs[nIdx] for k in distancesAndRoutes[point]["routes"] ]}
                        pointsToCheck.append(n)
                    elif distancesAndRoutes[n]["d"] == distancesAndRoutes[point]["d"] + 1:
                        distancesAndRoutes[n] = {"d": distancesAndRoutes[point]["d"] + 1,
                                                 "routes": [k + dirs[nIdx] for k in distancesAndRoutes[point]["routes"]] + distancesAndRoutes[n]["routes"]}
                        pointsToCheck.append(n)

    # dirPadRoutes[start] = {k:list(set(v["routes"])) for (k,v) in distancesAndRoutes.items()}
    dirPadRoutes[start] = {k: [sorted(list(set(v["routes"])), key=lambda x: pointsForRoute(x), reverse=True)[0]] for
                           (k, v) in distancesAndRoutes.items()}


def getNumpadSolutions(code):
    allSolutions = [""]
    position = "A"
    for keyIdx in range(len(code)):
        key = code[keyIdx]
        newSolutions = []
        for r in numpadRoutes[position][key]:
            for s in allSolutions:
                newSolutions.append(s + r + "A")
        allSolutions = newSolutions
        position = key
    minLength = min([len(j) for j in allSolutions])
    allSolutions = [k for k in allSolutions if len(k) == minLength]
    return allSolutions


def getDirpadSolutions(codeList):
    allSolutions = []
    for code in codeList:
        solutionsDirpad = [""]
        position = "A"
        for keyIdx in range(len(code)):
            key = code[keyIdx]
            newSolutionsDirpad = []
            for r in dirPadRoutes[position][key]:
                for s in solutionsDirpad:
                    newSolutionsDirpad.append(s + r + "A")
            position = key
            solutionsDirpad = newSolutionsDirpad
        allSolutions += solutionsDirpad
    minLength = min([len(j) for j in allSolutions])
    allSolutions = [k for k in allSolutions if len(k) == minLength]
    return allSolutions

# PART 1
finalSolution1 = 0
finalSolution2 = 0
for code in codes:
    print(f"---- CODE {code} ------")
    solutions = getNumpadSolutions(code)
    for i in range(10):
        print(i)
        solutions = getDirpadSolutions(solutions)
    minLength = min([len(k) for k in solutions])

    finalSolution1 += minLength*int(code[0:3])


    print( "We start with these solutions", len(solutions), solutions)
    for sol in [solutions[0]]:
        print(f"sol {sol}")
        first = sol[0]
        test0 = getDirpadSolutions([sol])
        print(len(test0[0]), test0)
        tupleCount = {}
        for char1 in "v<>^A":
            for char2 in "v<>^A":
                combo = char1 + char2
                tupleCount[char1+char2] = sol.count(char1+char2)

        tupleCount["A" + first] = tupleCount.get("A" + first, 0) + 1
        for _ in range(15):
            print(f"-------------- {_} ------------")
            print("tuplecount", tupleCount)
            tupleCount = {k: v for (k, v) in tupleCount.items() if v > 0}
            newTupleCount = {}
            for combo in tupleCount:
                char1 = combo[0]
                char2 = combo[1]
                comboRecurrences = tupleCount[combo]
                route = "A" + dirPadRoutes[char1][char2][0] + "A"
                # print("Combo:", combo, "Route : ", route)
                for i in range(len(route)-1):
                    # print( "route[i:i+2]:",route[i:i+2], comboRecurrences)
                    newTupleCount[route[i:i+2]] = newTupleCount.get(route[i:i+2],0) + comboRecurrences

            first = dirPadRoutes["A"][first][0][0]
            tupleCount = newTupleCount.copy()
            # tupleCount["A" + first] = tupleCount.get("A" + first, 0) + 1
            print(newTupleCount)
            print("Sum newtuplecounts", _, sum([v for v in newTupleCount.values()]))
            print("Sum tuplecounts", _, sum([v for v in tupleCount.values()]))

        length = sum([v for v in tupleCount.values()])

    finalSolution2 += length*int(code[0:3])
print(f"Day 21:\n  1) {finalSolution1}.")
print(finalSolution2)
#
# <Av<A>>^A                 v<,     >^    Av
# v<<A>>^Av<A<A>>^AvAA^<A>A
#
# GOED
# ^<A^^Avv>AvA
# ['<Av<A>>^A<AA>Av<AA>A^Av<A>^A'] 28
#  %%%   ['v<<A>>^Av<A<A>>^AvAA^<A>Av<<A>>^AAvA^Av<A<A>>^AAvA^A<A>Av<A<A>>^AvA^<A>A'] 72
# GOED
# <^<A^^Av>vvA>A
# ['v<<A>^Av<A>>^A<AA>Av<A>A<AA>^AvA^A'] 34
#  %%%   ['v<A<AA>>^AvA^<A>Av<A<A>>^AvAA^<A>Av<<A>>^AAvA^Av<A<A>>^AvA^Av<<A>>^AAvA^<A>Av<A>^A<A>A'] 86
#
# ^^<A<Av>vA>A
# ['<AAv<A>>^Av<<A>>^Av<A>A<A>^AvA^A'] 32
#  %%%   ['v<<A>>^AAv<A<A>>^AvAA^<A>Av<A<AA>>^AvAA^<A>Av<A<A>>^AvA^Av<<A>>^AvA^<A>Av<A>^A<A>A'] 82
#
#
# OFF BY ONE (33,81)
# <^<A>A>^^AvvvA
# ['v<<A>^Av<A>>^AvA^AvA^<AA>Av<AAA>^A'] 34
#  %%%   ['v<A<AA>>^AvA^<A>Av<A<A>>^AvAA^<A>Av<A>^A<A>Av<A>^A<Av<A>>^AAvA^Av<A<A>>^AAAvA^<A>A'] 82
#
# IFF BY ONE(31,77)
# ^<^^AvvvA^^Avv>A
# ['<Av<A>^AA>Av<AAA>^A<AA>Av<AA>A^A'] 32
#  %%%   ['v<<A>>^Av<A<A>>^AvA^<A>AAvA^Av<A<A>>^AAAvA^<A>Av<<A>>^AAvA^Av<A<A>>^AAvA^A<A>A'] 78
#

# 35534757796216 too low
# 355347577962162
# 355347577960253 too high
# 255347577960253 too high as well
# 355347577960253
# 100000000000000