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

func_dict  = {'addr':addr,'addi': addi,'mulr': mulr,'muli':muli,'banr': banr,'bani':bani,'borr':borr,'bori':bori,'setr':setr,'seti':seti,
              'gtir': gtir,'gtri':gtri, 'gtrr': gtrr, 'eqir': eqir,'eqri': eqri, 'eqrr': eqrr}
print(func_dict)

import numpy as np
import pandas as pd

lines = pd.read_csv("adventOfCodeInput19.txt", sep=' ', header=None, engine='python', skiprows = 1)
# lines = lines[0:7]
lines.columns = ['func','A', 'B', 'C' ]


lines = lines.astype({"B": int, "A": int, 'C': int})
print(lines)


text_file = open("adventOfCodeInput19.txt", "r")
input = text_file.read().split('\n')
text_file.close()
ipregister = int(np.array(input)[0].split(' ')[1])

print(ipregister)


register = np.array([1,0,0,0,0,0],dtype='int64')
count = 0
ip = 0
while ip < len(lines):
    func, A,B,C = lines.loc[ register[ipregister]]

    # print('ip', ip)

    # print('before:', register)
    register = func_dict[func](A,B,C,register)
    register[ipregister] += 1

    count += 1
    if count % 100000 == 0:
        print(count)
        print(register)
    # print(func, A, B, C)
    # print('result:', register)

print(register)
# puzzle 1 day 19: 2304

# [       0        0 10550400 10551330        1        1]