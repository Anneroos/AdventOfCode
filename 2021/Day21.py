from collections import defaultdict
# Part 1
positions = [5,8]
scores = [0,0]
die = 1 # die starts at 1
turn = 0 # player 0 or player 1
rolled = 0
while scores[0] < 1000 and scores[1] < 1000:
    positions[turn] = ((positions[turn] + 3*die + 2) % 10) + 1
    die = ((die + 3) % 100)
    rolled += 3
    scores[turn] += positions[turn]
    turn = 1 - turn
print(f"Part 1: {scores[turn]*rolled}.")

# Part 2 - start with computing how often each result appears after 3 throws with D3
diceSums=defaultdict(int)
for sum in [i + j + k + 3 for i in range(3) for j in range(3) for k in range(3)]:
    diceSums[sum] += 1

# Let the games begin!
games = defaultdict(int)
games[(5, 8, 0, 0, 0)] = 1  # (pos. player 0, pos. player 1, score player 0, score player 1, who is starting this turn)
wins = [0,0]

while len(games) > 0:  # Inspired by Dijkstra's algorithm :)
    nextgames = defaultdict(int)
    for game in games:
        turn = game[4]
        for i in range(3, 10):
            newgame = list(game)
            newgame[turn] = (newgame[turn] + i - 1) % 10 + 1
            newgame[turn + 2] += newgame[turn]
            newgame[4] = 1 - turn
            newgame = tuple(newgame)
            if newgame[turn + 2] >= 21:
                wins[turn] += games[game] * diceSums[i]
            else:
                nextgames[newgame] += games[game] * diceSums[i]
    games = nextgames
print(f"Part 2: Player {int(wins[1]>wins[0])+1} wins the most: a whopping {max(wins)} times!")