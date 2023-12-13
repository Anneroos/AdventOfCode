with open("input13.txt") as f:
    fields = f.read().split("\n\n")


def find_reflection(strings, mistakes_goal):
    for mirror in range(1, len(strings)):
        mistakes = 0
        for refl in range(min(mirror, len(strings) - mirror)):
            mirroring = True
            if strings[mirror - refl - 1] != strings[mirror + refl]:
                if mistakes_goal == 0:
                    mirroring = False
                    break
                else:
                    for idx in range(len(strings[mirror - refl - 1])):
                        if strings[mirror - refl - 1][idx] != strings[mirror + refl][idx]:
                            mistakes += 1
                            if mistakes > mistakes_goal:
                                mirroring = False
                                break
        if mirroring and mistakes == mistakes_goal:
            return mirror
    return -1


total1 = 0
total2 = 0
for field in fields:
    rows = field.split()
    columns = ["".join([row[i] for row in rows]) for i in range(len(rows[0]))]

    # Part 1
    rowRefl = find_reflection(rows, 0)
    if rowRefl >= 0:
        total1 += 100 * rowRefl
    else:
        colRefl = find_reflection(columns, 0)
        total1 += colRefl

    # Part 2
    rowRefl = find_reflection(rows, 1)
    if rowRefl >= 0:
        total2 += 100 * rowRefl
    else:
        colRefl = find_reflection(columns, 1)
        total2 += colRefl

print(f"Day 13:\n1) The number I get after summarizing all of my notes is {total1}.")
print(f"2) After summarizing the new reflection line in each pattern in my notes, the number I get is {total2}.")