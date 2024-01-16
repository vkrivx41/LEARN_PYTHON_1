
# 21: isspace()
# => Returns True when the string contains only space or whitespace characters, otherwise False

spaces_1: str = " "
spaces_2: str = "    "
spaces_3: str = "hello, world"

print(spaces_1.isspace())
print(spaces_2.isspace())
print(spaces_3.isspace())


# 22: istitle()
# => Returns True when the string is a valid title, otherwise False
# Note: It follows the title syntax with each word beginning
# with a capital case, this can be made with the title() function

title_1: str = "The Seven Rules Of Expectations"
title_2: str = "The seven rules of expectations"

print(title_1.istitle())
print(title_2.istitle())

# 23: isupper()
# => Returns True if the string is all in uppercase, otherwise False

case_1 = "Hello"
case_2 = "HELLO"

print(case_1.isupper())
print(case_2.isupper())

# 24: join(iterable: mandatory)
# => Joins an iterable(string, list, array, tuple) of items with the given string

fruits_1: list = ['banana', 'mango', 'avocado', 'lemon', 'grapes']
delimiter_1: str = "-"
delimiter_2: str = " "

text_1: str = delimiter_1.join(fruits_1)
text_2: str = delimiter_2.join(fruits_1)
text_3: str = "^".join(("lion", "leopard", "hippo", "elephant"))
text_4:str = "-".join("Scorpus")


print(text_1)
print(text_2)
print(text_3)
print(text_4)


# 25: ljust(spaces: mandatory, placeholder: optional)
# => Aligns the text as possible to the left

text_1: str = "text"
text_2: str = "         text"

print(text_1.ljust(20))
print(text_2.ljust(20, "-"))


# 26: lower()
# => Convert a given string full into lowercase

case_1 = "Hello"
case_2 = "HELLO"
case_3 = "heLLO"

print(case_3 == case_2)
print(case_1.lower())
print(case_2.lower())
print(case_3.lower())
print(case_3.lower() == case_2.lower())

# 27: lstrip(string: mandatory)
# => Removes a substring of the string from the left side
# Note: When the provided string is found not to be on the left then the whole process is omitted

text_1: str = "Some Text"

print(text_1.lstrip("Some"))
print(text_1.lstrip("Some "))
print(text_1.lstrip("Text"))


# 28: translate(translation_table: mandatory), 29: maketrans(string: mandatory, replacement: mandatory)
# maketrans() => creates a translation table by replacing some text with others
# translate() => creates a translation using the created translation table

# Note: The first two maketrans() arguments must have an equal length
# Note: EVery character in the first parameter match it's corresponding one in the second

translation_1: str = "This is a heart, but what is more special about my heart?"

table_1: dict = translation_1.maketrans('heart', 'novel')
table_2: dict = translation_1.maketrans('h', '❤')
table_3: dict = translation_1.maketrans({' ': '👌'})

print(table_1)
print(table_2, table_3.__class__)

print(translation_1.translate(table_1))
print(translation_1.translate(table_2))
print(translation_1.translate(table_3))


# 30: partition(delimiter: mandatory)
# => Returns a tuple of three elements with the delimiter in the center and other elements on the left or right

# Note: When the delimiter shows more than one time the first one is the only counting one.
# Note: When the delimiter is the last character of the string then the last element of the tuple is set to ''.
# Note: When the delimiter is not found in the string literal,
# then all of it is dumped in index 0 and the two other index holds empty strings.

expression_1: str = "a+b=c"
expression_2: str = "a+b=c+d"
expression_3: str = "a+b=c+d/"

partition_1: tuple = expression_1.partition("=")
partition_2: tuple = expression_2.partition("+")
partition_3: tuple = expression_3.partition("/")
partition_4: tuple = expression_3.partition("x")

print(partition_1)
print(partition_2)
print(partition_3)
print(partition_4)
