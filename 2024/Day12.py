with open("input12.txt") as f:
    lines = f.read().split("\n")


def findAllAdjacent(p):
    return [(p[0]-1,p[1]),(p[0]+1,p[1]),(p[0],p[1]-1),(p[0],p[1]+1)]


def findAdjacentInGrid(p, w, h):
    return [p for p in findAllAdjacent(p) if 0 <= p[0] < w and 0 <= p[1] < h]


def computePerimeter(region):
    peri = 0
    for p in region:
        peri += 4 - len([neighbor for neighbor in findAllAdjacent(p) if neighbor in region])
    return peri


def getNeighborByDir(p, direction):
    if direction == "N":
        return (p[0],p[1]-1)
    elif direction == "E":
        return (p[0]+1,p[1])
    elif direction == "S":
        return (p[0],p[1]+1)
    elif direction == "W":
        return (p[0]-1,p[1])
    else:
        return None


def computeWalls(region):
    walls = []
    for p in region:
        for dir in "NESW":
            n = getNeighborByDir(p, dir)
            if n not in region:
                walls.append([p,dir])
    return walls


def computeFenceDiscount(region):
    walls = computeWalls(region)
    sortedN = ["N", sorted([w[0] for w in walls if w[1] == "N"], key=lambda x: [x[1], x[0]])]
    sortedS = ["S", sorted([w[0] for w in walls if w[1] == "S"], key=lambda x: [x[1],x[0]])]
    sortedE = ["E", sorted([w[0] for w in walls if w[1] == "E"], key=lambda x: x)]
    sortedW = ["W", sorted([w[0] for w in walls if w[1] == "W"], key=lambda x: x)]
    fence = 0
    for directedWalls in [sortedN,sortedS,sortedE,sortedW]:
        dir = directedWalls[0]
        w = directedWalls[1]
        fence += 1  # You need at least 1 in each direction
        wall = w.pop(0)
        while len(w) > 0:
            nextwall = w.pop(0)
            if dir in "NS":
                if not (nextwall[1] == wall[1] and nextwall[0] == wall[0] + 1):
                    fence += 1
            elif dir in "EW":
                if not (nextwall[0] == wall[0] and nextwall[1] == wall[1] + 1):
                    fence += 1
            wall = nextwall
    return fence


def computeRegions(input):
    h = len(input)
    w = len(input[0])
    garden = {}
    for y in range(h):
        line = input[y]
        for x in range(w):
            type = line[x]
            garden[(x, y)] = type
    regions = []
    visited = {}
    for y in range(h):
        for x in range(w):
            if (x,y) not in visited:
                toVisit = [(x,y)]
                region = []
                while len(toVisit) > 0:
                    plot = toVisit.pop(0)
                    visited[plot] = 1
                    region.append(plot)
                    neighbors = findAdjacentInGrid(plot, w, h)
                    for n in neighbors:
                        if n not in toVisit and n not in region and garden[n] == garden[plot]:
                            toVisit.append(n)
                regions.append(region)
    return regions


def computeFencePrices(input):
    regions = computeRegions(input)
    price1 = 0
    price2 = 0
    for region in regions:
        area = len(region)
        perimeter = computePerimeter(region)
        fence = computeFenceDiscount(region)
        price1 += area*perimeter
        price2 += area * fence
    return price1, price2

result1, result2 = computeFencePrices(lines)
print(f"Day 12:\n  1) The total price of fencing all regions on this map is {result1}.")
print(f"  2) With the bulk discount, the total price of fencing all regions on this map is {result2}.")