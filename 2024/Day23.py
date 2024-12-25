with open("input23.txt") as f:
    input = f.read().split("\n")


from itertools import chain, combinations


# Define a function to create powersets of a minimumSize, given a list.
def powerset(iterable, minSize):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(minSize,len(s)+1))


connections = {}
for line in input:
    comp1,comp2 = line.split("-")
    connections[comp1] = connections.get(comp1,[]) + [comp2]
    connections[comp2] = connections.get(comp2, []) + [comp1]

trios = []
for comp in connections:
    if comp[0] == 't':
        other_computers = connections[comp]
        for i in range(len(other_computers)):
            for j in range(i+1, len(other_computers)):
                comp2 = other_computers[i]
                comp3 = other_computers[j]
                if comp3 in connections[comp2]:
                    trio = "-".join(sorted([comp, comp2, comp3]))
                    trios.append(trio)

trios = list(set(trios))

print(f"Day 23:\n  1) There are {len(trios)} sets of three inter-connected computers that have at least one computer with a name that starts with a t.")

## For part 2, I noticed that all computers are connected to 13 other computers.
# So first try to find a LAN party of size 14, if that doesn't work, find one of size 13, etc.
maxNrOfConnections = max([len(v) for v in connections.values()])
foundIt = False
for LANsize in range(maxNrOfConnections+1,2,-1):
    for comp, other_comps in connections.items():
        # Find all combinations of LANsize - 1 computers to make a possible LAN party with comp of size LANsize
        for computer_set in powerset(other_comps, LANsize-1):
            # Lets check if all the computers in this possible LAN party are actually connected
            superConnected = True
            for i in range(len(computer_set)):
                comp2 = computer_set[i]
                for j in range(i+1, len(computer_set)):
                    comp3 = computer_set[j]
                    if comp2 not in connections[comp3]:
                        superConnected = False
                        break
                if not superConnected:
                    break
            if superConnected: # That means we found a LAN party!
                sortedLAN = sorted([comp] + list(computer_set))
                print(f"  2) The password to get into the largest LAN party (of size {LANsize}) is {','.join(sortedLAN)}.")
                foundIt = True
                break
        if foundIt:
            break
    if foundIt:
        break
