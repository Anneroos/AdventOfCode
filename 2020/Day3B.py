text_file = open("input3.txt", "r")
input = text_file.read().split('\n')
text_file.close()
width = len(input[0])
slopes = [[1,1], [3,1], [5,1], [7,1], [1,2]]
treesArray = []
for slopeIndex in range(len(slopes)):
    slope = slopes[slopeIndex]
    trees = 0
    i = 0 # horizontal
    step = 0 # vertical step index
    while i < (len(input)):
        index = slope[0]*step % width # which horizontal position
        if input[i][index] == "#":
            trees += 1
        i += slope[1]
        step += 1
    treesArray.append(trees)
totalTrees = 1
for i in range(len(treesArray)):
    totalTrees = totalTrees*treesArray[i]
print("The number of trees for each slope are", treesArray, "and their product is" ,totalTrees, ".")