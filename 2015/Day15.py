import numpy as np
with open("input15.txt") as f:
    lines = f.read().split("\n")

ingredients = []
properties = []
for line in lines:
    ingredient, description = line.split(": ")
    ingredients.append(ingredient)
    myprops = []
    for kv in description.split(", "):
        key, value = kv.split(" ")
        myprops.append(int(value))

    properties.append(myprops)

properties = np.array(properties)

count = 0
maxscore1 = 0
maxscore2 = 0
winning1 = []
winning2 = []
for a in range(101):
    for b in range(101-a):
        for c in range(101-a-b):
            d = 100 - a - b - c

            cookieIngredients = np.array([a, b, c, d])
            cookieProperties = np.matmul(cookieIngredients, properties)
            cookieProperties[cookieProperties < 0] = 0
            score = np.prod(cookieProperties[:4])

            # score = max(0,5*a - b -d)*max(0,-a + 3*b -c)*max(0,4*c)*max(0,2*d)


            if score > maxscore1: # for part 1, always update maxscore
                winning1 = [a, b, c, d]
                maxscore1 = score
            # if 5 * a + 1 * b + 6 * c + 8 * d == 500:  # for part 2, only update maxscore if calories = 500cookieProperties
            if cookieProperties[4] == 500: # for part 2, only update maxscore if calories = 500
                if score > maxscore2:
                    maxscore2 = score
                    winning2 = [a,b,c,d]

print(f"Day 15 part 1: The winning cookie has a total score of {maxscore1}. Ingredients: {winning1}.")
print(f"Day 15 part 2: The winning 500-calory-cookie has a total score of {maxscore2}. Ingredients: {winning2}.")

