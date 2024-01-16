
# randint: generates a random integer number between the start -- inclusive and the end -- inclusive

"""
Values:  - the end can't be greater than the start
"""

from random import randint

for _ in range(5):
    value = randint(1, 8)

    print(value, end=" ")
print()

# random from a list

names: list[str] = ["nik", "bun", "ella", "joe"]

# one random name
random_name: str = names[randint(0, len(names))]

print(random_name)

# => generates a shuffled list of names

for _ in range(len(names)):
    value = randint(0, len(names) - 1)

    print(names[value], end=" ")
print()


# Note: This method is the same as the builtin shuffle method

def shuffled_names() -> list:
    new_names: list = []

    while len(new_names) < len(names):
        rand = randint(0, len(names) - 1)
        rand_name = names[rand]

        if rand_name not in new_names:
            new_names.append(rand_name)

    return new_names


shuffled_names_1 = shuffled_names()
shuffled_names_2 = shuffled_names()

print(shuffled_names_1)
print(shuffled_names_2)

