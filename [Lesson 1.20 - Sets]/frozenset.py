

# frozenset: A frozen set is a set that doesn't accept mutation

"""
Values: - Share all traits with normal sets but doesn't accept mutation
"""


counter: int = 0
for method in dir(frozenset):
    if "_" not in method:
        counter += 1
        print(counter, method)


setA: frozenset = frozenset([1, 5, 4, 9])
setB: frozenset = frozenset([7, 3, 1, 8, 4])

print(setA)
print(setB)

union = setA.union(setB)
intersection = setA.intersection(setB)

print(union)
print(intersection)


#