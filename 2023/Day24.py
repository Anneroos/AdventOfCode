with open("input24.txt") as f:
    lines = [[[int(i) for i in p.split(", ")] for p in line.split("@")] for line in f.read().splitlines()]

# testarea = [7, 27]
# testarea = [200000000000000, 400000000000000]
# total = 0
# for idxA, lineA in enumerate(lines):
#     for lineB in lines[idxA+1:]:
#
#         xA = lineA[0][0]
#         yA = lineA[0][1]
#         zA = lineA[0][2]
#         xB = lineB[0][0]
#         yB = lineB[0][1]
#         zB = lineB[0][2]
#         vxA = lineA[1][0]
#         vyA = lineA[1][1]
#         vzA = lineA[1][2]
#         vxB = lineB[1][0]
#         vyB = lineB[1][1]
#         vzB = lineB[1][2]
#
#         # xA + t*vxA = xB + s*vxB                                 -->  t*vxA = xB - xA + vxB *((yA + t*vyA -yB)/vyB)
#         # yA + t*vyA = yB + s*vyB -> (yA + t*vyA -yB)/vyB = s   --|
#         # -->  t * vxA * vyB = (xB - xA)*vyB + vxB * yA + vxB*t * vyA - vxB *yB
#         if vxA/vxB == vyA/vyB: #  (vxA * vyB - vxB * vyA) and (vxA * vzB - vxB * vzA) and (vyA * vzB - vyB * vzA) == 0:
#             print("parallel", lineA, lineB)
#         else:
#             t  = ((xB - xA) * vyB + vxB * yA - vxB * yB)/(vxA * vyB - vxB * vyA)
#             s = (yA + t*vyA -yB)/vyB
#             x = xA + t*vxA
#             y = yA + t*vyA
#             if t >0 and s> 0 and testarea[0] <= x <= testarea[1] and testarea[0] <= y <= testarea[1]:
#                 total += 1
# print(total)
#


# part 2


total = 0
for idxA, lineA in enumerate(lines):
    for lineB in lines[idxA+1:]:
        # print(lineA, lineB)

        xA = lineA[0][0]
        yA = lineA[0][1]
        zA = lineA[0][2]
        xB = lineB[0][0]
        yB = lineB[0][1]
        zB = lineB[0][2]
        vxA = lineA[1][0]
        vyA = lineA[1][1]
        vzA = lineA[1][2]
        vxB = lineB[1][0]
        vyB = lineB[1][1]
        vzB = lineB[1][2]

        # xA + t*vxA = xB + s*vxB                                 -->  t*vxA = xB - xA + vxB *((yA + t*vyA -yB)/vyB)
        # yA + t*vyA = yB + s*vyB -> (yA + t*vyA -yB)/vyB = s   --|
        # -->  t * vxA * vyB = (xB - xA)*vyB + vxB * yA + vxB*t * vyA - vxB *yB
        if vxA/vxB == vyA/vyB: #  (vxA * vyB - vxB * vyA) and (vxA * vzB - vxB * vzA) and (vyA * vzB - vyB * vzA) == 0:
            print("parallel", lineA, lineB)
        else:
            t  = ((xB - xA) * vyB + vxB * yA - vxB * yB)/(vxA * vyB - vxB * vyA)
            s = (yA + t*vyA -yB)/vyB
            x = xA + t*vxA
            y = yA + t*vyA
            # print(t,s,x,y)
            if t >0 and s> 0 and testarea[0] <= x <= testarea[1] and testarea[0] <= y <= testarea[1]:
                # print("Cross inside test area in future!")
                total += 1
            # elif t<0 or s<0:
            #     print("Crossed in passed for one or more of the hail stones")
            # else:
            #     print("Outside test area?")
print(total)