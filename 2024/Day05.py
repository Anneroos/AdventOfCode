# Processing input
with open("input05.txt") as f:
    orderRules, updates = f.read().split("\n\n")
    orderRules = orderRules.split("\n")
    updates = [[int(i) for i in row.split(",")] for row in updates.split("\n")]
    ordering = {}
    for rule in orderRules:
        l,r = [int(i) for i in rule.split("|")]
        ordering[l] = ordering.get(l,[]) + [r]


def checkOrder(update): # Checks if the order of pages in an update is in the right order
    validOrder = True
    for pageNr in range(len(update)):
        page = update[pageNr]
        for otherPageNr in range(pageNr + 1, len(update)):
            otherPage = update[otherPageNr]
            if page in ordering.get(otherPage, []):
                validOrder = False
                break
        if not validOrder:
            break
    return validOrder


def orderUpdate(update): # Orders an update if it's in the wrong order
    orderedUpdate = []
    for page in update:
        insertAt = 0
        for pageIdx in range(len(orderedUpdate)):
            otherPage = orderedUpdate[pageIdx]
            if page in ordering.get(otherPage,[]):
                insertAt = max(insertAt, pageIdx + 1)
        orderedUpdate = orderedUpdate[0:insertAt] + [page] + orderedUpdate[insertAt:]
    return orderedUpdate


score1 = 0
score2 = 0
for update in updates:
    validOrder = checkOrder(update)
    if validOrder:  # If the pages of an update are in the right order, add the middle page to the score of question 1
        score1 += update[int((len(update)-1)/2)]
    else:  # If the pages of an update are not in the right order, add the middle page of ther ordered update to score 2
        orderedUpdate = orderUpdate(update)
        score2 += orderedUpdate[int((len(update) - 1) / 2)]
print(f"Day 5:\n  When we add up the middle page numbers from the correctly-ordered updates, we get {score1}.")
print(f"  When we add up the middle page numbers from the ordered wrongly-ordered updates, we get {score2}.")

