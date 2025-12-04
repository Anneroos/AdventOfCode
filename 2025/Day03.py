# with open("input03.txt") as f:
#     banks = f.read().split("\n")
#
# totaljoltage = 0
# for b in banks:
#     print(b)
#
#     a = [(i,int(b[i])) for i in range(len(b) - 1)]
#     print(a)
#     a.sort(key=lambda x: (-x[1], x[0]))
#     print(a)
#     firstdigit = a[0][1]
#     firstloc = a[0][0]
#     print(f"first digit {firstdigit}, first loc{firstloc}")
#     c = [(i, int(b[i])) for i in range(firstloc + 1,len(b))]
#     print(c)
#     c.sort(key=lambda x: (-x[1], x[0]))
#
#     seconddigit = c[0][1]
#     print(str(firstdigit) + str(seconddigit))
#     joltage = 10*firstdigit + seconddigit
#     totaljoltage += joltage
# print(totaljoltage)



with open("input03.txt") as f:
    banks = f.read().split("\n")

def findJoltage(banks, nr_of_batteries_per_bank):
    totaljoltage = 0
    for b in banks:
        batteries = b
        joltage = ""
        for batidx in range(nr_of_batteries_per_bank):
            a = [(i,int(batteries[i])) for i in range(len(batteries) - nr_of_batteries_per_bank + 1 + batidx)]
            a.sort(key=lambda x: (-x[1], x[0]))

            digit = str(a[0][1])
            joltage += digit
            digit_loc = a[0][0]
            # print(digit, digit_loc)
            batteries = batteries[(digit_loc+1):]
            # print( "new batteries", batteries)
        # print(joltage)

        totaljoltage += int(joltage)
    return totaljoltage
print(findJoltage(banks,2))
print(findJoltage(banks,12))