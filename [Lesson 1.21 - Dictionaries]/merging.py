
# Merging: Is the way of merging two or more dictionaries together

dict_1: dict[str, int] = {'a': 1, 'b': 5}
dict_2: dict[str, int] = {'c': 9, 'b': 11}

print(dict_1)
print(dict_2)

# Method 1: update()
# Values of the first dict get replaced with values of the second or next one if the key matches

dict_1.update(dict_2)
dict_2.update(dict_1)

print(dict_1)
print(dict_2)

# Method 2: unpacking method or **
# Values of the first dict get replaced with values of the second or next one if the key matches

dict_1: dict[str, int] = {'a': 1, 'b': 5}
dict_2: dict[str, int] = {'c': 9, 'b': 11}

dict_3: dict[str, str] = {**dict_2, **dict_1}

print(dict_3)

# Ex 2
# This method also creates a shallow copy of the original

countries_and_player: dict[str, str] = dict(Brazil="Pele", Argentina="Messi", Germany="Gerd", Portugal="Cristiano")

countries_and_player_2 = {**countries_and_player, 'France': "Mbappe", 'Spain': "Xavi"}

countries_and_player['Poland'] = "Robert"

print(countries_and_player)
print(countries_and_player_2)


# Method 3: Pipe Operator Version 9 <=
# Values of the first dict get replaced with values of the second or next one if the key matches

dict_1: dict[str, int] = {'a': 1, 'b': 5}
dict_2: dict[str, int] = {'c': 9, 'b': 11}

dict_3: dict[str, int] = dict_1 | dict_2
dict_4: dict[str, int] = dict_2 | {'d': 7}

print(dict_3)
print(dict_4)

# Method 4: dict() method
# Values of the first dict get replaced with values of the second or next one if the key matches

dict_1: dict[str, int] = {'a': 1, 'b': 5}
dict_2: dict[str, int] = {'c': 9, 'b': 11}


dict_3: dict[str, int] = dict(dict_1.items() | dict_2.items())

print(dict_3)


