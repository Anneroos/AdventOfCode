from collections import defaultdict
import math

with open("input20.txt") as f:
    lines = f.read().split("\n")

class MyModule(object):
    def __init__(self):
        self.type = 'output'
        self.inputs = {}
        self.outputs = []
        self.state = 0
        self.name = ''

modules = defaultdict(MyModule)

for line in lines:
    left, right = line.split(" -> ")
    outputs = right.split(", ")
    if left == "broadcaster":
        name = "broadcaster"
        type = "broadcaster"
    else:
        name = left[1:]
        type = left[0]
    modules[name].name = name
    modules[name].type = type
    modules[name].outputs = outputs
    for o in outputs:
        modules[o].inputs[name] = 0
        modules[o].name = o

def pushButton():
    lows = 0
    highs = 0
    pulses = [['broadcaster', 0, 'button',0]]

    kjReceived1 = False # For part 2
    kjReceived1By = '' # For part 2
    while pulses:
        pulse = pulses.pop(0)
        currentModuleName = pulse[0]
        currentModule = modules[currentModuleName]
        receivedPulse = pulse[1]
        if receivedPulse == 1:
            highs += 1
        else:
            lows += 1
        if currentModuleName == "rx" and receivedPulse == 0:
            return True
        receivedFrom = pulse[2]
        timeSincePush = pulse[3]
        if currentModule.type == 'broadcaster':
            for receivingModule in currentModule.outputs:
                pulses.append([receivingModule, receivedPulse, currentModuleName, timeSincePush + 1])
        elif currentModule.type == '%': # flip-flop
            if receivedPulse == 0:
                currentModule.state = 1 - currentModule.state
                for receivingModule in currentModule.outputs:
                    pulses.append([receivingModule, currentModule.state, currentModuleName, timeSincePush + 1])
            # else: # ignore as flip-flopper

        elif currentModule.type == "&":
            # update memory
            currentModule.inputs[receivedFrom] = receivedPulse
            allHigh = min(currentModule.inputs.values())
            # Then, if it remembers high pulses for all inputs, it sends a low pulse; otherwise, it sends a high pulse.
            if currentModuleName == 'kj' and receivedPulse == 1: # For part 2
                kjReceived1 = True
                kjReceived1By = receivedFrom
            if allHigh == 1:  # send low to all outputs
                for receivingModule in currentModule.outputs:
                    pulses.append([receivingModule, 0, currentModuleName, timeSincePush + 1])
            else:  # send high to all outputs
                for receivingModule in currentModule.outputs:
                    pulses.append([receivingModule, 1, currentModuleName, timeSincePush + 1])
    return highs, lows, kjReceived1, kjReceived1By

totalHighs = 0
totalLows = 0
nrOfPushes = 0

# rx only depends on kj, and that is an '&' with inputs 'ln', 'dr', 'zx', 'vn'
stepsToReachModule = {'ln':-1, 'dr':-1, 'zx':-1, 'vn': -1}
found = False
while not found and nrOfPushes < 1000:
    nrOfPushes += 1
    returned = pushButton()
    totalHighs += returned[0]
    totalLows += returned[1]
    if nrOfPushes == 1000:
        print( f"Day 20:\n1) If we multiply the total number of low pulses sent by the total number of high pulses sent we get {totalLows*totalHighs}.")
    if returned[2] == True:
        stepsToReachModule[returned[3]] = nrOfPushes
        if len([i for i in stepsToReachModule.values() if i == -1]) == 0:
            found = True

print(f"2) The fewest number of button presses required to deliver a single low pulse to the module named rx is {math.lcm(*stepsToReachModule.values())}.")