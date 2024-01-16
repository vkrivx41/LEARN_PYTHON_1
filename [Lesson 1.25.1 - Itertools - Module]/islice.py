
# islice: is an itertools method that is used to slice an iterable or file into slices and return those

"""
Values: - The second parameter only means the stop count of the iteration
        - When the third parameter if passed it stands for the end values although it will not be included in the result
        - The forth parameter if passed stand for the step Note: only positive or None
"""

from itertools import islice, count

first_five = list(islice(range(10), 5))
last_five = list(islice(range(10), 5, 10))
last_five_step = list(islice(range(10), 5, 10, 2))
# last_five_step = list(islice(range(10), 5, 10, -2))  # ERROR: ValueError: Step for islice() must be a positive
# integer or None.

print(first_five)
print(last_five)
print(last_five_step)
# print()

# file opening and slicing for selection of desired lines

# header of the log file: 3 lines
with open("test.log", "r") as file:
    header = islice(file, 3)

    for line in header:
        print(line, end="")
    print()

# description of the log file: from line 4 to the end
with open("test.log", "r") as file:
    header = islice(file, 4, None)

    for line in header:
        print(line, end="")
