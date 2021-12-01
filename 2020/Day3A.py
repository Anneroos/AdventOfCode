text_file = open("input3.txt", "r")
input = text_file.read().split('\n')
text_file.close()
width = len(input[0])
trees = 0
for i in range(len(input)):
    index = 3*i % width
    if input[i][index] == "#":
        trees += 1
print("There are", trees, "trees in this direction!")