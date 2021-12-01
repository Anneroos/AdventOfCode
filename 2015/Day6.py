# 14-12-2020
import numpy as np
import matplotlib.pyplot as plt
import re

text_file = open("input6.txt", "r")
lines = text_file.read().split('\n')
text_file.close()

lights1 = np.zeros([1000,1000])
lights2 = np.zeros([1000,1000])

for line in lines:
    m = re.search('([\w\s]+) (\d+),(\d+) through (\d+),(\d+)$', line)
    command = m.group(1)
    x1 = int(m.group(2))
    y1 = int(m.group(3))
    x2 = int(m.group(4))
    y2 = int(m.group(5))
    if command == "turn on":
        lights1[x1:x2+1,y1:y2+1] = 1
        lights2[x1:x2 + 1, y1:y2 + 1] += 1
    if command == "turn off":
        lights1[x1:x2+1,y1:y2+1] = 0
        lights2[x1:x2 + 1, y1:y2 + 1] -= 1
        lights2[lights2 == -1] = 0
    if command == "toggle":
        lights1[x1:x2+1,y1:y2+1] =  1- lights1[x1:x2+1,y1:y2+1]
        lights2[x1:x2 + 1, y1:y2 + 1] += 2

print(f"Day 6 part 1: there are {int(lights1.sum())} ligths lit.")
print(f"Day 6 part 2: the total brightness is {int(lights2.sum())}.")


fig = plt.figure(figsize=(6, 3.2))

# ax = fig.add_subplot(111)
# ax.set_title('colorMap')
plt.imshow(lights2)
# ax.set_aspect('equal')
#
# cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
# cax.get_xaxis().set_visible(False)
# cax.get_yaxis().set_visible(False)
# cax.patch.set_alpha(0)
# cax.set_frame_on(False)
# plt.colorbar(orientation='vertical')
plt.show()

