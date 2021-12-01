text_file = open("input8.txt", "r")
instructions = text_file.read().split('\n')
text_file.close()

accumulator = 0
index = 0
tries = 0

visited = []
while tries < 1000000:
    if index in visited:
        break
    visited.append(index)
    instruction = instructions[index]
    instructionSplit = instruction.split(" ")
    operation = instructionSplit[0]
    argument = instructionSplit[1]
    sign = argument[0]
    number = int(argument[1:])

    if operation == "acc":
        if sign == "+":
            accumulator += number
        else:
            accumulator -= number
        index += 1
    elif operation == "jmp":
        if sign == "+":
            index += number
        else:
            index -= number
    elif operation == "nop":
        index += 1

    else:
        print("Something went wrong.")
        break

    tries += 1
print(f"The first index that is visited twice is {index}. The accumulator had the value {accumulator} at that point, which is the answer to the question.")

