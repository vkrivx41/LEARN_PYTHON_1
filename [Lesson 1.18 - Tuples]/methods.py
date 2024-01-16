# 1: count
# => Counts for the number of occurrences of an element, returns 0 if not found

fruits: tuple = "Mango", "Avocado", "Orange", "Pawpaw", "Blueberry"

counter_1: int = fruits.count("Mango")
counter_2: int = fruits.count("Lemon")

print(counter_1)
print(counter_2)

# 2 indexindex_1: int = cities.index("Kampala")
# => Returns the index of the first occurrence of the element, throws an error if not found

cities: tuple[str, ...] = ("Kinshasa", "Kigali", "Kampala")

index_1: int = cities.index("Kampala")
# index_2: int = cities.index("Accra")  # ERROR: ValueError: tuple.index(x): x not in tuple

print(index_1)

# copy
# deep copy
# => Tuples only accepts deep copy because they are immutable

cars: tuple[str, ...] = "Mercedes", "Bugatti", "Lamborghini", "Hammer", "SUV"

cars_copy = cars

print(cars_copy)
print(cars)

# shallow copy
# => This approach helps nothing as tuples are not to be changed

cars_again: tuple[str, ...] = "Mercedes", "Bugatti", "Lamborghini", "Hammer", "SUV"

cars_again_copy = tuple(cars_again)

print(cars_again)
print(cars_again_copy)

