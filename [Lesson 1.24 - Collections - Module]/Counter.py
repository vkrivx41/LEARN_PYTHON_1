
# Counter: is a datatype from the collections module that allows us to count the numbers of occurrences
# for all elements available in an iterable


"""
Values: - Returns a Counter object made of a dictionary filled with counts as keys and  the elements as values
        - Doesn't work for non-hashable types
        - Doesn't work for float and other incomparable types
"""

from collections import Counter


count: int = 0

marks: list[int] = [8, 5, 3, 2, 5, 8, 6, 6, 3, 1, 2, 8]
real_name: str = "Scorpus, The Scorpion"

counter_marks: Counter = Counter(marks)
counter_marks_list: list = list(counter_marks)

counter_name: Counter = Counter(real_name)

print(counter_marks)
print(counter_marks_list)

print(counter_name)


# methods

# 1: elements()
# => returns all the elements from the counter

marks: list[int] = [8, 5, 3, 2, 5, 8, 6, 6, 3, 1, 2, 8]

counter: Counter = Counter(marks)

elements = counter.elements()
print(elements)  #  <itertools.chain object at 0x000001D86C752290>
print(list(elements))


# 1: most_common(number)
# => returns a list of tuples filled with the counts and elements, the most common element from the counter,
# if the parameter is filled then the users option is regarded
# Note: If the count is out of range, then the complete counter is returned as a list

marks: list[int] = [8, 5, 3, 2, 5, 8, 6, 6, 3, 1, 2, 8]

counter: Counter = Counter(marks)

most_common = counter.most_common()
most_common_one = counter.most_common(1)  # the first most common element in a tuple (count, element)
most_common_two = counter.most_common(2)  # the two first most common element in a tuple
# [(count, element), (count, element)]
most_common_out = counter.most_common(78)

print(most_common)
print(most_common_one)
print(most_common_two)
print(most_common_out)

# 3: subtract(dict)  dict(element, count)
# => subtracts an element's count as defined in the dict

real_name: str = "Pascal, The great"

name_counter: Counter = Counter(real_name)

print(name_counter)

sub: dict = {'a': 1, ' ': 2}

name_counter.subtract(sub)

print(name_counter)
