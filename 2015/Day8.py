# 16-12-2020
with open("input8.txt") as f:
    lines = f.read().split("\n")
diff = 0
for line in lines:
    characters = 0
    i = 1
    # print(line)
    while i < len(line)-1:
        char = line[i]
        # print(i,char)
        characters += 1
        if char == "\\":
            if line[i+1] == "x":
                i += 4
            else:
                i += 2
        else:
            i += 1
    diff += len(line)-characters
    # print(line, len(line),characters)

print(f"Day8 part 1: {diff}.")


# part 2
diff = 0
for line in lines:
    characters = 6 # "" becomes "\"\"", now let's look at the part in the middel
    i = 1
    while i < len(line)-1:
        char = line[i]
        characters += 1
        if char == "\\" or char == "\"": # then we need to escape it. No special characters in input ;)
            characters += 1
        i += 1
    diff += characters - len(line)

print(f"Day8 part 2: {diff}.")
