
# zip: the zip function is a function that maps elements of one iterable with elements of another or even more than one

"""
Values: - creates a list of tuples containing elements of one iterable followed by elements of the next
        - zip is an iterator so it can be looped through, and work as many other iterators
"""


def main():
    print(zip([]))

    for method in dir(zip):
        print(method)


if __name__ == '__main__':
    main()

