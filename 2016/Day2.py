#02-12-2021
with open("input2.txt", "r") as f:
    lines = f.read().split("\n")

def findCode(numpad, startPos, instructions):
    x = startPos[0] # which column
    y = startPos[1] # which row
    code = ""
    for line in instructions:
        for i in line:
            newx,newy=x,y
            if i == "U":
                newy = max(0,y-1)
            elif i == "D":
                newy = min(len(numpad)-1, y+1)
            elif i == "L":
                newx = max(0,x-1)
            elif i == "R":
                newx = min(len(numpad[0])-1,x+1)
            if numpad[newy][newx] != "x": #For part 2
                x,y=newx,newy
        code += numpad[y][x]
    return code

#Part 1
numpad = [["1","2","3"],["4","5","6"],["7","8","9"]]
code=findCode(numpad, [1,1], lines)
print(f"Part 1: The code is {code}.")

#Part 2
numpad = [["x","x","1","x","x"], ["x","2","3","4","x"],["5","6","7","8","9"],["x","A","B","C","x"], ["x","x","D","x","x"]]
code=findCode(numpad, [0,2], lines)
print(f"Part 2: The code is {code}.")
