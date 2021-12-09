input = "11011110011011101"
import time

def dragonStep(string):
    # return string + "0" + "".join(["0" if string[len(string)-i-1] == "1" else "1" for i in range(len(string))])
    # return string + "0" + "".join(["0" if i == "1" else "1" for i in reversed(list(string))])
    return string + "0" + "".join([str(1 - int(i)) for i in reversed(list(string))])

def computeChecksum(string):
    string = string
    while len(string) % 2 == 0:
        string = "".join(["1" if  string[2*i] == string[2*i + 1]  else "0" for i in range(int(len(string)/2))])
    return string

def dragonChecksum(string, disksize):
    disksize = disksize
    string = string
    while len(string) < disksize:
        string = dragonStep(string)
    mid_time = time.time()
    print("Time after dragonsteps", mid_time - start_time)
    string = string[0:disksize]
    checksum = computeChecksum(string)
    mid_time = time.time()
    print("Time after checksum", mid_time - start_time)
    return checksum

start_time = time.time()
print(f"Part 1: The dragon checksum for a disk of size 272 is {dragonChecksum(input, 272)}.")
mid_time = time.time()
print(mid_time-start_time)
print(f"Part 2: The dragon checksum for a disk of size 3565184 is {dragonChecksum(input, 35651584)}.")
end_time = time.time()
print(end_time-start_time)


# TRYING DIFFERENT THINGS, BUT I WILL STAY SLOOOWWWW
input = "11011110011011101"
# input = "100"
import time
start_time = time.time()

def computeChecksum(string):
    string = string
    while len(string) % 2 == 0:
        string = "".join(["1" if  string[2*i] == string[2*i + 1]  else "0" for i in range(int(len(string)/2))])
    return string

def dragonChecksum(string, disksize):
    disk = {} #[None]*disksize
    disk = dict(zip(range(len(string)), [int(i) for i in list(string)]))
    print(disk)

    pointer = len(string)
    while disksize-1 not in disk:
        print(pointer)
        disk[pointer] = 0
        for i in range(pointer+1,min(2*pointer+1,disksize)):
            disk[i] = 1-disk[2*pointer-i]
        pointer = 2* pointer + 1
    mid_time = time.time()
    print(mid_time - start_time)
    checksum = "".join([str(disk[i]) for i in range(disksize)])

    while len(checksum) % 2 == 0:
        # print(len(checksum))
        checksum = "".join(["1" if  checksum[2*i] == checksum[2*i + 1]  else "0" for i in range(int(len(checksum)/2))])

    return checksum


print(f"Part 1: The dragon checksum for a disk of size 272 is {dragonChecksum(input, 272)}.")
mid_time = time.time()
print(mid_time-start_time)

print("start part 2")
print(f"Part 2: The dragon checksum for a disk of size 3565184 is {dragonChecksum(input, 35651584)}.")
end_time = time.time()
print(end_time-start_time)