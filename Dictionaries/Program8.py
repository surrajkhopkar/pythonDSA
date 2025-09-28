# dictionary comprehension
squares = {x:x**2 for x in range(10)}
print(squares)

# conditional dictionary comprehension
squares = {x:x**2 for x in range(10) if x%2==0}
print(squares)
