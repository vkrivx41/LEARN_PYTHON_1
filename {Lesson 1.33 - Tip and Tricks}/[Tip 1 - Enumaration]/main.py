# enumerate: creates a list of tuples where the first element is the index of the iteration and the second is the
# element

"""
Values: - enumerate creates an iterator behind the scenes, so it can do what all other iterators do
        - returns a list of tuples
"""


def main() -> None:
    for method in dir(enumerate):
        print(method)

    names: list[str] = ["Mike", "John", "Bob", "David", "Sarah"]

    # structure
    enumerated = enumerate(names)

    print(enumerated)
    print(list(enumerated))

    # looping

    for counter, name in enumerate(names):
        print(counter, name)

    # by zip

    for counter, name in zip(range(len(names)), names):
        print(counter, name)


if __name__ == '__main__':
    main()
