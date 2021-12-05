# 05-12-2021
import re
with open("input4.txt", "r") as f:
    rooms = f.read().split("\n")
alphabet = "abcdefghijklmnopqrstuvwxyz"
def computeCheckSum(name):
    letters = set(list(name))
    letters.discard('-')
    sortedletters = sorted(letters, key=lambda x: (-name.count(x), x))
    checksum = "".join(sortedletters[:5])
    return checksum

def decryptName(encryptedname, index):
    dictionairy = {}
    for i in range(len(alphabet)):
        dictionairy[alphabet[i]] = alphabet[(i+index)%26]
    decryptedname = ""
    for i in encryptedname:
        if i == "-":
            decryptedname += " "
        else:
            decryptedname += dictionairy[i]
    return decryptedname

sumIDs = 0
for room in rooms:
    s = re.search(r'([\w-]+)-(\d+)\[(\w{5})\]', room)
    name=s.group(1)
    id=int(s.group(2))
    checksum=s.group(3)
    if checksum == computeCheckSum(name):
        sumIDs += id
        realname = decryptName(name,id)
        if "north" in realname and "pole" in realname and "objects" in realname:
            northpoleroomid = id

print(f"Part 1: The sum of the IDs of the real rooms is {sumIDs}.")
print(f"Part 2: The id of the room where the North Pole objects are stored is {northpoleroomid}.")