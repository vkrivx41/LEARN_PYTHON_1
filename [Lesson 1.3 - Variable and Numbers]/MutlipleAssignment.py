
# Multiple Assignment => Allows us to assign values or a value to multiple variables using a single line of code


"""
Values: - Assignment follows the position order of the variables
        - The values are stored in tuples or list -- although they are written with no () or []
        - The values are unpacked from right to the corresponding variable on left
        - The count of the value must be equal to the length of variables
"""

# Before

name = "Pascal"
age = 18
favoriteColor = "Yellow"
attractive = True

# After

name, age, favoriteColor, attractive = "Bruno", 68, "Black", False
name, age, favoriteColor, attractive = ["Marshal", 16, "Green", True]
name, age, favoriteColor, attractive = ("Brian", 78, "Pink", True)

print(type(name), type(age))  # str int
print(name, age, favoriteColor, attractive)


# Note: This approach can also be used to assign a single value to multiple variables

# Before

pascalsAge = 89
briansAge = 89
brunosAge = 89

# After

pascalsAge = briansAge = brunosAge = 89
pascalsAge = briansAge = brunosAge = 89 - 1

print(pascalsAge, briansAge, brunosAge)

