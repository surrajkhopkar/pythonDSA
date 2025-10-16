people = [
    {'name': 'joe','age':24},
    {'name': 'jolly','age':34}
]

def get_name(person):
    return person['name']

print(list(map(get_name,people)))