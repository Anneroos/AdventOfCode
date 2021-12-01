with open("input18.txt") as f:
    lines = f.read().split("\n")

def evaluate(exercise):
    exerciseList = exercise.split(" ")
    answer = int(exerciseList[0]) # initialize
    operator = "" # initialize
    for i in range(1, len(exerciseList)):
        char = exerciseList[i]
        if char == "*" or char == "+":
            operator = char
        elif char.isnumeric():
            if operator == "*":
                answer = answer * int(char)
            elif operator == "+":
                answer = answer + int(char)
        else:
            print("We have a problem:", char)
            break
    return answer

def breakdown(exercise):
    index = exercise.find("(")
    if index >= 0: # We found a bracket! Let's find the closing one
        brackets = 1 # The one we just found
        otherindex = index + 1 # Let's start the search from the next index
        while brackets != 0:
            if exercise[otherindex] == "(": # Oh god, nested brackets...
                brackets += 1
            elif exercise[otherindex] == ")": # Closure!
                brackets -= 1
            otherindex += 1
        # Split exercise in three parts, and breakdown or evaluate the result further.
        return breakdown(exercise[0:index] + str(breakdown(exercise[index+1:otherindex-1])) + exercise[(otherindex):])
    else: #No brackets, easy peasy!
        return evaluate(exercise)

total = 0
for line in lines:
    total += breakdown(line)
print(f"Day 18 part 1: The total of these weird exercises is {total}.")