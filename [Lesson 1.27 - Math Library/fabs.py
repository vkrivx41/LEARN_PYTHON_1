
# fabs: is a math method that returns the absolute value of the input -- excludes the sign


"""
Values: - the builtin abs() function does the same also, there is no need of import the method for just this operation
       - the difference btn math.fabs() and abs() is that fabs returns a float, while abs returns an integer
"""

from math import fabs

number_1: float = -82.4
number_2: float = 50
number_3: float = -10

# math.fabs(number: int|float) -> float

fab_1 = fabs(number_1)
fab_2 = fabs(number_2)
fab_3 = fabs(number_3)

print(fab_1, fab_2, fab_3)


# abs(number: int|float) -> int

abs_1 = abs(number_1)
abs_2 = abs(number_2)
abs_3 = abs(number_3)

print(abs_1, abs_2, abs_3)
