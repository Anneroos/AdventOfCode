
text_file = open("input12.txt", "r")
lines = text_file.read().split('\n')
text_file.close()


waypoint = [10, 1]
# rotations = {0: [1,0],90:[0,-1],180:[-1,0],270: [0,1]}
# rotation = 0
# direction = [1,0] # East
position = [0,0]

def rotateWaypoint(waypoint_input, direction):
    waypoint_output = []
    if direction == "R":
        waypoint_output = [waypoint_input[1],-waypoint_input[0]]
    elif direction == "L":
        waypoint_output = [-waypoint_input[1], waypoint_input[0]]
    else:
        print("ERROR")
    return waypoint_output




for i in lines:
    instruction = i[0]
    number = int(i[1:])
    if instruction == "L" or instruction == "R":
        # print(i)
        timesToRotate = int(number/90)
        for j in range(timesToRotate):
            waypoint = rotateWaypoint(waypoint,instruction)
        # print(waypoint)

    elif instruction =="F":
        position[0] += waypoint[0]*number
        position[1] += waypoint[1]*number
    elif instruction == "N":
        waypoint[1] += number
    elif instruction == "E":
        waypoint[0] += number
    elif instruction == "S":
        waypoint[1] -= number
    elif instruction == "W":
        waypoint[0] -= number

print(f"We ended up at {position}, which has a manhattan distance {abs(position[0])+abs(position[1])} from where we started.")