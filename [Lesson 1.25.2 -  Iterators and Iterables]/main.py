# iterators and iterables are confusing topic because there are not easy to differentiate at first

# iterable: An iterable is something that can be looped over, this is a list, tuple, set, dict, generator, string, file,
# and other entities
""""
Values: - iterables contain a magic method called __iter__() that enables looping because it creates an iterator behind
            the scenes
        - don't remember their state of iteration
        - don't have __next__() magic method
"""

# checking for an iterable

nums: list[int] = [1, 2, 3]

# 1: it can be looped over
for num in nums:
    print(num)

# 2: it contains the __iter__() method
# nums: float = 5.7  # this is not an iterable

if "__iter__" in dir(nums):
    print("Entity is an iterable")
else:
    print("Entity is not an iterable")

