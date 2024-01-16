# tuple: is a immutable basic data-structure that stores elements and allows duplicates in them

"""
Values: - when comparing tuples an evaluation of one element from one side to the equivalent one from the other is done,
 once one of them is great, the great side becomes the bigger, regardless of the remaining elements of the sequence

"""

import sys


def main() -> None:
    # the version info

    print(sys.version_info) # sys.version_info(major=3, minor=12, micro=0, releaselevel='final', serial=0)

    if sys.version_info >= (3, 11):
        print("You are running python 3.11 or higher")
    else:
        print("The Python version you are running is outdated")

    # comparing

    tuple_1: tuple[int, ...] = (2, 1, 2)
    tuple_2: tuple[int, ...] = (2, 2, 2)

    print(tuple_1 >= tuple_2)


if __name__ == "__main__":
    main()
