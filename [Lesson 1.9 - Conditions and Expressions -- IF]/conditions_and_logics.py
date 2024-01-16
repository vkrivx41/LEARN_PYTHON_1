#


number_1: int = int(input("Enter a number: "))
number_2: int = int(input("Enter another number: "))

# logical operator or

if number_1 > number_2 or number_1 < number_2:
    print(f"{number_1} is not equal to {number_2}")
else:
    print(f"{number_1} is equal to {number_2}")

# logical operator and

if number_1 % 2 == 0 and number_2 % 2 == 0:
    print(f"Both {number_1} and {number_2} are even numbers")
elif number_1 % 2 != 0 and number_2 % 2 != 0:
    print(f"Both {number_1} and {number_2} are odd numbers")
else:
    print(f"Either {number_1} or {number_2} is an even number.")

# logical operator not

if not number_1 % 2 == 0:
    print(f"{number_1} is an odd number")
else:
    print(f"{number_1} is an even number")


