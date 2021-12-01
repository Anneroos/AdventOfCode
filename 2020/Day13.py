import math
currentTime=1005526
input = "37,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,x,x,x,587,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,13"#,19,x,x,x,23,x,x,x,x,x,29,x,733,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,17"
busesTimeList = input.split(",")

buses = [ int(i) for i in busesTimeList if i != "x"]

minTimeToWait = max(buses)
for bus in buses:
    timeToWait = bus-(currentTime%bus)
    if timeToWait < minTimeToWait:
        minTimeToWait = timeToWait
        winningBus = bus
print(f"Part 1: The first bus to arrive is bus {winningBus}, it will arrive in {minTimeToWait}. So the answer is {minTimeToWait*winningBus}.")

# Part 2
# When which bus should arrive
busesDict = {}
for i in range(len(busesTimeList)):
    bus = busesTimeList[i]
    if bus != 'x':
        busesDict[int(bus)] = i


N = 1
for bus in buses:
    N = N*bus
# print(math.prod(buses))

print(f"N is {N}")

def EuclidExtended(a,b):
    old_r = a
    r = b
    old_s = 1
    s = 0
    old_t = 0
    t = 1
    while r != 0:
        quotient = (old_r // r)

        (old_r, r) = (r, old_r - quotient * r)
        (old_s, s) = (s, old_s - quotient * s)
        (old_t, t) = (t, old_t - quotient * t)
    return old_s, old_t

sum = 0
for bus in buses:
    Nrest = int(N/bus)
    print(Nrest)
    (r,s) = EuclidExtended(bus,Nrest)
    print(r*bus + s*Nrest)
    e = s * Nrest
    a = - busesDict[bus]
    print(a,e,r,s)
    sum += a * e
print(sum)
print(sum % N)
print(busesDict)
