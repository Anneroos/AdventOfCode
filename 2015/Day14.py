# 19-12-2020
with open("input14.txt") as file:
    lines = file.read().split("\n")


timeToTravel=2503
maxDistance = 0
fastestReindeer = ""
for line in lines:
    a = line.split(" ")
    reindeer = a[0]
    speed = int(a[3])
    flytime = int(a[6])
    resttime = int(a[13])
    cycletime = flytime + resttime
    cycles = timeToTravel // cycletime
    rest = timeToTravel % cycletime
    distance = cycles * (flytime*speed) + min(rest,flytime)*speed

    if distance > maxDistance:
        maxDistance = distance
        fastestReindeer = reindeer
print(f"Day 14 part 1: Reinder {fastestReindeer} is the fastest, and travels {maxDistance} km in {timeToTravel} seconds.")

# re.search("(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for 53 seconds.

# Part 2: initliaze a dictionairy with info about the reindeer
reindeers = {}
maxDistance = 0
fastestReindeer = ""
for line in lines:
    a = line.split(" ")
    reindeer = a[0]
    speed = int(a[3])
    flytime = int(a[6])
    resttime = int(a[13])
    reindeers[reindeer] = {"speed": speed, "flytime": flytime, "timeFlown" : 0, "resttime": resttime, "timeRested" : 0, "state": "fly", "score":0, "distance":0}

# Now loop 2053 times, and compute scores. :)
for i in range(timeToTravel):
    winners = []
    winningDistance = 0
    for name in reindeers.keys():
        reindeer = reindeers[name]
        # Move or rest
        if reindeer["state"] == "fly":
            reindeer["distance"] += reindeer["speed"]
            reindeer["timeFlown"] += 1
            if reindeer["timeFlown"] >= reindeer["flytime"]:
                reindeer["state"] = "rest"
                reindeer["timeRested"] = 0
        elif reindeer["state"] == "rest":
            reindeer["timeRested"] += 1
            if reindeer["timeRested"] >= reindeer["resttime"]:
                reindeer["state"] = "fly"
                reindeer["timeFlown"] = 0
        # now every reindeer has moved, compute who is winning
        if reindeer["distance"] > winningDistance:
            winningDistance = reindeer["distance"]
            winners = [name]
        elif reindeer["distance"] == winningDistance:
            winners.append(name)
    # award points to the winners of this round
    for name in winners:
        reindeers[name]["score"] += 1


winningScore = 0
winner = ""
for name in reindeers.keys():
    if reindeers[name]["score"] > winningScore:
        winningScore = reindeers[name]["score"]
        winner = name
print(f"Day 14 part 2: According to the new rules {winner} has won with {winningScore} points!")