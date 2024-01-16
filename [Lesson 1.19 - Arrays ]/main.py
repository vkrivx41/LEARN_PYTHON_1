# Array: Is a mutable builtin data-structure that stores values of the same type allowing even duplicates

from array import array

"""
Values: - Arrays only stores values of the same data-type
        - Arrays uses C language type-codes to demonstrate and address values to be stored in an array
"""

"""
Type-codes: 'b' -> signed char
            'B' -> unsigned char
            'u' -> unicode char
            'h' -> signed short
            'H' -> unsigned short
            'i' -> signed int
            'I' -> unsigned int
            'l' -> signed long
            'L' -> unsigned long
            'f' -> float
            'd' -> double
"""


def array_functions() -> None:
    counter: int = 0
    for method in dir(array):
        if "_" not in method:
            counter += 1
            print(counter, method)


array_functions()
