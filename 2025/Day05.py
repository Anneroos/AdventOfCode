with open("2025/input05.txt") as f:
    ranges, ingredients = f.read().split("\n\n")
    ranges = [[int(t) for t in r.split("-")] for r in ranges.split("\n")]
    ingredients = [int(i) for i in ingredients.split("\n")]
    
freshIngredients = []
for i in ingredients:
    fresh = False
    for r in ranges:
        if i in range(r[0], r[1]+1):
            fresh = True
            freshIngredients.append(i)
            break
print(f"Day 5:\n  1) {len(freshIngredients)}")


ranges.sort(key=lambda x:x[0])
newranges = []
for i in range(len(ranges)):

    if i < len(ranges) - 1:
        if ranges[i][1] >= ranges[i+1][0]:
            ranges[i+1][0] = ranges[i][0]
            if ranges[i][1] > ranges[i + 1][1]:
                ranges[i+1][1] = ranges[i][1]
        else:
            newranges.append(ranges[i])
    else:
        newranges.append(ranges[i])
        
totalFreshIngredients = 0
for r in newranges:
    totalFreshIngredients += r[1] - r[0] + 1
print(f"  2) {totalFreshIngredients}")