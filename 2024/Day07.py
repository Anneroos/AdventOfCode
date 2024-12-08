with open("input07.txt") as f:
    lines = f.read().split("\n")

total_calibration_result1 = 0
total_calibration_result2 = 0
for line in lines:
    test_value, numbers = line.split(": ")
    test_value = int(test_value)
    numbers = [int(i) for i in numbers.split(" ")]
    # print(test_value, numbers)
    values1 = [numbers.pop(0)]
    values2 = values1.copy()
    # print(values1)
    while numbers:
        n = numbers.pop(0)
        values1 = set([i + n for i in values1] + [j * n for j in values1])
        values2 = set([i + n for i in values2] + [j * n for j in values2] + [int(str(k) + str(n)) for k in values2])
        # print(values1)

    if test_value in values1:
        total_calibration_result1 += test_value
    if test_value in values2:
        total_calibration_result2 += test_value

print(total_calibration_result1)
print(total_calibration_result2)
