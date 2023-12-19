import re
with open("input19.txt") as f:
    puzzleinput = f.read().split("\n\n")
    workflowsinput = puzzleinput[0].split("\n")
    partsinput = puzzleinput[1].split("\n")

### PARSING INPUT
parts = []
for line in partsinput:
    part = {}
    t = re.findall("\w=\d+", line)
    for s in t:
        part[s[0]] = int(s[2:])
    parts.append(part)

workflows = {}
for line in workflowsinput:
    workflow = {}
    workflow_name = re.search("^\w+",line).group()
    rulesRaw = re.findall("^\w+\{(.+)\}", line)[0].split(",")
    rules = []
    for idx, rule in enumerate(rulesRaw):
        if idx < len(rulesRaw) - 1:
            check = rule[0]
            compare = rule[1]
            number = int(rule[2:].split(":")[0])
            goTo = rule[2:].split(":")[1]
            rules.append({'check': check, "compare": compare, "number": number, "goTo": goTo})
        else:
            rules.append({'goTo': rule})
    workflows[workflow_name] = rules

### PART 1
totalsum = 0
for part in parts:
    next_workflow_name = "in"
    while next_workflow_name not in ["A","R"]:
        current_workflow = workflows[next_workflow_name]
        for rule in current_workflow:
            if 'compare' in rule:
                if rule['compare'] == ">":
                    if part[rule['check']] > rule['number']:
                        next_workflow_name = rule['goTo']
                        break
                elif rule['compare'] == "<":
                    if part[rule['check']] < rule['number']:
                        next_workflow_name = rule['goTo']
                        break
            else:
                next_workflow_name = rule['goTo']
    if next_workflow_name == "A":
        totalsum += sum(part.values())
print(f"Day 19:\n1) If we add together all of the rating numbers for all of the parts that ultimately get accepted, we get {totalsum}.")


### PART 2
def findNrCombinations(startRanges):
    rangesToCheck = [startRanges]
    acceptedRanges = []
    while rangesToCheck:
        range = rangesToCheck.pop(0)
        workflowname = range['workflow']
        if workflowname == "A":
            acceptedRanges.append(range)
            continue
        elif workflowname == "R":
            continue
        current_workflow = workflows[workflowname]
        for rule in current_workflow:
            if 'compare' in rule:
                category = rule['check']
                number = rule['number']
                rangecopy = range.copy()
                if rule['compare'] == ">":
                    if number >= range[category][1]:
                        # go to next rule with complete range
                        continue
                    elif number < range[category][0]:
                        # full range gets send to next workflow
                        range['workflow'] = rule['goTo']
                        rangesToCheck.append(range)
                        break
                    else:
                        # range gets split, one part we consider later, with the rest we go to the next rule
                        rangecopy = range.copy()
                        rangecopy[category] = [number + 1, range[category][1]]
                        range[category] = [range[category][0], number]
                        rangecopy['workflow'] = rule['goTo']
                        rangesToCheck.append(rangecopy)
                        continue
                if rule['compare'] == "<":
                    if number <= range[category][0]:
                        # go to next rule with complete range
                        continue
                    elif number > range[category][1]:
                        # full range gets send to next workflow
                        range['workflow'] = rule['goTo']
                        rangesToCheck.append(range)
                        break
                    else:
                        # range gets split, one part we consider later, with the rest we go to the next rule
                        rangecopy = range.copy()
                        rangecopy[category] = [range[category][0], number - 1]
                        range[category] = [number, range[category][1]]
                        rangecopy['workflow'] = rule['goTo']
                        rangesToCheck.append(rangecopy)
                        continue
            else:
                # rest, full range gets send to next workflow
                range['workflow'] = rule['goTo']
                rangesToCheck.append(range)
    return sum([(range['x'][1] - range['x'][0] + 1) * (range['m'][1] - range['m'][0] + 1)  * (range['a'][1] - range['a'][0] + 1)  * (range['s'][1] - range['s'][0] + 1) for range in acceptedRanges])

print(f"2) There are {findNrCombinations({'x':[1,4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000], 'workflow': 'in'})} distinct combinations of ratings that will be accepted by the Elves' workflows.")