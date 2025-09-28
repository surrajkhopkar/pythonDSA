# mathematical operations
# union operation i.e combine all the elements.

set1 = {1,2,3,4,5,6,7}
set2 = {4,5,6,7,8,9,10}

print(set1.union(set2))

# intersection i.e. common elements

print(set1.intersection(set2))

# intersection update all the common elements from set1 and set2 will be updated to set1

set1.intersection_update(set2)
print(set1)

# difference

set1 = {1,2,3,4,5,6,7}
set2 = {4,5,6,7,8,9,10}

print(set1.difference(set2))
set1.difference_update(set2)
print(set1)