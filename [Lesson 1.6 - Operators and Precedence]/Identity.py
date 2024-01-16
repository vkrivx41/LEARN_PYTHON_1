# Identity operators: unlike comparison operators which only checks for the values the operands contains,
# identity operators check and only returns true when the two
# operands have the same address in memory, this is proved by the id function

"""Values: - Two variables initiated with exactly the same values doesn't differ in memory -- just in python and it's
for memory utilization """

name_1 = "nik"
name_2 = "nik"
name_3 = name_1

expression_1 = name_1 is name_2
expression_2 = name_2 == name_2
expression_3 = name_3 is name_1
expression_4 = name_3 is name_2
expression_5 = name_2 is not name_3

print(id(name_1), id(name_2), id(name_3))
print(expression_1, expression_2, expression_3, expression_4, expression_5)

number_1 = 500
number_2 = 490

number_2 += 10  # The values are the same but they don't share the same address in memory

print(number_2, number_1)
print(number_2 == number_1)
print(number_2 is number_1)
print(number_2 is not number_1)

# For lists and tuples
# => It is different for tuples and list because they consume a little bit in memory when initiating

marks_1 = 9, 4, 2, 8, 5
marks_2 = 9, 4, 2, 8, 5
marks_3 = marks_2

print(marks_2 == marks_1)
print(marks_2 is marks_1)
print(marks_3 is not marks_1)


# For objects


class Dog():
    def __init__(self, name):
        self.name = name

    def barks(self):
        print("The dog " + self.name + " barks")


dog_1 = Dog("Habbi")
dog_2 = Dog("Habbi")
dog_3 = dog_1

print(dog_1, dog_2, dog_3)
print(id(dog_1) == id(dog_3))

print(dog_1 == dog_2)
print(dog_1 is dog_2)
print(dog_3 is dog_1)
print(dog_3 is dog_2)
print(dog_3 is not dog_2)


# With dicts

cities_1 = {
    1: "Kinshasa", 2: "Kigali", 3: "Kampala", 4: "Accra", 5: "Abuja"
}

cities_2 = {
    1: "Kinshasa", 2: "Kigali", 3: "Kampala", 4: "Accra", 5: "Abuja"
}

cities_3 = cities_2

print(id(cities_1), id(cities_2))

print(cities_1 == cities_2)
print(cities_1 is cities_2)
print(cities_1 is not cities_3)
print(cities_2 is not cities_3)
print(cities_1 == cities_3)
