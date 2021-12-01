import time
t0 = time.time()

state = "##..##....#.#.####........##.#.#####.##..#.#..#.#...##.#####.###.##...#....##....#..###.#...#.#.#.#"
# state = "#..#.#..##......###...###"
leftindex = 0
import pandas as pd

lines = pd.read_csv("adventOfCodeInput12.txt", sep=' ', header=None, engine='python', skiprows=2)
lines.columns = ['string', 'arrow', 'result']
lines.drop(['arrow']    ,inplace=True, axis=1)
lines.set_index('string', inplace = True)
# print(lines)
stoppedat = 0
for i in range(1,50000000000+1):
    if state[0] == '#':
        leftindex -= 4
        # print('move 4')
        state = '....' + state
    elif state[1] == '#':
        leftindex -= 3
        state = '...' + state
        # print('move 3')
    elif state[2] == '#':
        leftindex -= 2
        state = '..' + state
        # print('move 2')
    elif state[3] == '#':
        leftindex -= 1
        state = '.' + state
        # print('move 1')

    if state[-1] == '#':

        state = state + '....'
    elif state[-2] == '#':

        state = state + '...'
    elif state[-3] == '#':

        state = state + '..'
    elif state[-4] == '#':

        state = state + '.'
    # print(state)
    tempstate = '..'
    for k in range(2,len(state)-2):
        part = state[k-2:k+3]
        result = lines.loc[part]['result']
        tempstate += result

    if tempstate[4:len(tempstate)] in state:
        state = tempstate + '..'
        stoppedat = i
        print("stoppedat ",i , "leftindex was", leftindex)
        leftindex = leftindex + (50000000000 - stoppedat)
        print("steps to go: ",(50000000000 - stoppedat), "so new leftindex: ", leftindex )
        break

    state = tempstate + '..'

print(state)

total = 0
totalplants = 0
for i in range(len(state)):
    if state[i] == '#':
        total += (i+leftindex)
        totalplants += 1
print("nr of plants:", totalplants)
print("total score",total)
print("leftindex",leftindex)



t1 = time.time()

print("time: ", t1-t0)
# 3999999999920 was this too low?
# 7999999991840 too high