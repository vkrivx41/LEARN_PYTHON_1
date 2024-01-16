
# Note: Other functionalities like slicing, searching, and iterating a tuple works similarly to a list


# declaration

# empty tuple

empty_tuple_1: tuple = ()
empty_tuple_2: tuple = tuple()

print(empty_tuple_1)
print(empty_tuple_2)

# single element
# => When creating a tuple with a single element we add a comma at the end, otherwise it will be string

single_element_tuple_1: tuple[str] = ("Scorpus", )
single_element_tuple_2: tuple[int] = (4_10, )  # yield to tuple
single_element_tuple_3: tuple[int] = (4_10)  # yield to int

print(type(single_element_tuple_1), single_element_tuple_1)
print(type(single_element_tuple_2), single_element_tuple_2)
print(type(single_element_tuple_3), single_element_tuple_3)


# duplicate elements
# => A tuple definition can be wrapped in brackets or not

person_1: tuple = ("Scorpus", 19, "Kigali")
person_2: tuple = "Mugnes", 20, "Paris"

print(person_1)
print(person_2)


# iteration

odd_numbers: tuple = tuple(range(1, 10, 2))

for element in odd_numbers:
    print(element)

# searching

if 5 in odd_numbers:
    print("Is in")
else:
    print("Is not in")


# slicing

even_numbers: tuple = tuple(range(0, 10, 2))

first_three: tuple = even_numbers[0:3]
from_end_start_step_2: tuple = even_numbers[::-2]

print(first_three)
print(from_end_start_step_2)

# using slice() function

slice_1: slice = slice(1, 4, 2)

print(even_numbers[slice_1])


# sorting => returns a list

fruits: tuple = "Mango", "Lemon", "Watermelon", "Cherry"

fruits_sorted: list = sorted(fruits)
fruits_sorted_reversed: list = sorted(fruits, reverse=bool(1))
fruits_sorted_by_length: list = sorted(fruits, key=lambda fruit: len(fruit))

print(fruits_sorted)
print(fruits_sorted_reversed)
print(fruits_sorted_by_length)

