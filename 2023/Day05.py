with open("input05.txt", "r") as f:
    almanac = [map.split("\n") for map in f.read().split('\n\n')]

# --------- part 1
seeds = [{"seed": int(i)} for i in almanac[0][0].split(": ")[1].split()]
mappings = {}
for map in almanac[1:]:
    mapping = {}
    sourceName, _, destinationName = map[0].split()[0].split("-")
    for seed in seeds:
        source = seed.get(sourceName)
        seed[destinationName] = source # default, if not in map
        for line in map[1:]:
            destinationStart, sourceStart, range_length = [int(i) for i in line.split()]
            if sourceStart <= source < sourceStart + range_length:
                seed[destinationName] = destinationStart + (source - sourceStart)
    mappings[sourceName] = { "destination": destinationName, "map": mapping}
locations = [seed['location'] for seed in seeds]
print(f"Day 5:\n1) The lowest location number that corresponds to any of the initial seed numbers is {min(locations)}.")

# --------- part 2
seedsNrs = [int(i) for i in almanac[0][0].split(": ")[1].split()]
ranges = {'seed': [ ([seedsNrs[2*i], seedsNrs[2*i + 1]]) for i in range(round(len(seedsNrs)/2))]}
ranges['seed'].sort()

mappings = {}
for map in almanac[1:]:
    name = map[0].split()[0]
    sourceName = name.split("-")[0]
    destinationName = name.split("-")[2]
    mappings = [[int(i) for i in line.split()] for line in map[1:]]
    mappings = sorted(mappings, key=lambda x: x[1], reverse=False)
    mapIdx = 0
    rangesToConsider = ranges[sourceName].copy()
    resultRanges = []
    while len(rangesToConsider) > 0:
        range = rangesToConsider.pop(0)
        range_start = range[0]
        range_length = range[1]
        range_end = range[0] + range_length - 1
        if mapIdx >= len(mappings):
            resultRanges.append(range)
        else:
            map_range = mappings[mapIdx][2]
            source_range_start = mappings[mapIdx][1]
            source_range_end = mappings[mapIdx][1] + map_range - 1
            dest_range_start = mappings[mapIdx][0]
            dest_range_end = mappings[mapIdx][0] + map_range - 1
            if range_start < source_range_start:
                if range_end < source_range_start: # range is to the left of the map-part
                    resultRanges.append(range)
                elif range_end >= source_range_start: # range is partly to the left of the map-part, split range in two.
                    resultRanges.append([range_start, source_range_start - range_start - 1])
                    rangesToConsider.insert(0, [source_range_start, range[1] - (source_range_start - range_start)]) # reconsider this range later
                    rangesToConsider.sort() # just to be sure
            elif range_start >= source_range_start and range_start <= source_range_end:
                if range_end <= source_range_end: # range completely inside this map-part
                    resultRanges.append([dest_range_start + (range_start - source_range_start), range_length])
                else: # range is partly in and partly to the right of the map-part
                    resultRanges.append([dest_range_start + (range_start - source_range_start),   (source_range_end - range_start) + 1 ])
                    rangesToConsider.insert(0, [source_range_end + 1,  range_length - (source_range_end - range_start) - 1]) # reconsider this range later
                    rangesToConsider.sort() # just to be sure
            else: # range is completely to the right of the map-aprt, so lets check out the next map-part!
                rangesToConsider.insert(0, range)
                rangesToConsider.sort()
                mapIdx += 1
    resultRanges = [list(j) for j in set([tuple(i) for i in resultRanges])] # deduplication
    resultRanges.sort()
    ranges[destinationName] = resultRanges # store for use in the next iteration
print(f"2) The lowest location number that corresponds to any of the initial seed numbers is {ranges['location'][0][0]}.")