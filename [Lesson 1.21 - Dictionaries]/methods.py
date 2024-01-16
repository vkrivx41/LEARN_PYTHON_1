
# 1: clear()
# => clears the entire dictionary and empties it
from typing import KeysView

from typing_extensions import ValuesView

my_dict: dict[tuple, str] = {
    (1, 2, 3): "a",
    (4, 5, 6): "b",
    (7, 8, 9): "c"
}

print(my_dict)
print(my_dict[(1, 2, 3)])

my_dict.clear()

print(my_dict)

# 2 copy()
# => creates a shallow copy of the original dictionary

original_singers: dict[str, str] = {
    'BurnaBoy': "Nigeria",
    'Innos B': "DRC",
    'Rema': "Nigeria",
    'Diamond': "Tanzania",
}

copied_singers: dict[str, str] = original_singers.copy()

print(original_singers)
print(copied_singers)

original_singers['Sarkodie'] = "Ghana"

print(original_singers)
print(copied_singers)


# 3 fromkeys
# => created a new dictionary with keys from an iterable an values as values

from_dict: dict[int, str] = original_singers.fromkeys([1, 2, 3, 4, 5], 'a')
print(from_dict)

# 4 get
# => returns an element after being found, doesn't throw an error if not,
# but displays a custom messages or None if not set

countries_and_players: dict[str, str] = dict(Brazil="Pele", Argentina="Messi", Germany="Gerd", Portugal="Cristiano")

print(countries_and_players)

player_1: str = countries_and_players.get('Brazil')
player_2: str = countries_and_players.get('Pakistan')
player_3: str = countries_and_players.get('Rwanda', "No player found from that country")

print(player_1)
print(player_2)
print(player_3)


# 5 items() -> returns a dict_items
# => returns all the items of the dict including the keys and values, as a list of type dict_items
# and values stored in tuples
# Note: 'dict_items' object is not subscriptable, i.e it can't be indexed or accessed explicitly

countries_and_cities: dict[str, str] = {
    'USA': "Washington",
    'Russia': "Moscow",
    'DRC': "Kinshasa",
    'China': "Beijing",
}

print(countries_and_cities.items())

# 6 keys()
# => returns only the keys of the dict

keys: KeysView[str] = countries_and_players.keys()
print(keys)

# 7 pop(key: Any) -> element
# => chops an element off the dictionary, and returns the element if told so

colors: dict[int, str] = {1: "Yellow", 2: "Red", 3: "Blue", 4: "Green"}

print(colors)

colors.pop(2)
print(colors)

popped_color: str = colors.pop(3)
print(popped_color)
print(colors)

# 8 popitem()
# => Same to pop() but doesn't need a key to pop, it chops off the last elemet
colors: dict[int, str] = {1: "Yellow", 2: "Red", 3: "Blue", 4: "Green"}

print(colors)

colors.popitem()
print(colors)

# 9 setdefault(key, value)
# => Returns the value of the key if found, otherwise None or the passed default value positional argument 2
colors: dict[int, str] = {1: "Yellow", 2: "Red", 3: "Blue", 4: "Green"}

print(colors)
print(colors.setdefault(0))
print(colors.setdefault(9, "Pink"))
print(colors.setdefault(5, "Khaki"))


# 10 update()
# => merges a new dict to an existing one
# Note: if the key in the first dict matches another one in the second dict, then it's value is replaced

colors: dict[int, str] = {1: "Yellow", 2: "Red", 3: "Blue", 4: "Green"}
colors_2: dict[int, str] = {7: "Purple", 8: "Violet", 2: "Black"}

colors.update(colors_2)
# colors.update(dict(11="Scarlet", 12="Indigo"))  # Can't work
print(colors)

# 11 values() -> dict_values
# => returns the values of the dict

colors: dict[int, str] = {1: "Yellow", 2: "Red", 3: "Blue", 4: "Green"}

values: ValuesView[str] = colors.values()
print(values)
