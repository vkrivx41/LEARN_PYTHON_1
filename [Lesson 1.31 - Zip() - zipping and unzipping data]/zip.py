
# combination

names: list[str] = ["Bob", "Mike", "John", "David"]
ages: list[int] = [16, 18, 61, 76]

# Method 1

for i in range(len(names)):
    print(f"Name: {names[i]}, Age: {ages[i]}")

# Method 2: zip

zipped_names_and_ages: list = list(zip(names, ages))
print(zipped_names_and_ages)

for name, age in zipped_names_and_ages:
    print(f"Name: {name}, Age: {age}")


# use-cases

# 1: Finding the profit from sales list and costs list

sales: list[int] = [100, 210, 290, 190, 420]
costs: list[int] = [90, 120, 200, 210, 400]

for sale, cost in zip(sales, costs):
    print("Profit:", sale - cost)


# 2: unzipping zipped elements

zipped_names_and_ages = [("Mike", 30, 10000), ("John", 86, 50000), ("Jeremy", 56, 220000), ("Pascal", 41, 900000)]

names, ages, salaries = zip(*zipped_names_and_ages)

print(names, list(names))
print(ages, list(ages))
print(salaries, list(salaries))

# 3: sorting two separate list with linked elements
# => In this way the order of the linkage between the elements is not lost, and well sorted as well

numbers: list[int] = [4, 1, 3, 2]
letters: list[str] = ['b', 'd', 'a', 'c']

numbers_and_letters_sorted = sorted(zip(numbers, letters))
letters_and_numbers_sorted = sorted(zip(letters, numbers))

print(numbers_and_letters_sorted)
print(letters_and_numbers_sorted)


# 4: creating a dictionary

names: list[str] = ['Mike', 'John', 'Jeremy', 'Pascal']
ages: list[int] = [30, 86, 56, 41]
salaries: list[int] = [10000, 50000, 220000, 900000]

employees = dict(zip(names, ages))

print(employees)

# zip as an iterator

zipped = zip(names, ages)

print(next(zipped))
print(next(zipped))
print(next(zipped))

for name, age in zipped:
    print(name, age)

# After all the operations the zip object gets exhausted

print(zipped)
print(list(zipped))

# print(zipped_list)
