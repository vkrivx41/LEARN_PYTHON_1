
# filter: as the name suggests this high-order function returns elements that have been filtered through
# and met some crucial criteria
from typing import Callable, Iterable, Union

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


def expensive_checker(item: dict) -> bool:
    return item['price'] >= 50


expensive_items = filter(expensive_checker, line_items)

print(expensive_items)
print(list(expensive_items))


# ex: 2

questions: list[dict[str, Union[int, str]]] = [
    {
        'number': 1,
        'question': "What the fuck is this the trigger of World War 2?"
    },
    {
        'number': 2,
        'question': "What is the meaning of a First-class function in programming?"
    },
    {
        'number': 3,
        'question': "Who inverted NETVEX?"
    },
]

discrimination_words: list[str] = ["fuck", "bitch", "nigga", "pussy", "ass", "dick",]


def discrimination_checker(question: dict) -> bool:
    for word in discrimination_words:
        return word not in question['question']
    return True


pure_questions = filter(discrimination_checker, questions)

print(questions)
print(list(pure_questions))


# custom filter

def my_filter(func: Callable, elements: Iterable) -> list:
    collection: list = []

    for element in elements:
        if func(element):
            collection.append(element)

    return collection


def filter_strong_password(password: str) -> bool:
    return len(password) >= 8


passwords: list[str] = ["nik123", "954036vkr", "1562780938", "king^8ifs", "my_password", "0980", "3319ok"]

strong_passwords = my_filter(filter_strong_password, passwords)

print(list(strong_passwords))
