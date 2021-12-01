text_file = open("input6.txt", "r")
groups = text_file.read().split('\n\n')
text_file.close()
questionsTotal = 0
for group in groups:
    peepsAnswers = group.split("\n")
    nrOfPeepsInGroup = len(peepsAnswers)
    if len(peepsAnswers) == 1:
        questionsTotal += len(peepsAnswers[0])
    else:
        questionsGroupAll = 0
        for question in peepsAnswers[0]:
            allYes = True
            for peep in peepsAnswers[1:]:
                if question not in peep:
                    allYes = False
                    break
            if allYes:
                questionsGroupAll += 1
        questionsTotal += questionsGroupAll


print("questionsTotal", questionsTotal)

