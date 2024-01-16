
# starmap: is an itertools method that is used to map through values of a list of tuples to return some calculations


from itertools import starmap

numbers: list[tuple] = [(0, 2), (1, 2), (2, 2)]

squares = list(starmap(pow, numbers))

print(squares)
