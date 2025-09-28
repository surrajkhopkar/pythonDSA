# merge two dictionaries into one
dict1 = {"a":1,"b":2,"c":3}
dict2 = {"b":1,"c":4,"d":5}

# keyword arguments - any arguments which are present in the form of key-value pairs
merged_dict={**dict1,**dict2}
print(merged_dict)
