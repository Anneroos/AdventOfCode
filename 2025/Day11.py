with open("2025/input11.txt") as f:
    lines = f.read().splitlines()

allpoints = []
connections={'out': []}
for line in lines:
    point, others = line.split(": ")
    others = others.split(" ")
    connections[point] = others
    allpoints.append(point)

def findPaths(points, startpoint, endpoint, avoid):
    paths = {p:0 for p in points}
    paths[startpoint] = 1
    pathsToEnd = 0

    while True:  
        stillbusy = False
        for point in [k for k in paths.keys() if paths[k] > 0]:
            nr = paths[point]  
            
            others = connections[point]
            paths[point] = 0            
            for o in others:
                if o == endpoint:
                    pathsToEnd += nr
                elif o not in avoid:                    
                    stillbusy = True               
                    paths[o] = paths.get(o,0) + nr
        if not stillbusy:
            break
    return pathsToEnd
        
print(f"Day 11:\n  1) {findPaths(allpoints, 'you', 'out', [])}.")

dac2fft = findPaths(allpoints, 'svr', 'fft', ['dac']) * findPaths(allpoints, 'fft', 'dac', []) * findPaths(allpoints, 'dac', 'out', [])
fft2dac = findPaths(allpoints, 'svr', 'dac', ['fft']) * findPaths(allpoints, 'dac', 'fft', []) * findPaths(allpoints, 'fft', 'out', [])
print(f"  2) {dac2fft+fft2dac}.")