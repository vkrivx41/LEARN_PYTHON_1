
# choice: is a method that chooses a single value from a list or sequence of values

from random import choice

names: list[str] = ["nik", "bun", "ella", "joe"]

choice_name: str = choice(names)

print(choice_name)

# ex: 2

greetings: list[str] = ["Hy", "Hello", "Hey", "Howdy", "Hola"]

greeting = choice(greetings)
sentence = greeting + ", Scorpus!"

print(sentence)

