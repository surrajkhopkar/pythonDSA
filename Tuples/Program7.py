# iterate through nested tuples
tup = ((1,2,3),("abd",3.14,"def"),["joe","bidden","usa"])
for sub_tup in tup:
    for item in sub_tup:
        print(item,end=" ")
