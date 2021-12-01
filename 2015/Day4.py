# 14-12-2020
import hashlib
input = 'yzbqklnj'
# part 1
i =0
while True:
    currentinput = input+str(i)
    result = hashlib.md5(currentinput.encode()).hexdigest()
    if str(result[0:5]) == "00000":
        print(f"Day 4 part 1: {i}")
        break
    i += 1
# part 2
i =0
while True:
    currentinput = input+str(i)
    result = hashlib.md5(currentinput.encode()).hexdigest()
    if str(result[0:6]) == "000000":
        print(f"Day 4 part 2: {i}")
        break
    i += 1