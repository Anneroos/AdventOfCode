with open("input01.txt","r") as f:
    sumsOfColaries = sorted([sum([int(j) for j in i.split("\n")]) for i in f.read().split('\n\n')])
print(f"Day 1: \n1) The elf carrying the most calories, is carrying {sumsOfColaries[-1]} calories.")
print(f"2) The three elves carrying the most calories, are carrying in total {sumsOfColaries[-1] + sumsOfColaries[-2] + sumsOfColaries[-3]} calories.")
