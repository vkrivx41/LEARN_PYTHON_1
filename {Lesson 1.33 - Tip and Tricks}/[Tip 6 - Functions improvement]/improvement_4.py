
# 4: using doc-strings to document what the function is all about, it's parameters and return value


def perimeter(length: float, width: float) -> float:
    """
    Returns the perimeter of the rectangle as meter-squared using the formula 2 * (length + width)
    :param length: The length of the rectangle in meters
    :param width: The width of the rectangle in meters
    :return: The perimeter of the rectangle
    """
    return 2 * (length + width)


perimeter_1 = perimeter(18.3, 19.3)

print(perimeter_1)
