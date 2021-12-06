fish = [1,1,5,2,1,1,5,5,3,1,1,1,1,1,1,3,4,5,2,1,2,1,1,1,1,1,1,1,1,3,1,1,5,4,5,1,5,3,1,3,2,1,1,1,1,2,4,1,5,1,1,1,4,4,1,1,1,1,1,1,3,4,5,1,1,2,1,1,5,1,1,4,1,4,4,2,4,4,2,2,1,2,3,1,1,2,5,3,1,1,1,4,1,2,2,1,4,1,1,2,5,1,3,2,5,2,5,1,1,1,5,3,1,3,1,5,3,3,4,1,1,4,4,1,3,3,2,5,5,1,1,1,1,3,1,5,2,1,3,5,1,4,3,1,3,1,1,3,1,1,1,1,1,1,5,1,1,5,5,2,1,5,1,4,1,1,5,1,1,1,5,5,5,1,4,5,1,3,1,2,5,1,1,1,5,1,1,4,1,1,2,3,1,3,4,1,2,1,4,3,1,2,4,1,5,1,1,1,1,1,3,4,1,1,5,1,1,3,1,1,2,1,3,1,2,1,1,3,3,4,5,3,5,1,1,1,1,1,1,1,1,1,5,4,1,5,1,3,1,1,2,5,1,1,4,1,1,4,4,3,1,2,1,2,4,4,4,1,2,1,3,2,4,4,1,1,1,1,4,1,1,1,1,1,4,1,5,4,1,5,4,1,1,2,5,5,1,1,1,5]
fishes = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0} # I am going to keep track of the number of fish that have a certain amount of days left. I don't see them as individuals :P
for f in fish:
    fishes[f] = fishes.get(f,0) + 1 # read input into my new dictionairy
def fishDays(fishesDict, nrOfDays):
    for day in range(nrOfDays):
        readyfishes = fishesDict[0] # remember the number of fishes that are ready to create new fish
        for i in range(1,9): #
            fishesDict[i-1] = fishesDict[i] # move the fishes "one day to the left" ;)
        fishesDict[6] += readyfishes # the fishes that were ready reset back to 6 days
        fishesDict[8] = readyfishes # new fishes!
    return fishesDict
print(f"Part 1: After 80 days there are {sum(fishDays(fishes.copy(), 80).values())} fishes.")
print(f"Part 2: After 256 days there are {sum(fishDays(fishes.copy(), 256).values())} fishes.")