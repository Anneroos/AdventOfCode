with open("input24.txt", "r") as f:
    lines = [i.rstrip().split(' ') for i in f.read().splitlines()]

import time
st = time.time()

def input(location):
    def f(dic,inputCount):
        print("Input!", inputCount)
        dic[location] = "n"+ str(inputCount)
        return dic, True
    return f

def add(location, v):
    def f(dic,inputCount):
        d = dic[v] if v in "xyzw" else v
        try:
            # print(d, dic[location])
            dic[location] = str(int(d) + int(dic[location]))
        except:
            # print(d, dic[location])
            if d == "0":
                dic[location] == dic[location]
            elif dic[location] == "0":
                dic[location] = d
            else:
                dic[location] =  "(" + dic[location] + " + " + d + ")"
        return dic, False
    return f

def mul(location, v):
    def f(dic,inputCount):
        d = dic[v] if v in "xyzw" else v
        # print(d, dic[location], d == "0", dic[location] == "0")
        if d != "1": # if 1 you don't need to do anything
            if dic[location] == "0" or  d == "0":
                dic[location] = "0"
            elif dic[location] == '1':
                dic[location] = d
            else:
                dic[location] = "(" + dic[location] + ")  *  (" + d + ")"
        return dic, False
    return f

def div(location, v):
    def f(dic,inputCount):
        d = dic[v] if v in "xyzw" else v
        if d != "1":
            dic[location]= "int(("+ dic[location] + ") / (" + d + "))"
        return dic, False
    return f

def mod(location, v):
    def f(dic,inputCount):
        d = dic[v] if v in "xyzw" else v
        if dic[location] != "0":
            dic[location]= "(" + dic[location] +  ") % (" + d + ")"
        return dic, False
    return f

def eql(location, v):
    def f(dic,inputCount):
        d = dic[v] if v in "xyzw" else v
        # if literally the same:
        if d == dic[location]:
            dic[location] = "1"
        else:
            dic[location] = "(1 if " + dic[location] + "==" + d + " else 0)"
        return dic, False
    return f

functions = []
for line in lines:
    instruction = line[0]
    location = line[1]
    value = 0 if len(line)==2 else line[2]
    if instruction == "inp":
        functions.append(input(location))
    elif instruction == "add":
        functions.append(add(location, value))
    elif instruction == "mul":
        functions.append(mul(location, value))
    elif instruction == "div":
        functions.append(div(location, value))
    elif instruction == "mod":
        functions.append(mod(location, value))
    elif instruction == "eql":
        functions.append(eql(location, value))

t = {"w": "0", "x": "0", "y":"0", "z": "0"} # i = 0
inpc = 0
m = 0
t = {"w": "n1", "x": "0", "y":"(n0 + 1)", "z": "(n0 + 1)"} # i = 6
m = 25
inpc = 2
t = {"w": "n2", "x": "0", "y":"(n1 + 7)", "z": "26*(n0+1) + (n1 + 7)"} # i = 6
m = 38
inpc = 3
t = {"w": "n2", "x": "0", "y":"(n1 + 7)", "z": "26*(n0+1) + (n1 + 7)"} # i = 6
m = 43
inpc = 3
t = {"w": "n3", "x": "1", "y":"(n2 + 13)", "z": "((26*(n0+1) + (n1 + 7))*(26) + (n2 + 13))"} # i = 6
m = 55
inpc = 4
t = {"w": "n3", "x": "(n2 + 13)", "y":"(n2 + 13)", "z": "((26*(n0+1) + (n1 + 7))*(26) + (n2 + 13))"} # i = 6
m = 58
inpc = 4
t = {"w": "n3", "x": "0", "y":"(n2 + 13)", "z": "((26*(n0+1) + (n1 + 7)))"} # i = 6
m = 62
inpc = 4
# n2 + 7 = n3  ->> x=0 From now on assume this is the case!
t = {"w": "n4", "x": "1", "y":"0", "z": "((26*(n0+1) + (n1 + 7)))"} # i = 6
m = 80
inpc = 5
t = {"w": "n5", "x": "n4", "y":"n4", "z": "(((((26*(n0+1) + (n1 + 7))))))"} # i = 6
m = 95
inpc = 6
# n4-4=n5 >>> x = 0 na eql x 0
t = {"w": "n5", "x": "0", "y":"n4", "z": "(((((26*(n0+1) + (n1 + 7))))))"} # i = 6
m = 98
inpc = 6
t = {"w": "n6", "x": "1", "y":"0", "z": "(26*(n0+1) + (n1 + 7))"} # i = 6
m = 116
inpc = 7
t = {"w": "n7", "x": "n6+11", "y":"n6+11", "z": "(((26*(n0+1) + (n1 + 7)))  *  (26) + (n6 + 11))"} # i = 6
m = 130
inpc = 8
t = {"w": "n7", "x": "0", "y":"n6+11", "z": "(((26*(n0+1) + (n1 + 7)))  *  (26) + (n6 + 11))"} # i = 6
m = 133
inpc = 8
t = {"w": "n8", "x": "n7+6", "y":"n7+6", "z": " (((((26*(n0+1) + (n1 + 7)))  *  (26) + (n6 + 11)))  *  (26) + (n7 + 6))"} # i = 6
m = 148
inpc = 9
t = {"w": "n8", "x": "0", "y":"n7+6", "z": " (((((26*(n0+1) + (n1 + 7)))  *  (26) + (n6 + 11)))  *  (26) + (n7 + 6))"} # i = 6
m = 151
inpc = 9
# n8+1=n9 Assume
t = {"w": "n9", "x": "0", "y":"n8+1", "z": "(((((26*(n0+1) + (n1 + 7)))  *  (26) + (n6 + 11)))  *  (26) + (n7 + 6))"} # i = 6
m = 170
inpc = 10
t = {"w": "n10", "x": "n7+6", "y":"0", "z": "(((26*(n0+1) + (n1 + 7)))  *  (26) + (n6 + 11))"} # i = 6
m = 185
inpc = 11
# n7+6=n10! Assume
t = {"w": "n10", "x": "0", "y":"0", "z": "(((26*(n0+1) + (n1 + 7)))  *  (26) + (n6 + 11))"} # i = 6
m = 188
inpc = 11
t = {"w": "n11", "x": "(n6 + 11)", "y":"0", "z": "((26*(n0+1) + (n1 + 7))) "} # i = 6
m = 203
inpc = 12
# n6 +8 = n11 Assume
t = {"w": "n11", "x": "0", "y":"0", "z": "((26*(n0+1) + (n1 + 7))) "} # i = 6
m = 206
inpc = 12
t = {"w": "n12", "x": "(n1+7)", "y":"0", "z": "(n0+1)"} # i = 6
m = 221
inpc = 13
# n1-2=n12 Assume!
t = {"w": "n12", "x": "0", "y":"0", "z": "(n0+1)"} # i = 6
m = 224
inpc = 13
t = {"w": "n13", "x": "(n0+1)", "y":"0", "z": "0"} # i = 6
m = 239
inpc = 14
# n0-8=n13 Assume?
t = {"w": "n13", "x": "0", "y":"0", "z": "0"} # i = 6
m = 242
inpc = 14


print(t)
test = 252
for i in range(m,test):#len(functions)):
    f = functions[i]
    print(i, lines[i])
    t, b = f(t, inpc)
    # print("b", b)
    if b:
        inpc += 1
    print("--------------------"+str(i)+"---------------------", inpc)
    for k,v in t.items():
        print(k, "  :  ",v)
print("**")
99299513899971
n0,n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13 = [9,9,2,9,9,5,1,3,8,9,9,9,7,1]
print(eval(t["z"]))



# ORIGINALS
def input(location):
    def f(dic,nr,inputCount):
        dic[location]=nr[inputCount]
        return dic, True
    return f

def add(location, v):
    def f(dic,nr,inputCount):
        d = dic[v] if v in "xyzw" else int(v)
        dic[location]+=d
        return dic, False
    return f

def mul(location, v):
    def f(dic,nr,inputCount):
        d = dic[v] if v in "xyzw" else int(v)
        dic[location]*=d
        return dic, False
    return f

def div(location, v):
    def f(dic,nr,inputCount):
        d = dic[v] if v in "xyzw" else int(v)
        dic[location]= int(dic[location]/d)
        return dic, False
    return f

def mod(location, v):
    def f(dic,nr,inputCount):
        d = dic[v] if v in "xyzw" else int(v)
        dic[location]= dic[location] % d
        return dic, False
    return f

def eql(location, v):
    def f(dic,nr,inputCount):
        d = dic[v] if v in "xyzw" else int(v)
        dic[location] = int(dic[location]==d)
        return dic, False
    return f

functions = []
for line in lines:
    instruction = line[0]
    location = line[1]
    value = 0 if len(line)==2 else line[2]
    if instruction == "inp":
        functions.append(input(location))
    elif instruction == "add":
        functions.append(add(location, value))
    elif instruction == "mul":
        functions.append(mul(location, value))
    elif instruction == "div":
        functions.append(div(location, value))
    elif instruction == "mod":
        functions.append(mod(location, value))
    elif instruction == "eql":
        functions.append(eql(location, value))

# Een andere poging was
def superFunction(dic, numberList, lineIdx, inputIdx):
    print(lineIdx, dic, inputIdx)
    if lineIdx == len(lines):
        return dic
    else:
        dic,t = functions[lineIdx](dic, numberList, inputIdx)
        if t:
            inputIdx += 1
        return superFunction(dic, numberList, lineIdx + 1, inputIdx)


# state = {"n1":0,"n2":0,"n3":0,"n4":0,"n5":0,"n6":0,"n7":0,"n8":0,"n9":0,"n10":0,"n11":0,"n12":0,"n13":0,"n14":0,1:0}
# t = {"w": state.copy(), "x": state.copy(), 'y' : state.copy(), "z": state.copy()}
# print(t)

# print(superFunction({"x":0,"y":0,"z":0,"w":0},[1,2,3,4,5,6,7,8,7,6,5,4,3,2],0,0))

def findBiggestodelNr():
    storage = {}
    result = -1
    number = 99299513899979#89188593129498
    c =0
    # number = 11111111111111
    while result != 0 and c<10:
        # print(number,c)
        c+=1
        number -= 1
        # number+=1
        numberlist = [int(i) for i in list(str(number))]
        if len(numberlist) !=14 or sum([1 if i!=0 else 0 for i in numberlist]) != 14:
            # Go to next number
            continue
        integers = {"x":0,"y":0,"z":0,"w":0}
        idx = 0
        inputCount = 0
        for l in range(13):
            # print("tuple(numberlist[:13-l])",tuple(numberlist[:13-l]), "13-l",13-l)
            if tuple(numberlist[:13-l]) in storage:
                idx,values = storage[tuple(numberlist[:13-l])]
                integers = dict(zip(["x","y","z", "w"],values))
                inputCount = 13-l
                # print(number, "Found something in storage!")
                # print("l", l, "idx", idx, "values", values, "inputcount", inputCount, integers)
                break
        # print("Hi", number)
        while idx < test:#len(lines):
            integers, inputTest = functions[idx](integers, numberlist,inputCount)
            if inputTest:
                inputCount += 1
                storage[tuple(numberlist[:inputCount])] = (idx+1,(integers["x"], integers["y"], integers["z"], integers["w"]))


            # line = lines[idx]
            # instruction = line[0]
            # location = line[1]
            # value = 0 if len(line) < 3 else integers[line[2]] if line[2] in "xyzw" else int(line[2])
            # if instruction == "inp":
            #     integers[location] = numberlist[inputCount]
            #     inputCount += 1
            #     storage[tuple(numberlist[:inputCount])] = (idx + 1, (integers["x"], integers["y"], integers["z"], integers["w"]))
            # elif instruction == "add":
            #     integers[location] += value
            # elif instruction == "mul":
            #     integers[location] *= value
            # elif instruction == "div":
            #     integers[location] = int(integers[location]/value)
            # elif instruction == "mod":
            #     integers[location] = integers[location] % value
            # elif instruction == "eql":
            #     integers[location] = int(integers[location] == value)
            idx += 1
        result = integers["z"]

        # if number % 1000000 == 999999:
        et = time.time()
        print(number, result)
        # print(et-st, "sec")
    return result

print(findBiggestodelNr())

# Om er 0 uit te laten komen:
# n0-8=n13
# n1-2=n12
# n2 + 7 = n3
# n4-4=n5
# n5 + 4 = n4
# n6 +8 = n11
# n7+6=n10
# n8+1=n9

# Dus max = 99299513899971
# en min =  93185111127911