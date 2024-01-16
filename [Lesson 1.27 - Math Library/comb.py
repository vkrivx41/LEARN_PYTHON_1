
# comb: is a math method that is short for "Combinations" it returns the number of ways to choose k items from n
# items without repetition or order

"""
Values: - syntax: # comb(n, k)
        - it performs the formula of the combinations method from the itertools module
        - n = 5, k = 3, Formula: n! / k! (n - k)! => 5! / 3! (5 - 3)! => 120 / 12 => 10
"""

from math import comb
from itertools import combinations

# ex: scenario of number of combinations possible where 10 people will seat in 6 seats

num_people: int = 10
num_seats: int = 6

combo = comb(num_people, num_seats)
print(combo)

# combination approach

people: list[str] = ["nik", "bun", "ella", "joe", "gav"]
seats: int = 3

combo_1 = combinations(people, seats)
print(list(combo_1))
