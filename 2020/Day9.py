text_file = open("input9.txt", "r")
numbers = text_file.read().split('\n')
text_file.close()
numbers = [int(i) for i in numbers]
# Part 1
for i in range(25,len(numbers)):
    number = numbers[i]
    valid = False
    for k in range(i-25,i):
        numberk = numbers[k]
        for l in range(k+1,i):
            numberl = numbers[l]
            if numberl != numberk and number == numberk+numberl:
                valid = True
    if not valid:
        invalidnumber = number
        break
print(f"The first invalid number is{invalidnumber}.")

# Part 2
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        list = numbers[i:j+1]
        sum = 0
        for k in list:
            sum += k
        if sum == invalidnumber:
            minnr = min(list)
            maxnr = max(list)
            print(f"I found the following list of numbers that add up to the invalid number: {list}.")
            print(f"The smallest number in that list is {minnr} and the biggest number is {maxnr}. They add up to {minnr + maxnr}, which is the answer of the second question.")
        elif sum > invalidnumber:
            break

        # print(sum,list)