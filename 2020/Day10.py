text_file = open("input10.txt", "r")
numbers = text_file.read().split('\n')
text_file.close()
numbers = [int(i) for i in numbers]
numbers = sorted(numbers)

currentJolt = 0
differences ={1:0,2:0,3:0}
for i in numbers:
    diff = i - currentJolt
    differences[diff] += 1
    currentJolt = i

differences[3] += 1
print(f"Antwoord op vraag 1 van vraag 10: {differences[3]*differences[1]}.")
# part 2



numbers = [0] + numbers

count_per_list = {}

def count_combinations(list):
    if len(list) == 1:
        return 1
    elif len(list) >=3 and list[2]-list[0] <= 3:
        if tuple([list[0]]+list[2:]) in count_per_list.keys():
            count_skip = count_per_list[tuple([list[0]] + list[2:])]
        else:
            count_skip =  count_combinations([list[0]] + list[2:])
            count_per_list[tuple([list[0]] + list[2:])] = count_skip
        if tuple(list[1:]) in count_per_list.keys():
            count_take = count_per_list[tuple(list[1:])]
        else:
            count_take = count_combinations(list[1:])
            count_per_list[tuple(list[1:])] = count_take
        return count_skip + count_take
    else:
        if tuple(list[1:]) in count_per_list.keys():
            count_take = count_per_list[tuple(list[1:])]
        else:
            count_take = count_combinations(list[1:])
        return count_take

print(f"Er zijn {count_combinations(numbers)} combinaties mogelijk!")

# # Sander
# from collections import defaultdict
# my_joltage = max(numbers)+3
# pos = defaultdict(int)
# pos[0] = 1
# for num in numbers + [my_joltage]:
#     for d in [1,2,3]:
#         pos[num] += pos[num-d]
# print(pos[my_joltage])
