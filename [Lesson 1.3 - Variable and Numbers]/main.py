# Variables: A variable is a container of values, it actually behaves as tehe values that is stores

"""
Values: - Stores multiples data-types: int, bool, str, float
        - Helps the program to reuse the value stored in the variable multiple times without worrying about declaring it again
        - They can be resigned with new values that technically replace the previous ones
        - They help in calculation and provide code support
"""


name = input("What is your name? ")
age = int(input("What is your age? "))
gender = "Male"
weight = 182.277
country = "Kenya"
programming_language = "Python"
hobby = "Chess"
lovesReadingNovels = False

print(name + " is a "+ gender)
print(name + " is " + str(age) + " years old.")
print(name + " lives in the country of " + country)
print(name + " loves writing code in " + programming_language + " and other popular programming languages")
print(name + " hobby is playing " + hobby)
print(name + " weight is " + str(weight) + "lbs")
print("After 1 years " + name + "'s age will be " + str(age + 1))
print(name + " loves reading novels: " + str(lovesReadingNovels))

print()


# Note: By default the print function accepts only one data-type at a time
# We cannot mix strings with integers or floats so for that to work we cast the integers to strings
# The + symbol is used as a concatenation -- it is good for strings

# Using , in the print function opens up a new set of parameter
# and automatically puts in a free space before and after it

# Ex:
print("My name is:", name, "I'm", age, "years old")


# Checking variable types

# type(object, bases, dict)
# -- The dict contains the available properties if the object is a class
# -- The bases can be the parent or root classes or objects of the current called object

# Note : object.__class__ can be used as the alternative way to check for the type of a variable

print(type(name)) # <class 'str'>
print(name.__class__)  # <class 'str'>
print(type(weight))
