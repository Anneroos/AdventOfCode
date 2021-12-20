with open("input4.txt", "r") as f:
    input = f.read().split("\n\n")
numbers = [int(i) for i in input[0].split(",")]
cards = [[[int(j) for j in line.split()] for line in card.split("\n")] for card in input[1:]] # Hoera voor compacte for loop statements

def crossOffNumber(card, number):
    # I replace the called number with an -1
    for i in range(5):
        for j in range(5):
            if card[i][j] == number:
                card[i][j] = -1
    return card

def checkBingo(card):
    bingo = False
    #check rows
    for line in card:
        if line.count(-1) == 5:
            bingo = True
    # check columns
    for i in range(5):
        if [line[i] for line in card].count(-1) == 5:
            bingo = True
    return bingo

def computeScore(card, number):
    score = 0
    for line in card:
        for i in line:
            if i != -1:
                score += i
    return score*number

# initialize some stuff
ranking =[0]*len(cards) # To see which card wins when
nrOfWinners = 0 # How many cards have won so far

# Let's play bingo!
for i in numbers: # Call numbers one by one
    for j in range(len(cards)): # Loop through cards
        if ranking[j] == 0: # if the card won already, let's not bother any more
            cards[j] = crossOffNumber(cards[j], i)
            isBingo = checkBingo(cards[j])
            if isBingo:
                nrOfWinners += 1
                ranking[j] = nrOfWinners
                if nrOfWinners == 1: # we have a winner!
                    winner = j
                    winningScore = computeScore(cards[j],i)
                if nrOfWinners == len(ranking): # we have a loser!
                    loser = j
                    losingScore = computeScore(cards[j], i)
    if ranking.count(0) == 0: # All cards had bingo already, let's stop
        break

print(f"Part 1: Score of the winning card: {winningScore}.")
print(f"Part 2: Score of the losing card: {losingScore}.")