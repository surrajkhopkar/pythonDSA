def temperature_converter(temp,unit):
    """This function converts temperature between Celcius and Fahrenheit"""
    if unit == "C":
        return (temp*9/5)+32
    elif unit  == "F":
        return (temp-32)*5/9
    
converted_temp = temperature_converter(39,"C")
print(converted_temp)

converted_temp1 = temperature_converter(101,"F")
print(converted_temp1)
    
