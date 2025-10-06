def print_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_details(name="Firmino", age=36, salary=1000,team="Fluminese")


## Combining positional and keyword arguments

def print_details1(*args, **kwargs):
    for arg in args:
        print(f"Positional argument: {arg}")
    for key,value in kwargs.items():
        print(f"{key}:{value}")

print_details1(1,2,3,4,5,"liverpool", 44.5, 6600, name="Firmino", age=36, salary=1000,team="Fluminese")