# 14-12-2020
text_file = open("input2.txt", "r")
lines = text_file.read().split('\n')
text_file.close()

totalPaperNeeded = 0
totalRibbonNeeded = 0
for line in lines:
    dimensions = [int(i) for i in line.split('x')]
    print(dimensions)
    bottom = dimensions[0]*dimensions[1]
    side = dimensions[0]*dimensions[2]
    front = dimensions[1]*dimensions[2]
    slack = min(bottom,side,front)
    paperNeeded = 2*bottom + 2*side + 2*front + slack
    totalPaperNeeded += paperNeeded
    ribbonWrap = 2*min(dimensions[0]+dimensions[1],dimensions[1]+dimensions[2],dimensions[0]+dimensions[2])
    volume = dimensions[0]*dimensions[1]*dimensions[2]
    ribbonNeeded = ribbonWrap + volume
    totalRibbonNeeded += ribbonNeeded
print(f"The elves need {totalPaperNeeded} square feet of paper and {totalRibbonNeeded} feet of ribbon.")