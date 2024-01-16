
# Arithmetic: Are operators used to perform arithmetic operations upon their operands

number_1 = 9
number_2 = 4

addition = number_1 + number_2
print(addition)

subtraction = number_1 - number_2
print(subtraction)

multiplication = number_1 * number_2
print(multiplication)

division = number_1 / number_2
print(division)

floor_division = number_1 // number_2  # no floating points in result set
print(floor_division)

modulus_or_remainder = number_1 % number_2
print(modulus_or_remainder)

power = number_1 ** number_2  # equiv =>  pow(number_1, number_2)
print(power)


# With dictionaries

cities = {
    1: "Kinshasa", 2: "Kigali", 3: "Kampala", 4: "Accra", 5: "Abuja"
}


print(cities)
# print(cities + 2) => TypeError: unsupported operand type(s) for +: 'dict' and 'int'
