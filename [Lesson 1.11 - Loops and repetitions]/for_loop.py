# for loop: is a loop or code-repetition algorithm that is used to count numbers, iterates through objects and iterables as well as doing all repetition related stuffs

"""
Values: - Must have a stopping index -- unlike while which sometimes runs infinitely
        - an _ can be used to take the place of the iterated items when its not necessary to be using it
        - The range function is used to create a list on the fly for iteration purposes
"""

# The range function
# range(start, end, step)

"""
Values: - when only one parameter is produced the start is omitted and default to zero and that place it taken as the end
"""

# print hello, scorpus 3*
# => This alternative used a user-defined list to iterate the amount of times the list measures by length

for i in [1, 2, 3]:
    print("Hello, scorpus")

# => Here we use the underscore to represent the iterables bcs the variable of it is not going to be used any where in the loop

for _ in [1, 2, 3]:
    print("Hello, scorpus")

# => This alternative also works correct bcs we iterate through a string of length 3

for _ in "1" * 3:
    print("Hello, scorpus")

# => the range() function create a list during code execution to iterate through
# => here the loop should run from 0 to 3 but not through 3, i.e 0, 1, 2

for _ in range(3):
    print("Hello, scorpus")

# other range parameter

for number in range(10):
    print(number)

# here we shall go all the way from 1 to 9, bcs 10 is omitted

for number in range(1, 10):
    print(number)

# here we shall go all the way from 10 to 2, bcs 1 is omitted, and the step must be -1 to start from the top to the bottom decrementing the number by 1

for number in range(10, 1, -1):
    print(number)

# => this runs from 9 to 0
for number in range(9, 0, -1):
    print(number)

# the step parameter in deep

# => this returns all odd numbers from the range of 1 to 100
for number in range(1, 100, 2):
    print(number)

# => this returns all even numbers from the range of 0 to 100
for number in range(0, 100, 2):
    print(number)

# => this is the alternative algorithm of the above example, returns all even numbers from the range of 100 to -1
for number in range(100, -1, -2):
    print(number)

# fizz buzz
# => we use the continue statement to avoid printing both Fizz and Buzz on a number that is a Fizz Buzz, but repeat the loop if found that number

for number in range(1, 100):
    if number % 3 == 0:
        if number % 5 == 0:
            print(f"{number}: Fizz Buzz")
            continue  # the loop will restart over once it finds out this number
        print(f"{number}: Fizz")
    elif number % 5 == 0:
        print(f"{number}: Buzz")
    else:
        print(f"{number}:")

# => This is an alternative of the Fizz Buzz example which doesn't use the continue statement

for number in range(100, 0, -1):
    if number % 3 == 0 and number % 5 == 0:
        print(f"{number}: Fizz Buzz")
    elif number % 3 == 0:
        print(f"{number}: Fizz")
    elif number % 5 == 0:
        print(f"{number}: Buzz")
    else:
        print(f"{number}:")

# prime numbers


numbers = range(1, 100)
prime_numbers = []

for number in numbers:
    if number & 1 != 0:
        if number % 3 != 0 and number % 5 != 0:
            prime_numbers.append(number)

print(prime_numbers)


# iterate strings

name = "Scorpus"

for character in name:
    print(character, end="-")

print()


# remove the last hyphen

# we define a variable as a counter and increment it on each iteration, and when it reaches the length of the name it must bring the last character and then break the loop to avoid it from continuing which can result into print double last character and a -

counter = 0
for character in name:
    counter += 1

    if counter >= len(name):
        print(character, end="")
        print()  # this is to put a new line after the last character
        break  # continue can also work the same here, bcs it will revert back to the beginning and skip the if statement

    print(character, sep="", end="-")


# change a word into lowercase
# we set our list to None by default to prevent side-effects and mutation and then check if it is None and set it to an empty list before adding or appending any raw data to it

def change_to_lower(word, lower_word=None):
    if lower_word is None:
        lower_word = []
    for char in word:
        if char.isupper():
            char = char.lower()

        lower_word.append(char)

    return "".join(lower_word)


print(change_to_lower("HellO"))
print(change_to_lower("LuiGi"))
print(change_to_lower("MARIO"))


# dictionaries
# => we unpack a dictionary the same way, but using the .items() method on it allow us to access both the keys and values

cities = {'drc': 'kns', 'rda': 'kgl', 'ug': 'kmp'}

for country, city in cities.items():
    print(country,"=" , city)

# we use to .values() method to only access the values

for city in cities.values():
    print(city)


# for tuples

numbers = (1, 2, 3, 4, 5)

for number in numbers:
    print(number)
    # for tuples

#  for sets

numbers = {1, 2, 3, 4, 5}

for number in numbers:
    print(number)