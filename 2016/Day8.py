with open("input8.txt", "r") as f:
    input = f.read().splitlines()
import numpy as np
myscreen = np.array([[0]*50]*6)

def printScreen(screen):
    for i in range(6):
        print("".join(["." if pixel==0 else "#" for pixel in screen[i]]))

def rect(screen,wide,tall):
    screen[:tall,:wide] = 1
    return screen

def rotateColumn(screen, column, amount):
    screen[:,column] = list(screen[6-amount:, column]) + list(screen[:6-amount, column])
    return screen

def rotateRow(screen, row, amount):
    screen[row,:] = list(screen[row, 50-amount:]) + list(screen[row, :50-amount])
    return screen

for i in input:
    splitted = i.split(" ")
    if splitted[0] == 'rect':
        A,B = [int(j) for j in splitted[1].split("x")]
        myscreen = rect(myscreen, A, B)
    elif splitted[0] == "rotate":
        if splitted[1] == "row":
            myscreen = rotateRow(myscreen, int(splitted[2][2:]),int(splitted[4]))
        elif splitted[1] == "column":
            myscreen = rotateColumn(myscreen, int(splitted[2][2:]), int(splitted[4]))
print(f"There should be {sum(sum(myscreen))}  pixels lit.")
print(f"The screen would show:")
printScreen(myscreen) # UPOJFLBCEZ