# Mutable: is a value or variable's value that can be changed, modified, or updated over time
# Immutable: is a value or variable's value that can't be changed, modified, or updated over time


"""
Values: - mutable: list, set, dict, file
        - immutables: str, int, float, None, bool
"""

# tuples: immutable

x: tuple = (1, 2)
y: tuple = x

# mutation doesn't occur on the y values, becuase they don't share the same address in memory
x = (1, 2, 3)

print(x, y)

# lists: mutable

a: list = ['a', 'b']
b: list = a

# mutation does occur on both list 'a' and list 'b'
a[1] = 'c'

print(a, b)

# function that mutate values: Impure function
# => even the outside list gets mutated too because the function depends on it to perform the sort() function which
# doesn't return a value

numbers_list: list = [9, 0, -1, 3, 8]


def sort_numbers(numbers: list) -> list:
    numbers.sort()

    return numbers


numbers_from_func = sort_numbers(numbers_list)

print(numbers_from_func)
print(numbers_list)

# Functions that doesn't mutate values: Pure functions
# => the outside list will not be mutated too because the function doesn't depend on it to perform the sorted() function
# which does return a value

names_list: list[str] = ["Bob", "anna", "Nik", "zen"]


def sort_names(names: list) -> list:
    return sorted(names, key=lambda name: name.casefold())


names_from_func = sort_names(names_list)

print(names_from_func)
print(names_list)
