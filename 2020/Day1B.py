text_file = open("input1.txt", "r")
input = text_file.read().split('\n')
text_file.close()

numbers = [ int(i) for i in input]

for i  in range(len(numbers)):
    a = numbers[i]
    for j in range(i,len(numbers)):
        b = numbers[j]
        for k in range(j, len(numbers)):
            c = numbers[k]
            if a + b + c == 2020:
                print("Het antwoord op de tweede vraag van dag 1 is:", a*b*c)




