from typing import Iterable, Callable

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
        'name': "Ear Phones",
        'price': 10.00,
        'quantity': 2
    },
    {
        'name': "Wireless Keyboard",
        'price': 25.99,
        'quantity': 2
    },
]


def my_map(func: Callable, elements: Iterable, params: dict) -> list:
    collection = []

    for element in elements:
        collection.append(func(element, params))

    return collection


def usd_to_rwf(item: dict, params: dict):
    tax = item['price'] * params['tax'] * params['count']
    price = round(item['price'] * item['quantity'] * params['count'] + tax, 2)

    def converter():
        return {
            'name': item['name'],
            'price': f"{price:,}",
            'quantity': item['quantity']
        }

    return converter()


rwf_items = my_map(usd_to_rwf, line_items, {'count': 1000, 'tax': .2})
naira_items = my_map(usd_to_rwf, line_items, {'count': 500, 'tax': .4})

print(list(rwf_items))
print(list(naira_items))
