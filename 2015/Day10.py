# 16-12-2020 met Wouter
import time
t0 = time.time()

input = "3113322113"
def look_and_say(written,n):
    for j in range(n):
        listToSay = ""
        currentIndex = 0
        for i in range(1,len(written)+1):
            if i == len(written) or written[i] != written[currentIndex]:
                listToSay += str(i-currentIndex) + str(written[currentIndex])
                currentIndex = i
        written = listToSay

    return written

def look_and_say_woett(written,n):
    for j in range(n):
        listToSay = ""
        currentIndex = 0
        while currentIndex < len(written):
            otherIndex = currentIndex + 1
            while otherIndex < len(written) and written[otherIndex] == written[currentIndex]:
                otherIndex += 1
            listToSay += str(otherIndex-currentIndex) + str(written[currentIndex])
            currentIndex = otherIndex
        written=listToSay

    return written


t0 = time.time()
print(f"Day 10 part 1: after 40 iterations, the list is {len(look_and_say(input,40))} characters long.")
t1 = time.time()
print(f"This took {t1-t0} seconds.\n")

t0 = time.time()
print(f"Day 10 part 1 Woett\'s way: after 40 iterations, the list is {len(look_and_say_woett(input,40))} characters long.")
t1 = time.time()
print(f"This took {t1-t0} seconds.\n")
t0 = time.time()
print(f"Day 10 part 2: after 50 iterations, the list is {len(look_and_say(input,50))} characters long.")
t1 = time.time()
print(f"This took {t1-t0} seconds.\n")


t0 = time.time()
print(f"Day 10 part 2 Woett\'s way:: after 50 iterations, the list is {len(look_and_say_woett(input,50))} characters long.")
t1 = time.time()
print(f"This took {t1-t0} seconds.\n")