text_file = open("input6.txt", "r")
groups = text_file.read().split('\n\n')
text_file.close()
questionsTotal = 0
for group in groups:
    group = group.replace("\n","")
    questions = []
    for i in group:
        if i not in questions:
            questions.append(i)
    questionsTotal += len(questions)

print("questionsTotal", questionsTotal)