with open("input3.txt", "r") as f:
    lines=f.read().split("\n")

# Function that computes the most common value per position for a given set of binary numbers
def findMostCommonValues(inputarray):
    n = len(inputarray[0])
    zeros = [0]*n
    ones = [0]*n
    for line in inputarray:
        for i in range(len(line)):
            if line[i] == "0":
                zeros[i] += 1
            elif line[i] == "1":
                ones[i] += 1
    mostCommonValue = ""
    for i in range(n):
        if zeros[i] > ones[i]:
            mostCommonValue += "0"
        elif zeros[i] < ones[i]:
            mostCommonValue += "1"
        elif zeros[i] == ones[i]:
            mostCommonValue += "-"
    return mostCommonValue

mostCommonValue = findMostCommonValues(lines)
gamma = ""
epsilon = ""
for i in range(len(mostCommonValue)):
    gamma = gamma + "1" if mostCommonValue[i] == "1" else gamma + "0"
    epsilon = epsilon + "0" if mostCommonValue[i] == "1" else epsilon + "1"
gamma = int(gamma,2)
epsilon = int(epsilon, 2)
print(f"Part 1: The gamma rate is {gamma} and the epsilon  rate is {epsilon}. Hence, the power consumption is {gamma*epsilon}.")

#Part 2
oxygen = [line for line in lines]
scrubber = [line for line in lines]
for i in range(len(lines[0])):
    oxygen_mostCommonValue = findMostCommonValues(oxygen)
    if oxygen_mostCommonValue[i] == "1" or oxygen_mostCommonValue[i] == "-":
        oxygen = [line for line in oxygen if line[i] == "1"]
    elif oxygen_mostCommonValue[i] == "0":
        oxygen = [line for line in oxygen if line[i] == "0"]

    scrubber_mostCommonValue = findMostCommonValues(scrubber)
    if scrubber_mostCommonValue[i] == "1" or scrubber_mostCommonValue[i] == "-":
        if len(scrubber) > 1: 
            scrubber = [line for line in scrubber if line[i] == "0"]
    elif scrubber_mostCommonValue[i] == "0":
        if len(scrubber) > 1:
            scrubber = [line for line in scrubber if line[i] == "1"]

oxygen_nr = int(oxygen[0],2)
scrubber_nr = int(scrubber[0],2)
print(f"Part 2: The oxygen generator rating is {oxygen_nr} and the CO2 scrubber rating is {scrubber_nr}. So the life support rating is {oxygen_nr*scrubber_nr}.")