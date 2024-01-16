
# perm: is a math method that is short for "permutations" it returns the number of ways to choose k items from n
# items with repetition and order

"""
Values: - syntax: # perm(n, k)
        - it performs the formula of the permutations method from the itertools module
        - n = 5, k = 3, Formula: n! / (n - k)! => 5! / (5 - 3)! => 120 / 2 => 60
"""

from math import perm
from itertools import permutations

# ex: scenario of number of permutations possible where 10 people will seat in 6 seats

num_people: int = 10
num_seats: int = 6

perm = perm(num_people, num_seats)
print(perm)

# permutations approach

people: list[str] = ["nik", "bun", "ella", "joe", "gave"]
seats: int = 3

perm_1 = permutations(people, seats)
print(list(perm_1))
# print(len(list(perm_1)))
