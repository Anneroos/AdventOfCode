#08-12-2021
with open("input10.txt", "r") as f:
    lines = f.read().splitlines()

class Bot():
    def __init__(self, index):
        self.index = index
        self.values = []
    def talk(self):
        print(f"hoi, ik ben bot {self.index}")
    def add_value(self, inputvalue):
        self.values.append(inputvalue)
    def defineRules(self,lowBuddy, highBuddy):
        self.lowBuddy = lowBuddy
        self.highBuddy = highBuddy
    def passValues(self):
        if min(self.values) == 17 and max(self.values) == 61:
            print(f"Part 1: Bot {self.index} compares 61 and 71.")
        self.lowBuddy.add_value(min(self.values))
        self.highBuddy.add_value(max(self.values))
        self.values = []
t = Bot(5)
bots = {}
outputs = {}
for line in lines:
    splitted = line.split(" ")
    if splitted[0] == "value":
        index = int(splitted[5])
        if index not in bots.keys():
            bots[index] = Bot(index)
        bots[index].add_value(int(splitted[1]))
    else:
        index = int(splitted[1])
        if index not in bots.keys():
            bots[index] = Bot(index)
        lowType = splitted[5]
        lowIndex = int(splitted[6])
        highType = splitted[10]
        highIndex = int(splitted[11])
        if lowType == "bot" and lowIndex not in bots.keys():
            bots[lowIndex] = Bot(lowIndex)
        elif lowType == "output" and lowIndex not in outputs.keys():
            outputs[lowIndex] = Bot(lowIndex)
        if highType == "bot" and highIndex not in bots.keys():
            bots[highIndex] = Bot(highIndex)
        elif highType == "output" and highIndex not in outputs.keys():
            outputs[highIndex] = Bot(highIndex)

        lowBuddy = bots[lowIndex] if lowType == "bot" else outputs[lowIndex]
        highBuddy = bots[highIndex] if highType == "bot" else outputs[highIndex]
        bots[index].defineRules(lowBuddy, highBuddy)

n = 1
while n>0:
    n = 0
    for botIndex in bots.keys():
        bot = bots[botIndex]
        if len(bot.values) > 1:
            n += 1
            bot.passValues()

print(f"Part 2: Multiplying the values of outputs 0, 1 and 2 gives {outputs[0].values[0] * outputs[1].values[0]* outputs[2].values[0]}.")