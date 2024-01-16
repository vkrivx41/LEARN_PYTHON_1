
even_numbers: set[int] = set(range(0, 10, 2))
odd_numbers: set[int] = set(range(1, 10, 2))
prime_numbers: set[int]  = {2, 3, 5, 7}

random_numbers_1: set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
random_numbers_2: set[int] = {1, 2, 3, 10, 11, 12}

# 1: union()
# => returns the element available in both sets, i.e the combination of both sets
# Note: duplicates are omitted

union_1 = even_numbers.union(odd_numbers)
union_2 = odd_numbers.union(prime_numbers)

print(union_1)
print(union_2)

# 2: intersection()
# => Finds element that appear in both sets, i.e element both sets share

intersection_1 = even_numbers.intersection(odd_numbers)
intersection_2 = even_numbers.intersection(prime_numbers)

print(intersection_1)
print(intersection_2)

# 3: difference()
# => returns elements available in set 1 that are not available in set 2

diff_1 = random_numbers_1.difference(random_numbers_2)
diff_2 = random_numbers_2.difference(random_numbers_1)

print(diff_1)
print(diff_2)

# 4: symmetric_difference()
# => returns elements available in set 1 that are not available in set 2, and also elements in set 2 that are not
# available in set 1

diff_1 = random_numbers_1.symmetric_difference(random_numbers_2)
diff_2 = random_numbers_2.symmetric_difference(random_numbers_1)

print(diff_1)
print(diff_2)

# 5: intersection_update()
# => updates a set with the intersection of it and the other set
# Note: The new set appears with values of the intersection evaluation

setA: set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB: set[int] = {1, 2, 3, 10, 11, 12}

setA.intersection_update(setB)

print(setA)

# 6: difference_update()
# => updates a set with the difference of it and the other set
# Note: The new set appears with values of the difference evaluation

setA: set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB: set[int] = {1, 2, 3, 10, 11, 12}

setB.difference_update(setA)

print(setB)


# 7: symmetric_difference_update()
# => updates a set with the symmetric_difference_update of it and the other set
# Note: The new set appears with values of the symmetric_difference_update evaluation

setA: set[int] = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB: set[int] = {1, 2, 3, 10, 11, 12}

setB.symmetric_difference_update(setA)

print(setB)

# 8 issubset(set)
# => returns True if a set is a subset of the compared one, i.e if all set elements appears also in the compared set,
# otherwise False

setA: set[int] = {1, 2, 3, 4, 5, 6}
setB: set[int] = {1, 2, 3}

subset_1: bool = setA.issubset(setB)
subset_2: bool = setB.issubset(setA)

print(subset_1)
print(subset_2)

# 9 issuperset(set)
# => returns True if a set is a superset of the compared one, i.e if some of the set elements are the only elements in
# the compared set, otherwise False
# Note: the opposite of issubset() method

setA: set[int] = {1, 2, 3, 4, 5, 6}
setB: set[int] = {1, 2, 3}

superset_1: bool = setA.issuperset(setB)
superset_2: bool = setB.issuperset(setA)

print(superset_1)
print(superset_2)

# 7 isdisjoint(set)
# returns True if the compared sets doesn't have any similar elements, be 1 or more elements, otherwise False

setA: set[int] = {1, 2, 3, 4, 5, 6}
setB: set[int] = {1, 2, 3}
setC: set[int] = {7, 8, 9}

disjoint_1: bool = setA.isdisjoint(setB)
disjoint_2: bool = setB.isdisjoint(setA)
disjoint_3: int = setB.isdisjoint(setC)

print(disjoint_1)
print(disjoint_2)
print(disjoint_3)

