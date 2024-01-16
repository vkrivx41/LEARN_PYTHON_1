

# Itertools: Is a builtin module that provide with us many methods to work with Iterables
# Iterables: Are sequentail data that allows us to iterate and loop through them ex (list, dict, tuple, etc)

import itertools


def itertools_methods() -> None:
    counter: int = 0
    for method in dir(itertools):
        if "_" not in method:
            counter += 1
            print(counter, method)


if __name__ == "__main__":
    itertools_methods()


