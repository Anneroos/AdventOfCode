import numpy as np

text_file = open("adventOfCodeInput2.txt", "r")
input = text_file.read().split('\n')
text_file.close()
lines = np.array(input)

testinput = np.array(['abcdef' , 'bababc' , 'abbcde' ,'abcccd' , 'aabcdd' ,  'abcdee' , 'ababab'])


twocount = 0
threecount = 0

for word in lines:
    myalfadict = {}
    twofound = False
    threefound = False
    for i in range(len(word)):
        letter = word[i]
        if letter not in myalfadict:
            count = word.count(letter)
            myalfadict[letter] = count
            if count == 2 and not twofound:
                twocount += 1
                twofound = True

            if count == 3 and not threefound:
                threecount += 1
                threefound = True

            if twofound and threefound:
                break

print("Answer for day 2 puzzle 1: ", twocount*threecount)

# lines = np.array(['abcde','fghij','klmno','pqrst','fguij','axcye','wvxyz'])
n = len(lines)

answer = ''
for i in range(n):
    for j in range(i,n):
        diff = 0
        for c1, c2 in zip(lines[i], lines[j]):
            if(c1 != c2):
                diff +=1
            if(diff>1):
                break
        if diff==1:

            #make anser:
            for c1, c2 in zip(lines[i], lines[j]):
                if (c1 == c2):
                    answer += c1


            break


print("Answer for day 2 puzzle 1: ", answer)

