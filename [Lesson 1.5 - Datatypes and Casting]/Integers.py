# Integer: integers are a fundamental data type used to represent whole numbers,
#           both positive and negative, without any fractional or decimal part.

"""
Values: - Used for calculations and math operations
        - Integers in python have an unlimited precision: Python's integers have unlimited precision,
                meaning they can be arbitrarily large or small, limited only by available memory.
                This is in contrast to some other programming languages with fixed-size integers.
        - Using the int() function to cast values doesn't round up the numbers -- but floors
        - The int() function can not cast strings with floating points Ex: 13.85, 45.09 etc
"""

number_1 = 10
number_2 = '5'
number_3 = 13.95

print(number_1, type(number_1))
print(number_2, type(number_2))
print(number_3, type(number_3))

# number_3 = number_1 + number_2  => unsupported operand
# solution

number_2 = int(number_2)

number_4 = number_1 + number_2
number_5 = number_1 + number_3  # expression will resolve to a float result
number_6 = number_1 + int(number_3)

print(number_4)
print(number_5, number_5.__class__)
print(number_6, number_6.__class__)

number_7 = "13.87"
print(number_7, number_7.__class__)

# number_7 = int(number_7)
print(number_7, number_7.__class__)

number_8 = '-90'
print(int(number_8) * 10)

# Integer formatting
# => Underscores can be used to format long integers for the programmer just for readability purposes.

number_9 = 100_000
number_10 = -670_900_000_001

print(number_9, number_10)

# Exponential and Mantissa
# => Integers in python can be written in exponential form
# => Once integers are written in exponential form they are automatically casted to floats

number_11 = 100e3  # 10 * 10 ^ 3
number_12 = 5e-2  # 5 * 10 ^ -2

print(number_11, number_12)

# Limitation
# =>Python integers have no exact precision -- they can flow up to the device memory limit.

print(4567890987653456789987654457890987456789 * 4678934567890987654345678987654345678 * 9876543456789098765456788765456)


# Hexadecimal and Binary representation
# => Python allows you to represent integers in hexadecimal (base 16)
# and binary (base 2) notations using the 0x and 0b prefixes, respectively.

number_13 = 0b1001  # => 9
number_14 = 0x15  # => 21

print(number_13, number_14)


# Conversion

number_15 = 56
number_16 = 0x0 + number_15

print(number_16.to_bytes(10, "big"))
