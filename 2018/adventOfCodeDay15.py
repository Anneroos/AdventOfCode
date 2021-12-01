import numpy as np
import pandas as pd
from collections import deque
text_file = open("adventOfCodeInput15.txt", "r")
input = text_file.read().split('\n')

input = input[0:7]

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
# print(matrix)
size = len(matrix)
# print(size, "size")



unitslist = []
nrOfUnits = 0

for i in range(size):
    for j in range(size):
        symbol = matrix[i][j]
        if symbol == 'G' or symbol == 'E':
            unitslist.append({'symbol':symbol,'i':i,'j': j})
            nrOfUnits += 1

units = pd.DataFrame(unitslist)
units = units.sort_values(['i', 'j'])
units['health'] = 200

# print(units)

def neighbors(point):
    x, y = point
    return [(x-1, y), (x, y-1),(x,y+1), (x+1, y)]



def move(startPoint, mazeMatrix, type):
    visited = set([startPoint])
    queue = deque([startPoint])
    if type == 'G':
        enemytype = 'E'
    else:
        enemytype = 'G'
    # enemySpots = findEnemySpots(enemytype, mazeMatrix)
    enemyDist = size*size

    distanceMatrix = np.zeros([size,size]).astype(int)
    distanceMatrix[:,:] = -1
    distanceMatrix[startPoint] = 0
    # print(distanceMatrix)
    foundSpot = False
    while queue and not foundSpot:
        currentpoint = queue.popleft()
        # print("current point is")
        # print(currentpoint)

        currenti = currentpoint[0]
        currentj = currentpoint[1]
        if distanceMatrix[currenti, currentj] > enemyDist:
            break
        for neighbor in neighbors(currentpoint):
            # print('neighbor', neighbor)


            if mazeMatrix[neighbor] == '.':
                newdist = distanceMatrix[currenti,currentj] + 1

                if distanceMatrix[neighbor[0],neighbor[1]] > newdist or distanceMatrix[neighbor[0],neighbor[1]] == -1:
                    distanceMatrix[neighbor[0],neighbor[1]] = newdist
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    # print(queue,'queue')
                # if enemySpots[neighbor] == 1:
            if mazeMatrix[neighbor] == enemytype:
                # print('found enemy neighbor!', neighbor)
                enemyDist = distanceMatrix[neighbor[0],neighbor[1]]
                foundSpot = True
                currentpoint
                break
        # print('distancematrix!')
        # print(distanceMatrix)
    # print('current enemy-near-point, to go to: ', currentpoint)

    while distanceMatrix[currentpoint] > 1 :
        curdist = distanceMatrix[currentpoint]
        for neighbor in neighbors(currentpoint):
            if distanceMatrix[neighbor] == curdist - 1:
                currentpoint = neighbor
                break
    # print('lets move towards', currentpoint)
    # enemyDistances = distanceMatrix*enemySpots
    # print('enemydistances', enemyDistances)


    # print('min enemy dist', enemydistances[(enemydistances > 0)].min())
    # print('argmin', enemydistances[(enemydistances > 0)].argmin())



    return currentpoint


# def findEnemySpots(type,mazeMatrix):
#     enemies = (mazeMatrix == type).astype(int)
#     enemySpots = np.zeros([len(mazeMatrix), len(mazeMatrix)]).astype(int)
#
#     size2 = len(mazeMatrix)*100
#
#     for xi in range(len(mazeMatrix)):
#         for yj in range(len(mazeMatrix)):
#             if enemies[xi,yj] == 1:
#                 for neighbor in neighbors((xi,yj)):
#                     if mazeMatrix[neighbor] == '.':
#                         enemySpots[neighbor] = 1
#
#     return enemySpots


print(units)



somePartyWon = False
count = 0
while not somePartyWon and count < 25:
    count += 1
    unitsToRemove = np.array([])
    print('---', count, '----')

    for index, row in units.iterrows():
        if row['health'] >0 :
            # print(row)
            symbol= row['symbol']
            if symbol == 'G':
                enemysymbol = 'E'
            else:
                enemysymbol = 'G'
            i = row['i']
            j = row['j']

            newcoord = move((i, j), matrix, symbol)
            matrix[i,j] = '.'
            matrix[newcoord] = symbol
            units.loc[index, ['i', 'j']] = [newcoord[0],newcoord[1]]

            maxHealthNeighbors = 201

            # attack weakest neighborrrrrr

            # for neighbor in neighbors((i,j)):
            #     enemy = units[ (units['i'] == neighbor[0]) and (units['j'] == neighbor[1] ) ]
            #     print(enemy)
            #     if len(enemy):
            #         print('an enmey')
            #     # if units[units[['i','j']] == [neighbor[0], neighbor[1]] ] < maxHealthNeighbors:

            maxHealthNeighbors = 201
            indexEnemy = -1
            enemyPoint = (0,0)
            for indexE, rowE in units[units['symbol'] == enemysymbol].iterrows():
                if abs(rowE['i'] - i) + abs(rowE['j'] - j)   == 1:
                    if np.all(units.loc[indexE, ['health']] >0) and np.all(units.loc[indexE, ['health']] < maxHealthNeighbors):
                        maxHealthNeighbors = units.loc[indexE, ['health']]
                        indexEnemy = indexE
                        enemyPoint = (rowE['i'], rowE['j'])

            if indexEnemy != -1:
                units.loc[indexEnemy, ['health']] -= 3
                if np.all(units.loc[indexEnemy, ['health']]) <= 0:
                    print('below 0!')
                    matrix[enemyPoint] = '.'
                    print(matrix)
                    unitsToRemove = np.append(unitsToRemove, indexE)



    if len(unitsToRemove):
        units = units.drop( unitsToRemove, axis = 0)
        print('removed someone!')


    units = units.sort_values(['i', 'j'])

    print("matrix", count, 'count',matrix)
    print(units)


move((5,1), matrix, 'E')



