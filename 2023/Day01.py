import re
with open("input01.txt","r") as f:
    lines =  f.read().split('\n')
    
# Part 1
digits = [[j for j in i if j.isnumeric()] for i in lines]
firstLastDigit = [int("".join([l[0],l[-1]])) for l in digits]
print(f"Day 1: \n1) {sum(firstLastDigit)} ")

# Part 2
total = 0
numbers = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9, 
           "0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
for line in lines:
    minIndexDigit = [len(line),""]
    maxIndexDigit = [-1, ""]
    for n in numbers.keys():
        indicesFound = [m.start() for m in re.finditer(n, line)]
        if len(indicesFound) > 0:
            if min(indicesFound) < minIndexDigit[0]:
                minIndexDigit = [min(indicesFound), n]
            if max(indicesFound) > maxIndexDigit[0]:
                maxIndexDigit = [max(indicesFound), n]
    total += numbers[minIndexDigit[1]]*10 + numbers[maxIndexDigit[1]]
print(f"2) {total} ")
