# function hinting: Even function parameter and return value can be type hinted, by default function return None


def function_type_cast(param_1: int, param_2: str) -> str:
    return f"{param_1} has value: {param_2}"


value_1 = function_type_cast(45, "101101")
value_2 = function_type_cast(23, "10111")
value_3 = function_type_cast("78", True)

print(value_1)
print(value_2)
print(value_3)


# Note: This function will blow up errors in mypy console becuase of the return value not being expected,
# but will run fluently in python because there is no code syntax or logic violations


def perimeter(length: int, width: int) -> None:
    return 2 * (length * width)


rectangle_1 = perimeter(4, 8.3)
print(rectangle_1)


#

def print_sequence(sequence: list[int]) -> list[str]:
    l: list = []

    for seq in sequence:
        value: str = str(seq)
        l.append(value)
    return l


seq_1 = print_sequence([1, 2, 3])
seq_2 = print_sequence([True, True, False])
seq_3 = print_sequence([56.0, -.09])
seq_4 = print_sequence("Hello world")

print(seq_1)
print(seq_2)
print(seq_3)
print(seq_4)
