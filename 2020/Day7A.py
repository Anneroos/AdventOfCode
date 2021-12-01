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
                amount = contentSplit[0]
                contentsDict[content] = amount
        rulesDict[containerDescr] = contentsDict

rulesFlipped = {}
for bagColorParent in rulesDict.keys():
    for bagColorChild in rulesDict[bagColorParent]:
        includedInArray = rulesFlipped.get(bagColorChild,[])
        includedInArray.append(bagColorParent)
        rulesFlipped[bagColorChild] = includedInArray

colorsToCheck = rulesFlipped["shiny gold"]
checked = []
while len(colorsToCheck) >0:
    currentColor = colorsToCheck.pop(0)
    checked.append(currentColor)
    if currentColor in rulesFlipped.keys():
        for color in rulesFlipped[currentColor]:
            if color not in checked and color not in colorsToCheck:
                colorsToCheck.append(color)

print(f"There are {len(checked)} colors of bags that can contain a shiny gold bag.")

