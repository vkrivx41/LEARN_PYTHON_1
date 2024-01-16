
# 1: the first improvement we can add to our functions is type hinting the return values, this help the programmer
# and other external users to know how to operate with function which returns None and the otherwise.


def perimeter(length: float, width: float) -> float:
    return 2 * (length + width)


perimeter_1 = perimeter(18.3, 19.3)

print(perimeter_1)

# None


def print_perimeter(length: float, width: float) -> None:
    print(2 * (length + width))


print_perimeter(19.6, 8.0)
