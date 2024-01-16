
# random: generates a random floating point number between 0 -- inclusive and 1 -- exclusive
# uniform: generates a random floating point number between the start -- inclusive and the end -- exclusive

"""
Values: - the floating point numbers comes with a precision of 16 digits after the point
        - the start or end can either be greater than the other
"""

from random import uniform, random

# random()

value: float = random()

print(value)

# uniform

for _ in range(5):
    rand = uniform(1, 10)

    print(rand, end=" ")
print()

for _ in range(5):
    rand = uniform(90, 21)

    print(rand, end=" ")




