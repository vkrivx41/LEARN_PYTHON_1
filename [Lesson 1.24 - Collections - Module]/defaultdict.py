
# defaultdict: creates a dict with a default value that is returned when a non-existing key is invoked


"""
Values - Different datatypes have their own default values
    int => 0
"""


from collections import  defaultdict

my_dict: dict[str, int] = defaultdict(int)

my_dict.update({'a': 1, 'b': 2})

value_1: int = my_dict['a']  # 1
value_2: int = my_dict['x']  # o

print(value_1)
print(value_2)


# string
# default => " "

my_dict: dict[int, str] = defaultdict(str)

my_dict.update({1: 'a', 2: 'b'})

value_1: str = my_dict[1]  # 1
value_2: str = my_dict[10]  # o

print(value_1)
print(value_2)

# bool: False

my_dict: dict[int, bool] = defaultdict(bool)

my_dict.update({1: True, 2: False})

print(my_dict[1])
print(my_dict[9])


# Float: 0.0
