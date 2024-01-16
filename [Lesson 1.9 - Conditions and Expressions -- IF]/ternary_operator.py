
# Ternary operator: is a short form of expressing a if statement on a single line

"""
Values: - limited only to problems with a maximum of two expressions
        - Can not perform elif statements
"""

red_lights: bool = False
green_lights: bool = True

number_1: int = 34
# if approach
# 1
if red_lights and not green_lights:
    print("Stop")
else:
    print("Go")

# 2

if number_1 % 2 == 0:
    print("Even")
else:
    print("Odd")


# ternary approach
# All the expression and the else statement id put on a single line

expression_1 = "Stop" if red_lights and not green_lights else "Go"
expression_2 = "Even" if number_1 % 2 == 0 else "Odd"

print(expression_1)
print(expression_2)

# Using functions


def is_even(number):
    return number % 2 == 0


# if approach

if is_even(number_1):
    print("EVen")
else:
    print("Odd")

# ternary approach

expression_3 = "Even" if is_even(number_1) else "Odd"

print(expression_3)
