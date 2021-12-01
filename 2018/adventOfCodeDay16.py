import numpy as np

def addr(A,B,C,inputregister):
    register = inputregister.copy()
    register[C] = register[A] + register[B]
    return register

def addi(A,B,C,inputregister):
    register = inputregister.copy()
    register[C] = register[A] + B
    return register

def mulr(A,B,C,inputregister):
    register = inputregister.copy()
    register[C] = register[A] * register[B]
    return register

def muli(A,B,C,inputregister):
    register = inputregister.copy()
    register[C] = register[A] * B
    return register

def banr(A,B,C,inputregister):
    register = inputregister.copy()
    register[C] = register[A] & register[B]
    return register

def bani(A,B,C,inputregister):
    register = inputregister.copy()
    register[C] = register[A] & B
    return register

def borr(A,B,C,inputregister):
    register = inputregister.copy()
    register[C] = register[A] | register[B]
    return register

def bori(A,B,C,inputregister):
    register = inputregister.copy()
    register[C] = register[A] | B
    return register

def setr(A,B,C,inputregister):
    register = inputregister.copy()
    register[C] = register[A]
    return register

def seti(A,B,C,inputregister):
    register = inputregister.copy()
    register[C] = A
    return register

def gtir(A,B,C,inputregister):
    register = inputregister.copy()
    register[C] = int(A > register[B])
    return register

def gtri(A,B,C,inputregister):
    register = inputregister.copy()
    register[C] = int(register[A] > B)
    return register

def gtrr(A,B,C,inputregister):
    register = inputregister.copy()
    register[C] = int(register[A] > register[B])
    return register

def eqir(A,B,C,inputregister):
    register = inputregister.copy()
    register[C] = int(A == register[B])
    return register

def eqri(A,B,C,inputregister):
    register = inputregister.copy()
    register[C] = int(register[A] == B)
    return register

def eqrr(A,B,C,inputregister):
    register = inputregister.copy()
    register[C] = int(register[A] == register[B])
    return register

func_list  = [addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr]




def checkall(A,B,C,inputregister,output):
    # results1 =  [func(A,B,C,inputregister) for func in func_list]
    # print(results1)
    results = np.array( [output == func(A, B, C, inputregister) for func in func_list])

    # nrOfTrue2 = 0
    # for func in func_list:
    #     result =  func(A, B, C, inputregister)
    #     if output == result:
    #         nrOfTrue2 += 1
    #     print(output, result, output== result)

    nrOfTrue = results.sum()
    # if(nrOfTrue != nrOfTrue2):
    #     print('NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')
    return results, nrOfTrue






text_file = open("adventOfCodeInput16.txt", "r")

input = text_file.read().split('\n')
input1 = input[0:3003]
input2 = input[3006:]
text_file.close()
lines = np.array(input1)
# print(lines)

count = 0

opcodeMatrix = np.ones([16,16]).astype(int)
for row in range(len(lines)):
    text = lines[row]

    if row % 4 == 0:
        input = np.array(text.replace(':',',').replace('[','').replace(']','').split(',')[1:]).astype(int).tolist()
    if row % 4 == 1:
        [opcode, A,B,C] = np.array(text.split(' ' )).astype(int)[:]

    if row % 4 == 2:
        outputregister = np.array(text.replace(':', ',').replace('[', '').replace(']', '').split(',')[1:]).astype(int).tolist()
    if row % 4 == 3:
        results, nrOfTrue = checkall(A, B, C, input, outputregister)
        # print('-----',opcode,'---', A,B,C,'---' ,input, outputregister, '-----')
        results = results.astype(int)
        # print(results)
        # print('matrix row was')
        # print(opcodeMatrix[opcode,:])
        opcodeMatrix[opcode,:] = opcodeMatrix[opcode,:]*results

        # print("result:")
        # print(opcodeMatrix[opcode, :])

        if nrOfTrue >= 3:
            count += 1

print("Answer puzzle 1 dau 16:",count)
print("Matrix")
print(opcodeMatrix)

resultaat = [8,15,11,3,13,6,7,2,12,9,4,14,0,10,1,5]

print(input2)



puzzleregister = [0,0,0,0]
for i in range(len(input2)):
    [opcode,A,B,C] = np.array(input2[i].split(' ')).astype(int)
    print(i)
    print(opcode,A,B,C)
    puzzleregister = func_list[opcode](A,B,C,puzzleregister)
    print(puzzleregister)

print(puzzleregister)