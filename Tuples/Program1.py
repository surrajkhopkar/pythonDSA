#empty tuple
empty_tuple = ()
print(empty_tuple)
print(type(empty_tuple))

#convert list to tuple
lst = [1,2,3]
tup = tuple(lst)
print(tup)

#convert tuple to list
tup = (1,2,3)
lst = list(tup)
print(lst)

#mixed tuple
mixed_tuple = (1,"hello", 3.14, [1,2,3],{"name":"joe","place":"india"})
print(mixed_tuple)