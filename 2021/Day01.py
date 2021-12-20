 # Compact solution
import numpy as np
with open("input1.txt","r") as f:
    n=np.array([int(i) for i in f.read().split('\n')])
l=len(n)
print(sum(n[1:]-n[0:l-1]>0))  # true=1, false=0
print(sum(n[3:l]-n[0:l-3]>0)) # Only need to compare x1 with x4, etc.


#Initial solution
import numpy as np
text_file = open("input1.txt", "r")
numbers = np.array([int(i) for i in text_file.read().split('\n')])
text_file.close()
t = numbers[1:]-  numbers[0:len(numbers)-1]
print(f"Solution 1a: {sum(t>0)}")

l = len(numbers)
A = numbers[0:l-2] + numbers[1:l-1] + numbers[2:l]
print(f"Solution 1b: {sum(A[1:]-  A[0:l-3]>0)}")



