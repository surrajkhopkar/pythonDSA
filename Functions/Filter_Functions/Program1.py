def is_even(num):
    if num % 2 == 0:
        return True
    
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

print(list(filter(is_even,lst)))