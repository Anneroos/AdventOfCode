import numpy as np
np.set_printoptions(threshold=np.inf)

text_file = open("input11.txt", "r")
lines = text_file.read().split('\n')
text_file.close()
dict = {'.':-1, 'L':0, '#':1}
seats = [[dict[i] for i in list(line)] for line in lines]

print(seats)

# seatsCopy = seats.copy()
# print(seatsCopy)
m = len(seats)
n = len(seats[0])
print(m,n)
seats = np.array(seats)
print(seats)

tries = 0
while tries < 1000:
    seatsNext = np.zeros([m, n])
    tries += 1
    print(tries)
    for i in range(m):
        for j in range(n):
            currentSeat = seats[i][j]
            # print(currentSeat)
            # seats[]
            # print(i,m, " --- ",j,n)
            minRow = max(0,i-1)
            maxRow = min(m,i+2)
            minCol = max(0,j-1)
            maxCol = min(n,j+2)
            # print(minRow,maxRow,minCol,maxCol)
            rowsAround = seats[minRow:maxRow]
            # print(rowsAround)
            if currentSeat == 1:
                nrOfSeatsTakenAround = -1
            else:
                nrOfSeatsTakenAround = 0
            seatsAround = seats[minRow:maxRow,minCol:maxCol]
            nrOfSeatsTakenAround += seatsAround[seatsAround==1].sum()

            # print(f"currentSEat {currentSeat} with seats around {seatsAround}")
            currentSeatNext = currentSeat
            if currentSeat == 1:
                if nrOfSeatsTakenAround  >= 4:
                    currentSeatNext = 0
            if currentSeat == 0:
                if nrOfSeatsTakenAround == 0:
                    currentSeatNext = 1
            # print(currentSeatNext, "next seats")
            seatsNext[i,j] = currentSeatNext
    print(seatsNext)
    test = seatsNext[seatsNext == 1].sum()
    print("Aantal bezette stoelen", test)
    if (seats == seatsNext).all():

        break
    seats = seatsNext

