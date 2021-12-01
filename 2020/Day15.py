import time
start = time.time()

input = [6,19,0,5,7,13,1]
# input = [0,3,6]

# def numberSpoken(startnumbers,number):
#     dict = {}
#     for i in range(len(startnumbers)):
#         dict[input[i]] = [i + 1]
#     nrOfPlayers = len(startnumbers)
#     lastNumberSaid = startnumbers[nrOfPlayers - 1]
#     for index in range(nrOfPlayers+1, number+1):
#         if lastNumberSaid in dict.keys() and len(dict[lastNumberSaid])>=2:
#             n = len(dict[lastNumberSaid])
#             age = dict[lastNumberSaid][n-1] - dict[lastNumberSaid][n-2]
#             nextnumber = age
#         else:
#             nextnumber = 0
#         array = dict.get(nextnumber,[])
#         array.append(index)
#         dict[nextnumber] = array
#         lastNumberSaid = nextnumber


def numberSpoken(startnumbers,number):
    dict = {}
    nrOfPlayers = len(startnumbers)
    for i in range(nrOfPlayers-1):
        dict[input[i]] = i + 1
    lastNumberSaid = startnumbers[nrOfPlayers - 1]
    for index in range(nrOfPlayers, number):
        lastTimeSaid = dict.get(lastNumberSaid,"None")
        if lastTimeSaid != "None":
            nextnumber = index - lastTimeSaid
        else:
            nextnumber = 0
        dict[lastNumberSaid] = index
        lastNumberSaid = nextnumber

    return nextnumber
print(f"Day 15 part 1: {numberSpoken(input, 2020)}.")
print('It took', time.time()-start, 'seconds.')

start = time.time()
print(f"Day 15 part 2: {numberSpoken(input, 30000000)}.")
print('It took', time.time()-start, 'seconds.')

