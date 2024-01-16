
# filterfalse: is an itertools method that is used to returned values which yield False during filtration

from itertools import filterfalse, dropwhile, takewhile

names: list[str] = ["Nik", "Scorpus", "Mugnes", "Isaac", "Bob", "Dave"]


def greater_than_two(number: int) -> bool:
    return number > 2  # return True if number > 2 else False


def short_names(name: str) -> int:
    return len(name) <= 4  # return True if len(name) <= 4 else False


result_1 = list(filterfalse(greater_than_two, [6, 0, -9, 3, 2, 1, 5]))
print(result_1)

result_2 = list(filterfalse(short_names, names))
print(result_2)


# dropwhile
# => returns values from an iterable if the filtration has met an element that doesn't the criteria, and all the remaing
# part of the iterable is returned

result_3 = list(dropwhile(short_names, names))
print(result_3)


# takewhile
# => returns values from an iterable until it reaches a value that evaluates to True
# Note: All the values starting from the True one are omitted
# Note: takewhile != dropwhile

result_4 = list(takewhile(short_names, names))
print(result_4)