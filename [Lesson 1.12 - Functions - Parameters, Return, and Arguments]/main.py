
# functions: is a vast concept in almost all programming that enable programs to break large and complex tasks
# into small-wrapped blocks of code stored if a piece of objects -- a function

"""
Values: - Function emphasizes cleaner and readable code
        - In python and other languages a function can take zero or more parameters
        - In python a function returns None by default
        - In python two or more functions can be defined with the same name and cause no harm to the interpreter, it is not recommended for the user because it may lead to misunderstanding of the program
"""

# ex: 1
# => this function prints the two statements and returns None because if has no return value
# Note: When we print it will execute all the statements inside it and then print None at the end marking the default return value
import math


def sayHello():
    print("Hello, Scorpus")
    print("How are you feeling?")


sayHello()
print(sayHello())

# ex: 2 return value
# => this function returns a string saying hello to scorpus, that means that it return value is no longer None but string <str>
# Note: After returning a value from a function we can store the value inside a variable a reuse it everywhere in code


def sayHello():
    return """
        Hello, Scorpus
        How are you feeling?
    """


greeting = sayHello()

print(greeting)
print(sayHello())

# ex: functions a objects
# => Each time we create a function is occurs a unique space in memory, no two function can point to the same address even though they might have same return values


def pi():
    return math.pi


def piTwo():
    return math.pi


print(pi)
print(piTwo)

# => Comparing the function will return False
print(pi == piTwo)

# => Comparing the return value of alike function yields to True
print(pi() == piTwo())

# ex: 4 functional assignment
# => When we assign a function to a variable in code, that variable also takes and points to the same address as the function it is assigned to, this is done to maintain memory and avoid redundancy
# Note: Comparison using the identity operator 'is' also yield to True, because the pointed memory address is the same for the two functions

another_pi = pi

print(pi)
print(another_pi)
print(pi == another_pi)
print(pi is another_pi)
print(id(pi), id(another_pi))
print(pi(), another_pi())

# ex: 5 arguments and parameter
# => A function allows to take a certain amount of parameters either zero or more, the values provided when calling the function is programmatically called parameters and the ones wrapped between the parenthesis are called arguments


def find_sum(num1, num2):
    return num1 + num2


result_1 = find_sum(10, -8)
result_2 = find_sum(918, 7819)

print(result_1)
print(result_2)


# ex: 6 possible errors
# => there are errors that probably occurs when writing function
# Note: the arguments and parameter count must match


def area_of_a_circle(radius):
    return round(math.pi * math.pow(radius, 2), 2)


circle_1 = area_of_a_circle(10)
circle_2 = area_of_a_circle(-8.6)
# circle_3 = area_of_a_circle()  # ERROR: TypeError: area_of_a_circle() missing 1 required positional argument: 'radius'

print(circle_1)
print(circle_2)
# print(circle_3)
