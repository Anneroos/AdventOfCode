import re
import math
import copy

with open("input19.txt") as f:
    lines = f.read().split("\n")
Blueprints = []
for line in lines:
    linestring = "Blueprint (d+)\: Each ore robot costs (d+) ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."

    matchObj = re.match(r'^Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.$', line)
    
    # blueprintnr = int(matchObj.group(1))

    # orerobotcost = (int(matchObj.group(2)), 0, 0)
    # clayrobotcost = (int(matchObj.group(3)), 0, 0)
    # obsidianrobotcost = (int(matchObj.group(4)),  int(matchObj.group(5)), 0)
    # geoderobotcost = (int(matchObj.group(6)), 0, int(matchObj.group(7)))
    # blueprinttuple = (orerobotcost, clayrobotcost, obsidianrobotcost, geoderobotcost, blueprintnr)
    blueprint = {"name": int(matchObj.group(1)),
                 "ore": {"ore":int(matchObj.group(2)), "clay": 0, "obsidian":0},
                 "clay": {"ore": int(matchObj.group(3)), "clay": 0, "obsidian": 0},
                 "obsidian": {"ore": int(matchObj.group(4)), "clay": int(matchObj.group(5)), "obsidian": 0},
                 "geode": {"ore": int(matchObj.group(6)), "clay": 0, "obsidian": int(matchObj.group(7))}
                 }
    Blueprints.append(blueprint)


class robotState():
    def __init__(self, blueprint, minutes):
        self.bp = blueprint
        self.minutes = minutes #?
        self.resources = {"ore": 0, "clay": 0, "obsidian":0, "geode":0}
        self.robots = {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0}
        self.maxNeeded = {}
        for res in ["ore", "clay", "obsidian" ]:
            self.maxNeeded[res] = max([self.bp[rob][res] for rob in self.robots])
        print(self.maxNeeded)
        self.history = []
        # self.listOfRobots = listOfRobots
    def computeNextSteps(self):
        bestPossibleScore = self.resources["geode"] + self.minutes*self.robots["geode"] + self.minutes*(self.minutes-1)/2
        if bestPossibleScore < bestGeodeScore:
            self.finishTime()
            geodeScore = self.resources["geode"]
            # finishedRobots.append(self)
            return geodeScore
        else:
            copiesMade = 0
            for robottype in self.robots:
                if robottype == "geode" or not self.resources[robottype] + self.minutes*self.robots[robottype] >= self.minutes * self.maxNeeded[robottype]:
                    T = self.computeTimeToWaitForNextRobot(robottype)
                    if T < self.minutes:
                        self.makeCopy(T+1, robottype)
                        copiesMade += 1
            if copiesMade == 0:
                self.finishTime()
                geodeScore = self.resources["geode"]
                # finishedRobots.append(self)
                return geodeScore
            else:
                return -1

    def finishTime(self):
        for res in self.robots:
            self.resources[res] += self.minutes*self.robots[res]
        self.minutes = 0
    def computeTimeToWaitForNextRobot(self, robottype):
        needs = self.bp[robottype]
        minTime = -1

        for res in needs:
            if needs[res] >0:
                if self.robots[res] == 0:
                    minTime = self.minutes
                else:
                    T = math.ceil((needs[res] - self.resources[res] )/ self.robots[res])
                    if T >= minTime:
                        minTime = T
                # print(f"robottype {robottype}, resource {res},mintime{minTime}, T {T}. self.robots[res] {self.robots[res]}, needs[res] {needs[res]},self.resources[res] {self.resources[res]}")
        # print(f"Final mintime {minTime}")
        minTime = self.minutes if minTime == -1 else minTime #max(1, minTime)
        return minTime

    def makeCopy(self, T, robottype):
        newRobotState = copy.deepcopy(self)
        # Get new resources from the robots
        for res in newRobotState.robots:
            newRobotState.resources[res] += T*newRobotState.robots[res]
        # Add a new robot
        newRobotState.robots[robottype] += 1
        # Pay for the new robot
        # print("Paying! old resources, after adding from robots", newRobotState.resources)
        for res in self.bp[robottype]:
            newRobotState.resources[res] -= newRobotState.bp[robottype][res]
        # print( "after paying", newRobotState.resources)
        newRobotState.minutes -= T
        newRobotState.history.append([newRobotState.minutes, robottype, T, copy.deepcopy(newRobotState.robots), copy.deepcopy(newRobotState.resources)])
        # print("minutes left for new robot", newRobotState.minutes)
        robotList.append(newRobotState)
#
# # Part 1
# qualityLevels = []
# for bp in Blueprints:
#     print("Blueprint:", bp)
#     r = robotState(bp,24)
#     robotList = [r]
#     bestGeodeScore = 0
#     bestPath = None
#     finishedRobots = []
#     while len(robotList) > 0:
#         rob = robotList.pop()
#         geodeScore = rob.computeNextSteps()
#         if geodeScore >= bestGeodeScore:
#             bestGeodeScore = geodeScore
#             bestPath = rob.history
#     print(f"QUality level = {bp['name'] * bestGeodeScore}, Best Geode score for this blueprint {bp['name']} is {bestGeodeScore}")
#     qualityLevels.append(bp["name"] * bestGeodeScore)
# print(qualityLevels)
# print(sum(qualityLevels))


# Part 2
geodeScores = []
for bp in Blueprints[:3]:
    print("Blueprint:", bp)
    r = robotState(bp,32)
    robotList = [r]
    bestGeodeScore = 0
    bestPath = None
    finishedRobots = []
    while len(robotList) > 0:
        rob = robotList.pop()
        geodeScore = rob.computeNextSteps()
        if geodeScore >= bestGeodeScore:
            print("new highscore!", geodeScore)
            bestGeodeScore = geodeScore
            bestPath = rob.history
    print(f"Quality level = {bp['name'] * bestGeodeScore}, Best Geode score for this blueprint {bp['name']} is {bestGeodeScore}")
    geodeScores.append(bp["name"] * bestGeodeScore)

print(geodeScores)
print(math.prod(geodeScores))
# 12240 too high!