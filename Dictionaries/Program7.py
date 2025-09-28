# nested dictionaries
students = {
    "student1" : {"name":"Krish", "age": 45, "grade": 44},
    "student2" : {"name":"Anand", "age": 33, "grade": 22},
    "student3" : {"name":"Rock", "age": 66, "grade": 77}
}
print(students)

# access nested dictionary elements
print(students["student2"]["age"])
print(students["student2"]["grade"])

# iterating over nested dictionaries
for student_id,student_info in students.items():
    print(f"{student_id}:{student_info}")
    for key,value in student_info.items():
        print(f"{key}:{value}")

