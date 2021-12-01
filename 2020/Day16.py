import re
import numpy as np

text_file = open("input16.txt", "r")
input = text_file.read().split('\n\n')
text_file.close()

rules = input[0].split("\n")
myticket = [int(n) for n in input[1].split("\n")[1].split(",")]
print(myticket)
tickets = input[2].split("\n")[1:]

nrOfCols = len(myticket)

rulesDict = {}
for rule in rules:
    m = re.search("([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)", rule)
    if m:
        field = m.group(1)
        ranges = [[int(m.group(2)),int(m.group(3))],[int(m.group(4)),int(m.group(5))]]
        rulesDict[field] = ranges

numbersAllowed = []
for field in rulesDict.keys():
    ranges = rulesDict[field]

    for ran in ranges:
        for i in range(ran[0],ran[1]+1):

            if i not in numbersAllowed:
                numbersAllowed.append(i)



# Part 1
numbersAllowed = sorted(numbersAllowed)
invalidNumbersTotal = 0

for ticket in tickets:
    ticket = [int(n) for n in ticket.split(",")]
    ticketValid = True
    for number in ticket:
        if number not in numbersAllowed:
            ticketValid = False
            invalidNumbersTotal += number
            break
print(invalidNumbersTotal)

# part 2

def checkTicket(ticket):
    ticketValid = True
    for number in ticket:
        if number not in numbersAllowed:
            ticketValid = False
            break
    return ticketValid

validTickets = []
for ticket in tickets:
    ticket = [int(n) for n in ticket.split(",")]
    if checkTicket(ticket):
        validTickets.append(ticket)
print(len(validTickets))



validTickets = np.array(validTickets)

validFieldsPerColumn = []
for col in range(nrOfCols):
    print("Column nr:",col)
    column = validTickets[:,col]
    validFields = []
    for field in rulesDict:
        validField = True
        ranges = rulesDict[field]
        for number in column:
            # print(number, ranges[0][0], ranges[0][1], ranges[0][0]<= number <= ranges[0][1])
            if not(ranges[0][0]<= number <= ranges[0][1] or ranges[1][0]<= number <= ranges[1][1]):
                validField = False
                break
        if validField:
            validFields.append(field)
    validFieldsPerColumn.append(validFields)
    # print(col, validFields)

print(validFieldsPerColumn)

fieldsToColumn = {}

solved = False
tries = 0
changedSomething = True
while not solved and tries < 1000 and changedSomething:
    tries +=1
    print("##",tries)
    changedSomething = False
    for col in range(nrOfCols):
        currentFields = validFieldsPerColumn[col]
        if len(currentFields) == 1 and currentFields[0] not in fieldsToColumn.keys():
            changedSomething = True
            fixedField = currentFields[0]
            fieldsToColumn[fixedField] = col
            # remove this field from other cols
            for othercol in range(nrOfCols):
                # print(othercol)
                if othercol != col:
                    # print(validFieldsPerColumn[othercol])
                    if fixedField in validFieldsPerColumn[othercol]:
                        validFieldsPerColumn[othercol].remove(fixedField)
                        # print(validFieldsPerColumn[othercol])
            # print(fieldsToColumn)


print(validFieldsPerColumn)

solution = 1
for i in range(nrOfCols):
    field = validFieldsPerColumn[i][0]
    m = re.search("departure.+", field)
    if m:
        print(i, field)
        solution = solution*myticket[i]

print(f"Day 16 part 2: {solution}.")


