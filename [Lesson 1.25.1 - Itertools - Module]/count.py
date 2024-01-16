
# count: Is an itertools method that generates numbers to be counted through

"""
Values: - By default the starting number is zero 0 and the end is infinity
        - Unlike range(), itertools.count() accepts decimal steps Ex: 5.5 or -2.8
        - It doesn't contain the end point of the iteration, i.e the count goes on to infinity
        - Once one parameter is only passed, it is considered as a start point
"""

from itertools import count, zip_longest

counter_infinity = count()
counter_from_three = count(3)
counter_with_step = count(10, -2.5)  # count(start=10, step=-2.5)

for number in counter_infinity:
    if number >= 7:
        break
    print(number ** 2)

# next()
# => returns the next number in the count iteration

print(next(counter_infinity))
print(next(counter_infinity))
print(next(counter_infinity))
print(next(counter_infinity))
print(next(counter_infinity))

#

print(next(counter_from_three))
print(next(counter_from_three))
print(next(counter_from_three))

# with steps

print(next(counter_with_step))
print(next(counter_with_step))
print(next(counter_with_step))
print(next(counter_with_step))
print(next(counter_with_step))
print(next(counter_with_step))

# count to zip

days: tuple[str, ...] = "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"

sales_data: list[int] = [600, 890, 110, 900, 480, 380]

daily_data = list(zip(count(1), sales_data))
daily_data_with_label = list(zip(days, sales_data))

print(daily_data)
print(daily_data_with_label)


# zip_longest()
# => zips and pairs iterables together without getting exhausted

data: list[int] = [600, 400, 300, 870, 780]

daily_data_1 = list(zip(range(1, 10), data))
daily_data_longest = list(zip_longest(range(1, 8), data))

print(daily_data_1)
print(daily_data_longest)
