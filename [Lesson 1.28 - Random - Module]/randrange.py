
# randrange: picks a random number from a range

"""
Values: - it accepts steps
"""

from random import randrange

# random odd numbers from 1 - in to 10 - ex

for _ in range(10):
    value = randrange(1, 10, 2)

    print(value, end=" ")
