
# default parameter: python issues an error when we have omitted an argument either on purpose or deliberately, but default parameters let you eliminate that, by setting default values to undefined arguments

"""
Value: - When using numbers as default values it is better to user float than int, bcs when int is used only int values are expected but with            floats where any value is welcome
       - Default parameters must come after positional ones if any
"""

# ex: 1, Finding Force
# => This function will calculate the force using mass and acceleration inputs, but if the mass or acceleration is not given python will issue an error


def forceFinderNoDefault(mass, acceleration):
    return mass * acceleration


result_1 = forceFinderNoDefault(5.6, 4)
# result_2 = forceFinderNoDefault(mass=87)  # ERROR: TypeError: forceFinder() missing 1 required positional argument: 'acceleration'
# result_2 = forceFinderNoDefault(87)  # ERROR: TypeError: forceFinder() missing 1 required positional argument: 'acceleration'
print(result_1)


# ex: 2
# => This function will calculate the force using mass and acceleration inputs, but if the acceleration is not given then it will default to 10

def forceFinderWithDefault(mass, acceleration=10.0):
    return round(mass * acceleration, 2)


result_1 = forceFinderWithDefault(78.3, 8)
result_2 = forceFinderWithDefault(34, 14.678)

result_3 = forceFinderWithDefault(34)
result_4 = forceFinderWithDefault(mass=55)
# result_5 = forceFinderWithDefault(acceleration=55)  ERROR: TypeError: forceFinderWithDefault() missing 1 required positional argument: 'mass'
# result_5 = forceFinderWithDefault()  ERROR: TypeError: forceFinderWithDefault() missing 1 required positional argument: 'mass'

print(result_1)
print(result_2)
print(result_3)
print(result_4)


def forceFinder(mass=1, acceleration=10.0):
    return round(mass * acceleration, 2)


result_1 = forceFinder(13, 6.7)
result_2 = forceFinder(13)
result_3 = forceFinder(mass=45)
result_4 = forceFinder()
result_5 = forceFinder(acceleration=4.7)

print(result_1)
print(result_2)
print(result_3)
print(result_4)
print(result_5)


# Mutation control

# ex:1 Prime numbers


prime_numbers_array = []


def prime_numbers(start, end, primary_numbers, numbers_array):
    for number in range(start, end):
        if number in primary_numbers:
            numbers_array.append(number)
        elif number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
            numbers_array.append(number)
    return numbers_array


range_1 = prime_numbers(5, 20, [1, 2, 3, 5, 7], prime_numbers_array)
print(prime_numbers_array)

# Re-using this array appends even more values to it, making it total mutated and lose it originality, this is a side-effect
range_2 = prime_numbers(5, 20, [1, 2], prime_numbers_array)
print(prime_numbers_array)

range_3 = prime_numbers(89, 120, [1, 2], prime_numbers_array)
print(prime_numbers_array)

print(range_1)
print(range_2)
print(range_3)
# the prime_numbers_array has been mutated, which is not a good practice in code


# Solution
# We create default values for every possible argument, and for mutable value we set them to None(immutable) first and later change them to the mutable state to avoid side-effects


def prime_numbers(start=0, end=100, primary_numbers=None, numbers_array=None):
    if numbers_array is None:
        numbers_array = []
    if primary_numbers is None:
        primary_numbers = [1, 2, 3, 5, 7]

    for number in range(start, end):
        if number in primary_numbers:
            numbers_array.append(number)
        elif number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
            numbers_array.append(number)
    return numbers_array


range_1 = prime_numbers(4, 50)
range_2 = prime_numbers(start=10, end=101)
range_3 = prime_numbers(end=330)

print(range_1)
print(range_2)
print(range_3)

# ex: 3 Sentence generator


def generate_sentence(words_array, separator=" ", full_sentence=None, count=None):
    if full_sentence is None and count is None:
        full_sentence = ""
        count = 0

    for word in words_array:
        count += 1

        if count < len(words_array):
            word = word + separator
        elif count >= len(words_array):
            word = word + "?"

        full_sentence += word

    return full_sentence


generative_1 = ["Hello", "friend"]
generative_2 = ["How", "are", "you"]
generative_3 = ["How", "are", "you", "doing"]

sentence_1 = generate_sentence(generative_1, "+")
sentence_2 = generate_sentence(generative_2, "_")
sentence_3 = generate_sentence(generative_3)

print(sentence_1)
print(sentence_2)
print(sentence_3)
