# packing and unpacking tuple
packed_tuple = 1,2,3.14
print(packed_tuple)

# unpacking tuple
a,b,c = packed_tuple
print(c)

# unpacking with *
numbers = (1,2,3,4,5,6)
first,*middle,last = numbers
print(first)
print(middle)
print(last)
print(type(middle))