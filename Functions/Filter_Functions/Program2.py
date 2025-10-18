# filter function with lambda function

numbers = [1,2,3,4,5,6,7,8,9,10]
greater_than_five = list(filter(lambda x:x>5,numbers))
print(greater_than_five)

# filter with lambda function and multiple conditions

numbers = [1,2,3,4,5,6,7,8,9,10]
even_greater_than_five = list(filter(lambda x:x%2==0 and x>5, numbers))
print(even_greater_than_five)