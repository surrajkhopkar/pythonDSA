# map multiple iterables

numbers1 = [1,2,3]
numbers2 = [3,4,5]

added_numbers = list(map(lambda x,y:x+y,numbers1,numbers2))
print(added_numbers)