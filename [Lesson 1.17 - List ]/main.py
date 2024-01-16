
# List: Is a mutable datatype or data-structure that stores multiple elements of different types at a single time,
# while also allowing duplicates

"""
Values: - Accept duplicate elements
        - Store different elements of different data-types
        - Values in the list can be changed over time
        - Take a bit more time during compilation and code execution according to other data-structures
"""


def list_functions() -> None:
    """
    This function prints all list functions excluding all the dumb ones
    :return: None, because it prints methods down
    """

    counter: int = 0
    for method in dir(list):
        if "_" not in method:
            counter += 1

            print(f"{counter}: " + method)


list_functions()
