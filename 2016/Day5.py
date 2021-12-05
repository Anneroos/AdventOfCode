# 05-12-2021
input="ffykfhsq"
import hashlib
password1 = ""
password2 = {}
index = 0
goodDigits = [str(i) for i in range(8)]
while len(password1) < 8 or len(password2.keys()) < 8:
    temp = hashlib.md5((input+ str(index)).encode('utf-8')).hexdigest()
    if temp[0:5] == "00000":
        temp5 = temp[5]
        if len(password1) < 8: # part 1
            password1 += temp5
        if temp5 in goodDigits and temp5 not in password2.keys(): # part 2
            password2[temp5] = temp[6]
    index += 1
print(f"Part 1: Pasword: {password1}.")

password2final = [""]*8
for key in password2.keys():
    password2final[int(key)] = password2[key]

print(f"Part 2: Pasword: {''.join(password2final)}. ")