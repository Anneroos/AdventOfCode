import math
text_file = open("input14.txt", "r")
lines = text_file.read().split('\n')
text_file.close()
import time
start_time = time.time()

reactions = {}
for line in lines:
    amount = 0
    output = -1
    element = "TESTYTEST"
    lineList = line.split(' ')
    input = {}
    thingCounter = 0
    outputReady = False
    for word in lineList:

        thingCounter += 1
        if thingCounter == 1:
            if word == "=>":

                outputReady = True
                thingCounter =0
            else:
                amount = int(word)
        elif thingCounter == 2:
            if word[-1] == ',':

                word = word[:-1]

            thingCounter = 0
            element = word
            if outputReady:
                output = amount
                finalelement = element
            else:
                input[element] = amount

    reactions[finalelement] = {"input": input, "output": output}

need = {'FUEL' : 1}
have = {}
oreneeded = 0
# attempts = 0
while len(need.keys()) > 0:
    neededelement = list(need.keys())[0]
    neededoutput = need.get(neededelement)
    input = reactions.get(neededelement)["input"]
    output = reactions.get(neededelement)["output"]
    nrOfReactions = math.ceil(neededoutput/output)
    need.pop(neededelement, None)
    for element in input.keys():
        stillhave = have.get(element,0)
        neededofthiselement = input[element]*nrOfReactions
        if stillhave > neededofthiselement:
            have[element] -= neededofthiselement
        else:
            if stillhave > 0:
                have.pop(element, None)
            if element == "ORE":
                oreneeded += + neededofthiselement - stillhave
            else:
                need[element] = need.get(element, 0) + neededofthiselement - stillhave
    leftover = nrOfReactions*output - neededoutput
    if leftover > 0:
        have[neededelement] = leftover
solutionPuzzle1 = oreneeded
print("Solution of puzzle 1 of day 14: We need", oreneeded, "ORE for 1 FUEL")
print("--- Total time: %s seconds ---" % (time.time() - start_time))
start_time2 = time.time()
oreAvailable = 1000000000000

have = {}

# attempts = 0

fuelToMake = math.floor(oreAvailable/solutionPuzzle1)
need = {'FUEL' : fuelToMake}
fuelMade = 0
rounds = 0
keepTrying = True
while oreAvailable >= 0 and fuelToMake >= 0:
    rounds += 1
    print("Round",rounds,"Fuel to make",fuelToMake)
    oreneeded = 0
    while len(need.keys()) > 0:
        neededelement = list(need.keys())[0]
        neededoutput = need.get(neededelement)
        input = reactions.get(neededelement)["input"]
        output = reactions.get(neededelement)["output"]
        nrOfReactions = math.ceil(neededoutput/output)
        need.pop(neededelement, None)
        for element in input.keys():
            stillhave = have.get(element,0)
            neededofthiselement = input[element]*nrOfReactions
            if stillhave > neededofthiselement:
                have[element] -= neededofthiselement
            else:
                if stillhave > 0:
                    have.pop(element, None)
                if element == "ORE":
                    oreneeded += + neededofthiselement - stillhave
                else:
                    need[element] = need.get(element, 0) + neededofthiselement - stillhave
        leftover = nrOfReactions*output - neededoutput
        if leftover > 0:
            have[neededelement] = leftover
    oreAvailable -= oreneeded
    if oreAvailable >= 0:
        fuelMade += fuelToMake
    fuelToMake = math.floor(oreAvailable/solutionPuzzle1)
    if fuelToMake == 0:
        fuelToMake =1
    need = {'FUEL': fuelToMake}

print("Amount of fuel made",fuelMade)

print("--- Total time: %s seconds ---" % (time.time() - start_time2))
