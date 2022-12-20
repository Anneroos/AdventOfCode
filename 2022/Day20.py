with open("input20.txt") as f:
    originalnumbers = [int(x) for x in f.read().split("\n")]

def dictToList(dict):
    numberlist = []
    point = dict["start"]["next"]
    while point != "start":
        numberlist.append(point[1])
        point = dict[point]["next"]
    return numberlist

def mixing(inputnumbers, rounds, withDecryptionKey):
    dict = {"start" : {}}
    numbers = inputnumbers
    if withDecryptionKey:
        for idx in range(len(numbers)):
            numbers[idx] = numbers[idx]*811589153 # % len(numbers)

    for idx in range(len(numbers)):
        n = numbers[idx]
        if idx == 0:
            dict[(idx,n)] = {"prev": "start", "next": (idx+1, numbers[idx+1])}
            dict["start"]["next"] = (0, n)
        elif idx == len(numbers)-1:
            dict[(idx,n)] = {"prev": (idx-1, numbers[idx-1]), "next": "start"}
            dict["start"]["prev"] = (idx, n)
        else:
            dict[(idx,n)] = {"prev": (idx-1, numbers[idx-1]), "next": (idx+1, numbers[idx+1])}

    # Let the mixing begin
    for round in range(rounds):
        for idx in range(len(numbers)):
            n = numbers[idx]
            current = (idx, n)
            mixingNumber = n % (len(numbers) - 1)
            if mixingNumber != 0:
                next = dict[current]["next"]
                prev = dict[current]["prev"]
                # First tie prev en next together
                dict[prev]["next"] = next
                dict[next]["prev"] = prev
                # Now find a new place for n
                direction = "next" if mixingNumber > 0 else  "prev"
                otherdirection = "prev" if mixingNumber > 0 else "next"
                if dict[current][direction] == "start":
                    current = dict[current][direction]  # loop one extra
                for i in range(abs(mixingNumber)):
                    current = dict[current][direction]

                    if dict[current][direction] == "start":
                        current = dict[current][direction] # loop one extra

                other = dict[current][direction]
                dict[current][direction] = (idx, n)
                dict[other][otherdirection] = (idx, n)
                dict[(idx, n)][otherdirection] = current
                dict[(idx, n)][direction] = other

    finallist = dictToList(dict)
    start = finallist.index(0)
    a = finallist[(start + 1000) % len(finallist)]
    b = finallist[(start + 2000) % len(finallist)]
    c = finallist[(start + 3000) % len(finallist)]

    return a+b+c
#
answer1 = mixing(originalnumbers,1,False)
print(answer1)
answer2 = mixing(originalnumbers,10,True)
print(answer2)
