# Booleans: Booleans are a fundamental data type used to only two possible values: True or False

"""
Values: - The result is either True or False -- these values are case-sensitive
        - Basically used in decision making and controlling the flow of the program
        - Building block of control flow statements
        - The builtin constructor bool() cast the value to bool - zero or empty values as handled as False otherwise True
"""

number_1 = 10
number_2 = 5

number_3 = number_1 > number_2
number_4 = number_2 == number_1

print(number_3, number_4)

# Logical operations
# or, and, not -- case-sensitive

x = True
y = False

print(x or y)  # Either x or y must be True and yes x is True
print(x and y)  # Both x and y must be True and not y is not True
print(not y)  # The opposite of y -- which in this case is True

# Casting
# Only zero and empty is casted to False

value_1 = bool(0)
value_2 = bool()
value_3 = bool("56789")
value_4 = bool(True)
value_5 = bool(-18.9)

print(value_1, value_2, value_3, value_4, value_5)

# Calculations
# True => 1 and False => 0

value_6 = False + 1  # 0 + 1
value_7 = True - False  # 1 - 0
value_8 = True / 5  # 1 / 5
value_9 = True * False  # 1 * 0
value_10 = False - 10  # 0 - 10

print(value_6, value_7, value_8, value_9, value_10)

# Comparison

value_11 = True == 1
value_12 = False == 0
value_13 = True > False

print(value_11, value_12, value_13)


# Int casting

value_14 = int(True)
value_15 = int(False)
value_16 = int(True * 9)
value_17 = float(True)
value_18 = str(False)

print(value_14, value_15, value_16, value_17, value_18)
