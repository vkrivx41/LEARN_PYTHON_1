# iterator: an iterator is an object with a state, that it remembers where it is during iteration

"""
Values: - iterators contain a magic method called __iter__() that enables looping because it creates an iterator behind
            the scenes
        - they have __next__() magic method to remember current element and move to the next element of the iteration
        - when an iterator is used it gets exhausted and can't be used again
        - iterator are memory efficient compared to lists and other builtin data-structures
"""

# creating an iterator
# => all iterators are iterable, so we need to create an iterable first

countries: list[str] = ["DRC", "Rwanda", "Uganda", "Kenya", "Tanzania"]
float_number: float = 45.79

countries_iter = iter(countries)  # countries.__iter__()
# float_iter = iter(float_number)  # ERROR: TypeError: 'float' object is not iterable

print(countries_iter)  # <list_iterator object at 0x00000278F0241A80>
print(type(countries_iter))  # <class 'list_iterator'>

# checking for an iterator
# => when can loop for the __iter__ method in the dir list

if "__iter__" in dir(countries_iter):
    print("The object is an iterator ")
else:
    print("The object is not an iterator")

# using an iterator
# next()

numbers: tuple[int, ...] = (1, 2, 3)
numbers_iter = iter(numbers)

print(next(numbers_iter))
print(next(numbers_iter))
print(next(numbers_iter))
# print(next(numbers_iter)) # ERROR: StopIteration -> bcs the iterator has been exhausted

# built-in iterators
# => the range function creates an iterator behind the scenes and returns a single value each time it is told to do so
odd_numbers_list: list = [1, 3, 5, 7, 9]
odd_numbers_range: range = range(1, 10, 2)

print(odd_numbers_list)
print(odd_numbers_range)
print("List memory in bytes:", odd_numbers_list.__sizeof__())
print("Range memory in bytes:", odd_numbers_range.__sizeof__())

# looping an iterable

for odd_number in odd_numbers_range:
    print(odd_number)
print()

# looping an iterable
# => the next() function calls the next element in the iterator and exhaust it so it can not be used again,
# the iteration is continued on the next value when looped over

odd_numbers_range_iter = odd_numbers_range.__iter__()

print(next(odd_numbers_range_iter))
print(next(odd_numbers_range_iter))

print("Start for loop: ")
for odd_number in odd_numbers_range_iter:
    print(odd_number)

# The iterator becomes empty because all of it's values are exhausted
print(odd_numbers_range_iter)
print(list(odd_numbers_range_iter))

# for loop behind the scenes

odd_numbers_list_iter = odd_numbers_list.__iter__()

next(odd_numbers_list_iter)
next(odd_numbers_list_iter)

while True:
    try:
        element = next(odd_numbers_list_iter)
    except StopIteration:
        break
    else:
        print(element)

# map as an iterator

nums: list[int] = [1, 2, 3, 4, 5, 6]

square_numbers = map(lambda num: num * num, nums)

print(next(square_numbers))
print(next(square_numbers))
print(next(square_numbers))
print(next(square_numbers))

