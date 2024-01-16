
# cycle: Is an itertools method that is used to cycle against an iterable an infinity number of times

from itertools import cycle

numbers: list[int] = [1, 2, 3]

cycle_1 = cycle(numbers)

# counter for terminating the loop

counter: int = 0
for cyc in cycle_1:
    counter += 1
    if counter >= 12:
        break
    print(cyc)


# sets don't have a certain ordet to follow so the data order during cycling is always arbitrary

switch: set[str] = {"On", "off"}

switcher = cycle(switch)

#  on or off can come first

print(next(switcher))
print(next(switcher))
print(next(switcher))
print(next(switcher))

