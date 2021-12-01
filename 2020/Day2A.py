import re
text_file = open("input2.txt", "r")
input = text_file.read().split('\n')
text_file.close()
nrGoodPasswords =0
for line in input:
    m = re.search('(\d+)-(\d+)\s(.?):\s(.+?$)', line)
    if m:
        minimum = int(m.group(1))
        maximum = int(m.group(2))
        letter = m.group(3)
        password = m.group(4)
        occurences = password.count(letter)
        if occurences >= minimum and occurences <= maximum:
            nrGoodPasswords += 1
print("Er zijn", nrGoodPasswords, "goede paswoorden.")
