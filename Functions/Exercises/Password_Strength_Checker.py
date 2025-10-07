def is_strong_password(password):
    """This function checks if password id strong or not"""
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$%^&*_+' for char in password):
        return False
    return True

print(is_strong_password('Liverpool@2025'))
print(is_strong_password('Liverpool05'))
print(is_strong_password('qwertyuiopasdf'))
print(is_strong_password('asbnf'))
    

    