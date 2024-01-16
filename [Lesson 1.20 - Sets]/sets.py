
# empty set

empty_set: set = set()

print(empty_set, type(empty_set))

# duplicate
# => When duplicate elements are adding to a set, only the first occurrence is kept

duplicate_set_1: set[int] = {1, 5, 6, 2, 5}  # second five is not stored
duplicate_set_2: set[str] = set(['Scorpus', 'Tug', 'Nik', 'Scorpus'])  # second Scorpus is not stored

print(duplicate_set_1)
print(duplicate_set_2)

# searching

even_numbers: set[int] = set(range(0, 10, 2))

if 5 in even_numbers:
    print("In")
else:
    print("Not in")


# iteration

for number in even_numbers:
    print(number)


# appending
# This approach adds elements at the end of the set

more_even_numbers = even_numbers | {10, 12, 14}
print(more_even_numbers)
