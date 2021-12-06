with open("input6.txt","r") as f:
    lines = f.read().splitlines()

def mostCommonCharacter(list, index):
    letters = {}
    for word in list:
        letters[word[index]] = letters.get(word[index],0) + 1
    print(letters)
    t=sorted(letters.keys(), key= lambda x: letters[x], reverse=True)
    return t
message1 = ""
message2 = ""
for i in range(len(lines[0])):
    sortedLetters = mostCommonCharacter(lines, i)
    message1 += sortedLetters[0]
    message2 += sortedLetters[-1]
print(message1)
print(message2)