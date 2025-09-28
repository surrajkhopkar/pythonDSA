# iterating over dictionaries

student = {"name":"Krish", "age": 25, "grade": 25}

# iterating over keys
for keys in student.keys():
    print(keys)

# ietrating over values
for values in student.values():
    print(values)

# iterate over key,value pairs
for key,value in student.items():
    print(f"{key}:{value}")
