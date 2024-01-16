
# map: is a high-order function that takes a function as a parameter with an iterable
# to loop through are run through that function

"""
Values: - The function can either be a lambda or def function
        - It returns an iterator that can then to converted to an iterable for use
"""

from timeit import default_timer as timer
from typing import Iterable, Callable

numbers: list[int] = list(range(1, 5))

squared_numbers_lambda = map(lambda number: number * number, numbers)

print(squared_numbers_lambda)
print(list(squared_numbers_lambda))


def square_numbers(num: int) -> int:
    return num * num


squared_numbers_def = map(square_numbers, numbers)

print(squared_numbers_def)
print(list(squared_numbers_def))


def apply_first_name(name: str) -> str:
    return "Kapulo " + name


full_names = map(apply_first_name, ("Pascal", "Junior", "Mikael", "Mugnes"))

print(list(full_names))


# tax adder application, use-cases

def tax_adder(item: dict) -> dict:
    return {
        'name': item['name'],
        'price': round(item['price'] + item['price'] * .02, 2) * item['quantity'],
        'quantity': item['quantity']
    }


line_items: list[dict] = [
    {
        'name': "Gym Bag",
        'price': 56.12,
        'quantity': 3
    },
    {
        'name': "Mobile Phone",
        'price': 900.00,
        'quantity': 1
    },
    {
        'name': "Wireless Keyboard",
        'price': 25.99,
        'quantity': 2
    },
]


tax_added = map(tax_adder, line_items)

print(line_items)
print(list(tax_added))


# money currency converter
# USD == RWF

def usd_to_rwf(item: dict):

    def converter(count: int):
        return {
            'name': item['name'],
            'price': item['price'] * count,
            'quantity': item['quantity']
        }

    return converter(1200)


items_in_rwf = map(usd_to_rwf, line_items)

print(line_items)
print(list(items_in_rwf))


# custom map function

def my_map(func: Callable, elements: Iterable) -> list:
    collection = []

    for element in elements:
        collection.append(func(element))

    return collection


def square_numbers(number: int) -> int:
    return pow(number, 2)


start_1 = timer()
square_numbers_from_my_map = my_map(square_numbers, list(range(1, 5)))
end_1 = timer()
print(end_1 - start_1)

start_2 = timer()
square_numbers_from_map = map(square_numbers, list(range(1, 5)))
end_2 = timer()
print(end_2 - start_2)

print(square_numbers_from_my_map, "Size:", square_numbers_from_my_map.__sizeof__())
print(list(square_numbers_from_map), "Size:", list(square_numbers_from_map).__sizeof__())


price_converter = my_map(usd_to_rwf, line_items)

print(price_converter)
