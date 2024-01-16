
# A list has up to 11 methods in total

from typing import Union

# 1. append(new_item: str)
# adds a new element at the end of the list

people: list[str] = ["Mario", "Elon", "Gates"]
print(people)

people.append("Luigi")
print(people)

# 2: clear()
# As the name suggest, the whole list is cleared, and made empty

fruits: list[str] = ["Banana", "Apple", "Mango"]
print(fruits)

fruits.clear()
print(fruits)

# 3: copy()
# Performs a shallow copy of the original list, the new created list doesn't share the same address in
# memory with the old one, so this prevents mutations
# Note: This is different on two dimensional arrays

original_people: list[str] = ["Mario", "Elon", "Gates"]
print(original_people)

copied_people = original_people.copy()
print(copied_people)

# Any activity performed on one list doesn't affect the other

copied_people.append("Jobs")
original_people.remove("Mario")

print(original_people)
print(copied_people)

# Mutating an element in a two or more dimensional-array affects also the original or copy array

original_people_dimensional: list[Union[str, list[str]]] = ["Mario", ["Elon", "Bob"], "Gates"]

copied_people_dimensional = original_people_dimensional.copy()

original_people_dimensional[1][1] = "Cat"

print(original_people_dimensional)
print(copied_people_dimensional)

# shallow copy: method 2

fine_fruits: list[str] = ["blueberry", "avocado", "pineapple"]

fruits_copy = list(fine_fruits)
print(fine_fruits)
print(fruits_copy)

fine_fruits[1] = "cherry"

print(fine_fruits)
print(fruits_copy)

# 4: count(element: str)
# counts the number of occurrences for a certain element and returns it
# Note: 0 is returned if the element is not found

countries: list[str] = ["DRC", "Rwanda", "Burundi", "Uganda"]

counter_1: int = countries.count("DRC")
counter_2: int = countries.count("Tanzania")

print(counter_1)
print(counter_2)

# This method can also be used for searching

if countries.count("Rwanda") != 0:
    print("The country exists")
else:
    print("The country doesn't exist")

# 5: extend()
# appends a new iterable element (str, list, tuple) at the end of the list

cities: list[Union[str, list[list[str]]]] = ["Kinshasa", "Kigali", "Abuja"]
more_cities: list[str] = ["Cairo", "Accra"]

cities.extend(more_cities)
print(cities)

cities.extend(["Bujumbura", "Kampala"])
print(cities)

cities.extend("Gaborone")
print(cities)

# adding a new list at the end of the list

cities.append([["Antananarivo", "Lusaka"]])
print(cities)

# 6: index(element)
# Returns the index of a certain element in the list, otherwise will throw an error

presidents: list[str] = ["Kagame", "Biden", "Felix", "Museveni"]

index_1 = presidents.index("Kagame")
index_2 = presidents.index("Felix")
# index_3 = presidents.index("Trump") ERROR: ValueError: 'Trump' is not in list

print(index_1, index_2)

# 7: insert(index: int, element: Any)
# Inserts a new element in the list at a specific index
# Note: if the index is out of range then the element is appended at the end
# Note: if the index is out of range but negative the element is appended at the beginning of the list

websites: list[str] = ["google.com", "php.net", "pythpn.org"]
print(websites)

websites.insert(1, "mega.nz")
print(websites)

websites.insert(9, "github.io")
print(websites)

websites.insert(-300, "scorpus.world")
print(websites)

# 8: pop(element: Any)
# Removes an element from the end of the list and also returns it when told so

prime_numbers: list[int] = [2, 3, 5, 7, 11, 13, 17, 19]
print(prime_numbers)

prime_numbers.pop()
print(prime_numbers)

popped_prime: int = prime_numbers.pop()

print(popped_prime)
print(prime_numbers)

# 9: remove(element: Any)
# Removes a specified element from the list, throws an error if the element is not found

odd_numbers: list[int] = list(range(1, 10, 2))
print(odd_numbers)

odd_numbers.remove(5)
print(odd_numbers)

# odd_numbers.remove(6)
# print(odd_numbers)

# 10: reverse()
# Reverses the list

even_numbers: list[int] = list(range(0, 10, 2))
print(even_numbers)

# This mutates the original list

even_numbers.reverse()
print(even_numbers)

# 11: sort(key, reverse)
# Sorts a list in ascending order

people: list[str] = ["Elon", "Trump", "Luigi", "Mario"]
print(people)

people.sort()
print(people)

# We can add a key to follow when sorting bcs when sorting strings the ones which small letters at
# the beginning comes last
# Note: Using this method mutates the original list
# Note: We can use a key to modify the sorting strategy by using a lambda or normal function

people_again: list[str] = ["elon", "Trump", "Luigi", "mario"]
print(people_again)

people_again.sort()
print(people_again)

# we can fold the case of the names to return them in order

people_again.sort(key=lambda name: name.casefold())
print(people_again)

# we can also reverse the sorted list
people_again.sort(key=lambda name: name.casefold(), reverse=True)
print(people_again)


# sort by length
print()
people_again.sort(key=lambda name: len(name), reverse=True)

print(people_again)


# Other builtins

# sorted()
# This method prevents mutation of the original list

mixed_numbers: list[int] = [4, 2, -9, 7, -5, 4, 2]
print(mixed_numbers)

sorted_mixed_numbers = sorted(mixed_numbers)

print(mixed_numbers)
print(sorted_mixed_numbers)

# include keys

sorted_mixed_numbers_again = sorted(sorted_mixed_numbers, reverse=False, key=lambda number: number * -1)

print(sorted_mixed_numbers)
print(sorted_mixed_numbers_again)

# reversed()

float_numbers: list[float] = [6.9, -.9, 72.9, 34.2]
print(float_numbers)

float_numbers_reversed = reversed(float_numbers)

print(float_numbers)
print(float_numbers_reversed)  # <list_reverseiterator object at 0x000001EB9AFE1270>
print(list(float_numbers_reversed))
