
# 1: capitalize()
# => makes the first character of the string into capital letter regardless of the cases of the remaining ones

greeting_1 = "Hello"
greeting_2 = "GOOD Morning"

print(greeting_1.capitalize())
print(greeting_2.capitalize())

print()
print()


# 2: casefold()
# => creates a new version of string into lowercase for case-less comparisons

name_1 = "PascaL"
name_2 = "pAsCAl"

print(name_1 == name_2)
print(name_1.casefold())
print(name_2.casefold())
print(name_2.casefold() == name_1.casefold())


print()
print()

# 3: center(spaces: mandatory, placeholder: optional)
# => places a string in the center of the provided number of spaces on the left and the right side
# Note: When the string is longer than the spaces then, nothing happens
# Note: When the spaces length is an odd number more spaces go to the end -- right

name_3: str = "Scorpus"

print(name_3.center(4))
print(name_3.center(20))
print(name_3.center(20, "*"))


print()
print()

# 4: count(string: mandatory)
# => counts and returns the number of existence of a certain determined piece of character or string
# Note: When the string or character is not found zero -- 0 is returned

text_1: str = "abc_abc_abc_abc"

print(text_1.count("ab"))
print(text_1.count("cb"))
print(text_1.count("xyz"))


print()
print()

# 5: encode(encoding: optional, error: optional)
# => encodes the provided string into a certain encoding type
# Note: When errors is set to 'strict', errors are issued in case they are found

name_4 = "Pascal Kapulo"
name_5 = "Scorpus&❤️"

print(name_4.encode())
print(name_4.encode(encoding="UTF-8", errors='strict'))
print(name_4.encode(encoding="ASCII", errors='strict'))
print(name_5.encode(encoding="UTF-8", errors='strict'))
print(name_4.encode(encoding="latin_1", errors='strict'))
# print(name_5.encode(encoding="ASCII", errors='strict'))
# print(name_5.encode(encoding="ASCII", errors='strict'))  # UnicodeEncodeError: 'ascii'
# codec can't encode character '\u2695' in position 7: ordinal not in range(128)
# print(name_4.encode(encoding="mp3", errors='strict'))  # LookupError: unknown encoding: mp3

print()
print()

# 6: endswith(character|string|tuple: mandatory)
# => return True with a string ends with the provided arguments otherwise False

ending_tuple = ("id", 'meda')

text_2: str = "simple"
text_3: str = "android"

print(text_2.endswith("e"))
print(text_2.endswith("z"))
print(text_2.endswith(('e', 'y')))  # this can match both 'simple' and 'simply'
print(text_2.endswith(('x', 'p')))
print(text_3.endswith(ending_tuple))


print()
print()

# 7: expandtabs(spaces: optional)
# => expands the normal spaces a tab can occupy
# Note: If the tabsize is omitted the default tab spacing is then assumed

text_3: str = "text\ttext\text"
text_4 = "Names\tAge\tMarks"

students_1 = [
    {'name': "Scorpus", 'age': 19, 'marks': 11},
    {'name': "Orion", 'age': 91, 'marks': 56},
    {'name': "PinkMate", 'age': 83, 'marks': None}
]

print(text_3)
print(text_3.expandtabs())
print(text_3.expandtabs(10))

print()
print(text_4.expandtabs(10))

for x in students_1:
    printable_1 = str(x['name']) + "\t"
    printable_2 = str(x['age']) + "\t"
    printable_3 = str(x['marks']) + "\t"

    print(printable_1.expandtabs(10), end="")
    print(printable_2.expandtabs(10), end="")
    print(printable_3.expandtabs(10))

print()
print()

# 8: find(character|string: mandatory, start: optional, end: optional)
# => returns the index of the first occurrence of the provided piece of character or string
# Note: When the parameter is not found -1 is returned as the index
# Note: We can also specify the starting and ending searching indices if we need to

text_4: str = "Scorpus is gonna rule the world!"

print(text_4.find("world"), text_4[text_4.find("world"):])
print(text_4.find("africa"))

print(text_4.find('rule', 0, -1))
print(text_4.find('world', 1, 4))

# 9: format(args*, kwargs*: mandatory)
# => used as an alternative to f-strings, to format strings and provide a fancy manner of expressing texts and numbers

text_5: str = "{subject} is doing: {action}."
text_6: str = "{} is doing {}."
text_7: str = "{food} goes with {drink}."

format_1 = text_5.format(subject="Cat", action="meow")
format_2 = text_6.format("Cat", "meow")
format_3 = text_7.format(food="Bread", drink="tea")

print(format_1)
print(format_2)
print(format_3)


# 10: format_map(args*, kwargs*: mandatory)
# => map a dictionary to a specific format string
# Note: The parameters in the string must be totally equivalent to the keys of the dictionary

coordinates_1 = {'x': 1, 'y': -.7}
captials_1 = {'Congo': "Kinshasa", 'Rwanda': "Kigali"}

text_7: str = "The coordinates of x and y are: ({x}, {y})"
text_8: str = "The capital cities of Congo and Rwanda are: ({Congo}, {Rwanda})"

format_4 = text_7.format_map(coordinates_1)
format_5 = text_8.format_map(captials_1)
format_6 = text_7.format_map({'x': 4.5, 'y': 14, 'z': 34})

print(format_4)
print(format_5)
print(format_6)


