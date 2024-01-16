
# 11: index(character, string: mandatory, start: optional, end: optional)
# => returns the index of the provided sequence of characters or string
# Note: once the provided string or character is not found, a ValueError is issued
# Advice: Not the recommended alternative to the find() function

text_1: str = "Scorpus is gonna rule the world!"

print(text_1.index('world'))
print(text_1.index('Scorpus'))
# print(text_1.index('world', 0, 4)) ValueError: substring not found


# 12: isalnum()
# => Returns True if the string contain alpha numeric digits or a mixture of both alphabets and numbers, otherwise False
# Long: is alpha numeric

numeric_1 = "ivx410"
numeric_2 = "2348903"
numeric_3 = "Scorpus"
numeric_4 = "Scorpus$#"

print(numeric_1.isalnum())
print(numeric_2.isalnum())
print(numeric_3.isalnum())
print(numeric_4.isalnum())

# 13: isalpha()
# => Returns True if the string contain only alphabets otherwise False
# Long: is alpha

numeric_1 = "ivx410"
numeric_2 = "ivx"

print(numeric_1.isalpha())
print(numeric_2.isalpha())

# 13: isascii()
# => Returns True if the string contain only characters available in the ASCII table otherwise False
# Long: is ascii

numeric_1: str = "❤"
numeric_2: str = "ivx#!"

print(numeric_1, numeric_2)
# print(numeric_1.isascii())
# print(numeric_2.isascii())

# 15: isdecimal()
# => checks if a given string is a decimal and then returns True otherwise, False
# Note: Returns also False when a floating point number is passed in

numeric_1 = "1234567890"
numeric_2 = "46.89"

print(numeric_1.isdecimal())
print(numeric_2.isdecimal())

# 16: isdigit()
# => checks if a given string is a decimal, digit, or a numeric symbol and then returns True otherwise, False
# Note: Returns also False when a floating point number is passed in

numeric_1 = "1234567890"
numeric_2 = "¹²³⁴⁵⁶⁷⁸⁹⁰"
numeric_3 = "46.89"

print(numeric_1.isdigit())
print(numeric_2.isdigit())
print(numeric_3.isdigit())


# 17: isnumeric()
# => checks if a given string is a decimal, digit, numeric symbol, or a foreign language numeric symbol
# (ex: japanese, romans, etc) and then returns True otherwise, False
# Note: Returns also False when a floating point number is passed in

numeric_1 = "1234567890"
numeric_2 = "¹²³⁴⁵⁶⁷⁸⁹⁰"
numeric_3 = "一二三四"
numeric_4 = "46.89"


print(numeric_1.isnumeric())
print(numeric_2.isnumeric())
print(numeric_3.isnumeric(), numeric_3)
print(numeric_4.isnumeric())

# 18: isidentifier()
# => checks if a given string is a valid sample of a python identifier name

identifier_1 = "varaiable_1"
identifier_2 = "varaiable-1"
identifier_3 = "1varaiable"
identifier_4 = "varaiable&"

print(identifier_1.isidentifier())
print(identifier_2.isidentifier())
print(identifier_3.isidentifier())
print(identifier_4.isidentifier())


# 19: islower()
# => Return True if the string is in lowercase otherwise False

case_1 = "hello"
case_2= "Hello"
case_3 = "HELLO"

print(case_1.islower())
print(case_2.islower())
print(case_3.islower())
print("HELlo".lower().islower())

# 20: isprintable()
# => Returns True if the string is printable, this means that if it doesn't
# have any newline escape sequence (\n, \t, ...)

printable_1 = "hello"
printable_2 = "hello\n"
printable_3 = "hello\t"

print(printable_1.isprintable())
print(printable_2.isprintable())
print(printable_3.isprintable())

