# We can also unpack arguments in the arguments list, for both list and dictionaries


def print_vector(x: int, y: int, z: int) -> None:
    print("<%s, %s, %s>" % (x, y, z))


print_vector(6, 9, 1)

# *
# => unpacks anything from an iterable

vector_list_1: list[int] = [5, 0, 1]
vector_list_2: list[int] = [-8, 3, 1, 6]
vector_tuple_1: tuple[float, ...] = .5, 8.1, -7.1
vector_range_1: range = range(9, 12)
vector_string_1: str = "123"

# We can use the asterisk sign to perform unpacking at argument level
# Note: We can not pass a list with more than 3 element because it would trigger a type error

print_vector(*vector_list_1)
print_vector(*vector_tuple_1)
print_vector(*vector_range_1)
print_vector(*vector_string_1)
# print_vector(*vector_list_2)  # ERROR: TypeError: print_vector() takes 3 positional arguments but 4 were given


# **
# => unpacks a dictionary at argument level
# Note: We can not pass a dict with more than 3 element because it would trigger a type error

vector_dict_1: dict[str, int] = {'x': 5, 'y': -7, 'z': 4}
vector_dict_2: dict[str, int] = {'x': 5, 'y': -7, 'z': 4, 'b': 7}

print(*vector_dict_1)  # this only unpacks the keys
print(*vector_dict_1.values())  # this only unpacks the values
print(*vector_dict_1.items())  # this unpacks all the keys and values as tuples

#

print_vector(**vector_dict_1)
# print_vector(**vector_dict_2)  # ERROR: TypeError: print_vector() got an unexpected keyword argument 'b'
