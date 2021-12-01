card = 15628416
door = 11161639
# card =5764801
# door =17807724

modulo = 20201227
loopDoor =-1
loopCard = -1
foundCard = False
foundDoor = False

loop = 1
number =1
while not foundCard or not foundDoor:
    number = number*7 % modulo
    if number == card:
        foundCard = True
        loopCard = loop
    if number == door:
        foundDoor = True
        loopDoor = loop
    loop+=1
print(loopCard,loopDoor)

t = 1
for i in range(loopDoor):
    t = t * card % modulo
print(t)
