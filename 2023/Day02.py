with open("input02.txt","r") as f:
    lines =  f.read().split('\n')
    
maxColors = {'green': 13, 'red': 12, 'blue': 14 }
totalPossible = 0
totalPower = 0

for i in range(1, len(lines)+1):
    line = lines[i-1]
    possible = True
    minimumSet = {'green': 0, 'red': 0, 'blue': 0}
    game, draws = line.split(": ")
    draws = draws.split("; ")

    for d in draws:
        # Parse input
        draw = d.split(", ")
        drawDict = {}
        for cubes in draw:
            nr, color = cubes.split(" ")
            nr = int(nr)
            drawDict[color] = nr

        # Computations for part 1 and part 2
        for color in drawDict:
            # part 1
            if drawDict[color] > maxColors[color]:
                possible = False
            # part 2
            minimumSet[color] = max(drawDict[color], minimumSet[color])

    # Part 1
    if possible:
        totalPossible += i
    # Part 2
    power = minimumSet['red'] * minimumSet['green'] * minimumSet['blue']
    totalPower += power
    
print(f"Day 2:\n1) The sum of the IDs of the possible games is {totalPossible}.")
print(f"2) The sum of the power of the sets is {totalPower}.")
