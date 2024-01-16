
# else statement: Improve our code readability and reduces bugs in the future
# by stopping the execution after having failed the previous ones

number_1: int = int(input("Enter a number: "))
number_2: int = int(input("Enter another number: "))

if number_1 < number_2:
    print(f"{number_1} is less than {number_2}")
elif number_1 > number_2:
    print(f"{number_1} is greater than {number_2}")
else:
    print(f"{number_1} is equal to {number_2}")


