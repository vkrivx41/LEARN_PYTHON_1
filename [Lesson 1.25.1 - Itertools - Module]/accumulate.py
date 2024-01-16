
# accumulate: is a special itertools method that is used to accumulate values in an iterable by running a particular
# operator on it, usually addition by default

from itertools import accumulate
import operator

marks_1: list[int] = [56, 24, 97, 25, 98, 46, 67, 92, 78, 81]
marks_2: list[int] = [82, 78, 45, 23, 91, 77, 65, 69, 60, 40]


def accumulated_total(numbers: list) -> accumulate:
    return accumulate(numbers)


total_list_1: list = list(accumulated_total(marks_1))
total_list_2: list = list(accumulated_total(marks_2))

print(total_list_1)
print(total_list_2)

total_1: int = total_list_1[-1]
total_2: int = total_list_2[-1]

print(total_1)
print(total_2)


# use another operator
# ex: multiplication : from the operator module

numbers: list = list(range(1, 6))

multiplication: list = list(accumulate(numbers, operator.mul))
subtraction: list = list(accumulate(numbers, operator.sub))
division: list = list(accumulate(numbers, operator.truediv))  # truediv != floordiv

print(multiplication)
print(subtraction)
print(division)

# max, min
# => are functions used to find the max or min value in an iterable

numbers: list[int] = [6, 2, -8, 9, 0, 5, 1, 4]

max_value: list = list(accumulate(numbers, func=max))
min_value: list = list(accumulate(numbers, func=min))
pow_value: list = list(accumulate(numbers, func=pow))

print(max_value, max_value[-1])
print(min_value, min_value[-1])
print(pow_value, pow_value[-1])
