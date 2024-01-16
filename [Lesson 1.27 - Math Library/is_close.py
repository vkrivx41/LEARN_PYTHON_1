# isclose: return True if number_1 and number_2 are close to each other, otherwise False

"""
Values: - Syntax: isclose(a, b, rel_tol, abs_tol)
        - this method is generally used in comparison of floats
        - rel_tol: (default 1e-9) is the Relative Tolerance,
                it is multiplied to the largest number (a or b), and the smaller input value must be in the range from
                that result and the largest number
        - abs_tol: (default 1e-9) is the Absolute Tolerance,
            it is subtracted from the largest number (a or b), and the smaller input value must be in the range from
            that result and the largest number
"""

from math import isclose

number_1: int = 3
number_2: int = 4

# rel_tol

# number_1 must be between 4 * 0.5 = 3 and 4
close_1 = isclose(number_1, number_2, rel_tol=0.5)

# number_1 must be between 4 * 0.2 = 3.2 and 4
close_2 = isclose(number_1, number_2, rel_tol=0.2)

print(close_1)
print(close_2)

# abs_tol

# number_1 must be between 4 - 2 = 2 and 4
close_3 = isclose(number_1, number_2, abs_tol=2)

# number_1 must be between 4 - 0.2 = 3.8 and 4
close_4 = isclose(number_1, number_2, abs_tol=0.2)

print(close_3)
print(close_4)

# comparison

float_1 = .3
float_2 = .1 + .1 + .1

print(float_1)  # 0.3
print(float_2)  # 0.30000000000000004

print(float_2 - float_1)

is_equal_by_comparison = float_1 == float_2
is_equal_by_close = isclose(float_1, float_2, rel_tol=.551115e-11)

print(is_equal_by_comparison)
print(is_equal_by_close)
print(f"{5.551115123125783e-17: e} == 0.000000000000000055115")
