# import math
with open("input05.txt") as f:
    ranges, ingredients = f.read().split("\n\n")
    ranges = [[int(t) for t in r.split("-")] for r in ranges.split("\n")]
    print(ranges)
    ingredients = [int(i) for i in ingredients.split("\n")]
    print(ingredients)

freshIngredients = []
for i in ingredients:
    fresh = False
    for r in ranges:
        if i in range(r[0], r[1]+1):
            fresh = True
            freshIngredients.append(i)
            break
print(freshIngredients)
print(len(freshIngredients))


ranges.sort(key=lambda x:x[0])
print(ranges)
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
print(newranges)
totalFreshIngredients = 0
for r in newranges:
    totalFreshIngredients += r[1] - r[0] + 1
print(totalFreshIngredients)

# 366181852921043 too high
# 366181852921027