
# Comparison: are operators available for the purpose of comparing values to help in decision making and control flow

"""
Values: - They yield a bool answer -- True or False
        - According to he level of precedence > comes in before than <, and < comes before == and !=
        - The associativity -- the side from which the operation takes place from is right-to-left
        - When comparing more than 2 operands the result of the first operation is
        considered to be the largest and it's then compared to the rest of the expression

"""

number_1 = 10
number_2 = 5

greater_than = number_1 > number_2
less_than = number_1 < number_2
greater_than_or_equal = number_1 >= number_2
less_than_or_equal = number_1 <= number_2
not_equal = number_1 != number_2
equal = number_1 == number_2


print(greater_than, less_than, greater_than_or_equal, less_than_or_equal, not_equal, equal)


# For strings
# => A string is greater than the other when it's first character comes first in the alphabet,
# this method of comparison can also be used for sorting purposes.

string_1 = "bob"
string_2 = "pascal"
string_3 = "nik"

greater_than = string_1 > string_2 > string_3
less_than = string_1 < string_2 > string_3

print(greater_than, less_than)


print(6 < 5 > 9 < 6 < 1 > 4)  # 6 < 9 < 6 < 4, 9 < 6 => False
print(7 < 8 < 9 > 3 < 2 < 0 > 6)  # 7 < 8 < 9 < 2 < 6, 8 < 9 < 6, 9 < 6 => False
print(4 == 6 < 1)  # 4 == 6 => False
print(5 == 8 == 8)  # 5 == 8



# List and tuples
# => The multiplication of all elements in the list or tuple is the converted to a single value to be compared through

list_1 = [4, 6, 1]
list_2 = [0, 20]
list_3 = ['nik', 'bun']

greater_than = list_1 > list_2
less_than = list_1 < list_2
# greater_than_or_equal = list_1 >= list_3  Error: Unsupported operand btn str and int

print(greater_than, less_than, greater_than_or_equal)

# With dicts
#  => dictionaries doesn't support comparison operations

cities_1 = {
    1: "Kinshasa", 2: "Kigali", 3: "Kampala", 4: "Accra", 5: "Abuja"
}

cities_2 = {
    1: "Kinshasa", 2: "Kigali", 3: "Kampala", 4: "Accra", 5: "Abuja"
}

# greater_than = cities_1 > cities_2 => TypeError: '>' not supported between instances of 'dict' and 'dict'

print(greater_than)