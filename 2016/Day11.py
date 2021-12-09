# 9-12-2021
# I parsed the input with my brain and converted it to these "states"
# in the funny schema: chip, gen, chip, gen, chip, gen, chip, gen, elevator.
# where each pair "chip, gen" belong to each other. :)
startstate = (1,1,1,1,2,2,2,2,3,2,1)
hardstartstate = (1,1,1,1,1,1,1,1,2,2,2,2,3,2,1)

# I found this trick on reddit: (2,2,1,1) and (1,1,2,2) are basically the same state.
# So here is a function that orders the pairs. It does magic!
def orderState(state):
    orderedState = sorted([(state[2*i],state[2*i+1]) for i in range(int(len(state) / 2))])
    return tuple([item for sublist in orderedState for item in sublist] + [state[-1]])

def checkState(state):
    valid = True
    elevator = state[-1]
    nrOfPairs = int(len(state) / 2)
    if elevator not in range(1,5):
        return False
    for k in range(nrOfPairs):
        chip = state[k*2]
        gen = state[k*2 + 1]
        if chip != gen:
            # if chip is not on same floor as its generator, we need to make sure there are no other generators around
            if chip in [state[2*j+1] for j in range(nrOfPairs)]:
                valid = False
                break
    return valid

def findMoves(state):
    elevator = state[-1] # Where is the elevator now? The elevator can go up or down, and can take 1 or 2 elements from that floor
    elementsOnElevatorFloor = [i for i in range(len(state)-1) if state[i] == elevator] # Excluding elevator itself
    # Another hint from Reddit: try moves up with 2 items if possible (else take only 1)
    # or go down with 1 item (or else 2 items)
    movesUp = [tuple([elevator + 1 if k in (i, j, len(state) - 1) else state[k] for k in range(len(state))]) for i in elementsOnElevatorFloor for j in elementsOnElevatorFloor if elevator + 1 in range(1, 5) and i < j]
    movesUp = [s for s in movesUp if checkState(s)]
    if len(movesUp) == 0 :
        movesUp = [tuple([elevator + 1 if k in (i, len(state) - 1) else state[k] for k in range(len(state))]) for i in elementsOnElevatorFloor if elevator + 1 in range(1, 5)]
        movesUp = [s for s in movesUp if checkState(s)]
    movesDown = [tuple([elevator - 1 if k in (i, len(state) - 1) else state[k] for k in range(len(state))]) for i in
                 elementsOnElevatorFloor if elevator - 1 in range(1, 5)]
    movesDown = [s for s in movesDown if checkState(s)]
    if len(movesDown) == 0:
        movesDown = [tuple([elevator - 1 if k in (i, j, len(state) - 1) else state[k] for k in range(len(state))]) for i in
                     elementsOnElevatorFloor for j in elementsOnElevatorFloor if elevator - 1 in range(1, 5) and i < j]
        movesDown = [s for s in movesDown if checkState(s)]
    # Combine moves up and down, AND do the magic ordering trick! Also, don't go down to an empty level.
    moves = list(set([orderState(s) for s in  movesUp + movesDown if min(s) >= min(state) ]))

    ## My old version:
    ## possibleNewStates = [tuple([elevator + move if k in (i,j,len(state)-1) else state[k] for k in range(len(state))]) for i in elementsOnElevatorFloor for j in elementsOnElevatorFloor for move in [-1,1] if elevator + move in range(min(state),5) and i<=j]
    ## newstates = [s for s in possibleNewStates if min(s) >= min(state) ] #  checkState(s)]
    return moves

def findMinNrOfSteps(state):
    state = state
    movesToCheck = [state]
    statesAndSteps = {state: 0}
    goal = tuple([4] * len(state))
    goalFound=False
    while len(movesToCheck) > 0  and not goalFound:
        state = movesToCheck.pop(0)
        newstates = findMoves(state)
        for s in newstates:
            if s == goal:
                goalFound = True
            if s not in statesAndSteps:
                statesAndSteps[s] = statesAndSteps[state] + 1
                movesToCheck.append(s)
    return statesAndSteps[goal]

print(f"Part 1: We need {findMinNrOfSteps(startstate)} elevator moves.")
print(f"Part 2: Now we need {findMinNrOfSteps(hardstartstate)} moves.")

