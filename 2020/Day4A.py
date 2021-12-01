text_file = open("input4.txt", "r")
input = text_file.read().split('\n')
text_file.close()
import re

currentPassport = ""
passports = []
for line in input:
    if len(line) == 0:
        passports.append(currentPassport)
        currentPassport = ""
    else:
        currentPassport += " " + line
mandatory = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] #, "cid"]

validPassports = 0
for passport in passports:
    valid = True
    for info in mandatory:
        m = re.search('('+ info + ':)', passport)
        if not m:
            valid = False
            break
    if valid:
       validPassports += 1
print("There are", validPassports, "passports with the 7 mandatory fields.")

