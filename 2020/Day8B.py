text_file = open("input8.txt", "r")
instructions = text_file.read().split('\n')
text_file.close()

win = False
for i in range(len(instructions)):
    visited = []
    index = 0
    tries = 0
    accumulator = 0
    while tries < len(instructions)+1:
        if index in visited:
            break
        if index >= len(instructions):
            win = True
            break
        visited.append(index)
        instruction = instructions[index]
        instructionSplit = instruction.split(" ")
        operation = instructionSplit[0]
        if i == index:
            if operation == "jmp":
                operation = "nop"
            elif operation == "nop":
                operation = "jmp"
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
            print("Something went wrong.", i , index)
            break
        tries += 1

    if win:
        break



print(f"For i={i} I changed the operation to {operation}, which resulted in the program to end properly! \nThe accumulator ended at {accumulator}, which is the answer to part 2 of day 8.")

