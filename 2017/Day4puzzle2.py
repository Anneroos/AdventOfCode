import pandas as pd
file = pd.read_csv(r"C:\Users\Anneroos/PycharmProjects/MijnEersteProject/puzzleinput3.txt", sep='\n',  header=None)

def checkPassPhrase(string):
    words = string.split(' ')
    # reorder each word
    words = list(map(lambda x: ''.join(sorted(x)), words))
    for i in range(len(words)):
        count = words.count(words[i])
        if(count>1): # not a valid pass phrase
            return False
    # otherwise it's valid!
    return True

# apply this function to every element in the 0th column of file
file2 = file[0].apply(checkPassPhrase)
answer = file2.sum() # True = 1, False = 0
print("This time there are ", answer, "valid pass phrases")



