
# namedtuple: is a special method or object from the collections library that creates a tuple with keys

from collections import namedtuple

Color = namedtuple("Color", ['red', 'green', 'blue'])

color_1 = Color(55, 100, 255)
color_2 = Color(255, 255, 255)
color_3 = Color(red=255, green=255, blue=255)

print(color_1)
print(color_2)
print(color_3)


# accessing

red_for_color_1 = color_1.red
green_for_color_2 = color_2.green
blue_for_color_3 = color_3.blue

print(red_for_color_1)
print(green_for_color_2)
print(blue_for_color_3)


# alternative ways

# 1: dictionaries

color_1: dict[str, int] = {'red': 55, 'green': 100, 'blue': 255}

print(color_1)
print(color_1['red'])
