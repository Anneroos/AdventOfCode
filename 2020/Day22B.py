import time
t0 = time.time()
with open("input22.txt") as f:
    player1, player2 = f.read().split("\n\n")

player1 = [int(i) for i in player1.split("\n")[1:]]
player2 = [int(i) for i in player2.split("\n")[1:]]

states = {}
def playGame(array1,array2, gameIndex):
    # print(f"-----------####### NEW GAME! {gameIndex} ######## -------------")
    states[gameIndex] = {}
    round = 0

    while len(array1) >0 and len(array2) >0 :
        # print("length of states", len(states))

        # stateHash = hash(tuple(array1+[-1]+array2))
        stateHash = tuple(array1 + [-1] + array2)
        # stateHash = str(array1 + [-1] + array2)


        if stateHash in states[gameIndex]:
            # print("WIN BY INFINITE LOOP")
            winnerIdx = 0
            winner = array1
            # print(array1)
            # print( array2)
            score = 0
            for i in range(1, len(array1) + 1):
                score += array1[len(array1) - i] * i
            break
        else:
            states[gameIndex][stateHash] = round
            crabcard = array1.pop(0)
            playercard = array2.pop(0)
            # print(f"Player 1 plays: {crabcard}, player2 plays {playercard}")
            # print("player1", array1)
            # print("player2", array2)

            if playercard <= len(array2) and crabcard <= len(array1):
                # print("recursion")
                winnerIdx, score = playGame(array1[0:crabcard],array2[0:playercard],gameIndex+1)
                if winnerIdx == 0:
                    array1.append(crabcard)
                    array1.append(playercard)
                else:
                    array2.append(playercard)
                    array2.append(crabcard)

            else:
                # print("normal")
                if crabcard > playercard:
                    array1.append(crabcard)
                    array1.append(playercard)
                if playercard > crabcard:
                    array2.append(playercard)
                    array2.append(crabcard)
            round += 1

        if len(array1)>0:
            winner = array1
            winnerIdx = 0
        else:
            winner = array2
            winnerIdx = 1


    score = 0
    for i in range(1,len(winner)+1):

        score+=winner[len(winner)-i]*i
    # print(f"Player {winnerIdx+1} won game {gameIndex} with a score of {score}.")

    return winnerIdx, score

winnerIdx, score = playGame(player1, player2,1)
print(f"Day 22 part B: Player {winnerIdx+1} won the game of Recursive Combat with a score of {score}.")
t1 = time.time()
print(f"This calculation took {t1 - t0} seconds.")