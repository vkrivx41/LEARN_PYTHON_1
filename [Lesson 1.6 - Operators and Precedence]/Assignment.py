
# Assignment Operators: are operators used to assign values to variables

number_1 = 10
number_2 = 5


assignment = number_2
print(assignment)

# Compound operators
number_3 = 0
number_4 = 0
number_5 = -1.7
number_6 = number_7 = number_8 = 14
number_9 = 10e-3  # 10 * 10 ^ -3

number_3 += number_1  # number_3 = number_3 + number_1
number_4 -= number_2  # number_4 = number_4 - number_2
number_5 *= number_1  # number_5 = number_5 * number_1
number_6 /= number_2  # number_6 = number_6 / number_2
number_7 //= number_2  # number_7 = number_7 / number_2
number_8 %= number_2  # number_8 = number_8 % number_2
number_9 **= number_1 # number_9 = number_9 ** number_1

print(number_3, number_4, number_5, number_6, number_7, number_8, number_9)


number_10 = 9
# number_10 += number_1 + number_6 => No error
# number_10 += number_1 += number_6 => ERROR: Invalid syntax

# With booleans

number_10 += True
print(number_10)


# With strings
# => The two strings are merged together to form just one
# => Eligible operators is only +=

name_1, name_2 = "nik", "bun"

name_1 += name_2
name_2 += "ella"

# name_1 -= name_2 => ERROR: Unsupported operand

print(name_1, name_2)

# With lists
# => The two lists or tuples are merged together and form one containing all the values
# => Eligible operators is only +=

marks_1 = [6, 2, 0, 8, 7]
marks_1 += [1, 3]
# marks_1 -= [1, 3] => ERROR: Unsupported operand

print(marks_1)


# With dictionaries

cities = {
    1: "Kinshasa", 2: "Kigali", 3: "Kampala", 4: "Accra", 5: "Abuja"
}


print(cities)

# cities += {0: "Cape Town"} => TypeError: unsupported operand type(s) for +=: 'dict' and 'dict'

print(cities)