input = [1, 2, 3, 4, 8, 7, 5, 9, 6]
# input = [3, 8, 9, 1, 2, 5, 4, 6, 7]
minIdx = min(input)
maxIdx = max(input)

cups = {}

class Cup:
    def __init__(self, idx):
        self.idx = idx
        self.right = None
        self.left = None


    def setRightCup(self,other):
        self.right = other
        return self

    def setLeftCup(self,other):
        self.left = other
        return self

    def unsetRightCup(self):
        self.right = None
        return self

    def unsetLeftCup(self):
        self.left = None
        return self

    def printMe(self):
        print(f"My index is {self.idx}, the cup to the left has index {self.left}, and the cup to the right is cup {self.right}")



for i in range(len(input)):
    index = input[i]
    left = input[i-1] if i > 0 else input[len(input)-1]
    right = input[i+1] if i < len(input)-1 else input[0]
    currentCup = Cup(index).setLeftCup(left).setRightCup(right)
    cups[index] = currentCup


currentCup = cups[input[0]]
currentCup.printMe()
round = 0
while round < 100:
    print(f"Round {round}")
    cup = currentCup
    answer = "(" + str(cup.idx) + ")"
    for i in range(maxIdx - minIdx):
        cup = cups[cup.right]
        answer += " " + str(cup.idx)

    print(answer)

    firstcup = cups[currentCup.right]

    secondcup = cups[firstcup.right]

    thirdcup = cups[secondcup.right]
    fourthcup = cups[thirdcup.right]

    pickedup = [firstcup.idx, secondcup.idx, thirdcup.idx]
    print("Picked up", firstcup.idx, secondcup.idx, thirdcup.idx)

    destinationCup = cups[currentCup.idx - 1 if currentCup.idx >minIdx else maxIdx]
    while destinationCup.idx in pickedup:
        destinationCup = cups[destinationCup.idx - 1 if destinationCup.idx > minIdx else maxIdx]
    print("destination index",destinationCup.idx, "with to its left",destinationCup.left,"and to its right", destinationCup.right)
    destinationsRightCup = cups[destinationCup.right]

    currentCup.setRightCup(fourthcup.idx)
    fourthcup.setLeftCup(currentCup.idx)

    firstcup.setLeftCup(destinationCup.idx)
    destinationCup.setRightCup(firstcup.idx)

    thirdcup.setRightCup(destinationsRightCup.idx)
    destinationsRightCup.setLeftCup(thirdcup.idx)

    cup = currentCup
    answer = "(" + str(cup.idx) + ")"
    for i in range(maxIdx - minIdx):
        cup = cups[cup.right]
        answer += " " + str(cup.idx)

    print(answer)

    currentCup = cups[currentCup.right]
    round +=1

cup = cups[1]
answer = ""
for i in range(maxIdx-minIdx):
    cup.printMe()
    cup = cups[cup.right]
    answer += str(cup.idx)

print(answer)