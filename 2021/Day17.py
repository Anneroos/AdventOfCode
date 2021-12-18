x1, x2, y1, y2 = 139, 187, -148, -89
def computeTrajectory(vx,vy):
    x, y, vx, vy, maxy = 0, 0, vx, vy, 0
    while vy >= 0 or y >= y1:
        x += vx
        y += vy
        vx = max(vx-1,0)
        vy -= 1
        maxy = max(maxy, y)
        if x1 <= x and x <= x2 and y1<= y and y <= y2:
            return True, maxy
        if y < y1 or x > x2:
            break
    return False, 0
highest, total = 0, 0
for vx in range(x2+1):
    print(vx)
    if vx*(vx+1)/2 < x1:
        continue
    for vy in range(y1,abs(y1)+1):
        b, maxy = computeTrajectory(vx, vy)

        if b:
            total += 1
            highest = max(maxy, highest)
print(f"Part 1: The highest point that is possible in a feasible trajectory is {highest}.")
print(f"Part 2: The total number of possible trajectories is {total}.")