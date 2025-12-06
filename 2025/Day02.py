import math
with open("2025/input02.txt") as f:
    ranges = [[int(t) for t in r.split("-")] for r in f.read().split(",")]
max_range = max([r[1] for r in ranges])
length_max_range = len(str(max_range))
max_pattern_length = math.floor(len(str(max_range))/2)
invalid_ids_1 = []
invalid_ids_2 = []
for pattern in range(1,10**max_pattern_length):
    pattern_length = len(str(pattern))
    max_repetition = math.floor(length_max_range/pattern_length)
    for rep in range(2, max_repetition + 1):
        number = int(str(pattern)*rep)
        invalid = False
        for r in ranges:
            if number in range(r[0],r[1]+1):
                invalid = True
                break
        if invalid:
            if rep == 2:
                invalid_ids_1.append(number)
            invalid_ids_2.append(number)

print(f"Day 2:\n  1) {sum(set(invalid_ids_1))}")
print(f"  2) {sum(set(invalid_ids_2))}")