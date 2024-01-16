
# Doc-string: Is full explanation of a function, determining what the params are, their types and what the return
# value is about

"""
Values - Written explicitly inside the function
       - We see what's the doc-strings are about after hovering over the function, either on the declaration block or
        the calling part
       - When there is no parameter applied, then the documentation appears with none
       - Exception can also be defined in the doc-string to demonstrate what kind of exception the function can handle
"""


def force_finder(mass: int, acceleration: float = 9.8) -> float:
    """
    Finds the force applied to a body by multiplying it's mass and acceleration

    :param mass: The mass of the body
    :param acceleration: The acceleration due to gravity applied
    :return: The product of the two entities (mass * acceleration)
    """

    return round(mass * acceleration, 2)


force_1 = force_finder(56, 3.19)
force_2 = force_finder(5.2)

print(force_1)
print(force_2)


def say_hello(first_name: str, last_name: str, time: int) -> str:
    """
    Greets a person according to the time given

    :param first_name: The first name of the person
    :param last_name: The last name of the person
    :param time: The time of the greeting
    :return: A greeting considering the time
    :exception : Exception
    """

    if type(time) == str:
        raise Exception("Time must be int")

    if time in range(0, 12):
        return f"Good morning, {first_name.upper()} {last_name}."
    elif time in range(12, 17):
        return f"Good afternoon, {first_name.upper()} {last_name}."
    elif time in range(17, 20):
        return f"Good evening, {first_name.upper()} {last_name}."
    else:
        return f"Good night, {first_name.upper()} {last_name}."


morning_greeting = say_hello("Scorpus", "Mnugnes", 12)
print(morning_greeting)

evening_greeting = say_hello("niK", "Bun", 19)
print(evening_greeting)

# evening_greeting = say_hello("niK", "Bun", "19")


# Read more about doc-string
# We can see what is stored in the doc-string by these two means

print(say_hello.__doc__)
print(help(say_hello))

