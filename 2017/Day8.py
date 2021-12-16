#15-12-2021
with open("input8.txt","r") as f:
    lines = f.read().splitlines()
registers = dict([[line.split(" ")[0],0] for line in lines])
highestValue = 0
for line in lines:
    splitted=line.split(" ")
    register1 = splitted[0]
    instr = -1 if splitted[1] == "dec" else 1
    amount = int(splitted[2])
    register2 = splitted[4]
    compare = splitted[5]
    value = splitted[6]


    if eval(str(registers[register2]) + compare + value):
        registers[register1] += instr*amount
        highestValue = max(registers[register1], highestValue)
print(f"Part 1: The largest value in any register at the end is {max(registers.values())}.")
print(f"Part 2: The highest value during the process was {highestValue}.")