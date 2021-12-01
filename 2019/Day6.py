
text_file = open("input6.txt", "r")
input = text_file.read().split('\n')
text_file.close()
# lines = np.array(input)
orbitDict = {'COM':{"prev":"none", "next":list(), "orbits":0, "distanceToSanta" : -1 }}
for x in input:
    base = x[:3]
    orbit = x[4:]
    # print(x,base,orbit)

    if base in orbitDict.keys():
        orbitDict.get(base)["next"].append(orbit)
        # print(orbitDict.get(base)["next"])

    else:
        orbitDict[base] = {"prev":"none", "next":[orbit], "orbits":0, "distanceToSanta" : -1 }



    if orbit in orbitDict.keys():
        orbitDict[orbit]["prev"] = base
    else:
        orbitDict[orbit] = {"prev":base, "next": [], "orbits":0, "distanceToSanta" : -1 }

print(orbitDict)
print("SANTA",orbitDict["SAN"])

checklist = ["COM"]

while len(checklist) > 0 :

    planet = checklist.pop(0)
    # print(planet, orbitDict[planet]["next"],orbitDict[planet]["orbits"]  )
    for place in orbitDict[planet]["next"]:
        checklist.append(place)
        orbitDict[place]["orbits"] = orbitDict[planet]["orbits"] + 1

totalNrOfOrbits = 0

for planet in orbitDict.keys():
    totalNrOfOrbits += orbitDict[planet]["orbits"]
print("tadaaa",totalNrOfOrbits)


orbitDict["SAN"]["distanceToSanta"] = -1
checklist2 = ["SAN"]
while len(checklist2) > 0:
    planet = checklist2.pop(0)
    print(planet)
    for place in orbitDict[planet]["next"]:
        print("--- ", place)
        if orbitDict[place]["distanceToSanta"] == -1 or orbitDict[place]["distanceToSanta"] > (orbitDict[planet]["distanceToSanta"] + 1):
            checklist2.append(place)
            orbitDict[place]["distanceToSanta"] = orbitDict[planet]["distanceToSanta"] + 1
    if planet != "COM":
        prev = orbitDict[planet]["prev"]
        print(prev)
        if orbitDict[prev]["distanceToSanta"] == -1 or orbitDict[prev]["distanceToSanta"] > (orbitDict[planet]["distanceToSanta"] + 1):
            checklist2.append(prev)

            orbitDict[prev]["distanceToSanta"] = orbitDict[planet]["distanceToSanta"] + 1

print(orbitDict["YOU"])
print(orbitDict["SAN"])