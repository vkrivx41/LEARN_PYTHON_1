
# We can unpack and pass as many arguments we want in the arguments list to be considered as one iterable in a
# function by the help of the asterisk prefix on the parameter definition

# args
# => packs every kind of argument pass in the parameter and casts it into a tuple-iterable

def double_number(*numbers) -> list:
    double_list: list = []

    for num in numbers:
        double_list.append(num * num)

    return double_list


doubled_1 = double_number(4, 8, 1, 9)
doubled_2 = double_number(-9, 0, 56.2, True)

print(doubled_1)
print(doubled_2)


def double_number_modified(number_1, *numbers) -> list:
    print(f"{number_1} is the first number it will be omitted")

    double_list: list = []

    for num in numbers:
        double_list.append(num * num)

    return double_list


doubled_modified_1 = double_number_modified(4, 8, 1, 9)

print(doubled_modified_1)

# kwargs
# => short for keyword argument


def define_city(**info) -> None:
    print(f"{info['city']} is the capital city of {info['country']}")


define_city(country="Rwanda", city="Kigali")
define_city(country="DRC", city="Kinshasa")
define_city(city="Cairo", country="Egypt")


def define_city_modified(country, **info) -> None:
    print(f"{info['city']} is the capital city of {country}, and it has a population of {info['population']} people.")


define_city_modified(country="Rwanda", city="Kigali", population="12_000_000")
define_city_modified(city="Kinshasa", population="90_000_000", country="DRC")


my_dict: dict[str, int] = {'a': 1, 'b': 2}

element_1, element_2 = my_dict.values()

print(element_1)
print(element_2)
