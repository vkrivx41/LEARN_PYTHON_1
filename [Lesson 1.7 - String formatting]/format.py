
# .format() => the format() function is a special string function used to provide
# advanced string formatting methods to simplify readability and improved UX

"""
Values: - It uses placeholders that later take values through the parameter list
"""
import math
from datetime import datetime

first_name = "Kapulo"
last_name = "Pascal"

sentence_1 = "My name is {} {}".format(first_name, last_name)
sentence_2 = "My name is {} {}".format(first_name.upper(), last_name.upper())

print(sentence_1)
print(sentence_2)


# Formatting Dictionaries

student = {
    'name': "Scorpus",
    'marks': 99
}

sentence_3 = "{} got {}% in the Brain test".format(student['name'], student['marks'])

print(sentence_3)

# Calculation

sentence_4 = "4 times 11 is equal to {}"
sentence_5 = sentence_4.format(4 * 11)

print(sentence_5)


# Padding

for value in range(1, 10):
    sentence_6 = "The value is {:02}".format(value)

    print(sentence_6)


# Float rounding

pi = 3.14159265
e = math.e

sentence_7 = "Pi is equal to {:.4f}".format(pi)
sentence_8 = "e is equal to {:.3f}".format(e)

print(sentence_7)
print(sentence_8)

# Date manipulation

birth_day = datetime(2004, 10, 4)

sentence_11 = "Scorpus has a birthday on {:%B %d, %Y}".format(birth_day)

print(sentence_11)


# Binary, Octal, Hexadecimal, E notation, and currency representation
# Binary => b, B, 0b
# Octal => o

number_1 = 891
number_2 = 67000000000

sentence_10 = "{} in binary is {}".format(number_1, bin(number_1))
sentence_11 = "{} in binary is {:b}".format(number_1, number_1)
sentence_12 = "{} in octal is {:o} or {}".format(number_1, number_1, number_1)
sentence_13 = "{} in hexadecimal is {:x} or {}".format(number_1, number_1, number_1)
sentence_14 = "{} in Scientific Notation is {:e}".format(number_2, number_2)
sentence_15 = "{} in currency format is {:,}".format(number_2, number_2)


print(sentence_10)
print(sentence_11)
print(sentence_12)
print(sentence_13)
print(sentence_14)


# Using indexed placeholders
# This reduced duplicate in the format() function's parameter list

tag_1 = "h1"
tag_2 = "p"
text_1 = "This is a headline"
text_2 = "This is a paragraph"

sentence_16 = "<{0}>{1}<{0}>".format(tag_1, text_1)
sentence_17 = "<{0}>{1}<{0}>".format(tag_2, text_2)

print(sentence_16)
print(sentence_17)


student = {
    'name': "Scorpus",
    'marks': 99
}


sentence_18 = "{0[name]} got {0[marks]}% in the Brain Test".format(student)

print(sentence_18)

# Using key-value pairs

sentence_19 = "My name is {first_name} {last_name}".format(first_name="Kapulo", last_name="Pascal")
sentence_20 = "My name is {first_name} {last_name}".format(last_name="Pascal".upper(), first_name="Pascal".upper())

print(sentence_19)
print(sentence_20)


# With lists or tuples
# Note: Using a negative symbol in the string with the format fucntion raises an error
# TypeError: tuple indices must be integers or slices, not str

marks_1 = 45, 56, 24, 98, 78, 67
marks_2 = marks_1 + (69, 71, 90)

sentence_21 = "The first marks in the list is {0[0]} and the last marks in list two is {1[8]}".format(marks_1, marks_2)

print(sentence_21)


def student():
    return {
        'name': "Scorpus",
        'marks': 99,
    }


sentence_22 = "{0[name]} got {0[marks]}%".format(student())

print(sentence_22)
