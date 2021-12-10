with open("input10.txt", "r") as f:
    lines = f.read().splitlines()

def chunkChecker(string):
    pendingBrackets = []
    opens = "([{<"
    closes = ")]}>"
    pointsCor = {")": 3, "]": 57, "}": 1197, ">": 25137}
    pointsIncom = {"(": 1, "[": 2, "{": 3, "<": 4} # Thanks Daniel for the idea to use the opening brackets

    # Check corruptness
    for i in string:
        if i in opens:
            pendingBrackets.append(i)
        elif i in closes:
            # closing bracket, does it match the last pending opening bracket?
            if closes.find(i) == opens.find(pendingBrackets[-1]):
                pendingBrackets.pop()
            else:
                return pointsCor[i], "corrupted"

    # Check incompleteness
    score = 0
    while len(pendingBrackets) > 0:
        score = score*5 + pointsIncom[pendingBrackets.pop()]
    return score, "incomplete"

checkLines = [chunkChecker(line) for line in lines]
answer1 = sum([k[0] for k in checkLines if k[1] == "corrupted"])
print(f"Part 1: The sum of scores for corrupt lines is {answer1}.")

incompleteScores = sorted([k[0] for k in checkLines if k[1] == "incomplete"])
answer2 = incompleteScores[int((len(incompleteScores)-1)/2)]
print(f"Part 2: The middle score for the incomplete lines is {answer2}.")
