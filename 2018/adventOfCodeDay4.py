import numpy as np
import pandas as pd

lines = pd.read_csv("adventOfCodeInput4.txt", sep=']', header=None, engine='python')
lines.columns = ['Time', 'Action']
lines['Time'] = lines['Time'].apply(lambda x : x.split('[')[1])
lines['Day'] = lines['Time'].apply(lambda x : x.split(' ')[0])
lines['Time'] = lines['Time'].apply(lambda x : x.split(' ')[1])
lines['Action'] = lines['Action'].apply(lambda x: x.split(' ')[2])
# lines.set_index(['Day','Time'],inplace = True)



linesSorted = lines.sort_values(by=['Day','Time'])

guardDict = {}
guardID = -1
tempTimeList = np.zeros(60)
# for i in range(10):#len(lines)):
for row in linesSorted.itertuples():
    # print(tempTimeList)
    time = getattr(row, "Time"),
    action = getattr(row, "Action"),
    time = time[0]
    action = action[0]
    # print(guardID, time,action)

    if action[0] == '#':
        if guardID != -1: # add timelist to previous guard

            guardDict[guardID] += tempTimeList

            tempTimeList = np.zeros(60)
        guardID = action.split('#')[1]
        if guardID not in guardDict:
            guardDict[guardID] = np.zeros(60)
    else:
        timenr = int(time[3:5])


        # change things in guard-dictionary
        if action == 'asleep':


            tempTimeList[timenr:] = 1
        elif action == 'up':

            tempTimeList[timenr:] = 0



maxSum = 0
winningGuard = -1
bestminute = -1
for guard, timelist in guardDict.items():
   guardSum = timelist.sum()
   if guardSum > maxSum:
       maxSum = guardSum
       winningGuard = guard
       bestminute = timelist.argmax()

print("The guard who sleeps the most is ",winningGuard, "namely ", maxSum, "minutes. His schedule looks like", guardDict[winningGuard])
print("He sleeps the most at minute",bestminute)
print("Answer to puzzle 1 of day 4:", int(winningGuard)*bestminute)


maxMinuteSleepTime = 0
winningGuard = -1
bestminute = -1
for guard, timelist in guardDict.items():
    # print(guard,timelist)
    maxMinuteSleepTimeGuard = timelist.max()
    # print(maxMinuteSleepTimeGuard)
    if maxMinuteSleepTimeGuard > maxMinuteSleepTime:
       maxMinuteSleepTime = maxMinuteSleepTimeGuard
       bestminute = timelist.argmax()
       winningGuard = guard

print("Guard", winningGuard, "sleeps a total of ", maxMinuteSleepTime, "at minute", bestminute)
print("Answer to puzzle 2 of day 4: ", int(winningGuard)*bestminute)
