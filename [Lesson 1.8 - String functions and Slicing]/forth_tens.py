
# 31: removeprefix(prefix: mandatory)
# => Removes the prefix of a given string

text_1: str = "f'Hello, {}': This is an f string"

prefix_rem_1 = text_1.removeprefix("f")

print(text_1)
print(prefix_rem_1)

# 32: removesuffix(suffix: mandatory)
# => Removes the suffix of a given string

text_1: str = "scorpus@netvex.ducy"
text_2: str = "scorpus@netvex.com"

prefix_suf_1 = text_1.removesuffix(".ducy")
prefix_suf_2 = text_2.removesuffix(".com")
#
print(prefix_suf_1)
print(prefix_suf_2)


# 33: replace(string: mandatory, replacer: mandatory, occurrence: optional)
# => replaces an existing portion of the string with a new one
# Note: Once the string to be replaced is not found, the whole process is omitted

text_1: str = "Scorpus is gonna rule the world! And the world will change to better."

replacement_1: str = text_1.replace("world", "africa")
replacement_2: str = text_1.replace("gonna", "going to")
replacement_3: str = text_1.replace("torment", "rule")
replacement_4: str = text_1.replace("world", "africa", 1)

print(text_1)
print(replacement_1)
print(replacement_2)
print(replacement_3)
print(replacement_4)


# 34: rfind(string: mandatory)
# => finds the first occurrence of the passed string starting from the right , and then returns it's index if found
# Note: If the searched string or character is not found the -1 is returned

text_1: str = "A: Some text on A"

finder_1 = text_1.rfind('A')
finder_2 = text_1.rfind('g')

print(finder_1)
print(finder_2)

# 35: rindex
# => finds the first occurrence of the passed string starting from the right , and then returns it's index if found
# Note: If the searched string or character is not found then, python raises an error

text_1: str = "A: Some text on A"

finder_1 = text_1.rindex('A')
# finder_2 = text_1.rindex('g') ERROR: ValueError: substring not found

print(finder_1)
print(finder_2)


# 36: rjust(spaces: mandatory, placeholder: optional)
# => justifies the text to the right with the number of spaces provided

text_1: str = "text"

justify_1 = text_1.rjust(20)
justify_2 = text_1.rjust(20, "_")

print(justify_1)
print(justify_2)

# 37: rpartition(delimiter: mandatory)
# => partitions a text into 3 parts that are put into a tuple starting from the right side

expression_1 = "a+b=c+d"

partition_1 = expression_1.partition("+")
partition_2 = expression_1.rpartition("+")
partition_3 = expression_1.rpartition("9")

print(partition_1)
print(partition_2)
print(partition_3)


# 38: rsplit(delimiter: mandatory, maxsplit: optional&keyword)
# => splits a string into an array using a given delimiter beginning from the right
# Note: When the delimiter is not found the whole text is put in the list a single element

text_1: str = "Scorpus never gives up!"

split_1 = text_1.rsplit(" ")
split_2 = text_1.rsplit("!")
split_3 = text_1.rsplit("8")
split_4 = text_1.rsplit(" ", maxsplit=2)

print(split_1)
print(split_2)
print(split_3)
print(split_4)


# 39: split(delimiter: mandatory, maxsplit: optional&keyword)
# => splits a string into an array using a given delimiter beginning from the left
# Note: When the delimiter is not found the whole text is put in the list a single element

text_1: str = "Scorpus never gives up!"

split_1 = text_1.split(" ")
split_2 = text_1.split("!")
split_3 = text_1.split("8")
split_4 = text_1.split(" ", maxsplit=2)

print(split_1)
print(split_2)
print(split_3)
print(split_4)


# 40: rstrip(string: mandatory)
# => strips a certain portion of a string from the given string starting from the right
# Note: When the passed sequence is not at the end of the string, the whole process is omitted

text_1: str = "The boy's name is Scorpus, Scorpus"

strip_1: str = text_1.rstrip("Scorpus")
strip_2: str = text_1.rstrip("name")

print(strip_1)
print(strip_2)


# 41: splitlines(keepends: optional&keyword)
# => takes a text with new line escape sequences and put in into an list
# Note: If the keepends parameter is set to True, even the escape sequences are returned
# Note: If the text doesn't have new lines then it is put in the list as a single element

text_1: str = "Scorpus is a very curious boy\n He loves learning about new things\n"

line_1 = text_1.splitlines()
line_2 = text_1.splitlines(keepends=True)

print(line_1)
print(line_2)

# 42: startswith(string: mandatory)
# => returns True if the string starts with the provided portion, otherwise False

text_1: str = "Scorpus"

starter_1 = text_1.startswith("S")
starter_2 = text_1.startswith("o")
starter_3 = text_1.startswith(("S", "o"))

print(starter_1)
print(starter_2)
print(starter_3)

# 43: strip(string: mandatory)
# => strips a part of a string from a text starting either from the left of right
# Note: Once the passed part of the starts starts with the character same to the character of the normal text,
# that character is striped off

text_1: str = "Scorpus lives by the Seven Rules of Expectations!"

strip_1 = text_1.strip("Scorpus")
strip_2 = text_1.strip("Expectations!")
strip_3 = text_1.strip("Seven")

print(text_1)
print(strip_1)
print(strip_2)
print(strip_3)

# 44: swapcase()
# => swaps the either to it's opposite one (upper => <= lower)

text_1: str = "Scorpus has power."
text_2: str = "SCORPUS HAS POWER."
text_3: str = "scorpus has power."

case_1: str = text_1.swapcase()
case_2: str = text_2.swapcase()
case_3: str = text_3.swapcase()

print(case_1)
print(case_2)
print(case_3)


# 45: title()
# => changes the target string into a title format

text_1: str = "the seven rules of expectations."
text_2: str = "I WILL NEVER GIVE-UP."

title_1: str = text_1.title()
title_2: str = text_2.title()

print(title_1)
print(title_2)

# 46: upper()
# => formats the text into upper case

text_1: str = "Scorpus is not nasty"
text_2: str = "Scorpus Is Not Naughty"

upper_1 = text_1.upper()
upper_2 = text_2.upper()

print(upper_1)
print(upper_2)

# 47: zfill
# => Adds zeros at the beginning of the text, * no really important
# Note: The number of zero are reduces by the length of the text

text_1: str = "text"

fill_1 = text_1.zfill(10)

print(fill_1)


# 48: len(string: mandatory)
# => returns the length of the string

text_1: str = "Scorpus"

len_1 = len(text_1)

print(len_1)


# Magical methods

# 49: __sizeof__()
# => returns the internal memory occupied by the string in bytes
# Note: Not only made for strings, works even for other data-types out there

text_1 = "Scorpus"

print(text_1.__sizeof__())

# 50: __add__(string: mandatory)
# => concatenates the string to the given text

text_1 = "Scorpus"

print(text_1.__add__(" Orion"))



# exercise
# 1. Remove a certain word from a text and replace it with empty string

# solution_1: usign replace()

text_1: str = "Scorpus has a computer."

replacement_1 = text_1.replace("has", "")

print(replacement_1)


text_1 = "N"

print(text_1)
