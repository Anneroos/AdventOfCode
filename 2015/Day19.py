with open("input19.txt") as f:
    inputs = f.read().split("\n\n")
replacements_list = [x.split(" => ") for x in inputs[0].split("\n")]
replacements = {}
for r in replacements_list:
    x = r[0]
    y = r[1]
    if x not in replacements.keys():
        replacements[x] = [y]
    else:
        replacements[x] = replacements[x] + [y]
print(replacements)
medicine = inputs[1]
molecules = set(replacements.keys())
print("Molecules: ", molecules)
results = []

for x in range(len(medicine)):
    print("x", x)
    a = medicine[x]
    b = medicine[x:x+2]
    target = None
    if a in molecules:
        target = a
    elif b in molecules:
        target = b
    print( "Target: ", target)
    if target is not None:
        print(medicine[:max((x),0)] )
        print([replacements.get(target)] )
        print( medicine[x + len(target):])
        for y in replacements[target]:
            result = medicine[:max((x),0)] + y + medicine[x+len(target):]
            print(result)
            results.append(result)
results = set(results)
print(len(results))
