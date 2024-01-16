
# Set: is a builtin data-structure that is unordered and mutable but doesn't allow duplicate elements


"""
Values - The order of a set is arbitrary and goes according to the environment on which the program is running
"""


def set_functions() -> None:
    counter: int = 0

    for method in dir(set):
        if "_" not in method:
            counter += 1
            print(counter, method)


set_functions()
