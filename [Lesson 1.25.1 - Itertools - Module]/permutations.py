
# permutations: is method that groups data from an iterable and make combinations of the possible outcomes,
# the order does matter

"""
Values: - The formula of finding permutations is finding the factorial of the length of the given Iterable
                as x! Ex: Iterable of len 4 will have 4! == 4 * 3 * 2 * 1 = 24 permutations
        - The order of the data does matter, so there can be duplicates
        - The length specification is not indeed a dependency for the creation
        - When the permutations object has been used it also gets exhausted
        - Although the object gets exhausted the memory address doesn't change
        - Returns a list of tuples when converted to a list
"""
import math
from itertools import permutations

numbers: list[int] = [0, 1, 2, 3, 4]

combination_for_all: permutations = permutations(numbers)
combination_for_4: permutations = permutations(numbers, 4)

for item in combination_for_4:
    print(item)


# race simulator
# => Here we are simulating a league and generate fixtures for all the team for Home and Away games

teams: list[str] = ["Arsenal", "Liverpool", "Chelsea", "Spurs", "M.City", "M.United", "Everton", "New Castle", ]

fixtures: permutations = permutations(teams, 2)
fixtures_list: list = list(fixtures)

fixtures_list_copy = fixtures_list.copy()


def fixtures_simulator(fixs: list) -> None:
    for fixture in fixs:
        print(fixture)


fixtures_simulator(fixtures_list_copy)

print(len(list(fixtures_list)))

# Scene
# Imagine we have 3 books and we want to simulate there arrangement on a table, when there are stacked over each other,
# what are the possible permutations that the books can be arrange into

books: list[str] = ["The art of Seduction", "A man of the People", "Gathering Blue", "A silent Boy"]

books_arrangement = permutations(books)  # 4 * 3 * 2 * 1 = 24
books_arrangement_by_two = permutations(books, 2)  # 3 * 4 = 12

print(len(list(books_arrangement_by_two)))

for arrangement in books_arrangement:
    print(arrangement)

# Finding the number of possible outcomes by formula

print(math.factorial(4))
print(math.factorial(7))
