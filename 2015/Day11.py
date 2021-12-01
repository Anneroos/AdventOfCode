# 16-12-2020 met Wouter
import string
passwordSanta = "vzbxkghb"

def checkPassword(password):
    if len(password) != 8:
        return False
    if "i" in password or "o" in password or "l" in password:
        return False
    street = False
    for i in range(len(password)-2):
        a = string.ascii_lowercase.index(password[i])
        b = string.ascii_lowercase.index(password[i+1])
        c = string.ascii_lowercase.index(password[i+2])
        if a+1 == b and b+1 == c:
            street = True
            break
    if not street:
        return False
    twopairs = False
    nrOfPairs = 0
    pairLetter = []
    for i in range(len(password)-1):
        if password[i] == password[i+1] and password[i] not in pairLetter:
            pairLetter.append(password[i])
            nrOfPairs += 1
    if nrOfPairs >= 2:
        twopairs = True
    return twopairs

alphabet = "abcdefghijklmnopqrstuvwxyz"
def nextpassword(password):
    newpassword = password
    n = len(password)
    currentIndex = n-1
    finished = False
    while not finished:
        if string.ascii_lowercase.index(password[currentIndex])<25:
            newpassword = newpassword[:currentIndex]+ alphabet[string.ascii_lowercase.index(password[currentIndex])+1]+ newpassword[currentIndex+1:]
            finished = True
        else:
            newpassword = newpassword[:currentIndex]+"a" + newpassword[currentIndex+1:]
            currentIndex -= 1
    return newpassword


# Part 1
while not checkPassword(passwordSanta):
    passwordSanta = nextpassword(passwordSanta)
print(f"Day 11 part 1: Santa\'s next password is {passwordSanta}.")

# Part 2
passwordSanta = nextpassword(passwordSanta)
while not checkPassword(passwordSanta):
    passwordSanta = nextpassword(passwordSanta)
print(f"Day 11 part 2: Santa\'s next password is {passwordSanta}.")


# OF JE DENKT GEWOON NA ;)