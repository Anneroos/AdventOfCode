with open("input02.txt","r") as f:
    strategyGuide = [i.split(" ") for i in f.read().split('\n')]

shapes = ["Rock", "Paper", "Scissors"]
scores = {"Win": 6, "Loss": 0, "Draw": 3}
shapeScores = {"Rock": 1, "Paper": 2, "Scissors": 3}
symbolToShape = {"A": "Rock", "B": "Paper", "C":"Scissors", "X": "Rock", "Y": "Paper", "Z": "Scissors"}
symbolToOutcome = {"Z": "Win", "X": "Loss", "Y": "Draw"}

def winOrLose(opp,me):
    if (opp=="Rock" and me=="Paper") or (opp=="Paper" and me=="Scissors") or (opp=="Scissors" and me=="Rock"):
        return "Win" # for p2
    elif (opp=="Rock" and me=="Scissors") or (opp=="Paper" and me=="Rock") or (opp=="Scissors" and me=="Paper"):
        return "Loss"
    else:
        return "Draw"

# Let's play Rock , Paper, Scissors!
totalScore1 = 0
totalScore2 = 0
for row in strategyGuide:
    opp = symbolToShape[row[0]]

    # Part 1 of question
    result1 = winOrLose(opp,symbolToShape[row[1]])
    totalScore1 += scores[result1] + shapeScores[symbolToShape[row[1]]]

    # Part 2 of question
    oppIndex = shapes.index(opp)
    outcome = symbolToOutcome[row[1]]
    myshape = opp # Draw by default, otherwise:
    if outcome == "Loss":
        myshape = shapes[(oppIndex+2) % 3]
    elif outcome == "Win":
        myshape = shapes[(oppIndex+1) % 3]
    totalScore2 += scores[outcome] + shapeScores[myshape]

print(f"Day 2: \n1) My score would be {totalScore1} if everything goes exactly according to my strategy guide.")
print(f"2) Now that I know the correct way to read the strategy guide, I know I would get a total score of {totalScore2}.")
