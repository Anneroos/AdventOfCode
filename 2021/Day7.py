with open("input7.txt", "r") as f: numbers = [int(i) for i in f.read().split(",")]
minfuel1 = int(min([sum([abs(k-i) for k in numbers]) for i in range(min(numbers),max(numbers))]))
minfuel2 = int(min([sum([abs(k-i)*(abs(k-i)+1)/2 for k in numbers]) for i in range(min(numbers),max(numbers))]))
print(f"Part 1: They must spend {minfuel1} to align. \nPart 2: They must spend {minfuel2} to align.")

#Alternative for part 1: Median!
import statistics
med = statistics.median(numbers)
print(f"Alternative method for Part 1: They must spend {sum([int(abs(k-med)) for k in numbers])} to align.")