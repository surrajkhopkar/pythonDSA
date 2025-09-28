# list comprehensions

lst = []

for x in range(10):
    lst.append(x**2)

print(lst)

# basic syntax
print([x**2 for x in range(10)])

# with conditional logic
print([x**2 for x in range(10) if x%2 == 0])

