with open("input10.txt") as f:
    lines = [[int(j) if j!= "." else -1 for j in k] for k in f.read().split("\n")]
h = len(lines)
w = len(lines[0])

def findAdjacent(p):
    l,c = p
    adjacents = [(l-1,c),(l+1,c),(l,c-1),(l,c+1)]
    return [p for p in adjacents if 0 <= p[0] < h and 0 <= p[1] < w]

# First we find for each position which positions around it are exactly +1 more
goodNeighbors = {}
for lineIdx in range(len(lines)):
    line = lines[lineIdx]
    for colIdx in range(len(line)):
        number = line[colIdx]
        neighbors = findAdjacent((lineIdx,colIdx))
        for n in neighbors:
            if lines[n[0]][n[1]] == number + 1:
                goodNeighbors[(lineIdx, colIdx)] = goodNeighbors.get((lineIdx, colIdx),[]) + [n]

# Now let's find the solutions for both questions
totalScore = 0
totalRating = 0
for lineIdx in range(len(lines)):
    line = lines[lineIdx]
    for colIdx in range(len(line)):
        number = line[colIdx]
        if number == 0:
            # Store both the neighbors and the number of ways to get there
            n = {k:1 for k in goodNeighbors.get((lineIdx, colIdx),[])}
            if len(n) > 0:
                for _ in range(8):
                    newn = {}
                    for t in n:
                        for k in goodNeighbors.get(t,[]):
                            newn[k] = newn.get(k,0) + n[t]
                    n = newn
            # For questions 1 we only need to count the number of 9s we can reach from this 0
            totalScore += len(n)
            # For question 2 we need to count the number of routes from this 0 to any 9
            totalRating += sum(n.values())

print(f"Day 10:\n  1) The sum of the scores of all trailheads on the topographic map is {totalScore}.")
print(f"  2) The sum of the ratings of all trailheads is {totalRating}.")
