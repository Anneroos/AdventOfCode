
text_file = open("input12.txt", "r")
lines = text_file.read().split('\n')
text_file.close()

rotations = {0: [1,0],90:[0,-1],180:[-1,0],270: [0,1]}
rotation = 0
direction = [1,0] # East
position = [0,0]

for i in lines:
    instruction = i[0]
    number = int(i[1:])
    if instruction == "L":
        rotation -= number + 360
        rotation = rotation % 360
        direction = rotations[rotation]
    elif instruction == "R":
        rotation += number + 360
        rotation = rotation % 360
        direction = rotations[rotation]
    elif instruction =="F":
        position[0] += direction[0]*number
        position[1] += direction[1]*number
    elif instruction == "N":
        position[1] += number
    elif instruction == "E":
        position[0] += number
    elif instruction == "S":
        position[1] -= number
    elif instruction == "W":
        position[0] -= number
print(f"We ended up at {position}, which has a manhattan distance {abs(position[0])+abs(position[1])} from where we started.")