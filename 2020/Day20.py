import numpy as np

with open("input20.txt") as f:
    piecesRaw = [x.split("\n") for x in f.read().split("\n\n")]

def flipArray(inputarray):
    newArray = np.zeros(len(inputarray))
    for i in range(len(inputarray)):
        newArray[i] = inputarray[len(inputarray)-1-i]
    return newArray

class Piece:
    def __init__(self, id, array):
        self.id = id
        self.array = array
        self.computeEdges()
        self.neighbors = []

    def computeEdges(self):
        self.top = self.array[0,:]
        self.left = self.array[:,0]
        self.bottom = self.array[9,:]
        self.right = self.array[:,9]
        self.edges = [self.left, self.top, self.right, self.bottom, flipArray(self.left), flipArray(self.top), flipArray(self.right), flipArray(self.bottom)]

    def addNeighbor(self, idx):
        self.neighbors.append(idx)

    def rotateRight(self):
        tempArray = np.zeros([10,10])
        for m in range(10):
            tempArray[:, 9-m] = self.array[m,:]
        self.array = tempArray
        self.computeEdges()

    def flip(self):
        tempArray = np.zeros([10,10])
        for m in range(10):
            tempArray[:,m] = self.array[:,9-m]
        self.array = tempArray
        self.computeEdges()





puzzle = []
piecesDict = {}
for pieceString in piecesRaw:
    piece = np.zeros([10,10])
    id = int(pieceString[0].split(" ")[1][0:4])
    for i in range(1,11):
        line  = list(pieceString[i])
        for j in range(10):
            if line[j] == "#":
                piece[i-1,j] = 1
    newPiece = Piece(id, piece)
    puzzle.append(newPiece)
    piecesDict[id] = newPiece


# print(puzzle)

for i in range(len(puzzle)):
    for j in range(i+1, len(puzzle)):

        piece_i = puzzle[i]
        piece_j = puzzle[j]
        for edge_i in piece_i.edges:
            for edge_j in piece_j.edges[:4]:
                if (edge_i == edge_j).all():
            # print(edge in piece_j.edges)
            # if edge in piece_j.edges:
            #         print("Found neighbor!")
                    piece_i.addNeighbor(piece_j.id)
                    piece_j.addNeighbor(piece_i.id)
                # else:
                    # print("not a neighbor")
multi = 1
corners = []
for piece in puzzle:
   if len(piece.neighbors) == 2:
       corners.append(piece.id)
       multi *= piece.id
print(f"Day 20 part 1: the product of the ID's of the corners is {multi}.")

# part 2, oh dear
solution = np.zeros([12*8,12*8])



toVisit = [(corners[2], 0, 0)]
visited = []

wherePiecesGo = {}
while len(toVisit)>0:
    (currentPiece_id, x, y) = toVisit.pop(0)
    # print(f"##################### {currentPiece_id} #######################")
    visited.append(currentPiece_id)
    wherePiecesGo[(x,y)] = currentPiece_id
    currentPiece = piecesDict[currentPiece_id]


    for neighbor in currentPiece.neighbors:

        neighborpiece = piecesDict[neighbor]
        found = False
        attempts = 0
        while attempts < 8 and not found:
            if attempts == 4:
                neighborpiece.flip()
            else:
                neighborpiece.rotateRight()

            if (currentPiece.right == neighborpiece.left).all(): # check right
                found = True
                if neighbor not in visited and (neighbor, x + 1, y) not in toVisit:
                    toVisit.append((neighbor, x + 1, y))
                    # print(f"Neighbor {neighbor} to the right at {x + 1, y}.")
                break
            elif (currentPiece.bottom == neighborpiece.top).all(): # check bottom
                found = True
                if neighbor not in visited and (neighbor, x, y + 1) not in toVisit:
                    toVisit.append((neighbor, x, y + 1))
                    # print(f"Neighbor {neighbor} to the bottom at {x, y + 1}.")
                break
            elif (currentPiece.left == neighborpiece.right).all(): # check left
                found = True
                if neighbor not in visited and (neighbor, x - 1, y) not in toVisit:
                    toVisit.append((neighbor, x - 1, y))
                    # print(f"Neighbor {neighbor} to the left at {x - 1, y}.")
                break
            elif (currentPiece.top == neighborpiece.bottom).all(): # check top
                found = True
                if neighbor not in visited and (neighbor, x, y-1) not in toVisit:
                    toVisit.append((neighbor, x, y - 1))
                    # print(f"Neighbor {neighbor} to the top at {x, y - 1}.")
                break
            attempts += 1




# print(wherePiecesGo)
minX = 0
minY = 0
for key in wherePiecesGo.keys():
    minX = min(key[0], minX)
    minY = min(key[1], minY)


for key in wherePiecesGo.keys():
    x = key[0] - minX
    y = key[1] - minY
    solution[y*8:y*8+8,x*8:x*8+8] = piecesDict[wherePiecesGo[key]].array[1:9,1:9]
# print(solution)



seamonsterString = ["                  # ","#    ##    ##    ###"," #  #  #  #  #  #   "]
seamonster = np.zeros([len(seamonsterString),len(seamonsterString[0])])
for i in range(len(seamonsterString)):
    line = seamonsterString[i]
    for j in range(len(line)):
        if line[j] == "#":
            seamonster[i, j] = 1

seamonsterParts = seamonster.sum()
# print("Seamonster has", seamonsterParts, "parts.")
# So now only search seamonsters

# print(solution.shape)
def rotateRight(array):
    tempArray = np.zeros(array.shape)
    for m in range(array.shape[0]):
        tempArray[:, array.shape[0]-1-m] = array[m,:]
    return tempArray

def flip(array):
    tempArray = np.zeros(array.shape)
    for m in range(array.shape[0]):
        tempArray[:,m] = array[:,array.shape[0]-1-m]
    return tempArray

seamonsterPlaces = np.zeros([12*8, 12*8])




round = 0
while round < 8:
    # print(round)
    if round == 4:
        solution = flip(solution)
        seamonsterPlaces = flip(seamonsterPlaces)
    else:
        solution = rotateRight(solution)
        seamonsterPlaces = rotateRight(seamonsterPlaces)

    for x in range(solution.shape[0] - seamonster.shape[0]):
        for y in range(solution.shape[1] - seamonster.shape[1]):


            test = (solution[x:x + seamonster.shape[0], y:y + seamonster.shape[1]] + seamonster == 2).sum()

            if test == seamonsterParts:
                seamonsterPlaces[x:x + seamonster.shape[0], y:y + seamonster.shape[1]] += seamonster


    round += 1

seamonsterPlaces[seamonsterPlaces>1] = 1

print(f"The habitat's water roughness is {(solution - seamonsterPlaces).sum()}.")

import matplotlib.pyplot as plt
showSeaMonsters = solution+seamonsterPlaces
for i in range(5):
    if i == 1:
        showSeaMonsters = flip(showSeaMonsters)
    else:
        showSeaMonsters = rotateRight(showSeaMonsters)
plt.imshow(showSeaMonsters)
plt.colorbar()
plt.show()
# solution + seamonsterPlaces