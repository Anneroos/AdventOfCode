# import math

# with open("2025/input08.txt") as f:
#     lines = [tuple([int(k) for k in l.split(",")]) for l in f.read().splitlines()]


# def distance(p, q):
#     return math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2 + (p[2]-q[2])**2) 

# distances = {}
# groupPerDistance = {}

# for i in range(len(lines)):
#     p = lines[i]
#     for j in range(i+1, len(lines)):
#         q = lines[j]
#         d = distance(p, q)
#         # print(d,p,q)
#         groupPerDistance[d] = groupPerDistance.get(d,[]) + [[p,q]]
        
#         # if p not in distances:
#         #     distances[p] = {q: d}
#         # else:
#         #     distances[p][q] = d
# groups = {lines[i]:i for i in range(len(lines))}
# # print(groups)
# # print("****")
# # print("shortest distances", sorted(groupPerDistance.keys())[:10])
# for d in sorted(groupPerDistance.keys())[:1000]:
#     edge = groupPerDistance[d][0]
#     # print(edge)
#     if len(groupPerDistance[d]) > 2:
#         print("ERROR, LEN>2")
#     p = edge[0]
#     q = edge[1]   
#     # print(groups[q]) 
#     p_group = groups[p]
#     for k,v in groups.items():
#         if v == p_group:
#             print(k,v , " ----> ", groups[q])
#             groups[k] = groups[q]
#             print("result", groups[k])
# groupSize={}
# for p,groupIdx in groups.items():
#     groupSize[groupIdx] = groupSize.get(groupIdx,0) + 1


# sizes = [v for v in groupSize.values()]
# sizes.sort(reverse=True)
# print(sizes)
# print(sizes[0] * sizes[1] * sizes[2])



import math

with open("2025/input08.txt") as f:
    lines = [tuple([int(k) for k in l.split(",")]) for l in f.read().splitlines()]


def distance(p, q):
    return math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2 + (p[2]-q[2])**2) 

distances = {}
groupPerDistance = {}

for i in range(len(lines)):
    p = lines[i]
    for j in range(i+1, len(lines)):
        q = lines[j]
        d = distance(p, q)
        # print(d,p,q)
        groupPerDistance[d] = groupPerDistance.get(d,[]) + [[p,q]]
        
        # if p not in distances:
        #     distances[p] = {q: d}
        # else:
        #     distances[p][q] = d
groups = {lines[i]:i for i in range(len(lines))}
# print(groups)
# print("****")
# print("shortest distances", sorted(groupPerDistance.keys())[:10])
for d in sorted(groupPerDistance.keys()):
    edge = groupPerDistance[d][0]
    # print(edge)
    if len(groupPerDistance[d]) > 2:
        print("ERROR, LEN>2")
    p = edge[0]
    q = edge[1]   
    # print(groups[q]) 
    p_group = groups[p]
    for k,v in groups.items():
        if v == p_group:
            # print(k,v , " ----> ", groups[q])
            groups[k] = groups[q]
            # print("result", groups[k])
    # print(len(groups.values()))
    print(set(groups.values()))
    if len(set(groups.values())) == 1:
        print(p,q,p[0]*q[0])
        print("HALLOO")
        break
