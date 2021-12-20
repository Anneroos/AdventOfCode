with open("input8.txt", "r") as f:
    lines = f.read().splitlines()


def sortLetters(pattern):
    return "".join(sorted(pattern))

def patternsToNumbers(inputpatterns):
    numbers = [""]*10 # We will fill such that numbers[i] contains the pattern the corresponds to it
    patterns = [sortLetters(p) for p in inputpatterns] # let's order the letters in each pattern for easy comparison with output later
    # We know 4 digits immediately because of their unique length:
    numbers[1] = [p for p in patterns if len(p) == 2][0]
    numbers[7] = [p for p in patterns if len(p) == 3][0]
    numbers[4] = [p for p in patterns if len(p) == 4][0]
    numbers[8] = [p for p in patterns if len(p) == 7][0]
    # Group together the other 6 digits in two groups according to their length
    length6 = [p for p in patterns if len(p) == 6] # 6, 9 and 0
    length5 = [p for p in patterns if len(p) == 5] # 2, 3 and 5
    # The 3 completely contains the 1, but 2 and 5 don't, so we can find 3
    numbers[3] = [p for p in length5 if sum([letter in p for letter in numbers[1]]) == 2][0]
    # The two letters that are in 4 but not in 1, should both be in 5, not in 2 (or 3). So we know 2 and 5.
    twolettersin4not1 = [i for i in numbers[4] if i not in numbers[1]]
    numbers[5] = [pattern for pattern in length5 if sum([letter in pattern for letter in twolettersin4not1]) == 2][0]
    numbers[2] = [p for p in length5 if numbers[3] != p and numbers[5] != p][0]
    # from 6, 9 and 0,  only the 6 doesn't completely contain the 1. So we found the 6!
    numbers[6] = [p for p in length6 if numbers[1][0] not in p or numbers[1][1] not in p][0]
    # Only 0 and 9 are to be distinguished! Well, 9 completely contains 3
    numbers[9] = [p for p in length6 if sum([i in p for i in numbers[3]]) == 5][0]
    numbers[0] = [p for p in length6 if numbers[6] != p and numbers[9] != p][0]
    return numbers

nrEasyNumbers = 0 # for part 1
totalOutput = 0 # for part 2
for line in lines:
    patterns = line.split(" | ")[0].split()
    output = line.split(" | ")[1].split()
    for pattern in output:
        if len(pattern) in [2,3,4,7]:
            nrEasyNumbers += 1
    orderedPatterns = patternsToNumbers(patterns) # array with the patterns in the order of the number the represent
    outputvalue = int("".join([str(orderedPatterns.index(sortLetters(o))) for o in output])) # use orderedPatterns to lookup the patterns in the output
    totalOutput += outputvalue

print(f"Part 1: I found {nrEasyNumbers} easy numbers.")
print(f"Part 2: The total output is {totalOutput}.")