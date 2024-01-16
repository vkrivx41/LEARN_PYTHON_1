
# creation or definition
# empty dict

empty_dict_1: dict = {}
empty_dict_2: dict = dict()

print(empty_dict_1)
print(empty_dict_2)

# key, value paris

countries_and_cities: dict[str, str] = {
    'USA': "Washington",
    'Russia': "Moscow",
    'DRC': "Kinshasa",
    'China': "Beijing",
}

print(countries_and_cities)


# second alternative: named arguments
# => Named arguments are essential for creating dictionaries
# Note: keys are not wrapped in brackets

countries_and_players: dict[str, str] = dict(Brazil="Pele", Argentina="Messi", Germany="Gerd", Portugal="Cristiano")

print(countries_and_players)

# indexing
# => when indexing we use the keys as a reference, throws an error when key not found

city_1: str = countries_and_cities['USA']
city_2: str = countries_and_cities['China']
player_1: str = countries_and_players['Argentina']
# city_3: str = countries_and_cities['India']  # ERROR: KeyError: 'India'

print(city_1)
print(city_2)
print(player_1)

# adding elements
# adds the new element at the end

countries_and_cities['India'] = "NewDehli"
countries_and_cities['Japan'] = "Tokyo"

print(countries_and_cities)


# searching
# => we use the key to search for a specific element in the dict, using membership operators

if "Japan" in countries_and_cities:
    print("In")
else:
    print("Out")


# iteration

# This returns only the keys
for element in countries_and_players:
    print(element)

# Values only
for values in countries_and_players.values():
    print(values)

# keys and values
for country, player in countries_and_players.items():
    print(f"{country} => {player}")
