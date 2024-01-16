# Enclosing scope: is the scope inside of anothe scope, it usually applied to nested function -- closures

from typing import Union


def outer():
    x = "outer x"  # local scope in the outer function

    def inner():
        x = "inner x"  # enclosed scope in the inner function
        print(x)

    print(x)
    inner()


outer()


# Ex: 2
# Note: x is available in both outer() and inner() function

def outer():
    x = "outer x"  # local scope in the outer function

    def inner():
        print(x)  # prints the outer x

    print(x)
    inner()


outer()

# ex: 3

x = "most outer x"


def outer():
    print(x)  # prints the most outer x

    def inner():
        print(x)  # prints the most outer x

    inner()


outer()


# ex: 4

def outer():
    def inner():
        x = "inner x"
        print(x)  # prints the inner x

    print(x)  # prints the most outer x
    inner()


outer()


# ex: 4

def outer():
    x = "outer x"

    def inner():
        print(x)  # prints the outer x

    print(x)  # prints the outer x
    inner()


outer()


# Enclosed scope mutation: nonlocal


def outer():
    x = "outer x"

    def inner():
        nonlocal x

        x = "outer: Mutated"
        print(x)

    print(x)
    inner()


outer()


# Counter example using closures

def counter_function():
    count = 0

    def inner_counter():
        nonlocal count

        count += 1
        return count

    return inner_counter


# Here we call the counter_function() and assing it to count which store the inner_counter function being returned by it,
# the count variable is assigned to 0

counts = counter_function()

# Each time we call counts() as a function -- it holds the inner_counter function, we add 1 to counts declared in the upper function by the help of the nonlocal statement

print(counts())  # 1
print(counts())  # 2
print(counts())  # 3
print(counts())  # 4
print()


# credits
# => The game with throw an error when the lives or credits are equal or under zero '0'


def lives_counter(lives: int):
    count: int = lives

    def counter():
        nonlocal count
        count -= 1

        if count > 0:
            return count

        raise Exception("Game over!")

    return counter


counting = lives_counter(5)

try:
    print(counting())
    print(counting())
    print(counting())
    print(counting())
    print(counting())
    print(counting())
except Exception:
    print("Game over")


# ex: add names

def add_name(old_list):
    names: list[str] = []
    count: int = 0

    def inner() -> list[str]:
        nonlocal names, count

        # check if the length of the names list is less than the old list to ensure that an element will be appended in it
        if len(names) < len(old_list):
            names.append(old_list[count])

        # increase the count by 1 each time, to ensure that we shall pick the next element from the old list in the next iteration
        count += 1

        return names

    return inner


# creation of a calling function that returns the inner function
names_list: list[str] = ["nik", "bun", "ella", "joe", "gav"]

adder = add_name(names_list)

# calling this function will append a new name to the list of names from the list of names_list and returns the list
# => If the new list's length is equal to the old list's length then the new list will be returned as it is

print(adder())
print(adder())
print(adder())
print(adder())
print(adder())
print(adder())
print(adder())
print(adder())
print(adder())
print(adder())
print(names_list)


# ex: add names

def add_name(old_list):
    names: list[str] = []
    count: int = 0

    def inner() -> Union[list[str], str]:
        nonlocal names, count

        # check if the length of the names list is less than the old list to ensure that an element will be appended in it
        if len(names) < len(old_list):
            names.append(old_list[count])
            return names

        # increase the count by 1 each time, to ensure that we shall pick the next element from the old list in the next iteration
        count += 1

        return "List out of range"

    return inner


# creation of a calling function that returns the inner function
names_list: list[str] = ["nik", "bun", "ella", "joe", "gav"]

adder = add_name(names_list)

# calling this function will append a new name to the list of names from the list of names_list and returns the list
# => If the new list's length is equal to the old list's length then the new list will be returned as it is

print(adder())
print(adder())
print(adder())
print(adder())
print(adder())
print(adder())
print(adder())
print(adder())
print(adder())
print(adder())
print(names_list)


# prizes


def prizes_determiner(prizes: list[str]):
    current_level: str = ""
    count: int = 0

    def inner(level=count):
        nonlocal current_level, count

        # return the previous level if the user has failed the question
        if level < 0:
            count += level

        # check if the count is less than the prizes and then return the current_level by one leve up
        if count < len(prizes):
            current_level = prizes[count]

        # increase the count, to ensure a new level will be picked next time
        count += 1

        return current_level

    return inner


levels = ["Beginner", "Amateur", "Intermediate", "Advanced", "Master", "Grand Master"]

questions: list[dict[str: str]] = [
    {'number': 1, 'question': "What is 2 * 2 : ", 'answer': "4"},
    {'number': 2, 'question': "What is 10 + 9 : ", 'answer': "19"},
    {'number': 3, 'question': "What is 6 / 3 : ", 'answer': "2"},
    {'number': 4, 'question': "What is 10 + 5 * 2 : ", 'answer': "20"},
    {'number': 5, 'question': "What is 11 - 15 : ", 'answer': "-4"},
    {'number': 6, 'question': "What is 0 / 18 : ", 'answer': "0"},
]

determiner = prizes_determiner(levels)

counter = 0

while counter < len(questions):
    number: int = questions[counter]['number']
    question: str = questions[counter]['question']
    answer: str = questions[counter]['answer']

    response: str = input(str(number) + ". " +question)

    if response != answer:
        end_level = determiner(-1)

        if counter == 0:
            end_level = "Zero"

        print(f"No levels up, your end level was {end_level} come back stronger the next time!")
        break

    if number == len(questions):
        end_level = determiner()

        print(f"Hooray, You have completed the whole question bank with the level {end_level}!")
        break

    new_level = determiner()
    print(f"You have completed the {new_level}'s level keep going!")

    counter += 1