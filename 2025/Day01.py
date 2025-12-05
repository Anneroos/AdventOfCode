with open("2025/input01.txt") as f:
    lines = f.read().split("\n")

value = 50
timesZero = 0
timesZero2 = 0
for line in lines:
    if line[0] == "L":
        dir = -1
    else:
        dir = 1
    for i in range(int(line[1:])):
        value += dir
        if value % 100 == 0:
            value = 0
            timesZero2 += 1
    if value % 100 == 0:
        timesZero += 1

print(f"Day 1:\n  1) {timesZero}")
print(f"  2){timesZero2}")