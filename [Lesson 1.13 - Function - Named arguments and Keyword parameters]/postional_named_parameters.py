# Positional arguments: are arguments that depends on the positions of the parameters
# Named arguments: are arguments that don't depend on the positions of the parameters, but on the names provided in the parameter list

"""
Values: - Both positional and named arguments can be mixed, but consider that positional arguments can't come after named ones
        - Named arguments are generally used to functions with a lot of confusing inputs
        - Only python built-in function accept named arguments after positional ones ex: print()
"""


# Positional


def divide(divisor, divider):
    return round(divisor / divider, 2)


result_1 = divide(4, 2)
result_2 = divide(-9.7, 2.01)
result_3 = divide(2, 4)

print(result_1)
print(result_2)
print(result_3)


def country_and_city(country, city, population):
    return f"{city} is a city in {country}, It has a population of {population} people. "


sentence_1 = country_and_city("DRC", "Kinshasa", 30_000_000)
sentence_2 = country_and_city("Ghana", "Accra", 23_000_000)

# => when we don't follow the positions of the parameters our program logic may fall.
# Thus this sentence will print that "Nigeria is a city in Lagos"

sentence_3 = country_and_city("Lagos", "Nigeria", 60_000_000)
sentence_4 = country_and_city(2_000_000, "Rwanda", "Kigali")
sentence_5 = country_and_city("Uganda", 16_000_000, "Kampala")

print(sentence_1)
print(sentence_2)
print(sentence_3)
print(sentence_4)
print(sentence_5)

# Named Arguments
# => Provides the solutions to the above issue, named arguments are generally used in case there is a lot of confusing arguments to be passed to a certain function


def divide(divisor, divider):
    return round(divisor / divider, 2)


# No change can be noticed here because either the positional or named arguments are passed accordingly
result_1 = divide(divisor=4, divider=2)
result_2 = divide(4, 2)

# There is a change here because 10 took the divider's place and divisor was set to -5.6 different to the positional arguments which just stayed the same, making it hard to retrieve the expected task

result_3 = divide(divider=10, divisor=-5.6)
result_4 = divide(10, -5.6)

print(result_1)
print(result_2)
print(result_3)
print(result_4)


# ex: 3


def country_and_city(country, city, population):
    return f"{city} is a city in {country}, It has a population of {population:,} people. "


result_1 = country_and_city(country="DRC", city="Kinshasa", population=30_000_00)
result_2 = country_and_city("DRC", "Kinshasa", 30_000_00)

result_3 = country_and_city(population=23_000_000, country="Ghana", city="Accra")

# Note: Both positional and named arguments can be mixed, but consider that positional arguments can't come after named ones

result_4 = country_and_city(population=23_000_000, country="Ghana", city="Accra")
# result_5 = country_and_city(city="Lagos", country="Nigeria", 60_000_000)
result_5 = country_and_city("Nigeria", city="Lagos", population=60_000_000)


print(result_1)
print(result_2)
print(result_3)
print(result_4)
print(result_5)


def perimeter_of_rectangle(length, width):
    return 2 * (length + width)


circle_1 = perimeter_of_rectangle(10, 5)
circle_2 = perimeter_of_rectangle(5, 10)


print(circle_1)
print(circle_2)
