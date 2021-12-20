with open("input2.txt","r") as f:
    lines = f.read().split("\n")
hor = 0
depth = 0
for line in lines:
    command = line.split(" ")[0]
    amount = int(line.split(" ")[1])
    if command == "down":
        depth += amount
    elif command == "up":
        depth -= amount
    elif command == "forward":
        hor += amount
    else:
        print(f"Unknown command: {command}")
print(f"Part 1. Horizontal position: {hor}. Final depth: {depth}. Answer: {hor*depth}.")

#Part 2
hor = 0
depth = 0
aim = 0
for line in lines:
    command = line.split(" ")[0]
    amount = int(line.split(" ")[1])
    if command == "down":
        aim += amount
    elif command == "up":
        aim -= amount
    elif command == "forward":
        hor += amount
        depth += aim*amount
    else:
        print(f"Unknown command: {command}")
print(f"Part 2. Horizontal position: {hor}. Final depth: {depth}. Answer: {hor*depth}.")