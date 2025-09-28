# use the dictionary to count the frequency of elements in the list
numbers = [1,1,1,2,2,2,3,3,3,4,4,5,5,6,6,7,7,7,8,8]
frequency = {}
for number in numbers:
    if number in frequency:
        frequency[number]+=1
    else:
        frequency[number]=1
print(frequency)

    