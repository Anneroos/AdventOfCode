import re
import time
time1 = time.time()
with open("input15.txt") as f:
    lines = f.read().split("\n")

sensors = []
beacons = {}
for line in lines:
    # print((line))
    matchObj = re.match(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line)
    sensorx = int(matchObj.group(1))
    sensory = int(matchObj.group(2))
    beaconx = int(matchObj.group(3))
    beacony = int(matchObj.group(4))
    dx = sensorx - beaconx
    dy = sensory - beacony
    d = abs(dx) + abs(dy) # max distance between sensor and beacon
    sensors.append({"sensorx": sensorx, "sensory": sensory, "beaconx":beaconx, "beacony":beacony, "d": d})
    beacons[(beaconx,beacony)] = 1
# just sort it already a bit
sensors = sorted(sensors, key=lambda sensor: sensor["sensorx"])
beacons = sorted(beacons, key=lambda beacon: beacon[0])

# ---- part 1 -----
# Only save x values incavex for the given y value
cavex = {}
y = 2000000
for sensor in sensors:
    sensorx = sensor["sensorx"]
    sensory = sensor["sensory"]
    beaconx = sensor["beaconx"]
    beacony = sensor["beacony"]
    d = sensor["d"]
    if beacony == y:
        cavex[beaconx] = "B"
    dy = abs(y-sensory) # y-distance from sensor to given y-line
    if d-dy >= 0:
        dx = d - dy # How much we can still move in x direction
        for x in range(sensorx - dx, sensorx + dx + 1):
            if x not in cavex: # If there is already a beacon at this point, don't overwrite it
                cavex[x] = "#"

time2 = time.time()

print(f"Day 15:\n1) In the row where y=2000000, there are {len([k for k in cavex if cavex[k] == '#'])} positions that cannot contain a beacon. Calculation took {time2-time1} seconds.")
# ------------ part 2 -----------------

size = 4000000
checks = 0
possiblePoint = ()
for y in range(size+1):
    xs = []
    for sensor in sensors:
        dy = abs(y-sensor["sensory"])
        d = sensor["d"]
        if dy <= d:
            x = [sensor["sensorx"] - (d-dy), sensor["sensorx"] + (d-dy)]
            xs.append(x)
            checks += 1
    xs = sorted(xs)
    checkx = 0
    for rangex in xs:
        while rangex[0] > checkx :
            possiblePoint = (checkx, y)
            if possiblePoint in beacons:
                checkx += 1
            else:
                break
        checkx = max(rangex[1]+1,checkx)
time2 = time.time()
print(f"2) The only position for the distress beacon is {possiblePoint}, with a tuning frequency of {4000000*possiblePoint[0] + possiblePoint[1]}. Calculation took {time2-time1} seconds.")


