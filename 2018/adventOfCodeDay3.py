import numpy as np
import pandas as pd

lines = pd.read_csv("adventOfCodeInput3.txt", sep=' |,|x|:|#', header=None, engine='python')

# TEST CASE

# lines = lines.head()
lines.drop(lines.columns[[0,2,5]], axis=1, inplace=True)
lines.columns = ['index','spaceleft','spaceup','width','height']
# print(lines)

n = len(lines)

matrix = np.zeros([n,n])
for i in range(n):
    left = lines['spaceleft'][i]
    up = lines['spaceup'][i]
    width = lines['width'][i]
    height = lines['height'][i]
    # matrix[left:(left+width)][up:(up+height)] += 1
    matrix[up:(up+height), left:(left+width)] += 1

# print(matrix > 0)
ans = (matrix > 1)
ans = ans.sum()

print("The answer to puzzle 1 of day 3 is ", ans)

ans2 = 0
for i in range(n):
    left = lines['spaceleft'][i]
    up = lines['spaceup'][i]
    width = lines['width'][i]
    height = lines['height'][i]
    # matrix[left:(left+width)][up:(up+height)] += 1
    patch = matrix[up:(up+height), left:(left+width)]
    if np.all(patch==1):
        ans2 = i+1 # start counting at 1

print("The answer to puzzle 2 of day 3 is ", ans2)



# adjMatrix = np.zeros([n, n])
#
# for i in range(n):
#     left1 = lines['spaceleft'][i]
#     up1 = lines['spaceup'][i]
#     width1 = lines['width'][i]
#     height1 = lines['height'][i]
#     # print(left1,up1,width1,height1)
#     overlap = False;
#     for j in range(n):
#         left2 = lines['spaceleft'][j]
#         up2 = lines['spaceup'][j]
#         width2 = lines['width'][j]
#         height2 = lines['height'][j]
#         # print(left2, up2, width2, height2)
#         if j != i and ((left1<=left2 and left1+width1 > left2) or (left1 >= left2 and left2 + width2 > left1)) and ((up1 <= up2 and up1+height1> up2) or (up2 >= up1 and up2+height2 > up1)):
#             overlap = True
#             adjMatrix[i][j] = 1
#
#
#
#
#     if (not overlap):
#         print("Answer to puzzle 2 of day 3: ", i)
#
#

