
# Annotations: Are machine readable meta-data that are added to our code for code readability, documentation,
# and improvement

# Note: Python is a dynamic-typed programming language, i.e it doesn't need to demonstrate the datatype of a value
# before assignment

"""
Values: - Annotations don't change how the interpreter compiles the code, it's just for documentation
        - Packages like "mypy" are used to check for code type hinting and annotations restrictions
        - When type-hinting a bool to int, the bool is converted to an integer, so that True is 1 and False is 0
"""

# Dynamic Assignment

value_1 = "Hello"
print(value_1)

value_1 = 2
print(value_1)

value_1 = True
print(value_1)


# type hint
# Note: type hinting doesn't restrict code execution, because hints are used only for documentation and
# readability enhancement

value_1: int = "Hello"
print(value_1)

value_1: int = 56
print(value_1)

bool_1: int = True
print(bool_1)


# Hinting list, tuples, and dict

list_1: list = ['nik', 689, True]
print(list_1)

names_1: list[str] = ["nik", "bun", "ella", "joe"]
print(names_1)

list_2: list[list[int]] = [[1, 2, 3], [4, 5, 6]]
print(list_2)

dict_1: dict[str, int] = {"a": 1, "b": 2, "c": 3}
print(dict_1)

tuple_1: tuple[bool] = False, True, True, False
print(tuple_1)

tuple_2: tuple[bool, bool, bool, bool] = True, False, True, False
print(tuple_2)