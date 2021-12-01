with open("input21.txt") as f:
    lines = f.read().split("\n")
import re

def union(array1, array2):
    newUnion = []
    for i in array1:
        if i in array2:
            newUnion.append(i)
    return newUnion

# Parse input
ingredientPerLine = []
allergenDict = {}
for line in lines:
    m = re.search("([\w\s]+) \(contains (.*)\)$",line)
    allergens = m.group(2).split(", ")
    ingredients = m.group(1).split(" ")
    ingredientPerLine.append(ingredients)
    for allergen in allergens:
        if allergen in allergenDict.keys():
            allergenDict[allergen] = union(allergenDict[allergen],ingredients)
        else:
            allergenDict[allergen] = ingredients

# Solve
changedSomething = True
allergensChecked = []
while changedSomething:
    changedSomething = False
    for allergen in allergenDict.keys():
        if allergen not in allergensChecked and len(allergenDict[allergen])==1:
            foundIngredient = allergenDict[allergen][0]
            allergensChecked.append(allergen)
            changedSomething = True
            # now remove ingredient from all other lists
            for otherallergen in allergenDict.keys():
                if allergen is not otherallergen and foundIngredient in allergenDict[otherallergen]:
                    allergenDict[otherallergen].remove(foundIngredient)

# print(allergenDict)

suspiciousIngredients = []
for allergen in allergenDict.keys():
    for ingredient in allergenDict[allergen]:
        suspiciousIngredients.append(ingredient)
suspiciousIngredients = list(set(suspiciousIngredients))
suspiciousIngredients = sorted(suspiciousIngredients)

totalNotSuspicious = 0
for line in ingredientPerLine:
    for ingredient in line:
        if ingredient not in suspiciousIngredients:
            totalNotSuspicious += 1
print(f" Day 21 part 1: {totalNotSuspicious}.")

# part 2
allergensChecked = sorted(allergensChecked)
dangerous = []
for allergen in allergensChecked:
    dangerous.append(allergenDict[allergen][0])
print(f" Day 21 part 2: {','.join(dangerous)}.")