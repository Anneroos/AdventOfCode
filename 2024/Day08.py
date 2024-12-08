with open("input08.txt") as f:
    lines = f.read().split("\n")
w = len(lines[0])
h = len(lines)


def isInGrid(pos):
    return 0 <= pos[0] < h and 0 <= pos[1] < w



poles = {}
for lineIdx in range(len(lines)):
    line = lines[lineIdx]
    for i in range(len(line)):
        char = line[i]
        if char != ".":
            poles[char] = poles.get(char,[]) + [(lineIdx, i)]

print(poles)
antinodes1 = {}
antinodes2 = {}
for poleName in poles.keys():
    locations = poles[poleName]
    for i in range(len(locations)):
        for j in range(i+1, len(locations)):
            loc1 = locations[i]
            loc2 = locations[j]
            diff = (loc2[0] - loc1[0], loc2[1] - loc1[1])
            steps = 0
            while steps >= 0:
                antinode1 = (loc1[0] - steps * diff[0], loc1[1] - steps * diff[1])
                antinode2 = (loc2[0] + steps * diff[0], loc2[1] + steps * diff[1])
                a1 = isInGrid(antinode1)
                a2 = isInGrid(antinode2)
                if a1:
                    antinodes2[antinode1] = antinodes2.get(antinode1, []) + [poleName]
                    if steps == 1:
                        antinodes1[antinode1] = antinodes1.get(antinode1, []) + [poleName]
                if a2:
                    antinodes2[antinode2] = antinodes2.get(antinode2, []) + [poleName]
                    if steps == 1:
                        antinodes1[antinode2] = antinodes1.get(antinode2, []) + [poleName]
                if not a1 and not a2:
                    break
                else:
                    steps += 1
            print(f"For loc1 {loc1} and loc {loc2} we get two antinodes: {antinode1} and {antinode2}")


nrOfAntinodes1 = 0
for a in antinodes1:
    if 0 <= a[0] < h and 0 <= a[1] < w:
        nrOfAntinodes1 += 1
nrOfAntinodes2 = 0
for a in antinodes2:
    if 0 <= a[0] < h and 0 <= a[1] < w:
        nrOfAntinodes2 += 1

print(nrOfAntinodes1)
print(nrOfAntinodes2)