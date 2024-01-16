# 1 add(new_element)
# => Adds a new element at the end of the set if it doesn't already exist, otherwise omits the whole process

my_set: set = set()

my_set.add(7)
my_set.add(1)
my_set.add(9)
my_set.add(7)  # Will not be added because it is duplicate

print(my_set)

# 2 clear()
# => clears out the entire set to empty

even_numbers: set[int] = {0, 2, 4, 6, 8}

print(even_numbers)

even_numbers.clear()

print(even_numbers)

# 3 copy()
# => creates a shallow copy of an original set
even_numbers: set[int] = set(range(0, 10, 2))

even_numbers_copy: set[int] = even_numbers.copy()

print(even_numbers)
print(even_numbers_copy)

even_numbers.add(10)
even_numbers.add(12)

print(even_numbers)
print(even_numbers_copy)


# 4 discard()
# => removes an element from the set, doesn't raise an error when the element is not found
setA: set[int] = {1, 2, 4, 5, 6, 9}

print(setA)

setA.discard(1)
setA.discard(7)

print(setA)

# 5 pop()
# => removes an element from the end[arbitrary] of the set and returns it if told so
# Note: The element removed is random because a set doesn't have a specific order of arranging items in it, so the
# positions of the items shuffles each compilation

setB: set[int] = {9, 1, 8, 5, 5, 7}

print(setB)

popped_element = setB.pop()

print(popped_element)
print(setB)

# 6 remove()
# => deletes a specific element from the set if found, and raise an error if not

setC: set[int] = {4, 9, 1, 5}

print(setC)

setC.remove(9)
# setC.remove(47)  # ERROR: KeyError: 47

print(setC)

# 7 update()
# => update a set with new elements

setD: set[int] = {5, 2, 6, 1, 9}

print(setD)

setD.update({7, 1, 9, 0, 5})

print(setD)


