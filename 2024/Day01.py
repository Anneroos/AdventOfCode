with open("input01.txt") as f:
    lines = [[int(j) for j in i.split("   ")] for i in f.read().split("\n")]
list1 = sorted([k[0] for k in lines])
list2 = sorted([k[1] for k in lines])
print(f"Day 1:\n  1) {sum([abs(list1[i] - list2[i]) for i in range(len(lines))])}.")

dict1 = {}
dict2 = {}
for i in range(len(lines)):
    dict1[list1[i]] = dict1.get(list1[i], 0) + 1
    dict2[list2[i]] = dict2.get(list2[i], 0) + 1

similarity_score = 0
for key in dict1.keys():
    similarity_score += key * dict1.get(key,0) * dict2.get(key,0)
print(f"  2) {similarity_score}.")
