
# randbits: generate a secret number from 0 to the given bits, default is 32 bits

"""
Values: - # 1 byte = 8 bits
"""

from secrets import randbits

for _ in range(5):
    random_16 = randbits(16)

    print(random_16, end=" ")
print()

for _ in range(5):
    random_8 = randbits(8)

    print(random_8, end=" ")
print()

for _ in range(5):
    random_4 = randbits(4)

    print(random_4, end=" ")
print()

for _ in range(5):
    random_2 = randbits(2)

    print(random_2, end=" ")
