# filter to check if age is greater than 25 in dictionaries

people = [
    {"name": "joe", "age": 34},
    {"name": "jose", "age": 24},
    {"name": "jade", "age": 26},
    {"name": "jolly", "age": 14},
]

def age_greater_than_25(person):
    return person['age'] > 25

greater_than_twentyfive = list(filter(age_greater_than_25, people))
print(greater_than_twentyfive)