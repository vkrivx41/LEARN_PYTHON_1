# f-string: is a feature poped out in python 3,
# and it is used to provide a cleaner way to format and display strings as long as other data types
import math
from datetime import datetime

first_name = "Kapulo"
last_name = "Pascal"

sentence_1 = "My name is " + first_name + " " + last_name
sentence_2 = f"My name is {first_name} {last_name}"
sentence_3 = f"My name is {first_name.upper()} {last_name.upper()}"

print(sentence_1)
print(sentence_2)
print(sentence_3)

# Formatting Dictionaries

student = {
    'name': "Scorpus",
    'marks': 99
}

sentence_4 = student['name'] + "ot g " + str(student['marks']) + "%"
sentence_5 = f"{student['name']} got {student['marks']}%"

print(sentence_4)
print(sentence_5)

# Calculation

sentence_6 = "4 times 11 is equal to " + str(4 * 11)
sentence_7 = f"4 times 11 is equal to {4 * 11}"

print(sentence_6)
print(sentence_7)

# Padding
# In order to add padding to numbers we add a colon - : and then
# write zero - 0 followed by the number of digits to be padded

for value in range(1, 10):
    sentence_8 = f"The value is {value: 02}"

    print(sentence_8)

# Float rounding -- automatic rounding
# We add a colon as an indicator of extra formatting followed by a
# dot and number of digits after the dot with the f prefix for the float specifier

pi = 3.14159265
e = math.e

sentence_9 = f"Pi is equal to {pi:.4f}"
sentence_10 = f"e is equal to {e:.3f}"

print(sentence_9)
print(sentence_10)

# Date formatting -- import datetime module
# For more date formatting keys look up on the python documentation or search online  or coreyms.com

birth_day = datetime(2004, 10, 4)

sentence_11 = f"Scorpus has a birthday on {birth_day:%B %d, %Y}"

print(sentence_11)

# Binary, Octal, Hexadecimal, E notation, and currency representation
# Binary => b, B, 0b
# Octal => o

number_1 = 891
number_2 = 67000000000

sentence_12 = f"{number_1} in binary is {bin(number_1)}"
sentence_13 = f"{number_1} in binary is {number_1: b}"
sentence_14 = f"{number_1} in octal is {number_1: o} or {oct(number_1)}"
sentence_15 = f"{number_1} in hexadecimal is {number_1: x} or {hex(number_1)}"
sentence_16 = f"{number_2} in Scientific Notation is {number_2: e}"
sentence_17 = f"{number_2} in currency format is {number_2:, }"

print(sentence_12)
print(sentence_13)
print(sentence_14)
print(sentence_15)
print(sentence_16)
print(sentence_17)

marks_1 = [72, 49, 91, 56]


def largerMarks(marks):
    return max(marks)


sentence_17 = f"The largest marks is {largerMarks(marks_1): 03}"
sentence_18 = f"The marks at the last position is {marks_1[-1]}"

print(sentence_17)
print(sentence_18)


