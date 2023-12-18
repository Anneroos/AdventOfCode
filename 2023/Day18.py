from collections import defaultdict
with open("input18.txt") as f:
    lines = [{'dir': line.split()[0], 'distance': int(line.split()[1]), 'truedistance': int(line.split()[2][2:7], 16), 'truedir': 'RDLU'[int(line.split()[2][7])]} for line in f.read().split("\n")]
    instructions1 = [{'dir': line['dir'], 'distance': line['distance']} for line in lines]
    instructions2 = [{'dir': line['truedir'], 'distance': line['truedistance']} for line in lines]

def computeCubicMetersOfLava(perimeterDirections):
    horizons = {}
    verticals = {}
    verticals2 = defaultdict(dict)
    place = (0,0)
    newplace = (0,0)
    lengthPerimeter = 0 # Keep count of the perimeter as we go around
    for idx, line in enumerate(perimeterDirections):
        dir = line['dir']
        distance = line['distance']
        if dir == "L":
            newplace = (place[0], place[1] - distance)
            horizons[place[0]] = horizons.get(place[0], []) + [[place[1] - distance, place[1]]]
        elif dir == "R":
            newplace = (place[0], place[1] + distance)
            horizons[place[0]] = horizons.get(place[0], []) + [[place[1], place[1] + distance]]
        # For every vertical edge, keep score of how we get in and out of this edge, so LR, RL, LL or RR.
        elif dir == "U":
            newplace = (place[0] - distance, place[1])
            verticals[place[1]] = verticals.get(place[1], []) + [[place[0] - distance, place[0]]]
            verticals2[place[1]][(place[0] - distance, place[0])] = perimeterDirections[(idx - 1)  % len(perimeterDirections)]['dir'] + perimeterDirections[(idx + 1) % len(perimeterDirections)]['dir']
        elif dir == "D":
            newplace = (place[0] + distance, place[1])
            verticals[place[1]] = verticals.get(place[1], []) + [[place[0], place[0] + distance]]
            verticals2[place[1]][(place[0] , place[0] + distance)] = perimeterDirections[(idx - 1)  % len(perimeterDirections)]['dir'] + perimeterDirections[(idx + 1)  % len(perimeterDirections)]['dir']
        place = newplace
        lengthPerimeter += distance
    cornerRows = sorted(horizons.keys())
    cornerCols = sorted(verticals.keys())

    # Now we are counting all the inside cubic meters
    totalinside = 0
    for cornerIdx, cornerCol in enumerate(cornerCols):
        # We do this by first considering all (column values of) corners and drawing vertical lines through them,
        # and counting how many *inside* cubes we find on this line
        lineAtCorners = 0
        # While traveling on these lines, we will encounter horizontal lines (which we see as vertical lines of length 1) and actual vertical lines.
        horizontalSegments = sorted([ [t[0],t[0]] for t in [[k for segment in v if segment[0] < cornerCol < segment[1]] for k,v in horizons.items() ] if t != []])
        verticalSegments = sorted(verticals[cornerCol] + horizontalSegments)
        # initialize some stuff
        inside = False
        startInside = cornerRows[0] - 1

        for seg in verticalSegments:
            type = verticals2[cornerCol].get(tuple(seg), "HH")            # HH = horizontal segment ;)
            oldinside = inside
            if type[0] == type[1]: # if RR, LL or HH, then we 'cross a border'
                inside = not inside
            if oldinside: # if we were inside, count the cubes since startInside!
                lineAtCorners += seg[0] - startInside
            if inside: # if we are now inside, set the startInside so we now where to count from
                startInside = seg[1] + 1
        totalinside += lineAtCorners

        # Also, we draw vertical lines in the 'intervals' between corners, and count how many inside cubes there are,
        # and multiply that by the width of the interval between corner values.
        if cornerIdx < len(cornerCols) - 1  and  cornerCol + 1 != cornerCols[cornerIdx + 1]:
            lineInBetween = 0
            inside = False
            startInside = cornerRows[0] - 1
            for cornerRow in cornerRows:
                for segment in horizons[cornerRow]:
                    if segment[0] <= cornerCol + 1 <= segment[1]:
                        # This is easier than the bit above, since we only cross horizontal lines, so we always switch
                        inside = not inside
                        if inside: # if we are now inside, set the startInside so we now where to count from
                            startInside = cornerRow + 1
                        elif not inside: # if we just went outside, count the cubes since startInside!
                            lineInBetween += cornerRow - startInside
            # Multiply the number of inside cubes that we found on lineInBetween with the width of the interval
            totalinside += lineInBetween * (cornerCols[cornerIdx + 1] - cornerCol - 1)
    return lengthPerimeter + totalinside

print(f"Day 18:\n1) The lagoon can hold {computeCubicMetersOfLava(instructions1)} cubic meters of lava.")
print(f"2) After the correct instructions, the lagoon can hold a whopping {computeCubicMetersOfLava(instructions2)} cubic meters of lava.")