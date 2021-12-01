input = [5	,1	,10,	0,	1,	7,	13,	14,	3,	12,	8,	10,	7,	12,	0,	6]
#input = [0,2,7,0] # test input
print(input)
import numpy as np


array = np.array(input)
length = len(array)
print(array)
# not so pretty met de 10000, but oh well...
arrayOfArrays = np.zeros(shape=(10000,length))
for i in range(10000):
    #print("iteratie ", i)
    idx = array.argmax()
    maxval = array[idx]
    array[idx]=0
    rest = maxval % length
    division = int((maxval-rest)/length)
    array += division
    #print("index =", idx, " , division =",division, ", rest =", rest, ", length =", length ,", rest+idx-length =",rest+idx-length)
    if idx+rest >= length:
        array[(idx + 1):length] += 1

        array[0:rest+idx-length+1] +=1
    else:
        array[idx+1:idx+rest+1] += 1

    # list of boolean values of which rows of arrayOfArrays are equal to array
    result = np.equal(arrayOfArrays, array).all(1)


    if(any(result)):
        print(i)
        winIdx = [index for index, x in enumerate(result) if x][0]
        print("Stopped after ", i + 1, "iterations. Have seen input before at ", winIdx, "so one cycle is ",
              (i - winIdx), "long")
        break
    else:
        arrayOfArrays[i] = array






