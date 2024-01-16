
# seed: creates a seed or stores a random process so that it can be used in debugging or optimization

"""
Values: - once we run a random method a seed it created to store it, anyone with that seed can rerun it and get the
            same result
        - a seed name must be an immutable data-type : int, str, ...
"""

import random

# seed 1
# => the same random numbers will continue to pop up because we have the same seed

random.seed(10)

for _ in range(5):
    rand: int = random.randint(100, 999)

    print(rand, end=" ")
print()


# seed 2
# => the same random numbers will continue to pop up because we have the same seed

random.seed("hello")

for _ in range(5):
    rand: int = random.randint(100, 999)

    print(rand, end=" ")
