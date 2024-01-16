
# Dictionary: Is a builtin data-structure, that uses key: value pairs to store data
# Note: The key reference on possible value to yield


"""
Values: - Doesn't allow duplicate keys
        - Keys must be only of hashable types or immutable types(str, int, float, tuple)
"""


def dict_functions() -> None:
    counter: int = 0

    for method in dir(dict):
        if "_" not in method:
            counter += 1
            print(counter, method)


dict_functions()
