with open("input04.txt", "r") as f:
    scratchcards = [[[int(k) for k in i.split()] for i in card.split(": ")[1].split(" | ")] for card in f.read().split('\n')]
totalScore1 = 0
totalCopies = {i:1 for i in range(1, len(scratchcards)+1) }
for index in range(1, len(scratchcards) + 1):
    nrsCorrect = [nr for nr in scratchcards[index - 1][1] if nr in scratchcards[index - 1][0]]
    totalScore1 += 0 if len(nrsCorrect) == 0 else pow(2, len(nrsCorrect) - 1)
    for copyIndex in range(index + 1, index + len(nrsCorrect) + 1):
        totalCopies[copyIndex] = totalCopies[copyIndex] + totalCopies[index]
print(f"Day 4:\n1) The scratchcard are worth a total of {totalScore1} points.")
print(f"2) We end up with a total of {sum(totalCopies.values())} scratchcards!")