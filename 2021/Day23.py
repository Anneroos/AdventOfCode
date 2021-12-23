from collections import defaultdict
with open("input23.txt", "r") as f:
    puzzles = f.read().split("\n\n")

goals = { "A": 3, "B": 5, "C": 7, "D": 9}
costs = { "A": 1, "B": 10, "C": 100, "D": 1000}

def readPuzzleInput(puzzle):
    maze = {}
    for lineIdx,line in enumerate(puzzle.split("\n")):
        for idx,char in enumerate(line):
            if char in "ABCD":
                maze[(lineIdx,idx)] = char
    return maze


def printState(state, prefix=""):
    print(state)
    stateDict = dict(state)
    height = max([k[0] for k in stateDict])
    print("Height", height)
    print(prefix + "#"*13)
    print(prefix + "#" + "".join(["." if (1, i) not in stateDict else stateDict[(1, i)] for i in range(1, 12)]) + "#")
    for h in range(2,height+1):
        print(prefix + "#" +  "".join(["#" if (h,i) not in stateDict else stateDict[(h,i)] for i in range(1,12)]) +"#"   )
    print(prefix + "  #########  ")
    print(" ")



def computeMinimumEnergy(puzzle):
    distances = defaultdict(lambda: 10000000)
    startstate = tuple(readPuzzleInput(puzzle).items())
    height = max([k[0] for k in dict(startstate)])
    distances[startstate] = 0
    stateToCheck = [startstate]
    goal = {}
    for h in range(2, height + 1):
        goal[(h, 3)] = "A"
        goal[(h, 5)] = "B"
        goal[(h, 7)] = "C"
        goal[(h, 9)] = "D"
    goal = tuple(sorted(goal.items()))
    while len(stateToCheck) > 0:
        statetuple = stateToCheck.pop(0)
        state = dict(statetuple)
        for k, v in state.items():
            if v in "ABCD":
                cost = costs[v]
                count = 0

                if goals[v] == k[1]:
                    if sum([state.get((l,k[1]),".") in [".",v] for l in range(k[0]+1,height+1)]) == height-k[0]:
                        # This point is already just fine where it is
                        continue
                if k[0] > 1:  # in a room, trying to move out of room
                    clearWay = True
                    for h in range(2,k[0]):
                        if (h,k[1]) in state:
                            clearWay = False
                    if not clearWay:
                        continue
                    if k[0] == 3 and (2, k[1]) in state:  # Can't move
                        continue
                    else:  # getting out of the room is possible, but can we go sideways?
                        # First, check to the right
                        dx = 1
                        while 1 <= k[1] + dx <= 11 and (1, k[1] + dx) not in state:
                            if k[1] + dx not in [3, 5, 7, 9]: # Yay, there is room here, and it's not above a room
                                newstate = state.copy()
                                newstate.pop(k)
                                newstate[(1, k[1] + dx)] = v
                                newstate = tuple(sorted(newstate.items()))
                                d = k[0] - 1 + dx
                                if newstate not in distances or distances[newstate] > distances[statetuple] + d*cost:
                                    stateToCheck.append(newstate)
                                    distances[newstate] = distances[statetuple] + d*cost
                                assert len(newstate) == (height-1)*4
                                count += 1
                            dx += 1
                        # Similar to the left
                        dx = 1
                        while 1 <= k[1] - dx <= 11 and (1, k[1] - dx) not in state:
                            if k[1] - dx not in [3, 5, 7, 9]:
                                newstate = state.copy()
                                newstate.pop(k)
                                newstate[(1, k[1] - dx)] = v
                                newstate = tuple(sorted(newstate.items()))
                                d = k[0] - 1 + dx
                                if newstate not in distances or distances[newstate] > distances[statetuple] + d*cost:
                                    stateToCheck.append(newstate)
                                    distances[newstate] = distances[statetuple] + d*cost
                                assert len(newstate) == (height-1)*4
                                count += 1
                            dx += 1
                else:  # moving into room? you can only move into your own room
                    col = goals[v]
                    # check if room is empty
                    roomOccupied = False
                    for h in range(2,height+1):
                        if state.get((h,col),".") not in [".", v]:
                            roomOccupied = True
                            continue
                    if roomOccupied:
                        continue
                    # Room empty! Check if route is empty.
                    emptyRoute=True
                    if col > k[1]:
                        for x in range(k[1]+1, col + 1):
                            if (1, x) in state:
                                emptyRoute = False
                                continue
                    else:
                        for x in range(col, k[1]):
                            if (1, x) in state:
                                emptyRoute = False
                                continue
                    if not emptyRoute:
                        continue
                    # The room and the route are free!
                    # Go into the lowest available spot in the room
                    newstate = state.copy()
                    newstate.pop(k)
                    for h in range(height-1):
                        if (height-h,col) not in state:
                            newstate[(height-h, col)] = v
                            d = abs(k[1]-col) + height - h - 1
                            break
                    newstate = tuple(sorted(newstate.items()))
                    if newstate not in distances or distances[newstate] > distances[statetuple] + d*cost:
                        stateToCheck.append(newstate)
                        distances[newstate] = distances[statetuple] + d*cost
                    assert len(newstate) == (height-1)*4
                    count += 1
                    pass
    return distances[goal]

print(f"Part 1: The least energy required to organize the amphipods is {computeMinimumEnergy(puzzles[0])}.")
print(f"Part 2: The least energy required to organize the amphipods is {computeMinimumEnergy(puzzles[1])}.")