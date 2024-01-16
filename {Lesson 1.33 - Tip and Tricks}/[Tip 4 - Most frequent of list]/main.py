
# Most frequent of a list: there are several different ways to look up for a most frequnt element in a list.

from collections import Counter

numbers: list[int] = [-4, 1, 6, 1, 1, -4, 1, 7, 1, -4, -4, 1, -4, 3, -4, -4, 1, -4]

# method 1: not efficient

current_max: int = 0
current_value: int = 0

for number in numbers:
    if numbers.count(number) > current_max:
        current_value = number
        current_max = numbers.count(number)

print(f"Occurrences: {current_max}, Element: {current_value}")


# method 2: efficient

counter = Counter(numbers)

element_most_common = counter.most_common(1)
current_max = element_most_common[0][1]
current_value = element_most_common[0][0]

print(f"Occurrences: {current_max}, Element: {current_value}")


# method 3: not efficient

greater = sorted(numbers, key=numbers.count, reverse=True)

current_value = greater[0]
current_max = greater.count(current_value)

print(f"Occurrences: {current_max}, Element: {current_value}")


# method 4: efficient

current_value = max(set(numbers), key=numbers.count)
current_max = numbers.count(current_value)

print(f"Occurrences: {current_max}, Element: {current_value}")





