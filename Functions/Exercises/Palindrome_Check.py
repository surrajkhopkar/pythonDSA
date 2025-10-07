def is_palindrome(s):
    s = s.lower().replace(" ","")
    return s == s[::-1]

print(is_palindrome('ekitike'))
print(is_palindrome('gakpo'))
    
