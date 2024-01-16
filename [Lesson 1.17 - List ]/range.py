
# range(): is a powerful builtin method used to create a range of integers

even_numbers_range: range = range(0, 10, 2)
odd_numbers_range: range = range(1, 10, 2)

print(even_numbers_range)  # range(0, 10, 2)
print(odd_numbers_range)  # range(1, 10, 2)

# converting a range to a list

even_numbers: list = list(even_numbers_range)
odd_numbers: list = list(odd_numbers_range)

print(even_numbers)
print(odd_numbers)

# index(element) -> int
# Find the index of an element

numbers: range = range(1, 10)

index_1: int = numbers.index(4)
index_2: int = numbers.index(9)

print(index_1, index_2)

# count(element: int) -> int
# counts the number of occurrences an element has in a range, 0 if not found

reversed_numbers: range = range(20, 5, -2)

counter_1: int = reversed_numbers.count(7)
counter_2: int = reversed_numbers.count(12)

print(counter_1, counter_2)

# start
# returns the start element of the range

two_to_thirteen: range = range(2, 14)
print(two_to_thirteen.start)


# step
# returns the step count of the range

stepped_minus_five: range = range(40, 12, -5)
print(stepped_minus_five.step)

# stop
# returns the stop element of the range

stopped_on_3: range = range(-7, 3, 2)
print(stopped_on_3.stop)

# Invalid range
# Note: a range can't be created we it's invalid, we can prove that but converting to a list which creates an empty list

# This range goes from up to down but the step is not negative
invalid_range_1: range = range(10, 4, 2)
print(invalid_range_1)
print(list(invalid_range_1))

# This range goes from down to up but the step not negative
invalid_range_2: range = range(1, 50, -12)
print(invalid_range_2)
print(list(invalid_range_2))
