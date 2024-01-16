
# OrderedDict: provides a dictionary which remembers the order of the elements as they were append in

"""
Values: python dictionaries also have this functionality and this makes this method redundant
"""

from collections import OrderedDict

my_dict: dict[str, int] = OrderedDict()

my_dict['a'] = 1
my_dict['c'] = 3
my_dict['d'] = 4

print(my_dict)

my_dict['b'] = 2

print(my_dict)
