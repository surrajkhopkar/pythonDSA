my_set = {1,2,3,4,5,6}

# add an element
my_set.add(7)
print(my_set)

# remove an element and if not present throw error
my_set.remove(11)
print(my_set)

# remove an element if present and ignore the error if not present
my_set.discard(11)
print(my_set)

# remove any random element
my_set.pop()
print(my_set)