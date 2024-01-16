# Floats: floats are a fundamental data type used to represent decimal numbers,
#           both positive and negative, with fractional or decimal part.

"""
Values: - Used for calculations and math operations
        -  Due to the finite precision of floats, some decimal numbers cannot be represented exactly
        - Python's float numbers are implemented using the IEEE 754 standard for floating-point arithmetic.
        This standard provides a fixed amount of precision (typically 64 bits or double-precision), which means that
        not all real numbers can be exactly represented. This can lead to issues with rounding and precision for some operations.
        - Using the float() function to cast values doesn't round up the numbers -- but floors
        - The float() function can cast strings with floating points Ex: 13.85, 45.09 etc
"""


number_1 = 1.9
number_2 = 45
number_3 = '78.01'

print(number_1, number_1.__class__)
print(number_2, number_2.__class__)
print(number_3, number_3.__class__)


number_4 = number_1 + number_2
print(number_4)

# number_5 = number_1 + number_3  => unsupported operand
number_3 = float(number_3)

number_5 = number_1 + number_3
print(number_5, round(number_5, 2))

# Float formatting
# => Underscores can be used to format long floats for the programmer just for readability purposes.

number_6 = 100_000.09
number_7 = -6.970_900_000_001

print(number_6, number_7)


# Exponential and Mantissa
# => Floats in python can be written in exponential form

number_8 = 10.05e3  # 10 * 10 ^ 3
number_9 = -5.5e-2  # 5 * 10 ^ -2

print(number_8, number_9)


# Hexadecimal and Binary representation
# => Python doesn't allows you to represent floats in hexadecimal (base 16)
# and binary (base 2) notations using the 0x and 0b prefixes, respectively.

# number_10 = 0b1001.101  # => 9
# number_11 = 0x15.6  # => 21

# print(number_10, number_11)


# Decimal Representation
# Due to casting the initial precision is 16 more digits after the point

number_10 = 0.1
number_11 = 0.1
number_12 = 0.1

number_13 = number_12 + number_11 + number_10
print(number_13)  # => 0.30000000000000004: Due to casting
print(round(number_13, 20))


# number_13 will be greater than 0.3 due to casting

print(number_13 > .3)  # True


# Division
# => Automatic division in python technically converts the result to a float

number_14 = 9
number_15 = 4
number_16 = 3

number_17 = number_14 / number_15
number_18 = number_14 / number_16

print(number_17)
print(number_18, number_18.__class__)

# Flow division
# Flow division or double-dash division converts the result to an int after rounding it.


number_14 = 19

number_19 = number_14 // number_15
print(number_19)
