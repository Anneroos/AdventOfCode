# depth: 9465
# target: 13,704

depth = 9465
targetx = 13
targety = 704


# depth = 510
# targetx = 10
# targety = 10

import numpy as np
import pandas as pd
from collections import deque
import time
t0 = time.time()

geoMatrix = np.zeros([targety+1,targetx+1]).astype(int)
erosionMatrix = np.zeros([targety+1,targetx+1]).astype(int)


for i in range(targety+1):
    for j in range(targetx+1):
        if (i == 0 and j == 0) or (i == targety and j == targetx):
            geoMatrix[i,j] = 0
            erosionMatrix[i, j] = (geoMatrix[i, j] + depth )% 20183
        else:
            if i == 0:
                geoMatrix[i, j] = (j * 16807 )% 20183
                erosionMatrix[i, j] = (geoMatrix[i, j] + depth) % 20183
            elif j == 0:
                geoMatrix[i, j] = (i * 48271) % 20183
                erosionMatrix[i, j] = (geoMatrix[i, j] + depth) % 20183
            else:
                geoMatrix[i, j] = (erosionMatrix[i-1, j] * erosionMatrix[i, j-1]) % 20183
                erosionMatrix[i, j] = (geoMatrix[i, j] + depth) % 20183



# print(geoMatrix)
# matrix = matrix + depth % 20183
# print(erosionMatrix)
matrix = erosionMatrix % 3
# print(matrix)
sommetje = matrix.sum()
print("The answer to puzzle 1 of day 22 is:", sommetje)
# matrix = matrix.astype(str)
# matrix[matrix == '0'] = '.'
# matrix[matrix == '1'] = '='
# matrix[matrix == '2'] = '|'

# for i in range(targety + 1):
#     print(''.join(matrix[i, :]))

def neighbors(point):
    x, y = point
    return [(x-1, y), (x, y-1),(x,y+1), (x+1, y)]


def computeGeo(i,j):
    nodes[i,j]= {}
    if (i == 0 and j == 0) or (i == targety and j == targetx):
        nodes[i,j]['geo'] = 0
    else:
        if i == 0:
            nodes[i, j]['geo'] = (j * 16807) % 20183
        elif j == 0:
            nodes[i, j]['geo'] = (i * 48271) % 20183
        else:
            if (i-1,j) not in nodes:
                computeGeo(i-1,j)
            if (i,j-1) not in nodes:
                computeGeo(i,j-1)
            nodes[i, j]['geo'] = (nodes[(i-1, j)]['erosion'] * nodes[(i, j-1)]['erosion']) % 20183
    nodes[i, j]['erosion'] = (nodes[i, j]['geo'] + depth) % 20183
    nodes[i, j]['rocktype'] = nodes[i,j]['erosion'] % 3
    nodes[i,j]['distances'] = [-1,-1,-1]


startpoint = (0,0)
nodes = {}


computeGeo(0,0)
nodes[0,0]['distances'] = [0,-1,-1]
visited = set()
visited.add(startpoint)
queue = deque()
queue.append(startpoint)

queue2 = pd.DataFrame(columns = ['x','y','dist'])
startpoint2 = {'x':0,'y':0,'dist': abs(targety-0)+abs(targetx-0)}
queue2 = queue2.append(startpoint2,  ignore_index=True)



count = 0
targetFound = False
targetDist = -1

while len(queue2)>0:
    count += 1

    queue2 = queue2.sort_values(['dist'])
    # print(queue2)
    # print(queue2.min(axis=1))
    [a,b,c] = queue2[['x','y','dist']].iloc[0]

    # print(a,b,c, '---- length queue', len(queue2))
    queue2 = queue2.drop_duplicates(keep='first')
    queue2.drop(queue2.index[0], inplace=True)



    currentpoint = (a,b)
    currentnode = nodes[currentpoint]
    currenttype = currentnode['rocktype']
    currentdistances = currentnode['distances']
    if count %10000 ==0:
        print(count, "--------current point is----------", currentpoint,currentdistances, 'type', currenttype, 'queue length', len(queue))
    if currentpoint == (targetx,targety):

        targetFound = True
        if(currentdistances[0] == -1):
            targetDist = currentdistances[1]+7
        else:
            targetDist = currentdistances[0]

    if targetFound:
        minDist = -1
        for t in range(3):
            if currentdistances[t] != -1:
                if minDist == -1:
                    minDist = currentdistances[t]
                else:
                    minDist = min(minDist,currentdistances[t])
        if minDist + abs(currentpoint[0]-targetx) + abs(currentpoint[1]-targety) >= targetDist:
            continue

    nexttype = (currenttype +1) %3
    nextnexttype = (currenttype + 2) % 3

    if currentdistances[currenttype] >= 0 and (currentdistances[nexttype]    == -1 or  currentdistances[currenttype] + 7 < currentdistances[nexttype]):
        nodes[currentpoint]['distances'][nexttype] = currentdistances[currenttype] + 7
        currentdistances = nodes[currentpoint]['distances']
    elif currentdistances[nexttype]  >= 0 and (currentdistances[currenttype] == -1 or  currentdistances[nexttype]    + 7 < currentdistances[currenttype]):
        nodes[currentpoint]['distances'][currenttype] = currentdistances[nexttype] + 7
        currentdistances = nodes[currentpoint]['distances']

    for neighbor in neighbors(currentpoint):
        if neighbor[0] >= 0 and neighbor[1] >= 0: #and neighbor != (0,0):
            if neighbor not in nodes:
                computeGeo(neighbor[0],neighbor[1])
            neighbornode = nodes[neighbor]
            neighbordistances = neighbornode['distances']
            neighbortype = nodes[neighbor]['rocktype']
            for tooltype in range(3):
                if currentdistances[tooltype] >= 0:
                    if tooltype == neighbortype or tooltype == ((neighbortype + 1)%3):
                        if neighbordistances[tooltype] < 0 or (neighbordistances[tooltype] >= 0 and currentdistances[tooltype] +1 < neighbordistances[tooltype]):
                            neighbordistances[tooltype] = currentdistances[tooltype] + 1
                            # does neighbor not in queue work?

                            # queue.append(neighbor)
                            queue2 = queue2.append({'x':neighbor[0],'y':neighbor[1],'dist':abs(targety-neighbor[1])+abs(targetx-neighbor[0])}, ignore_index=True)

            nodes[neighbor]['distances'] = neighbordistances

    nodes[currentpoint]['distances'] = currentdistances

print("targetDist:", targetDist)
print(nodes[targetx,targety])


t1 = time.time()

print("time: ", t1-t0)