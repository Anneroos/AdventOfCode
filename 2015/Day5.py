# 14-12-2020
text_file = open("input5.txt", "r")
strings = text_file.read().split('\n')
text_file.close()

def checkString1(stringToCheck):

    nrOfVowels = 0
    for vowel in ["a","e","i", "o", "u" ]:
        nrOfVowels += stringToCheck.count(vowel)
    contains3Vowels = True if nrOfVowels >=3 else False
    containsDoubleLetter = False
    for i in range(len(stringToCheck)-1):
        if stringToCheck[i] == stringToCheck[i+1]:
            containsDoubleLetter = True
            break
    containsBadSubstring = False
    for substring in ["ab", "cd", "pq", "xy"]:
        if stringToCheck.count(substring) >= 1:
            containsBadSubstring = True
    nice = (contains3Vowels and containsDoubleLetter and not containsBadSubstring)
    # print(string, "      3 vowels:",contains3Vowels, "       double:",containsDoubleLetter,"       bad substring:", containsBadSubstring, "       nice:", nice)
    return nice

def checkString2(stringToCheck):
    # twice the same combo of 2 letters
    twiceCombo = False
    for i in range(len(stringToCheck)-1):
        substr = stringToCheck[i:i+2]
        if stringToCheck[i+2:].count(substr) >= 1:

            twiceCombo = True
    repeatLetterAfter2 = False
    for i in range(len(stringToCheck) - 2):
        if stringToCheck[i] == stringToCheck[i+2]:
            repeatLetterAfter2 = True

    nice = twiceCombo and repeatLetterAfter2#(contains3Vowels and containsDoubleLetter and not containsBadSubstring)
    print(string, "      twiceCombo;",twiceCombo, "       repeat Letter after 2:",repeatLetterAfter2, "             nice:", nice)
    return nice

nrNiceStrings1 = 0
nrNiceStrings2 = 0
for string in strings:
    nrNiceStrings1 += 1 if checkString1(string) else 0
    nrNiceStrings2 += 1 if checkString2(string) else 0

print(f"Day 5 part 1: there are {nrNiceStrings1} nice strings.")
print(f"Day 5 part 2: there are {nrNiceStrings2} nice strings.")

