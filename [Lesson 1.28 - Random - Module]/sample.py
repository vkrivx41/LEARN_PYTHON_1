
# sample: randomly chooses a portion of elements from a sequence and returns it, the element are duplicate-free


"""
Values: - the same as choices but sample doesn't include duplicates
        - the sample or k can't be larger than population or be negative
"""

from random import sample, choices

deck: list[int] = list(range(1, 53))

hand_sample = sample(deck, k=5)
hand_choices = choices(deck, k=5)

print(hand_sample)
print(hand_choices)


# ex: 2

prizes: list[str] = ["$ 100", "$ 200", "$ 500", "A car", "A gun", "Infinity ammo", "An amour"]

sample_prizes_sample = sample(prizes, k=2)
sample_prizes_choices = choices(prizes, k=2)

print(sample_prizes_sample)
print(sample_prizes_choices)
