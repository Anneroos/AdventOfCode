import re

text_file = open("input7.txt", "r")
rules = text_file.read().split('\n')
text_file.close()
rulesDict = {}
for rule in rules:
    m = re.search('([\w\s]+) contain ([\d\w\s,]+).', rule)
    if m:
        container = m.group(1)
        contents = m.group(2)
        containerDescr = container.split(" ")
        containerDescr = containerDescr[0] + " " + containerDescr[1]
        contentsList = contents.split(", ")
        contentsDict = {}
        for content in contentsList:
            if content == "no other bags":
                pass
            else:
                contentSplit = content.split(" ")
                content = contentSplit[1] + " " + contentSplit[2]
                amount = int(contentSplit[0])
                contentsDict[content] = amount
        rulesDict[containerDescr] = contentsDict

def check_bags(bagcolor):
    contentsDict = rulesDict[bagcolor]
    if len(contentsDict.keys()) == 0:
        return 0
    else:
        amount = 0
        for colorChild in contentsDict.keys():
            amount += contentsDict[colorChild] + contentsDict[colorChild]*check_bags(colorChild)
        return amount
answer=check_bags("shiny gold")
print(f"One shiny bag contains {answer} other bags!")