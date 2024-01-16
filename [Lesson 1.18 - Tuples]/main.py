
# Tuple: is an immutable data-structure that stores multiples elements of different types at the same time


def tuple_functions() -> None:
    counter: int = 0

    for method in dir(tuple):
        if "_" not in method:
            counter += 1
            print(counter, method)


tuple_functions()
