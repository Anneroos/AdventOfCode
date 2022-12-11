import math
with open(         "input11.txt") as f:
    monkeyinputs = [x.split("\n") for x in f.read().split("\n\n")]

class Monkey():
    def __init__(self, idx, initstring, part):
        z = [x.strip() for x in initstring]
        self.name = "Monkey " + str(idx)
        self.part = part
        self.items = [int(x) for x in z[1].split("Starting items: ")[1].split(", ")]
        self.operation = z[2].split("Operation: new = ")[1].split(" ")
        self.test = int(z[3].split(" ")[-1])
        self.iftrue = int(z[4].split(" ")[-1])
        self.iffalse = int(z[5].split(" ")[-1])
        self.otherMonkeys = []
        self.itemsTested = 0
        self.bigTest = 1

    def defineOtherMonkeys(self, monkeys):
        self.otherMonkeys = monkeys

    def operateItem(self, item):
        self.itemsTested += 1
        term1 = self.operation[0]
        if term1 == "old":
            term1 = item
        else:
            term1 = int(term1)
        term2 = self.operation[2]
        if term2 == "old":
            term2 = item
        else:
            term2 = int(term2)
        result = term1 * term2 if self.operation[1] == "*" else term1 + term2
        if self.part == 1:
            result = math.floor(result / 3)
        elif self.part == 2:
            result = result % self.bigTest
        return result

    def testItem(self, item):
        if item % self.test == 0:
            return self.iftrue
        else:
            return self.iffalse

    def catch(self, item):
        self.items.append(item)

    def setBigTest(self, t):
        self.bigTest = t

    def throwItems(self):
        while len(self.items) > 0:
            item = self.items.pop(0)
            item = self.operateItem(item)
            throwTo = self.testItem(item)
            self.otherMonkeys[throwTo].catch(item)

def createMonkeys(part, inputs):
    monkeys = []
    bigTest = 1
    for i in range(len(inputs)):
        monkeyinput = inputs[i]
        m = Monkey(i, monkeyinput, part)
        monkeys.append(m)
        bigTest *= m.test
    for m in monkeys:
        m.defineOtherMonkeys(monkeys)
        m.setBigTest(bigTest)
    return monkeys

def solution(part, rounds, inputs):
    monkeys = createMonkeys(part, inputs)
    for round in range(1, rounds + 1):
        for m in monkeys:
            m.throwItems()
    s = sorted([m.itemsTested for m in monkeys], reverse=True)
    print(
        f"{part}) The level of monkey business after {rounds} rounds of stuff-slinging simian shenanigans is {s[0] * s[1]}.")

print("Day 11:")
solution(1, 20, monkeyinputs)
solution(2, 10000, monkeyinputs)