with open("input06.txt") as f:
    inp = f.read()
for i in range(len(inp) - 3):
    if len(set(list(inp[i:i+4]))) == 4:
        print(i+4)
        break
for i in range(len(inp) - 13):
    if len(set(list(inp[i:i+14]))) == 14:
        print(i+14)
        break