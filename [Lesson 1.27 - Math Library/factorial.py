
# factorial: is a math method that returns the mathematical factorial of a number

"""
Values: - it function runs the input recursively multiplying the number to that number - 1 each time until 1
        - Formula: ex: 5 => 5 * 4 * 3 * 2 * 1
        - accepts only integer values
"""

from math import factorial

# number_1: float = 10.9  # can't work bcs, input is float
number_1: int = 3
number_2: int = 10

fact_1 = factorial(number_1)
fact_2 = factorial(number_2)

print(fact_1)
print(fact_2)


def get_factorial(num: int) -> int:
    if type(num) != int or num <= 0:
        return 0
    current = 1

    for n in range(1, num + 1):
        current *= n
    return current


print(get_factorial(-9))
print(get_factorial(3))
print(get_factorial(10))
