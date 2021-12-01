import numpy as np
import time
start_time = time.time()


text_file = open("adventOfCodeInput5.txt", "r")
polymerOriginal = text_file.read().split('\n')[0]
text_file.close()
testpolymer = polymerOriginal[0:40]

# print(len(polymer), polymer)
def collapse(polymer):
    index=0
    while index < len(polymer)-1:
        letter0 = polymer[index]
        letter1 = polymer[index+1]
        # check if letter0 and letter1 are lower and upper case form of same letter
        if letter0.lower() == letter1.lower() and ( (letter0.islower() and letter1.isupper()) or (letter0.isupper() and letter1.islower())):
            # then remove that part of the string
            if index +2 < len(polymer):
                polymer = polymer[0:index] + polymer[index+2:]
            else:
                polymer = polymer[0:index]
            index -= 1 # go back one step!
            if(index <0): # but not if you were at index 0 already ;)
                index = 0
        else: # continue
            index+=1
    return polymer

# print(len(polymer), polymer)
print("Answer for puzzle 1 of Day 5 is", len(collapse(polymerOriginal)), ". Found in", (time.time() - start_time), "seconds")


shortest = len(polymerOriginal)
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in range(len(alphabet)):
    letter = alphabet[i]
    tempPolymer = polymerOriginal.replace(letter,'').replace(letter.upper(),'')
    resultlength = len(collapse(tempPolymer))
    if resultlength < shortest:
        shortest = resultlength
print("Answer for puzzle 2 of Day 6 is", shortest, ". Found in", (time.time() - start_time), "seconds")

