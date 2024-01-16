
# fsum: returns the sum of numbers in an iterable

"""
Values: - similar to builtin sum() function, but there is a bit difference, run the code below to notice
        - sometime sum() return more floating point values which are not precise
"""

from math import fsum

numbers: list[float] = [.2] * 13

fsum_value = fsum(numbers)
sum_value = sum(numbers)

print(fsum_value)
print(sum_value)


