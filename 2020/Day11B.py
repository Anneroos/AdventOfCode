import numpy as np

np.set_printoptions(threshold=np.inf)

text_file = open("input11.txt", "r")
lines = text_file.read().split('\n')
text_file.close()
dict = {'.': -1, 'L': 0, '#': 1}
seats = [[dict[i] for i in list(line)] for line in lines]

print(seats)

# seatsCopy = seats.copy()
# print(seatsCopy)
m = len(seats)
n = len(seats[0])
print(m, n)
seats = np.array(seats)
print(seats)

directions = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
print(directions)
tries=0
while True:
    seatsNext = np.zeros([m, n])
    tries += 1
    print("Tries",tries)
    for i in range(m):
        for j in range(n):
            # print("i,j: ",i,j)
            currentSeat = seats[i,j]
            nrOfSeatsTakenAround = 0
            for direction in directions:
                step = 1
                seatFound = False
                while not seatFound:
                    x = i+step * direction[0]
                    y = j+step * direction[1]
                    # print(x,y)
                    if x>=0 and x<m and y>=0 and y<n:
                        if seats[x,y] == 0:

                            seatFound = True
                        elif seats[x,y] == 1:

                            seatFound = True
                            nrOfSeatsTakenAround += 1
                    else:
                        seatFound = True
                    step += 1


            currentSeatNext = currentSeat
            if currentSeat == 1:
                if nrOfSeatsTakenAround >= 5:
                    currentSeatNext = 0
            if currentSeat == 0:
                if nrOfSeatsTakenAround == 0:
                    currentSeatNext = 1
            # print(currentSeatNext, "next seats")
            seatsNext[i, j] = currentSeatNext
    print(seatsNext)
    test = seatsNext[seatsNext == 1].sum()
    print("Aantal bezette stoelen", test)
    if (seats == seatsNext).all():
        print("Alles zelfde")
        break
    seats = seatsNext

