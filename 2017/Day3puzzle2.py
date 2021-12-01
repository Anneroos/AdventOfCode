import math
def idx2grid(number):
    #print("Start idx2grid")
    temp = int(math.ceil(math.sqrt(number)))
    if temp %2 ==0:
        temp += 1  # oneven getal boven sqrt
    hoekpunt = temp**2 # bijv 9, 25, 121
    ring = int((temp+1)/2-1) # hoeveelste ring, beginnend bij 0
    #print("ring: ", ring)
    rest = hoekpunt - number
    #print("rest: ",rest)
    xcoord = ring
    ycoord = ring
    if rest <= 2*(ring):
        xcoord -= rest
    elif rest <= 4 * (ring):
        xcoord -= 2*(ring)
        ycoord -= rest - 2*(ring)
    elif rest <= 6 * (ring):
        ycoord -= 2*(ring)
        xcoord -= - rest + 6*(ring)
    else:
        ycoord -= - rest + 8*(ring)
    return [xcoord,ycoord]

def grid2idx(x,y):
    #print("Start Grid2idx")
    ring = max(abs(float(x)),abs(float(y)))
    hoekpunt = (2*ring+1)**2
    if y == ring:
        n = hoekpunt - (ring - x)
    elif -x == ring:
        n = hoekpunt - 2*ring - (ring - y)
    elif -y == ring:
        n = hoekpunt - 4*ring - (ring + x)
    else:
        n = hoekpunt - 6*ring - (ring + y)
    return int(n)


import numpy as np


seq = np.array([0,1])

def countyourneighbours(n):
    sum = 0
    [x, y] = idx2grid(n)
    for i in [x-1,x,x+1]:
        for j in [y-1,y,y+1]:
            getal = int(grid2idx(i,j))

            if getal <  n:

                sum += seq[getal]
    return sum


number = 312051

maxtotnu = 1
while maxtotnu < number:
    new = countyourneighbours(len(seq))
    seq = np.append(seq, new)
    maxtotnu = new


print(seq)