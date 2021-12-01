text_file = open("input5.txt", "r")
input = text_file.read().split('\n')
text_file.close()
maxseat = 0
seats = []
for i in input:
    i = i.replace('F','0').replace('B','1').replace('L','0').replace('R','1')
    row = int(i[:7],2)
    column = int(i[7:],2)
    seat =  8*row + column
    seats.append(seat)
    maxseat = max(maxseat, seat)
print("The seat with the highest ID is ", maxseat)
seats = sorted(seats)
for i in range(1,len(seats)):
    if seats[i]-seats[i-1] > 1:
        print("Your seat is number", seats[i-1]+1)