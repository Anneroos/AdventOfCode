import re
with open("input19.txt") as f:
    lines = f.read().split("\n")
Blueprints = []
for line in lines:
    linestring = "Blueprint (d+)\: Each ore robot costs (d+) ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."

    matchObj = re.match(r'^Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.$', line)
    # print(matchObj)
    blueprintnr = int(matchObj.group(1))
    orerobotcost = (int(matchObj.group(2)), 0, 0)
    clayrobotcost = (int(matchObj.group(3)), 0, 0)
    obsidianrobotcost = (int(matchObj.group(4)),  int(matchObj.group(5)), 0)
    geoderobotcost = (int(matchObj.group(6)), 0, int(matchObj.group(7)))
    blueprinttuple = (orerobotcost, clayrobotcost, obsidianrobotcost, geoderobotcost, blueprintnr)

    Blueprints.append(blueprinttuple)

def computeMaxGeodes(bp, minutes, robots, resources):
    # Note that we can do a bit better: For any resource R that's not geode:
    # if you already have X robots creating resource R, a current stock of Y for that resource,
    # T minutes left, and no robot requires more than Z of resource R to build, and X * T+Y >= T * Z,
    # then you never need to build another robot mining R anymore.
    Z = [max(bp[0][0],bp[1][0],bp[2][0], bp[3][0]), max(bp[0][1],bp[1][1],bp[2][1], bp[3][1]), max(bp[0][2],bp[1][2],bp[2][2], bp[3][2])]
    bestgeodes = 0

    path = ()
    states = {(robots, resources, path ):1}
    for minute in range(minutes):
        print(f"Minute { minute}")
        newstates = {}
        for state in states:
            # print(state)
            robos = state[0]
            reses = state[1]
            path = state[2]
            newResources = (robos[0] + reses[0], robos[1] + reses[1], robos[2] + reses[2], robos[3]+ reses[3])

            maxrobots = []
            X = [robos[0], robos[1], robos[2]]
            T = minutes - minute - 1
            Y = [resources[0], resources[1], resources[2]]
            geodes = resources[3]
            if geodes > bestgeodes:
                bestgeodes = geodes
            if geodes + T*(T+1)/2 <= bestgeodes:
                pass # stop this path
            else:
                for roboidx in range(len(robos)):
                    # print(roboidx, [X[roboidx] * T + Y[roboidx] , T * Z[roboidx]] if roboidx !=3 else 0)
                    if roboidx ==3 or X[roboidx] * T + Y[roboidx] < T * Z[roboidx]:
                        costs =  bp[roboidx]
                        maxrobot = min([reses[residx]//costs[residx] for residx in range(3) if costs[residx] != 0])
                        maxrobots.append(1 if maxrobot >0 else 0)
                        if maxrobot >= 1:
                            newstate = ((robos[0] + (1 if roboidx==0 else 0), robos[1] + (1 if roboidx==1 else 0), robos[2] + (1 if roboidx==2 else 0), robos[3] + (1 if roboidx==3 else 0)),
                                        (newResources[0] - costs[0], newResources[1] - costs[1], newResources[2] - costs[2], newResources[3]),
                                        path + (roboidx,))

                            newstates[newstate] = 1
                # if no new robots
                if sum(maxrobots) != 3:
                    newstate = (robos, newResources, path + (-1,))
                    newstates[newstate] = 1

        states = newstates
        print(bestgeodes)
        # print( 'ore? ', max([s[1][0] for s in states]), 'clay? ', max([s[1][1] for s in states]),'obsidians? ', max([s[1][2] for s in states]), 'geodes? ', max([s[1][3] for s in states]))

    return sorted([k for k in states.keys()], key=lambda x: x[1][3]*100 + x[0][3]*10 +  x[1][2] + 0.1*x[1][2] + x[1][1]*0.01 +  + x[0][1]*0.001 + x[1][0]*0.0001 + x[0][0]*0.00001, reverse=True)[0]



initialrobots = (1,0,0,0) #{"orerobot":1, "clayrobot": 0, "obsidianrobot": 0, "geoderobot":0}
itinitalresources = (0,0,0,0)#{"ore": 0, "clay":0, "obsidian":0, "geode":0}

for blueprint in Blueprints[:1]:
    geodes = computeMaxGeodes(blueprint, 24 , initialrobots, itinitalresources)
    print(geodes)

# Each ore robot costs 3 ore.
# Each clay robot costs 4 ore.
# Each obsidian robot costs 4 ore and 16 clay.
# Each geode robot costs 3 ore and 15 *(4 ore and 16 *(4 ore)).



# What robot to build next?
# Based on decisions i nstead of minutes, net als dag 16 :) Rewrite!
