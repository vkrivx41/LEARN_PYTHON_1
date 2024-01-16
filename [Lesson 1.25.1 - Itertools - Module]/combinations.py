
# combinations: is an itertools method that groups data from an iterable and make combinations of the possible outcomes,
# regardless the order of the data

"""
Values: - The formula of finding the combinations of an Iterable is by adding the length minus 1 each time
            Ex: Iterable of len 4 will have: 4 + 3 + 2 + 1 = 10 combinations
        - The order of the data doesn't matter, so there can not be duplicates
        - The length specification is indeed a dependency for the creation
        - When the combinations object has been used it also gets exhausted
        - Although the object gets exhausted the memory address doesn't change
        - Returns a list of tuples when converted to a list
"""

from itertools import combinations, combinations_with_replacement

letters: list[str] = ["a", "b", "c", "d"]

result_for_2: combinations = combinations(letters, 2)
result_for_3: combinations = combinations(letters, 3)
result_for_4: combinations = combinations(letters, 4)
result_for_5: combinations = combinations(letters, 5)

print(list(result_for_2))
print(list(result_for_3))
print(list(result_for_4))
print(list(result_for_5))


for item in result_for_2:
    print(item)

# scene
# Imagine we have 5 students and there is a chair to sit on by only two of them, how many possible groups of them can
# sit on that chair

students: list[str] = ["Scorpus", "Mugnes", "Rotor", "Hubbard", "Takao", "nik"]

sitting_plan: combinations = combinations(students, 2)

for plan in sitting_plan:
    print(plan)


# combinations_with_replacement
# => This is like the normal combinations function but, it allows duplicates, whereby a group can appear twice or thrice
# because the order does matter
# Note: This is essential for creating password crackers

numbers: list[int] = [0, 1, 2, 3, 4]

combination_replace: combinations_with_replacement = combinations_with_replacement(numbers, 4)
combination_no_replace: combinations = combinations(numbers, 4)

for item in combination_replace:
    print(item)

print()

for item in combination_no_replace:
    print(item)

# Let's assume that there is a chair for 3 students now
# Note: there is a possibility of getting Scorpus, Scorpus, Scorpus

students: list[str] = ["Scorpus", "Mugnes", "Rotor", "Hubbard", "Takao", "nik"]

combination: combinations_with_replacement = combinations_with_replacement(students, 3)

# for item in combination:
#     print(item)
