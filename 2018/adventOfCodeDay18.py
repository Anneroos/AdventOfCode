import numpy as np
import pandas as pd

text_file = open("adventOfCodeInput18.txt", "r")
input = text_file.read().split('\n')

# input = input[0:10]

text_file.close()
maze = np.array(input)
lastrowlength = len(maze[len(maze)-1])


matrix = np.zeros([len(maze),len(maze[0])]).astype(str)
for i in  range(len(maze)):
    if i == len(maze)-1:
        matrix[i, 0:lastrowlength] = np.array(list(maze[i]))
        matrix[i,lastrowlength:] = ' '
    else:
        matrix[i, :] = np.array(list(maze[i]))

# print(matrix)
size = len(matrix)
# print(size, "size")



def aMinutePasses(acrematrix):
    tempmatrix = acrematrix.copy()
    for i in range(size):
        for j in range(size):
            current = acrematrix[i,j]

            mini = max((i-1),0)
            maxi = min((i+2),size)
            minj = max((j - 1), 0)
            maxj = min((j + 2), size)
            treesum = (acrematrix[mini:maxi, minj:maxj] == '|').sum()
            lumbersum = (acrematrix[mini:maxi, minj:maxj] == '#').sum()

            if current == '|' and lumbersum >= 3:
                tempmatrix[i,j] = '#'
            if current == '#' and (lumbersum < 2 or treesum < 1):
                tempmatrix[i,j] = '.'
            if current == '.' and treesum >= 3:
                tempmatrix[i,j] = '|'
    differentcount = (acrematrix != tempmatrix).sum()

    return tempmatrix, differentcount

#  FIND RESULT 1

acrematrix = matrix.copy()
for minute in range(10):
    acrematrix, differentcount = aMinutePasses(acrematrix)

result = (acrematrix == '#').sum() * (acrematrix == '|').sum()
for row in range(size):
    print(''.join(acrematrix[row,:]))
print("The answer to puzzle 1 of day 18 is", result)





# # PUZZLE 2
howmuchhistory = 30
history = np.empty([howmuchhistory,size,size]).astype(str)
minute = 0
samecounter = 0
stop = False
while not stop:

    matrix, differentcount = aMinutePasses(matrix)
    stop = False
    for countertje in range(howmuchhistory):
        if np.all(history[countertje,:,:] == matrix):
            print('same!', minute, countertje)
            stop = True
            samecounter = countertje
            break


    history[minute%howmuchhistory,:,:] = matrix#np.append(history,matrix)
    if not stop:
        minute += 1

minutesleft = 1000000000 -1 - minute
period = (minute - samecounter) % howmuchhistory
print('period:', period)
minutesleft = minutesleft % period
print('minutes left', minutesleft)
endmatrix = history[(samecounter + minutesleft) % howmuchhistory,:,:]
print("end matrix")
for row in range(size):
    print(''.join(endmatrix[row,:]))



# result = (matrix == '#').sum() * (matrix == '|').sum()


result2 = (endmatrix == '#').sum() * (endmatrix == '|').sum()

print("The answer to puzzle 2 of day 18 is", result2)


