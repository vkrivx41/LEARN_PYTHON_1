# lambda function: a lambda function is an anonymous function, it is defined without a name and without using the def keyword

"""
Values: - Can takes a various number of arguments but can only execute one expression
        - Suitable for one-liner expression because a lambda can't take two or more expression
        - Not highly recommended because lambda reduce code readability and maintenance
"""


# normal function

def exponential(base, exponent):
    return base * exponent


value_0 = exponential(-4, .7)
value_1 = exponential(4, 60)

print(value_0, value_1)

# lambda version: of the same code

exponential = lambda base, exponent: base * exponent

value_2 = exponential(8, 2)
value_3 = exponential(-7, 6)

print(value_2, value_3)


# lambda with default values:
# Note: as normal function lambda also has the ability to take one or more default values in the parameter considering the default parameters rules

force_calculator = lambda mass, acceleration=9.8: mass * acceleration

force_1 = force_calculator(5, 4.5)
force_2 = force_calculator(5)

print(force_1, force_2)


# lambda with named arguments
# Note: lambda functions can also take named arguments during function invoking


animals_action = lambda animal, action: f"{animal} does {action}"

action_1 = animals_action("cat", "meow")
action_2 = animals_action("moow", "cow")
action_3 = animals_action(action="woow", animal="dog")

print(action_1)
print(action_2)
print(action_3)


# immediate call
# Note: python lambda like any other programming language's anonymous function can be called immediately


area_1 = (lambda radius, pi=3.14: pi * radius ** 2)
area_2 = (lambda radius, pi=3.14: pi * radius ** 2)(3)

print(area_1)
print(area_2)

# lambda with inside logic

even_or_odd = (lambda number: number % 2 == 0 and "Even" or "Odd")(-3)

print(even_or_odd)


# What lambda can't do
# Note: A lambda function can't perform all these expression and processes, it's limited to only take one line of code

def odd_numbers(min: int, max: int) -> list[int]:
    odds: list = []

    for number in range(min, max):
        if number % 2 != 0:
            odds.append(number)

    return odds


odds_1 = odd_numbers(4, 17)

print(odds_1)

# lambda in a closure
# Note: Using lambda in an inner scope -- closure, eliminates the use of nonlocal keyword

# Normal function example


def multiplier(number: int):
    def inner(x):
        nonlocal number

        return x * number
    return inner


seven_multiplier = multiplier(7)

print(seven_multiplier(1), seven_multiplier(2))


# same example using lambda

def multiplier(num: int):
    return lambda x: x * num


nine_multiplier = multiplier(9)

for number in range(1, 13):
    print(nine_multiplier(number), end=" ")
