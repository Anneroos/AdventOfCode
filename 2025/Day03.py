with open("2025/input03.txt") as f:
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
print(f"Day 3:\n  1) {findJoltage(banks,2)}")
print(f"  2) {findJoltage(banks,12)}")