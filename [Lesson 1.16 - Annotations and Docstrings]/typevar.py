
# TypeVar
# Creates a generic type that can be of any data-type

from typing import TypeVar

K = TypeVar('K')
V = TypeVar('V')


# Here the value of the dict must be the same as of the value passed on the second param position
# Those values can be of any type, but as long as they are the same

def find_in_dict(d: dict[K, V], value: V) -> bool:
    return value in d.values()


my_dict = {'a': 2, 'b': 3}

print(find_in_dict(my_dict, 2))
print(find_in_dict(my_dict, 'x'))
