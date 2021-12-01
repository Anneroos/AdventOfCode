import pandas as pd
import numpy as np

#file = pd.read_csv(r"C:\Users\Anneroos/PycharmProjects/MijnEersteProject/testinput2.txt", sep=' ', header=None)
file = pd.read_csv(r"C:\Users\Anneroos/PycharmProjects/MijnEersteProject/puzzleinput2.txt", sep='\t',  header=None)

maxperrow = file.max(axis=1)
minperrow = file.min(axis=1)
diff = maxperrow -minperrow

answer = sum(diff)
print("Het antwoord op vraag 1 van dag 2 is ", answer)



#file2 =file.copy()*0 -1 # dataframe with only -1's

#booleantable = file < 0  # weird way to make FALSE table?
#print(booleantable)
#for i in range(1):
#    temp = file %file[i] == 0
#    print("% dingen")
#    print(file %file[i])
#    print(file[i])
#    print(temp)
#    file2[temp] = "** " + str(i)
#    booleantable = (booleantable)|(temp)

file3 = file.copy()*0
for i in range(16):
    for j in range(16):
        for k in range(16):
            if k != j and (file.loc[i,j] % file.loc[i,k] == 0):
                file3.loc[i,j] = int(file.loc[i,j]/file.loc[i,k])
#print(file3)
print("Het antwoord op vraag 2 van dag 2 is ", file3.sum().sum())


def rijoperator(row):
    for i in range(len(row)):
        for j in range(len(row)):
            if i!= j and row[i]%row[j] ==0:
                return int(row[i]/row[j])



print("Op een andere manier vind ik ook ", file.apply(rijoperator, axis=1).sum())




