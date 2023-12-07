with open("input07.txt", "r") as f:
    lines = [line.split() for line in f.read().split('\n')]

cardValues1 = {"AKQJT98765432"[i]:(14 - i) for i in range(13)}
cardValues2 = {"AKQT98765432J"[i]:(14 - i) for i in range(13)}

allHands1 = []
allHands2 = []

def scoreHand(handDict):
    if 5 in handDict.values():  # Five of a kind
        score = 7
    elif 4 in handDict.values():  # Four of a kind
        score = 6
    elif 3 in handDict.values():
        if 2 in handDict.values():  # Full house
            score = 5
        else:  # Three of a kind
            score = 4
    elif 2 in handDict.values():
        if len(handDict.keys()) == 3:  # Two pair
            score = 3
        else:  # One pair
            score = 2
    else:  # High card
        score = 1
    return score

for line in lines:
    hand = line[0]
    bid = int(line[1])
    handDict = {i: hand.count(i) for i in set(hand)}  # Q2Q44 -> {'Q':2, '4': 2, '2': 1}
    # part 1
    score1 = scoreHand(handDict)
    scoreArray1 = [score1] + [cardValues1[hand[idx]] for idx in range(5)] + [bid]
    allHands1.append(scoreArray1)
    # part 2
    scoreArray2 = [score1] + [cardValues2[hand[idx]] for idx in range(5)] + [bid]
    if "J" in hand:  # There is a Joker! Only consider changing all Jokers at once to a cardvalue we already have:
        for newvalue in [k for k in handDict.keys() if k != "J"]:
            newHandDict = handDict.copy()
            newHandDict[newvalue] = newHandDict[newvalue] + newHandDict["J"]
            newHandDict["J"] = 0
            newscore = scoreHand(newHandDict)
            if newscore > scoreArray2[0]:  # Better score! So this might be the new value of the hand
                scoreArray2[0] = newscore
    allHands2.append(scoreArray2)

print(f"Day 7:\n1) The total winnings are {sum([hand[6] * (idx + 1) for idx, hand in enumerate(sorted(allHands1,reverse=False))])}.")
print(f"2) With the new joker rule, the new total winnings are {sum([hand[6] * (idx + 1) for idx, hand in enumerate(sorted(allHands2,reverse=False))])}.")