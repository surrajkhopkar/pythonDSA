# shallow copy

student = {"name":"Krish", "age": 25, "grade": 25}
student_copy = student
print(student)
print(student_copy)

student['salary'] = 100
print(student)
print(student_copy)

# shallow copy creates different memory location

student1 = {"name":"Krish", "age": 25, "grade": 25}
student2 = student1.copy()
print(student1)
print(student2)

student1['salary'] = 100
print(student1)
print(student2)

