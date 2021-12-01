import numpy as np
import pandas as pd

lines = pd.read_csv("adventOfCodeInput10.txt", sep='<|>|,', header=None, engine='python')
# lines.columns = ['Time', 'Action']
# lines['Time'] = lines['Time'].apply(lambda x : x.split('[')[1])
# lines.set_index(['Day','Time'],inplace = True)

lines.drop(lines.columns[[0,3,6]], axis=1, inplace=True)
lines.columns = ['X','Y','dx','dy']
print(lines.head(10))


# [minx, miny] = lines.min()[['X','Y']]
# [maxx, maxy, maxdx, maxdy] = lines.max()
# lines['X'] += abs(minx)
# lines['Y'] += abs(miny)



# import matplotlib.pyplot as pyplot
# pyplot.scatter(lines['X'].head(30), lines['Y'].head(30))
# pyplot.show()


import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

dx = lines['dx']
dy = lines['dy']
x = lines['X']+10454*dx
y = lines['Y']+10454*dy

for t in range(4):
    if t == 0:
        points, = ax.plot(y, x, marker='o', linestyle='None')
        ax.set_ylim(165, 235)
        ax.set_xlim(100,160)
    else:
        new_y = x + 1*t*dx
        new_x = y + 1*t*dy
        points.set_data(new_x, new_y)
    plt.pause(1)