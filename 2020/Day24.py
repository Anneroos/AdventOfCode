with open("input24.txt") as f:
    lines = f.read().split("\n")


directions = []
for line in lines:
    # print(line)
    index = 0
    route = []
    while index <len(line):
        if line[index] == "e" or line[index] == "w":
            route.append(line[index])
            index += 1
        else:
            route.append(line[index:index+2])
            index += 2

    # print(route)
    directions.append(route)

# print(directions)


tiles = {}
for route in directions:
    x = 0
    y = 0
    for dir in route:
        # print(f"at ({x},{y}) going {dir} ")
        if dir == "e" or dir == "w":
            x = x+1 if dir == "e" else x-1
        elif dir == "sw" or dir == "se":
            y -= 1
            if y % 2 == 0:
                x += 1
            x = x-1 if dir =="sw" else x
        elif dir == "nw" or dir == "ne":
            y += 1
            if y % 2 == 0:
                x += 1
            x = x-1 if dir =="nw" else x

    # print(x,y, " -- ", tiles.get((x,y),0))





    tiles[(x,y)] = 1 - tiles.get((x,y),0)
nrOfFlippedTiles = 0
for key in tiles.keys():

    nrOfFlippedTiles  += tiles[key]
print(f"Day 24 part 1: {nrOfFlippedTiles}" )

# part 2
def determinesTilesToCheck(dict):
    tilesToCheck = []
    for key in dict:
        x = key[0]
        y = key[1]
        even = 1 if y %2 == 0 else 0
        tilesToCheck += [(x,y), (x+1,y),(x-1,y),(x-even,y+1),(x+1-even,y+1),(x-even,y-1),(x+1-even,y-1)]
    tilesToCheck = list(set(tilesToCheck))
    return tilesToCheck


for i in range(100):
    tilesToCheck = determinesTilesToCheck(tiles)
    tilesToFlip = []
    for tile in tilesToCheck:
        x = tile[0]
        y = tile[1]
        even = 1 if y % 2 == 0 else 0
        neighborsFlipped = 0
        for neighbor in [ (x+1,y),(x-1,y),(x-even,y+1),(x+1-even,y+1),(x-even,y-1),(x+1-even,y-1)]:
            neighborsFlipped += tiles.get(neighbor,0)
        if tiles.get(tile,0) == 1:
            if neighborsFlipped == 0 or neighborsFlipped > 2:
                tilesToFlip.append(tile)
        else:
            if neighborsFlipped == 2:
                tilesToFlip.append(tile)
    for tile in tilesToFlip:
        tiles[tile] = 1 - tiles.get(tile,0)
    nrOfFlippedTiles = 0

for key in tiles.keys():
    nrOfFlippedTiles += tiles[key]
print(f"Day 24 part 2: {nrOfFlippedTiles}" )