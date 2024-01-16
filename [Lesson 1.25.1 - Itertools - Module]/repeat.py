
# repeat: is an itertools method that is used to repeat a certain value a specified number of times

import itertools

counter: itertools.repeat = itertools.repeat(1, times=4)

print(counter)

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
# print(next(counter))  # ERROR: StopIteration

for item in counter:
    print(item)


#


squares = map(pow, range(10), itertools.repeat(2))

print(list(squares))




