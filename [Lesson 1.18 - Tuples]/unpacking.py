
# unpacking (works on lists too)
# => Is the technique of unpacking or creating variables to hold iterable's element on a single line
# Note: The variables count must match the length of the iterable, otherwise python issues an error

fruits: tuple [str, ...]= "Mango", "Lemon", "Watermelon", "Cherry"
one, two, three, four = fruits

print(one)
print(two)
print(three)
print(four)

# the * => returns a list of elements
# => the *, unpacks all the remaining part of elements from the iterable,

cars: tuple[str, ...] = "Mercedes", "Bugatti", "Lamborghini", "Hammer", "SUV"

# one, two = cars  # ERROR: ValueError: too many values to unpack (expected 2)

car_one, *others, car_last = cars
car_one_again, *others_again, car_second_last_again,car_last_again = cars

print(car_one)
print(car_last)
print(others)

print(car_one_again)
print(car_last_again)
print(others_again)
