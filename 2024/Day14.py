import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

with open("input14.txt") as f:
    input = f.read().split("\n")
w = 101
h = 103
# w = 11
# h = 7
robots = []
for line in input:
    p,v = [k.split("=")[1] for k in line.split(" ")]
    p = [int(i) for i in p.split(",")]
    v = [int(i) for i in v.split(",")]
    robots.append({"p": p, "v":v})

def moveRobots(robotarray, time):
    newrobotarray = []
    for r in robotarray:
        newrobotarray += [{"p": [(r["p"][0] + time * r["v"][0]) % w, (r["p"][1] + time * r["v"][1]) % h], "v": r["v"]}]
    return newrobotarray

quadrants = [0,0,0,0]
robotsAfter100s = moveRobots(robots, 100)
for robot in robotsAfter100s:
    x = robot["p"][0]
    y = robot["p"][1]
    if x < (w-1)/2:
        if y < (h-1)/2:
            quadrants[0] += 1
        elif y > (h-1)/2:
            quadrants[2] += 1
    elif x > (w-1)/2:
        if y < (h - 1) / 2:
            quadrants[1] += 1
        elif y > (h - 1) / 2:
            quadrants[3] += 1

score = 1
for q in quadrants:
    score = score*q
print(f"Day 14:\n  1) {score}.")
print(f"  2) Let's look at this animation.")
# My answer is 7916

def robotsAsMatrix(robotarray):
    ar = []
    for i in range(h):
        line = []
        for j in range(w):
            nr = [r["p"] for r in robotarray].count([j,i])
            line += [nr] if nr > 0 else [0]
        ar += [line]
    return ar

def updateRobotPositions(i):
    # I noticed that at 38 and 139 the points sort of align. So let's look only at 38 + 101*i
    # Then I also noticed it takes a while, so skip 70*101+38 seconds ahead ;)
    time = 38 + 101*(i+70)
    M = robotsAsMatrix(moveRobots(robots, time))
    matrix.set_array(M)
    frame_text.set_text(f"Frame: {time}")  # Update the frame number display

M=np.array(robotsAsMatrix(robots))


fig, ax = plt.subplots()
matrix = ax.matshow(M)
plt.colorbar(matrix)

ani = animation.FuncAnimation(fig, updateRobotPositions, frames=20, interval=50)
frame_text = ax.text(0.05, 1.05, "Frame: 0", transform=ax.transAxes, fontsize=20, color='black')
plt.show()

# I made use of this code to help me animate a matrix
# https://stackoverflow.com/questions/41827109/funcanimation-with-a-matrix

