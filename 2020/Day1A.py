
text_file = open("input1.txt", "r")
input = text_file.read().split('\n')
text_file.close()

numbers = [ int(i) for i in input]

for i  in range(len(numbers)):
    a = numbers[i]
    for j in range(i,len(numbers)):
        b = numbers[j]
        if a + b == 2020:
            print("Het antwoord op de eerste vraag van dag 1 is:", a * b)
