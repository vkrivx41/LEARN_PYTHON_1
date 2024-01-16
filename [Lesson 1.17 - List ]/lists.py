
# creation:
from typing import Union

my_list_1: list = ["nik", True, 89]
print(my_list_1)

# empty list

empty_list_1: list = list()
empty_list_2: list = []

print(empty_list_1, empty_list_2)

# accessing list
# Note: list can be accessed through slicing and indexing

# indexing

fruits_1: list = ["banana", "apple", "mango"]

fruit_1 = fruits_1[0]
fruit_2 = fruits_1[1]
fruit_last = fruits_1[-1]

print(fruit_1, fruit_2, fruit_last)

# slicing
# => In this method a part of a list is returned, not only a single element, a list is returned

prime_numbers:list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 31, 37, 41]

slice_1 = prime_numbers[0:4]
slice_2 = prime_numbers[6:9]
slice_3 = prime_numbers[::-1]  # used also as a reverse technique
slice_4 = prime_numbers[:4:-1]  # begin from the end and stop at index 5

print(slice_1)
print(slice_2)
print(slice_3)
print(slice_4)


# iterating
# We can iterate through a list bcs, it's iterable using a loop (for-in)

players: list[str] = ["Salah", "Trent", "Darwin", "Luiz"]

for player in players:
    print(player)


# searching elements
# We can easily search for elements in a list using the membership operators

computers: list[str] = ["Dell", "HP", "Macbook", "Lenovo"]

search_1 = "htc" in computers  # False
search_2 = "Dell" not in computers  # False

print(search_1)
print(search_2)

if "HP" in computers:
    print("Found the computer")
else:
    print("Computer not found")


# mutation
# We can reassign a new value into an existing list

fruits_1: list = ["banana", "cherry", "lemon"]

print(fruits_1)
print(fruits_1[0])

fruits_1[0] = "berry"
print(fruits_1)
print(fruits_1[0])


# concatenation
# List can be easily concatenated to others using the + symbol

list_one: list[int] = [4, -8, 2, 8, 3, 5, 1]
list_two: list[float] = [4.8, -8.78, 0.2, 8.0, 3.1, 5.78, 1.11]

# the highlight is bcs we are concatenating list[int] to list[float]
list_combined: list[Union[float, float]] = list_one + list_two

print(list_combined)

# repeated elements creation
# We can create a list with the repetition of a single one

list_rep_1: list[int] = [23] * 10
list_rep_2: list[str] = ["Hello", "World"] * 3
list_rep_3: list[bool] = [True] * -8  # This creates an empty list

print(list_rep_1)
print(list_rep_2)
print(list_rep_3)  # []

# using slice function

slice_1: slice = slice(3, 7)
slice_2: slice = slice(8, 2, -2)

print(slice_1, slice_2)

print([1, 2, 3, 4, 5, 6, 7, 8, 9, 0][slice_1])
print([1, 2, 3, 4, 5, 6, 7, 8, 9, 0][slice_2])
