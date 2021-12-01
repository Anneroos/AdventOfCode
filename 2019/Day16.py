import numpy as np
import math
import matplotlib.pyplot as plt

input16 = "59758034323742284979562302567188059299994912382665665642838883745982029056376663436508823581366924333715600017551568562558429576180672045533950505975691099771937719816036746551442321193912312169741318691856211013074397344457854784758130321667776862471401531789634126843370279186945621597012426944937230330233464053506510141241904155782847336539673866875764558260690223994721394144728780319578298145328345914839568238002359693873874318334948461885586664697152894541318898569630928429305464745641599948619110150923544454316910363268172732923554361048379061622935009089396894630658539536284162963303290768551107950942989042863293547237058600513191659935"
length = len(input16)  # 6500000
phase0 = np.zeros(length)
for i in range(length):
    phase0[i] = int(input16[i])

print("SOM", phase0.sum(),np.sum(phase0))
matrix = np.zeros((length,length))
pattern = [0,1,0,-1]
patternLength = len(pattern)
for k in range(length): # welke rij
    for m in range(length): # welke kolom
        matrix[k][m] = pattern[(math.floor((m+1)/(k+1))%patternLength)]
phase = phase0.copy()
for i in range(100):
    product = np.dot(matrix,phase)
    phase = np.mod(np.abs(product),10)
print("puzzle 1 ",phase[:8])

# PUZZLE 2?

location = 5975803
input16 = input16*10000
# print(input16)
length = len(input16)  # 6500000
print(length)

length = length - location
phase0 = np.zeros(length)
for i in range(length):
    phase0[i] = int(input16[location + i])



test = np.ones(length)
print(test)
for cykel in range(99):
    print(cykel)
    for i in range(1,length):
        test[i] = (test[i-1] + test[i])%10
print(test)



for i in range(8):
    print("Digit", i, "is", (np.dot(test,phase0)%10))
    phase0[0:length-1] = phase0[1:]
    phase0[length-1] = 0