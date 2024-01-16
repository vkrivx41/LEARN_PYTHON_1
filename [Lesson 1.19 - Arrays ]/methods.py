
from array import *

marks_1 = array('i', [4, 7, 1, 9, 3, 6])

# 1 append
# =>  appends a new element to the end of the array

print(marks_1)

marks_1.append(8)
# marks_1.append('C')  # ERROR: TypeError: 'str' object cannot be interpreted as an integer

print(marks_1)


# 2 byteswap() -> None
# => Swaps the elements in the array to their bytes version in memory, the values will be represented
# as the bytes they occupy in memory

marks_1.byteswap()
print(marks_1)  # bytes version

marks_1.byteswap()
print(marks_1)  # numeric version

# 3 count()
# => counts for the number of occurrences an element has and returns that, 0 is returned if not found

marks_1.append(8)

counter_1: int = marks_1.count(8)
counter_2: int = marks_1.count('7')

print(counter_1)
print(counter_2)

# 4 extend(Iterable) -> None
# => updates an array and adds more values to it, an iterable is expected

print(marks_1)

marks_1.extend([6, 3, 1])
marks_1.extend((11, 0, 14))

print(marks_1)

# 5 frombytes()
# 6 fromfile


# 7 fromlist()
# => appends new elements to the array from a list
marks_1.fromlist([12, 4, 5, ])

print(marks_1)
# 8 fromunicode()
# => appends new elements to the unicode array from a unicode

unicode_array = array("u", ['a', 'b', 'c'])

unicode_array.fromunicode("I")

print(unicode_array)

# 9 index()
# => returns the index of the first appearance of an element from the left

index_1: int = marks_1.index(1)
# index_2: int = marks_1.index(19)  # ERROR: ValueError: array.index(x): x not in array

print(index_1)

# 10 insert()
# => inserts a new element in the array at a specific index
# Note: When the index is out of range and negative the item will be added at index 0, and if it is positive it will
# be added at the end

marks_1.insert(2, 19)
marks_1.insert(-200, 56)
marks_1.insert(89, 12)

print(marks_1)

# 11 itemsize -> int
# => returns the amount of bytes a single element of the array occupies in memory
marks_2 = array('d', [56,9929, 99.038387, 78.9727, 45.7623])

int_size: int = marks_1.itemsize
double_size: int = marks_2.itemsize

print(int_size)
print(double_size)

# 12 pop() -> Any
# => removes the last element of the array and returns it if told so

print(marks_1[-1], marks_1[-2])

popped_marks_1 = marks_1.pop()
popped_marks_2 = marks_1.pop()

print(popped_marks_1)
print(popped_marks_2)
print(marks_1)

# 13 remove(Any) -> None
# => deletes a specific element from the array, and if not found an error is raised
# Note: if an element appears more than once, then the first occurrence is smashed out

marks_1.remove(56)
marks_1.remove(4)
# marks_1.remove(99)  # ERROR: ValueError: array.remove(x): x not in array

print(marks_1)

# 14 reverse() -> None
# =>  reverses the array

print(marks_1)

marks_1.reverse()

print(marks_1)

# 15 tobytes() -> bytes
# => converts the array to bytes and returns that

as_bytes = marks_1.tobytes()

print(as_bytes)

# 16 tofile()

# 17 tolist
# => converts tha array to a list

as_list: list[int] = marks_1.tolist()

print(as_list)

# 18 tounicode

# 19 typecode -> str
# => returns the type-code of the array

type_code_1: str = marks_1.typecode
type_code_2: str = marks_2.typecode

print(type_code_1)
print(type_code_2)

# 20 clear
# => an non builtin method to delete the entire array

# marks_1.clear() # ERROR

print(marks_1)

for number in range(len(marks_1)):
    marks_1.pop()

print(marks_1)




