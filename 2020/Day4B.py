text_file = open("input4.txt", "r")
input = text_file.read().split('\n')
text_file.close()
import re

currentPassport = ""
passportsStrings = []
for line in input:
    if len(line) == 0:
        currentPassport += " "
        passportsStrings.append(currentPassport)
        currentPassport = ""
    else:
        currentPassport += " " + line

mandatory = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
eyecolors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

passports = []
for passport in passportsStrings:
    currentPassport = {}
    valid = True
    for key in mandatory:
        m = re.search(key+":([#\w\d]+)\s", passport)
        if m:
            currentPassport[key] = m.group(1)
        else:
            valid = False
    currentPassport["valid"] = valid
    passports.append(currentPassport)

validPassports = 0
for passport in passports:
    if passport["valid"]:
        byr = int(passport["byr"])
        if not(byr>= 1920 and byr <= 2002):
            passport["valid"] = False
            print("Birth year not valid:", byr)

        iyr = int(passport["iyr"])
        if not (iyr >= 2010 and iyr <= 2020):
            passport["valid"] = False
            print("Issue year not valid:", iyr)

        eyr = int(passport["eyr"])
        if not (eyr >= 2020 and eyr <= 2030):
            passport["valid"] = False
            print("Expiration year not valid:", eyr)

        hgt = passport["hgt"]
        m = re.search("(\d+)(\w{2})$", hgt)
        if m:
            nr  = int(m.group(1))
            type = m.group(2)
            if type not in ["cm","in"] or (type == "cm" and not (nr >= 150 and nr <= 193)) or (type == "in" and not (nr >= 59 and nr <= 76)):
                print("Height not valid:", hgt)
                passport["valid"] = False
        else:
            print("No valid height", hgt)
            passport["valid"] = False

        hcl = passport["hcl"]
        m = re.search("(#[a-fA-F\d]{6})$", hcl)
        if not m:
            print("No valid hair color", hcl)
            passport["valid"] = False

        ecl = passport["ecl"]
        if ecl not in eyecolors:
            print("Eye color not valid:", ecl)
            passport["valid"] = False

        pid = passport["pid"]
        if len(pid) != 9 or not pid.isnumeric():
            print("Not a valid passport ID", pid)
            passport["valid"] = False

for passport in passports:
    if passport["valid"]:
        validPassports += 1

print("From the", len(passports), "passports, there are", validPassports, "passports with the 7 mandatory fields that have the right form.")