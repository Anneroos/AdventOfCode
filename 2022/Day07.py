with open("input07.txt") as f:
    inp = [line.split() for line in f.read().split("\n")]

currentDir = ["/"]
dirs = {"/" : {"dirs": [], "files":{}, "path": currentDir} }
def listToPath(dirList):
    if len(dirList) == 0:
        return dirList[0]
    else:
        return dirList[0] + "/".join(dirList[1:])
for line in inp:
    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "..":
                currentDir.pop()
            elif line[2] == "/":
                currentDir = ["/"]
            else:
                currentDir.append(line[2])
        elif line[1] == "ls":
            pass
        else:
            print("Unknown command")
    else:
        if line[0] == "dir":
            path = listToPath(currentDir)
            totalPath = listToPath(currentDir + [line[1]])
            if totalPath not in dirs.keys():
                dirs[totalPath] = {"dirs": [], "files":{}, "path": currentDir.copy() + [line[1]]}
                # add as subdir of dir
                if line[1] not in dirs[path]["dirs"]:
                    dirs[path]["dirs"].append(line[1])
            else:
                print("We've already seen this directory:", totalPath)
        else:
            size = int(line[0])
            name = line[1]
            totalPath = listToPath(currentDir)
            dirs[totalPath]["files"][name] = size

def sizeOfDir(direcs, mydir):
    totalSize = 0
    for dir in direcs[mydir]["dirs"]:
        totalPath = listToPath(direcs[mydir]["path"] + [dir])
        totalSize += sizeOfDir(direcs, totalPath)
    totalSize += sum(direcs[mydir]["files"].values())
    return totalSize

# part 1
sizesOfSMallDirs = 0
for dir in dirs:
    sizeDir = sizeOfDir(dirs,dir)
    if sizeDir <= 100000:
        sizesOfSMallDirs += sizeDir
print(f"Day 7:\n1) The sum of the sizes of directories with size at most 100000 is \033[1m{ sizesOfSMallDirs }\033[0m.")

# part 2
currentFreeSpace = 70000000 - sizeOfDir(dirs, "/")
needToFree = 30000000 - currentFreeSpace
sizeDirToDelete = 70000000
deletingDir = ""
for dir in dirs.keys():
    size = sizeOfDir(dirs,dir)
    if needToFree <= size < sizeDirToDelete:
        sizeDirToDelete = size
        deletingDir = dir
print(f"2) There is currently only {currentFreeSpace} space free, so we need to free at least { needToFree }. We can do this by removing directory {deletingDir} which has size \033[1m{sizeDirToDelete}\033[0m.")