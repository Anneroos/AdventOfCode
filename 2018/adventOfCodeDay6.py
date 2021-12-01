import numpy as np

# numpy.loadtxt(open("test.csv", "rb"), delimiter=",", skiprows=1)

pointsList = np.loadtxt("adventOfCodeInput6.txt",  usecols=range(2),delimiter=",")
# pointsList = np.array([[1, 1],[1, 6],[8, 3],[3, 4],[5, 5],[8, 9]])
# pointsList = np.array([[1, 1],[1, 101],[48, 51],[51, 48],[51, 51],[51, 54],[54, 51],[101, 1],[101, 101]])
print(len(pointsList))
[minx, miny] = np.min(pointsList, axis=0)
[maxx, maxy] = np.max(pointsList, axis=0)
# print(minx, maxx, miny, maxy)
rangex = int(maxx-minx+1)
rangey = int(maxy-miny+1)
matrix = np.zeros([rangex, rangey])
matrix2 = np.zeros([rangex, rangey])






def closestPoint(x,y):
    minDist = rangey+rangex
    result = -1
    total = 0
    for i in range(len(pointsList)):
        point = pointsList[i][:]

        dist = abs(point[0]-x)+abs(point[1]-y)
        total += dist
        if(dist < minDist):
            minDist = dist
            result = i
        elif dist == minDist:
            result = -1
    return result, total


# fill matrix with closest nieghbours
for i in range(rangex):
    for j in range(rangey):
        [result, total] = closestPoint(i + minx, j + miny)
        matrix[i][j] = result
        matrix2[i][j] = total

# print(matrix)

row1 = matrix[:,0].tolist()
row2 = matrix[:,rangey-1].tolist()
column1 = matrix[0,:].tolist()
column2 = matrix[(rangex-1),:].tolist()
# print("row1", row1)
# print("row2", row2)
# print("column1", column1)
# print("column2", column2)
boundary = np.unique(np.concatenate((row1,column1,row2,column2)))
# print(boundary)

# now let's find the winner for puzzle 1
maxSize = 0
totalSize = 0
winner = -1
for i in range(len(pointsList)):
    boolmatrix = (matrix == i)
    size = boolmatrix.astype(int).sum()
    totalSize += size
    if i not in boundary:
        # print(boolmatrix)
        # print("point ",i,"has size",size)
        if size > maxSize:
            winner = i
            maxSize = size

# print(totalSize, "total size", (matrix == i).astype(int).sum() , "rest ", rangex, rangey)

print("The answer to puzzle 1 of day 6: Point nr",winner+1,"has the biggest (finite) size of ", maxSize )



print("The answer to puzzle 2 of day 6 is", (matrix2 < 10000).astype(int).sum() )