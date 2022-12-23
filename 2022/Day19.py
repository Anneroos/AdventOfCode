# Quite a slow program, but it does the job.
# I have gotten some ideas from Reddit:
# - check decisions (which robots to make next) in stead of checking every minute what is possible
# - prune the paths that are hopeless, by checking the best geode score possible if you would make a geode robot every minute from now on
# - if you already have enough ore robots to make every robot you want for the rest of the time, don't make more ore robots
# and from Jacob:
# - make a class, and let it make copies of it self

import re
import math
import copy

with open("input19.txt") as f:
    lines = f.read().split("\n")

# Read in the input and store the blueprints in a list of dictionaries
Blueprints = []
for line in lines:
    linestring = "Blueprint (d+)\: Each ore robot costs (d+) ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."
    matchObj = re.match(r'^Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.$', line)
    blueprint = {"name": int(matchObj.group(1)),
                 "ore": {"ore":int(matchObj.group(2)), "clay": 0, "obsidian":0},
                 "clay": {"ore": int(matchObj.group(3)), "clay": 0, "obsidian": 0},
                 "obsidian": {"ore": int(matchObj.group(4)), "clay": int(matchObj.group(5)), "obsidian": 0},
                 "geode": {"ore": int(matchObj.group(6)), "clay": 0, "obsidian": int(matchObj.group(7))}
                 }
    Blueprints.append(blueprint)

# In this class robotState, I keep the state of one decision-path. I initialize it, and make copies to compute different paths
class robotState():
    def __init__(self, blueprint, minutes):
        self.bp = blueprint
        self.minutes = minutes #?
        self.resources = {"ore": 0, "clay": 0, "obsidian":0, "geode":0}
        self.robots = {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0}
        self.maxNeeded = {}
        for res in ["ore", "clay", "obsidian" ]:
            self.maxNeeded[res] = max([self.bp[rob][res] for rob in self.robots])
        self.history = [] # To check what the decisions were for the winning strategy
    def computeNextSteps(self): # Consider the different robot types, and decide which ones to build next
        # If the bestpossible score (by creating a geode robot every minute from now on) is less than the overall bestGeodeScore, stop this path
        bestPossibleScore = self.resources["geode"] + self.minutes*self.robots["geode"] + self.minutes*(self.minutes-1)/2
        if bestPossibleScore < bestGeodeScore:
            self.finishTime()
            geodeScore = self.resources["geode"]
            return geodeScore
        else:
            copiesMade = 0
            for robottype in self.robots:
                if robottype == "geode" or not self.resources[robottype] + self.minutes*self.robots[robottype] >= self.minutes * self.maxNeeded[robottype]:
                    T = self.computeTimeToWaitForNextRobot(robottype)
                    if T < self.minutes:
                        self.makeCopy(T+1, robottype)
                        copiesMade += 1
            if copiesMade == 0: # If there is not enough time left to build one of the robot, then finish the time and stop this path
                self.finishTime()
                geodeScore = self.resources["geode"]
                return geodeScore
            else:
                return -1

    def finishTime(self): # Let time run out, and add the resources that are still gathered by the current robots
        for res in self.robots:
            self.resources[res] += self.minutes*self.robots[res]
        self.minutes = 0
    def computeTimeToWaitForNextRobot(self, robottype): # Compute how much time is needed to gain enough matierials to build a certain robot
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
        minTime = self.minutes if minTime == -1 else minTime
        return minTime

    def makeCopy(self, T, robottype):
        newRobotState = copy.deepcopy(self)
        # Get new resources from the robots for the past T minutes
        for res in newRobotState.robots:
            newRobotState.resources[res] += T*newRobotState.robots[res]
        # Add a new robot
        newRobotState.robots[robottype] += 1
        # Pay for the new robot
        for res in self.bp[robottype]:
            newRobotState.resources[res] -= newRobotState.bp[robottype][res]
        newRobotState.minutes -= T
        newRobotState.history.append([newRobotState.minutes, robottype, T, copy.deepcopy(newRobotState.robots), copy.deepcopy(newRobotState.resources)])
        robotList.append(newRobotState)

# Part 1
qualityLevels = []
for bp in Blueprints:
    r = robotState(bp, 24)
    robotList = [r]
    bestGeodeScore = 0
    # bestPath = None
    finishedRobots = []
    while len(robotList) > 0:
        rob = robotList.pop()
        geodeScore = rob.computeNextSteps()
        if geodeScore >= bestGeodeScore:
            bestGeodeScore = geodeScore
            # bestPath = rob.history
    qualityLevels.append(bp["name"] * bestGeodeScore)

print(f"Day 19:\n1) The sum of the quality levels of the blueprints is \033[1m{sum(qualityLevels)}\033[0m.")

# Part 2
geodeScores = []
for bp in Blueprints[:3]:
    r = robotState(bp,32)
    robotList = [r]
    bestGeodeScore = 0
    # bestPath = None
    finishedRobots = []
    while len(robotList) > 0:
        rob = robotList.pop()
        geodeScore = rob.computeNextSteps()
        if geodeScore >= bestGeodeScore:
            bestGeodeScore = geodeScore
            # bestPath = rob.history
    geodeScores.append(bp["name"] * bestGeodeScore)

print(f"2) The maximum number of geodes possible for the first 3 blueprints after 32 minutes are {geodeScores}. The product of these scores is \033[1m{math.prod(geodeScores)}\033[0m.")
