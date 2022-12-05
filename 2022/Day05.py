import math
from copy import deepcopy

# --------------- reading and manipulating input -----------------
with open("input05.txt") as f:
    [stacksText, moves] = f.read().split("\n\n")
stacksText = stacksText.split("\n")
nrOfStacks = math.ceil(len(stacksText[-1])/4)
stacks = []
for stackIdx in range(nrOfStacks):
    stack = []
    for stackRowIdx in range(len(stacksText)-1):
        if 1+4*stackIdx < len(stacksText[stackRowIdx]):
            crate = stacksText[stackRowIdx][1+4*stackIdx]
            if crate is not " ":
                stack.append(crate)
    stacks.append(stack)
moves = [{"amount": int(move.split(" ")[1]), "stackFrom": int(move.split(" ")[3]) - 1, "stackTo" : int(move.split(" ")[5]) - 1} for move in moves.split("\n")]

# --------------- part 1 -----------------
stacks1 = deepcopy(stacks)
for move in moves:
    for i in range(move["amount"]):
        crate = stacks1[move["stackFrom"]].pop(0)
        stacks1[move["stackTo"]].insert(0, crate)
print(f"Day 4:\n1) The top crates are { ''.join([stack[0] for stack in stacks1])}.")

# --------------- part 2 -----------------
stacks2 = deepcopy(stacks)
for move in moves:
    subStack = []
    for i in range(move["amount"]):
        crate = stacks2[move["stackFrom"]].pop(0)
        subStack.append(crate)
    stacks2[move["stackTo"]] = subStack + stacks2[move["stackTo"]]
print(f"2) With the \"CrateMover 9001\" the top crates are { ''.join([stack[0] for stack in stacks2])}.")