# Membership operators: are operators which checks for relationships between two compared operands


group_members = ['nik', 'bun', 'ella', 'joe', 'gav']

bella_is_in_group = "bella" in group_members
nik_is_in_group = "nik" in group_members
joe_is_not_in_group = "joe" not in group_members
Gav_is_in_group = "Gav" in group_members  # => we should get False because all the values are case-sensitive

print(bella_is_in_group, nik_is_in_group, joe_is_not_in_group, Gav_is_in_group)

search_member = input("Enter the name of the member? ")

member_found = "is in the group" if search_member in group_members else "is not in the  group"
print(search_member + " " + member_found)

# With dictionaries
# => Target only the keys not values

countries_with_cities = {
    "DRC": "Kinshasa", "Rwanda": "Kigali", "Uganda": "Kampala"
}

burundi_in_dict = "Burundi" in countries_with_cities
DRC_in_dict = "DRC" in countries_with_cities
kigali_not_in_dict = "Kigali" not in countries_with_cities

print(burundi_in_dict, DRC_in_dict, kigali_not_in_dict)


# With strings

name_1 = "nik"

print("n" in name_1)
print("x" not in name_1)

# With int
# => Works with only iterable types

number_1 = 901

# print(1 in number_1) => TypeError: argument of type 'int' is not iterable
