# ceil: is a math function that returns smallest integer greater than or equal to the input

"""
Values: - if the number is negative the greatest number to it is returned, it this case it's always that number without
            floats
"""

from math import ceil, floor, inf

number_1: float = 6.8
number_2: float = -9.8
number_3: float = 2.3

ceil_1 = ceil(number_1)
ceil_2 = ceil(number_2)
ceil_3 = ceil(number_3)

print(ceil_1, ceil_2, ceil_3)

# floor: is a math function that returns largest integer less than or equal to the input

"""
Values: - if the number is negative the smaller number to it is returned, it this case it's always that number - 1 
            without floats
"""

floor_1 = floor(number_1)  # 6.8
floor_2 = floor(number_2)  # -9.8
floor_3 = floor(number_3)  # 2.3

print(floor_1, floor_2, floor_3)
