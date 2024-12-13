with open("input13.txt") as f:
    input = f.read().split("\n\n")


def findAandB(slopeA, slopeB, prizePos):
    if slopeA[0] != 0:
        B = round((prizePos[1] - slopeA[1]/slopeA[0] * prizePos[0])/(slopeB[1] - slopeA[1]/slopeA[0] * slopeB[0]))
        A = round((prizePos[0] - slopeB[0]*B)/slopeA[0])
    else:
        B = round(prizePos[0]/slopeB[0])
        A = round((prizePos[1] - slopeB[1] * prizePos[0]/slopeB[0])/slopeA[1])
    if slopeA[0] * A + slopeB[0] * B == prizePos[0] and slopeA[1] * A + slopeB[1] * B == prizePos[1]:
        return True, A, B
    else:
        return False, 0, 0


totalTokens1 = 0
totalTokens2 = 0
for block in input:
    inputA,inputB,inputPrize = block.split("\n")
    slopeA = [int(i.split("+")[1]) for i in inputA.split(": ")[1].split(", ")]
    slopeB = [int(i.split("+")[1]) for i in inputB.split(": ")[1].split(", ")]
    prizePos1 = [int(i.split("=")[1]) for i in inputPrize.split(": ")[1].split(", ")]
    prizePos2 = [prizePos1[0] + 10000000000000, prizePos1[1] + 10000000000000]

    answer1, A1, B1 = findAandB(slopeA, slopeB, prizePos1)
    answer2, A2, B2 = findAandB(slopeA, slopeB, prizePos2)

    totalTokens1 += 3 * A1 + B1
    totalTokens2 += 3 * A2 + B2
print(f"Day 13:\n  1) We need at lest {totalTokens1} tokens to win all possible prizes.")
print(f"  2) Using the corrected prize coordinates, we need at least {totalTokens2} tokens to win all possible prizes.")

# Let's solve these linear equations. Assume slopeA[0] is not null.
# slopeA[0] * A + slopeB[0] * B = prizePos[0]
# slopeA[1] * A + slopeB[1] * B = prizePos[1]
#
# ax + bY = e
# cx + dy = f
#
# ax + bY = e
# cx + dy - c/a * (ax + bY)= f - c/a * e
#
# ax + bY = e
# (d - c/a * b)y = f - c/a * e
# y = (f-c/a * e) / (d-c/a*b)