with open("input10.txt", "r") as f:
    lines = f.read().splitlines()

def chunkChecker(string):
    pendingBrackets = [] # Going to fill this with the opening brackets that are found, but not yet closed
    openingBrackets = "([{<"
    closingBrackets = ")]}>"
    corruptedPoints = {")": 3, "]": 57, "}": 1197, ">": 25137}
    incompletePoints = {")": 1, "]": 2, "}": 3, ">": 4}
    # first check for corruptness
    for i in string:
        if i in openingBrackets: # new opening bracket!
            pendingBrackets.append(i)
        elif i in closingBrackets:  # closing bracket, does it match?
            if closingBrackets.find(i) == openingBrackets.find(pendingBrackets[-1]): # if it matches the last opening bracket
                pendingBrackets.pop()
            else: # it doesn't match the last opening bracket
                return corruptedPoints[i], "corrupted"
        else:
            print("Unexpected character")

    # If we got till this point, then the line is not corrupt, but possibly incomplete.
    score = 0
    for i in range(len(pendingBrackets)):
        # for each pending opening bracket, find corresponding closing bracket and compute the score
        score = score*5 + incompletePoints[closingBrackets[openingBrackets.find( pendingBrackets.pop() )]]
    return score, "incomplete" if score > 0 else "good"

outputs = [chunkChecker(line) for line in lines]
answer1 = sum([k[0] for k in outputs if k[1] == "corrupted"])
print(f"Part 1: The sum of scores for corrupt lines is {answer1}.")
incompleteScores = sorted([k[0] for k in outputs if k[1] == "incomplete"])
answer2 = incompleteScores[int((len(incompleteScores)-1)/2)]
print(f"Part 2: The middle score for the incomplete lines is {answer2}.")
