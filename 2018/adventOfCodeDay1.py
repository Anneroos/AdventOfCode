import numpy as np

text_file = open("adventOfCodeInput1.txt", "r")
input = text_file.read().split('\n')
text_file.close()
lines = np.array(input)
array = np.array([int(s) for s in lines])
print("answer puzzle 1 of day 1: ", array.sum())

testinput = np.array([+7, +7, -2, -7, -4])

sum = 0
history = np.array([])
found = False
while not found:
    for x in array:
        sum += x

        if np.any(history == sum):
            history = np.append(history, sum)
            print("Answer puzzle 2 day 1: ", sum)
            found = True
            break
        history = np.append(history,sum)




