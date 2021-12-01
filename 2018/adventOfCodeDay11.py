import numpy as np
gridnumber = 568
width = 300

rackID = np.array(range(10+1, 10+ width+1))
# print("rackID, ",rackID)
yvalues = np.array(range(1,width+1))
# print("yvalues", yvalues)

power = np.outer(yvalues,rackID) % 1000
# print("power outer ", power)
power = power + gridnumber % 1000
# print("added gridnumber",power)
test = np.outer(np.ones(width).astype(int),rackID) % 1000
# test = power.dot(rackID)
# print("rackIDs as matrix",test)
power = power*test % 1000
# print(power)

power = (power/100).astype(int)-5
# print(power)


orig = power[0:width - 2, 0:width - 2]
move10 = power[1:width - 1, 0:width - 2]
move20 = power[2:width, 0:width - 2]
move01 = power[0:width - 2, 1:width - 1]
move11 = power[1:width - 1, 1:width - 1]
move21 = power[2:width, 1:width - 1]
move02 = power[0:width - 2, 2:width]
move12 = power[1:width - 1, 2:width]
move22 = power[2:width, 2:width]

squares = orig + move10+move20 + move01+move11+move21+move02+move12+move22

output = np.unravel_index(squares.argmax(),(width-2,width-2))

print("The answer for puzzle 1 of day 11: ", output[1]+1, output[0]+1)

#
# print("power")
# print(power)


squares = power
maxSquare = squares.max()
coords = np.unravel_index(squares.argmax(),(width,width))
forsize = 1
# print("max value for 1x1 square", maxSquare, "at coords", coords)
for size in range(2, width):
    # resize squares one step
    restSize = width-size+1
    # print("restSize", restSize)
    squares = squares[0:restSize,0:restSize]
    # print("squares")
    # print(squares)

    # add lower part
    for k in range(0,size):
        squares = squares + power[k:(restSize+k), (size-1):width]
    for k in range(0,size-1):
        squares = squares +   power[(size-1):width,k:restSize+k]

    tempmax = squares.max()
    # print("Size ", size, " has max", tempmax, "at coords", squares.argmax())
    if tempmax > maxSquare:
        maxSquare = tempmax
        coords = np.unravel_index(squares.argmax(),(width-size+1,width-size+1))
        forsize = size
        # print("new max!")# size ", size, "and max", maxSquare, "at coords", coords)

57289

print("The answer for puzzle 2 of day 11: ", coords[1]+1, coords[0]+1, forsize)
# print(orig)
