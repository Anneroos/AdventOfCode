import re
import numpy as np

text_file = open("input7.txt", "r")
lines = text_file.read().split('\n')
text_file.close()


# fill a dictionairy with information on the unique INPUT of a wire:
# the operator and wire(s) that go with that operator/gate
dict = {}
for line in lines:
    m = re.search('([\w\s\d]+) -> (\w+)', line)
    input = m.group(1)
    output = m.group(2)
    inputSplit = input.split(" ")
    length = len(inputSplit)
    if length == 3:
        dict[output] = {"operator" : inputSplit[1], "input": [inputSplit[0],inputSplit[2]]}
    elif length == 2:
        dict[output] = {"operator": "NOT", "input": [inputSplit[1]]}
    elif length == 1:
        dict[output] = {"operator": "DIRECT", "input": [inputSplit[0]]}


def calculateWire(wireName):
    if str(wireName).isnumeric():
        return int(wireName)
    operator = dict[wireName]["operator"]
    input = dict[wireName]["input"]
    if operator == "DIRECT":
        if input[0].isnumeric():
            result = int(input[0])
        else:
            result = calculateWire(input[0])
    elif operator == "NOT":
        otherWire = input[0]
        result = ~calculateWire(otherWire)
        if result <0:
            result += 65535 + 1
        return result
    elif operator == "AND":
        result = calculateWire(input[0]) & calculateWire(input[1])
    elif operator == "OR":
        result = calculateWire(input[0]) | calculateWire(input[1])
    elif operator == "RSHIFT":
        result = calculateWire(input[0]) >> int(input[1])
    elif operator == "LSHIFT":
        result = calculateWire(input[0]) << int(input[1])
    # If we finally have a numeric value, save it, so that we don't have to calculate again
    dict[wireName] = {"operator": "DIRECT", "input": [str(result)]}
    return result

part1 = calculateWire("a")
print(f"Day 7 part 1: {part1}")

# Part 2: reset the dictionairy...
dict = {}
for line in lines:
    m = re.search('([\w\s\d]+) -> (\w+)', line)
    input = m.group(1)
    output = m.group(2)
    inputSplit = input.split(" ")
    length = len(inputSplit)
    if length == 3:
        dict[output] = {"operator" : inputSplit[1], "input": [inputSplit[0],inputSplit[2]]}
    elif length == 2:
        dict[output] = {"operator": "NOT", "input": [inputSplit[1]]}
    elif length == 1:
        dict[output] = {"operator": "DIRECT", "input": [inputSplit[0]]}


# Use answer of part 1 as input for wire b
dict["b"]["input"] = [str(part1)]
# And calculate part 2!
part2 = calculateWire("a")
print(f"Day 7 part 2: {part2}.")