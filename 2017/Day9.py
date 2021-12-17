# 16-12-2021
with open('input9.txt', "r") as f:
    input=f.read()

def computeScore(index, level):
    garbage = 0
    score = level
    i = index
    while i < len(input):
        if input[i] == "{":
            subscore, endindex, subgarbage = computeScore(i + 1, level + 1)
            garbage += subgarbage
            score += subscore
            i = endindex
        elif input[i] == "}":
            i += 1
            return score, i, garbage
        elif input[i] == "<": # The garbage starts! Try to find closing >
            closed = False
            i += 1
            while not closed:
                if input[i] == "!":
                    i += 2
                elif input[i] != ">":
                    i += 1
                    garbage += 1
                elif input[i] == ">":
                    closed = True
                    i += 1
        elif input[i] == ",":
            i += 1
    return score, i, garbage
c=computeScore(0,0)
print(f"Part 1: The total score of all the groups is {c[0]}.")
print(f"Part 2: There are {c[2]} non-canceled characters in the garbage.")