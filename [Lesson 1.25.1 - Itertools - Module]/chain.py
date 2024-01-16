
# chain: is an itertools method that chains or concatenate more than one iterable together for memory efficiency
# and iteration

"""
Values: - Once a chain has be used for assignment, iteration, or any other operation, it gets exhausted and clears
            back to an empty chain, so it can be used again -- be careful with that
        - Better than the + operator
        - Allows iteration of all the applied iterables
        - The combined iterable can also be stored to be ysed for other tasks
"""

from itertools import chain

numbers: list[int] = [45, 25, 23, 65, 23, -45, 35]
names: tuple[str, ...] = "Scorpus", "Mugnes", "Nik"
letters: set[str] = {"a", "b", "c", "c"}

# approach 1

combined: chain = chain(numbers, names, letters)

print(combined)
for item in combined:
    print(item)

# we can create an iterable from the chain
combined: chain = chain(numbers, names, letters)

combined_list = list(combined)

print(combined_list)

# This code right here can't run because the chain has be used, and casted to an iterable
for item in combined:
    print(item)

# This code will run
for item in combined_list:
    print(item)

