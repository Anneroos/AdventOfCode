
input = [1, 2, 3, 4, 8, 7, 5, 9, 6]
# input = [3, 8, 9, 1, 2, 5, 4, 6, 7]
cupList = list(range(1,1000000+1))
cupList[0:len(input)] = input



minIdx = min(cupList)
maxIdx = max(cupList)

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



for i in range(len(cupList)):
    index = cupList[i]
    left = cupList[i-1] if i > 0 else cupList[len(cupList)-1]
    right = cupList[i+1] if i < len(cupList)-1 else cupList[0]
    currentCup = Cup(index).setLeftCup(left).setRightCup(right)
    cups[index] = currentCup


currentCup = cups[cupList[0]]
currentCup.printMe()
round = 0
while round < 10000000:
    if round % 10000 == 0:
        print(f"Round {round}")


    firstcup = cups[currentCup.right]

    secondcup = cups[firstcup.right]

    thirdcup = cups[secondcup.right]
    fourthcup = cups[thirdcup.right]

    pickedup = [firstcup.idx, secondcup.idx, thirdcup.idx]


    destinationCup = cups[currentCup.idx - 1 if currentCup.idx >minIdx else maxIdx]
    while destinationCup.idx in pickedup:
        destinationCup = cups[destinationCup.idx - 1 if destinationCup.idx > minIdx else maxIdx]

    destinationsRightCup = cups[destinationCup.right]

    currentCup.setRightCup(fourthcup.idx)
    fourthcup.setLeftCup(currentCup.idx)

    firstcup.setLeftCup(destinationCup.idx)
    destinationCup.setRightCup(firstcup.idx)

    thirdcup.setRightCup(destinationsRightCup.idx)
    destinationsRightCup.setLeftCup(thirdcup.idx)

    currentCup = cups[currentCup.right]
    round +=1

cupRight = cups[cups[1].right]
cupRightRight = cups[cups[cupRight.idx].right]
print(cupRight.idx,cupRightRight.idx,cupRight.idx*cupRightRight.idx)


# 12889883376 was too low