with open("input18.txt") as f:
    lines = f.read().split("\n")


def evaluate(exercise):
    if "*" in exercise: # evaluate the pieces first
        answer = 1 # since multiplication
        for piece in exercise.split(" * "):
            answer *= evaluate(piece)
        return answer
    else: # so only addition!
        exerciseList = exercise.split(" + ")
        answer = 0
        for i in range(len(exerciseList)): # I guess there should be an easier way to add up numbers in a list
            answer = answer + int(exerciseList[i])
        return answer

def breakdown(exercise): # Evaluate where the brackets are, if any
    index = exercise.find("(")
    if index >= 0:# There is a bracket!
        brackets = 1 # The one we just found
        otherindex = index + 1 # Let's start looking from the next index.
        while brackets != 0:
            if exercise[otherindex] == "(": # Oh god, nested brackets
                brackets += 1
            elif exercise[otherindex] == ")":
                brackets -= 1
            otherindex += 1 # On to the next one
        # Break the exercise down in to three parts and return that
        return breakdown(exercise[0:index] + str(breakdown(exercise[index+1:otherindex-1])) + exercise[(otherindex):])
    else: # No brackets! Easy peasy, just evaluate it :)
        return evaluate(exercise)

total = 0
for line in lines:
    total += breakdown(line)
print(f"Day 18 part 2: The total of these messed up exercises is {total}.")