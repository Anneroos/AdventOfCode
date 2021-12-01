import re

text_file = open("input2.txt", "r")
input = text_file.read().split('\n')
text_file.close()
nrGoodPasswords =0
for line in input:


    m = re.search('(\d+)-(\d+)\s(.?):\s(.+?$)', line)
    if m:

        index1 = int(m.group(1))
        index2 = int(m.group(2))
        letter = m.group(3)
        password = m.group(4)

        if (password[index1 - 1] == letter) != (password[index2 - 1] == letter):

            nrGoodPasswords += 1

    else:
        print("Niet gelukt")
        print(line)


print("Nu zijn er", nrGoodPasswords, "goede paswoorden.")
# found: 1234