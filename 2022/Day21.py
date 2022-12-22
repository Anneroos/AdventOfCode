with open( "input21.txt") as f:
    monkeylines = [x.split(": ") for x in f.read().split("\n")]

# Part 1
class Monkey():
    def __init__(self, monkeyline):
        self.name = monkeyline[0]
        self.task = monkeyline[1].split(" ")

    def yell(self, allm):
        if len(self.task) == 1:
            return int(self.task[0])
        else:
            othermonkey1 = allm[self.task[0]].yell(allm)
            othermonkey2 = allm[self.task[2]].yell(allm)
            asstring = str(othermonkey1) + self.task[1] + str(othermonkey2)
            return int(eval(asstring))

AllMonkeys = {}
for monkey in monkeylines:
    m = Monkey(monkey)
    AllMonkeys[m.name] = m
print(f"Day 21:\n1) The monkey named root will yell: \"{AllMonkeys['root'].yell(AllMonkeys)}\".")

# Part 2
class RealMonkey():
    def __init__(self, monkeyline):
        self.name = monkeyline[0]
        self.task = monkeyline[1].split(" ")
        if self.name == "root":
            self.task[1] = "-"
    def yell(self, allm):
        if self.name == "humn":
            # The imaginary number j can be used as a variable! :) Found this idea on reddit
            return 1j
        elif len(self.task) == 1:
            return int(self.task[0])
        else:
            othermonkey1 = allm[self.task[0]].yell(allm)
            othermonkey2 = allm[self.task[2]].yell(allm)
            asstring =  str(othermonkey1) +  self.task[1] + str(othermonkey2)
            return eval(asstring)

AllMonkeys = {}
for monkey in monkeylines:
    m = RealMonkey(monkey)
    AllMonkeys[m.name] = m

StringToEvaluateToZero = AllMonkeys["root"].yell(AllMonkeys)
real = StringToEvaluateToZero.real
imag = StringToEvaluateToZero.imag
x = int(-real/imag)
print(f"2) I need to yell {x}!")
