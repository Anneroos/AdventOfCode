with open("input12.txt", "r") as f:
    lines = f.read().splitlines()
import time
st = time.time()
# Read input and fill a dictionairy
caves = {}
for line in lines:
    t = line.split("-")
    caves[t[0]] = caves.get(t[0], []) + [t[1]]
    caves[t[1]] = caves.get(t[1], []) + [t[0]]

# For part 1: every lowercase cave name can appear only once in a path
def checkPath1(path):
    for p in path:
        if p.islower() and path.count(p) > 1:
            return False
    return True

# For part 2: max. one lower-case cave name may appear twice (but not start/end)
def checkPath2(path):
    n = set()
    for p in path:
        if p.islower():
            c = path.count(p)
            if c > 2:
                return False
            elif c > 1:
                n.add(p)
                if len(n) > 1 or p == "start" or p == "end":
                    return False
    else:
        return True

def computePaths(caves, pathchecker):
    paths = [["start"]]
    finishedpaths = 0
    while len(paths) > 0:
        newpaths = []
        for p in paths:
            pos = p[-1]
            if pos != "end":
                for next in caves[pos]:
                    if pathchecker(p + [next]):
                        if next == "end":
                            finishedpaths += 1
                        else:
                            newpaths.append(p + [next])
            else:
                finishedpaths.append(p)
        paths = newpaths
    return finishedpaths

print(f"Part 1: There are {(computePaths( caves, checkPath1))} paths.")
print(f"Part 2: There are {(computePaths( caves, checkPath2))} paths.")
et = time.time()
print(f"Both parts together took {et-st} seconds.")

# Nice idea found on reddit by bacontime for part 2, not used:
# "I gave each incomplete path a little flag to indicate whether the duplicate small cave had already been 'used up' for that path."
# Then you don't have to check the full path every time again

# # OMG check this (unreadable) solution by michalopler "Python, both parts can fit into a single tweet (<280 chars)"
# # It takes less than half a second
# # It might be nice to learn what's going on here...
# from functools import*
# N,s,E={},'start',frozenset()
# for l in open('input12.txt'):
#  p=l.strip().split('-')
#  for i in(0,1):N[p[i]]=N.get(p[i],E)|{p[~i]}
# c=lru_cache()(lambda v,S,f:sum((c(w,(S,S|{v})[v[0]>='a'],f|(w in S)),1)[w=='end']for w in N[v]-({s},S)[f]))
# print(c(s,E,1),c(s,E,0))
