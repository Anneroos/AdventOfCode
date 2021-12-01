# 16-12-2020
import re
import numpy as np
import json
with open("input12.txt") as file:
    input = file.read().split("\n")[0]
mydict = json.loads(input)

m = re.findall("(-?\d+)", input)
numbers = [int(n) for n in m]
print(f"Day 12 part 1: The sum of the numbers in the JSON file is {np.array(numbers).sum()}.")


def valueChecker1(book):
    # check for red
    # print(type(book))
    if type(book) == dict:
        total = 0
        for key in book.keys():
            entry = book[key]

            total += valueChecker1(entry)
        return total
    elif type(book) == list:
        total = 0
        for entry in book:
            total += valueChecker1(entry)
        return total
    elif type(book) == int:
        return book
    else:
        return 0
print(f"Day 12 part 1: The sum of the numbers in the JSON file is {valueChecker1(mydict)}.")


def valueChecker2(book):
    # check for red
    # print(type(book))
    if type(book) == dict:
        total = 0
        for key in book.keys():
            entry = book[key]
            if entry == "red":
                return 0
            else:
                total += valueChecker2(entry)
        return total
    elif type(book) == list:
        total = 0
        for entry in book:
            total += valueChecker2(entry)
        return total
    elif type(book) == int:
        return book
    else:
        return 0




answer1 = valueChecker2(mydict)
print(f"Day 12 part 2: {answer1}")