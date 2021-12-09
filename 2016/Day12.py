# 08-12-2021 - Samen met Wouter, omgeschreven naar iets met een Class. Zie onderaan voor het origineel.
with open("input12.txt", "r") as f:
    lines = f.read().splitlines()
lines = [line.split() for line in lines]

class AssemBunny:
    def __init__(self, dict, lines):
        self.registers = dict
        self.lines = lines
        self.run()
    def cpy(self,x,y):
        if x in self.registers.keys():
            self.registers[y] = self.registers[x]
        else:
            self.registers[y] = int(x)
    def inc(self,x):
        self.registers[x] += 1
    def dec(self,x):
        self.registers[x] -= 1
    def jnz(self,x,y):
        if x in self.registers.keys():
            t = self.registers[x]
        else:
            t=int(x)
        if t != 0:
            self.pointer += self.registers[y] if y in self.registers.keys() else int(y)
        else:
            self.pointer += 1
    def run(self):
        self.pointer = 0
        while self.pointer < len(self.lines):
            functionname = self.lines[self.pointer][0]
            if functionname == "cpy":
                self.cpy(self.lines[self.pointer][1], self.lines[self.pointer][2])
            elif functionname == "inc":
                self.inc(self.lines[self.pointer][1])
            elif functionname == "dec":
                self.dec(self.lines[self.pointer][1])
            elif functionname == "jnz":
                self.jnz(self.lines[self.pointer][1], self.lines[self.pointer][2])
            if functionname != "jnz":
                self.pointer += 1
    def returnRegisters(self, key):
        return self.registers[key]

answer1 = AssemBunny({"a": 0, "b": 0, "c": 0, "d": 0 },lines).returnRegisters("a")
print(f"Part 1: The value in register a is {answer1}.")
answer2 = AssemBunny({"a": 0, "b": 0, "c": 1, "d": 0 },lines).returnRegisters("a")
print(f"Part 2: The value in register a is {answer2}.")

# 318117, 9227771

# # Origineel
# print("Hallo Liefie")
#
# with open("input12.txt", "r") as f:
#     lines = f.read().splitlines()
#     lines = [line.split() for line in lines]
#
# pointer = 0
#
# registers = {
#     "a": 0,
#     "b": 0,
#     "c": 0,
#     "d": 0
# }
#
# def copyfunctie(x,y):
#     if x in "abcd":
#         registers[y] = registers[x]
#     else:
#         registers[y] = int(x)
#
# def inc(x):
#     registers[x]+=1
#
# def dec(x):
#     registers[x]-=1
#
# def jump(x,y):
#     if x in "abcd":
#         t=registers[x]
#     else:
#         t=int(x)
#     if t != 0:
#         amount = registers[y] if y in "abcd" else int(y)
#     else:
#         amount = 1
#     return amount
# count = 0
# while pointer < len(lines):
#     count += 1
#     if count % 100000 == 0:
#         print(count)
#     welkefunctie = lines[pointer][0]
#     if welkefunctie == "cpy":
#         copyfunctie(lines[pointer][1],lines[pointer][2])
#         pointer += 1
#     elif welkefunctie == "inc":
#         inc(lines[pointer][1])
#         pointer += 1
#     elif welkefunctie == "dec":
#         dec(lines[pointer][1])
#         pointer += 1
#     elif welkefunctie == "jnz":
#         pointer += jump(lines[pointer][1],lines[pointer][2])
#
# print(registers["a"])