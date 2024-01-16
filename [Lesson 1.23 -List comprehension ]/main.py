
# List comprehension: makes it possible to create and append element in a list using one line.

"""
Values: - It's not the best solution to writing code but it provides a simple a quick approach to working with lists
        - Can also take if-conditions and give out results according to the expression
"""


# Ex: 1: normal approach

squares: list[int] = []

for number in range(10):
    squares.append(number * number)

print(squares)

# Ex: 1:  Comprehension approach

squares: list[int] = [number * number for number in range(10)]

print(squares)


# Ex: 2:  Normal approach

squares: list[int] = []

for number in range(10):
    if number % 2 == 0:
        squares.append(number * number)

print(squares)

# Ex: 2: Comprehension approach

squares: list[int] = [number * number for number in range(10) if number % 2 == 0]

print(squares)