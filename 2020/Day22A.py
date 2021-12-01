with open("input22.txt") as f:
    player1, player2 = f.read().split("\n\n")

player1 = [int(i) for i in player1.split("\n")[1:]]
player2 = [int(i) for i in player2.split("\n")[1:]]

round = 0
while len(player1) >0 and len(player2) >0 :
    playercard = player1.pop(0)

    crabcard = player2.pop(0)

    if playercard > crabcard:
        player1.append(playercard)
        player1.append(crabcard)
    if crabcard > playercard:
        player2.append(crabcard)
        player2.append(playercard)

if len(player1)>0:
    winner = player1
    print("Player 1 won!")
else:
    winner = player2
    print("Player 2 won!")

score = 0
for i in range(1,len(winner)+1):

    score+=winner[50-i]*i
print(f"With a score of {score}.")