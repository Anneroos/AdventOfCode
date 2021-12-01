import numpy as np
import pandas as pd

lines = pd.read_csv("adventOfCodeInput23.txt", sep=',|<|>|=', header=None, engine='python')


lines.drop(columns=[0,1,5,6]    ,inplace=True, axis=1)
lines.columns = ['x','y', 'z','r']
# print(lines.columns)
# print(lines)


bossindex = lines['r'].idxmax()

size = len(lines)

adjacency = np.zeros([size,size])

for i in range(bossindex,bossindex+1):
    for j in range(size):
        if(i+j %100):
            print(i,j)
        nanobot1 = lines.loc[i]
        nanobot2 = lines.loc[j]
        if abs(nanobot1['x']-nanobot2['x'])+ abs(nanobot1['y']-nanobot2['y'])+ abs(nanobot1['z']-nanobot2['z']) <= nanobot1['r']:
            adjacency[i,j] = 1

bossSum = adjacency[bossindex,:].sum()
print(bossSum)

class nanobot:

    def __init__(self, x,y,z,r):
        self.x= x
        self.y = x
        self.z = x
        self.r = x

