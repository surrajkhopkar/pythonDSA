# modifying dictionary elements

student = {"name":"Krish", "age": 25, "grade": 25}
print(student)
student['age'] = 45
student['address'] = 'india'

print(student)

# delete key value pair
del student['grade']
print(student)