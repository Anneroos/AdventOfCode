# with open("input11.txt") as f:
#     numbers = [int(i) for i in f.read().split()]
#
# class Stone:
#     def __init__(self, number):
#         self.number = number
#         self.before = None
#         self.after = None
#
#     def setStoneBefore(self, before):
#         self.before = before
#         return self
#
#     def setStoneAfter(self, after):
#         self.after = after
#         return self
#
#     def blink(self):
#
#         # If             the             stone is engraved       with the number 0, it is replaced by a stone engraved with the number 1.
#         if self.number == 0:
#             # print("First rule, 0->1")
#             self.number = 1
#         # If            the             stone is engraved  with a number that has an even number of digits, it is replaced by two stones.The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone.(The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
#         elif len(str(self.number))%2 == 0:
#             # print(f"Second rule, even number of digits. Replace by two stones. {self.number}")
#             n = int(len(str(self.number))/2)
#
#             n1 = int(str(self.number)[0:n])
#             n2 = int(str(self.number)[n:])
#             # print(n1,n2)
#             newStone = Stone(n1)
#             self.number = n2
#             self.before.setStoneAfter(newStone)
#             newStone.setStoneBefore(self.before)
#             newStone.setStoneAfter(self)
#             self.before = newStone
#         # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
#         else:
#             # print("RUle 3, times 2024")
#             self.number = self.number * 2024
#
# startStone = Stone(-1)
# prevStone = startStone
# for n in numbers:
#     newStone = Stone(n)
#     newStone.setStoneBefore(prevStone)
#     prevStone.setStoneAfter(newStone)
#     prevStone = newStone
#
# def stonesAsList():
#     prevStone = startStone
#     listOfNumbers = []
#     while prevStone.after is not None:
#         stone = prevStone.after
#         listOfNumbers.append(stone.number)
#         prevStone = stone
#     return listOfNumbers
#
# def blink():
#     prevStone = startStone
#     while prevStone.after is not None:
#         stone = prevStone.after
#         stone.blink()
#         prevStone = stone
#
#
# for i in range(25):
#     # print(f"After blink {i+1}")
#     blink()
#
# stones = stonesAsList()
# # print(stones)
# print(len(stones))
#
# for i in range(50):
#     # print(f"After blink {i+1}")
#     blink()
#
# stones = stonesAsList()
# # print(stones)
# print(len(stones))
# # Initial arrangement:
# # 125 17
# #
# # After 1 blink:
# # 253000 1 7
# #
# # After 2 blinks:
# # 253 0 2024 14168
# #
# # After 3 blinks:
# # 512072 1 20 24 28676032
# #
# # After 4 blinks:
# # 512 72 2024 2 0 2 4 2867 6032
# #
# # After 5 blinks:
# # 1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32
# #
# # After 6 blinks:
# # 2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2



with open("input11.txt") as f:
    numbers = [int(i) for i in f.read().split()]
    stones = {n: numbers.count(n) for n in numbers}

def blink(stoneList):
    # print("Blink! Current stone list: ",stoneList)
    newStoneList = {}
    for n in stoneList.keys():
        # print(f"-- Stone {n}, nr of appearances {stoneList[n]} ")
        # If             the             stone is engraved       with the number 0, it is replaced by a stone engraved with the number 1.
        if n == 0:
            # print("First rule, 0->1")
            newStoneList[1] = newStoneList.get(1,0) + stoneList[0]

        # If            the             stone is engraved  with a number that has an even number of digits, it is replaced by two stones.The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone.(The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
        elif len(str(n))%2 == 0:
            # print(f"Second rule, even number of digits. Replace by two stones. {n}")
            nby2 = int(len(str(n))/2)

            n1 = int(str(n)[0:nby2])
            n2 = int(str(n)[nby2:])
            # print(n1,n2)
            newStoneList[n1] = newStoneList.get(n1,0) + stoneList[n]
            newStoneList[n2] = newStoneList.get(n2, 0) + stoneList[n]

        # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
        else:
            # print("RUle 3, times 2024")

            newStoneList[n*2024] = stoneList[n]
        # stoneList.pop(n, None)
    return newStoneList

for i in range(25):
    print(f"After blink {i+1}")
    stones = blink(stones)
    print(sum(stones.values()))
#
for i in range(25,75):
    print(f"After blink {i+1}")
    stones = blink(stones)
    print(sum(stones.values()))