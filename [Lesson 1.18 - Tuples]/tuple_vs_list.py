
# List are most used ones compared to tuples because they are more efficient and mutable allowing data manipulation
# and adjustment, but they are more memory-consumption compared to tuples

# Recommendations: - Use lists when mutation is expected and on few sum of data, otherwise tuple for large

import sys
import timeit

# size, tuple vs list

my_tuple: tuple = ("Scorpus", 19, "Kigali", True)
my_list: list = ["Scorpus", 19, "Kigali", True]

size_tuple: int = sys.getsizeof(my_tuple)
size_list: int = sys.getsizeof(my_list)

print(size_tuple, "bytes as tuple")
print(size_list, "bytes as list")


# time of execution: tuple vs list

time_tuple: float = timeit.timeit(stmt='(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)', number=1_000_000)
time_list: float = timeit.timeit(stmt='[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]', number=1_000_000)

print(time_tuple, "milliseconds for tuple")
print(time_list, "milliseconds for list")
