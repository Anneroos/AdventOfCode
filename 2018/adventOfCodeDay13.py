import numpy as np
import pandas as pd
text_file = open("adventOfCodeInput13.txt", "r")
input = text_file.read().split('\n')
text_file.close()
tracks = np.array(input)
lastrowlength = len(tracks[len(tracks)-1])

matrix = np.zeros([len(tracks),len(tracks[0])]).astype(str)
for i in  range(len(tracks)):
    if i == len(tracks)-1:
        matrix[i, 0:lastrowlength] = np.array(list(tracks[i]))
        matrix[i,lastrowlength:] = ' '
    else:
        matrix[i, :] = np.array(list(tracks[i]))
# print(matrix)

size = len(matrix)




cartslist = []
nrOfCarts = 0

for i in range(size):
    for j in range(size):
        symbol = matrix[i][j]
        if symbol == '^' or symbol == 'v' :
            cartslist.append({'i':i ,'j': j,'dir': symbol})
            matrix[i][j] = '|'
            nrOfCarts += 1
        if symbol == '<' or symbol == '>':
            cartslist.append({'i': i, 'j': j, 'dir': symbol})
            nrOfCarts += 1
            matrix[i][j] = '-'


carts = pd.DataFrame(cartslist)
carts = carts.sort_values(['i', 'j'])
carts['count'] = 0


tics = 0

directions = ['<', '^', '>', 'v']
while len(carts) > 1 :
    tics += 1
    # print('tic nr ', tics)
    cartstoremove = np.array([])
    for index, row in carts.iterrows():

        # print('----------', index,'-----------')
        # print(index, row)
        dir = row['dir']
        newi, newj = row[['i','j']]
        count = row['count']
        # print(dir, newi, newj, count)
        if dir == '>':
            newj += 1
        elif dir == '<':
            newj -= 1
        elif dir == 'v':
            newi += 1
        elif dir == '^':
            newi -= 1


        newspot = matrix[newi,newj]

        # print('new spot: ', newspot, 'dir now:', dir)
        if newspot == '+':
            # print("intersection! count", count)
            currentdirindex = directions.index(dir)
            # print(currentdirindex)
            newdirindex = (currentdirindex - 1 + count  )% 4
            # print(newdirindex)
            dir = directions[newdirindex]
            count = (count + 1) % 3
        elif newspot == "/":

            if dir == '>':
                dir = '^'
            elif dir == '^':
                dir = '>'
            elif dir == '<':
                dir = 'v'
            elif dir == 'v':
                dir = '<'
        elif newspot == '\\':
            # print('corner \\')
            if dir == '>':
                dir = 'v'
            elif dir == '^':
                dir = '<'
            elif dir == '<':
                dir = '^'
            elif dir == 'v':
                dir = '>'
        elif newspot == ' ':
            print('***********SHITTTT ******************')
        elif newspot == '-' or newspot == '|':
            # no direction change needed!
            pass
        else:
            print('huh, else ************************************************')
        # print('dir updated', dir, "count", count)
        carts.loc[index, ['i', 'j','dir','count']] = [newi, newj,dir,count]

        # check if a cart is that new position
        for index2, row2 in carts.iterrows():
            if index != index2 and row2['i'] == newi and row2['j'] == newj and index not in cartstoremove and index2 not in cartstoremove:
                print("CRASH! indexes",index,index2 , "at location", row2['j'], row2['i'])
                cartstoremove = np.append(cartstoremove, np.array([index,index2]))
                print("cartstoremove", cartstoremove)
                print(carts)
                break
    if len(cartstoremove):
        carts = carts.drop( cartstoremove, axis = 0)
    carts = carts.sort_values(['i', 'j'])
    # print(carts)


print(carts)