import numpy as np
import pandas as pd

lines = pd.read_csv("adventOfCodeInput17.txt", sep=',|=', header=None, engine='python')

# TEST CASE


# lines.drop(lines.columns[[0,2,5]], axis=1, inplace=True)
lines.columns = ['axis1','axis1nr','axis2','axis2range']
lines['axis1nr'] = lines['axis1nr'].astype(int)
lines['range1'] = lines['axis2range'].apply(lambda x: x.split('..')[0]).astype(int)
lines['range2'] = lines['axis2range'].apply(lambda x: x.split('..')[1]).astype(int)


# lines = lines.head(8)

xmin = min(lines[lines['axis1'] == 'x']['axis1nr'].min()   ,   lines[lines['axis1'] == 'y']['range1'].min())-1
xmax = max(lines[lines['axis1'] == 'x']['axis1nr'].max() , lines[lines['axis1'] == 'y']['range2'].max())+1
ymin = min(lines[lines['axis1'] == 'y']['axis1nr'].min() ,  lines[lines['axis1'] == 'x']['range1'].min() ) - 1
ymax = max(lines[lines['axis1'] == 'y']['axis1nr'].max(), lines[lines['axis1'] == 'x']['range2'].max())
print('xmin,xmax,ymin,ymax:', xmin,xmax,ymin,ymax)





matrix = np.empty([ymax-ymin+1,1+xmax-xmin]).astype(str)
matrix[:,:] = '.'






for index, row in lines.iterrows():
    axis1 = row['axis1']
    axis1nr = row['axis1nr']
    range1 = row['range1']
    range2 = row['range2']
    if axis1 == 'x':
        newaxis1nr = axis1nr - xmin
        newrange1 = range1 - ymin
        newrange2 = range2 - ymin
        matrix[newrange1:(newrange2 + 1), newaxis1nr] = '#'
    elif axis1 == 'y':
        newaxis1nr = axis1nr - ymin
        newrange1 = range1 - xmin
        newrange2 = range2 -  xmin
        matrix[newaxis1nr, newrange1:(newrange2+1)] = '#'


    lines.loc[index, ['axis1nr', 'range1', 'range2']] = [ newaxis1nr, newrange1, newrange2]


# SPRING OF WATER AT 500,0
matrix[0,500-xmin] = '+'



print(matrix)


def dropADrop(startpoint):
    spring = np.array(startpoint)
    print('spring', spring)
    areWeDoneYet = False
    currentpoint = spring
    count = 0

    while not areWeDoneYet and count < 1500:
        count += 1
        # print(count)
        currentpoint += [1, 0]
        if currentpoint[0] > ymax-ymin:
            return
        # print(currentpoint, "current")
        # print( matrix[currentpoint[0],currentpoint[1] ])
        if matrix[currentpoint[0],currentpoint[1] ] == '.' or matrix[currentpoint[0],currentpoint[1] ] == '|':
            # print('drop')
            matrix[currentpoint[0],currentpoint[1]] = '|'
        else:
            currentpoint -= [1, 0]
            if matrix[currentpoint[0], currentpoint[1]] == '.':

                matrix[currentpoint[0], currentpoint[1]] = '|'
            elif matrix[currentpoint[0], currentpoint[1]] == '#':
                print('bumped into # going upward! ********')
            # compute cloest '#' to left and right of current point
            leftpoint = currentpoint.copy()
            rightpoint = currentpoint.copy()
            while leftpoint[1] >= 0:
                if matrix[leftpoint[0], leftpoint[1]] == '#':
                    break
                leftpoint -= [0, 1]
            while rightpoint[1] <= xmax-xmin:


                if matrix[rightpoint[0],rightpoint[1]] == '#':
                    break
                rightpoint += [0,1]
            # check if we have a bottom below these points


            if leftpoint[1]>0 and rightpoint[1] <= xmax-xmin and np.all( np.bitwise_or((matrix[leftpoint[0]+1,leftpoint[1]+1:rightpoint[1]] == '#' ),(matrix[leftpoint[0]+1,leftpoint[1]+1:rightpoint[1]] == '~'))):
                # print("flood a line!")
                matrix[leftpoint[0] , leftpoint[1] + 1:rightpoint[1]] = '~'
                currentpoint -= [1,0]
            else:
                # flood to left
                # print('spread left and right')
                leftflood = currentpoint.copy() - [0,1]
                rightflood = currentpoint.copy() + [0,1]
                # print(matrix[leftflood[0]+1,leftflood[1]] )
                while (matrix[leftflood[0],leftflood[1]] != '#') and ( matrix[leftflood[0]+1,leftflood[1]] == '#' or matrix[leftflood[0]+1,leftflood[1]] == '~' ):
                    matrix[leftflood[0], leftflood[1]] = '|'
                    leftflood -= [0,1]
                # print(matrix[rightflood[0] + 1, rightflood[1]])
                while (matrix[rightflood[0], rightflood[1]] != '#') and ( matrix[rightflood[0] + 1, rightflood[1]] == '#' or matrix[rightflood[0] + 1, rightflood[1]] == '~'):
                    matrix[rightflood[0], rightflood[1]] = '|'
                    rightflood += [0, 1]
                if matrix[rightflood[0] +1, rightflood[1]] == '.':# or matrix[rightflood[0] +1, rightflood[1]] == '|':
                    matrix[rightflood[0] , rightflood[1]] = '|'
                    dropADrop(rightflood)
                if matrix[leftflood[0] +1, leftflood[1]] == '.':# or matrix[leftflood[0] +1, leftflood[1]] == '|' :
                    matrix[leftflood[0] , leftflood[1]] = '|'
                    dropADrop(leftflood)

                return
        # print(matrix)

# matrix = matrix[:10,0:500-xmin+3]
dropADrop([0,500-xmin])
print(matrix)



result = np.bitwise_or(matrix == '|', matrix == '~').sum()
print("Answer to puzzle 1 of day 17:",result)


result = ( matrix == '~').sum()
print("Answer to puzzle 2 of day 17:",result)

matrix[matrix == '.'] = 0
matrix[matrix == '#'] = 1
matrix[matrix == '|'] = 0.45
matrix[matrix == '~'] = 0.55
matrix[matrix == '+'] = 0.65
matrix = matrix.astype(type(0.3))


import matplotlib.pyplot as plt

from matplotlib.colors import LogNorm
Z = np.random.rand(6, 10)

fig, ax = plt.subplots(1, 1)
c = ax.pcolor(matrix)
# c = ax.pcolor(matrix[200:350,0:250])
ax.set_title('kleurtjes')



fig.tight_layout()
plt.show()


# 33245     too high
# 28245     too low