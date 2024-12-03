import re
myregex = r"(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don't\(\))"
with open("input03.txt") as txt:
    memory = txt.read()
matches = re.findall(myregex, memory)
enabled = True
total1 = 0
total2 = 0
for match in matches:
    if match[0] != '':
        numbers = [int(i) for i in match[0][4:-1].split(",")]
        total1 += numbers[0] * numbers[1]
        if enabled:
            total2 += numbers[0] * numbers[1]
    if match[1] != '':
        enabled = True
    if match[2] != '':
        enabled = False
print(total1)
print(total2)
