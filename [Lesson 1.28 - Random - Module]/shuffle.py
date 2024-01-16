# shuffle: shuffles elements in a sequence randomly

"""
Values: - doesn't return a value
"""
from random import shuffle, choice
from typing import TypeVar

R = TypeVar("R")

cards: list[int] = list(range(1, 53))

print(cards)

shuffle(cards)

print(cards)

# a custom shuffle method that returns a value


def custom_shuffle(seq: R) -> R:
    new_sequence: R = []

    while len(new_sequence) < len(seq):
        rand: int = choice(seq)

        if rand not in new_sequence:
            new_sequence.append(rand)

    return new_sequence


shuffled_cards = custom_shuffle(tuple(cards))

print(shuffled_cards)
