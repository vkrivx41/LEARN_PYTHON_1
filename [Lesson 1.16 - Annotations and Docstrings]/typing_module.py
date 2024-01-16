# Using the python builtin typing module we can import a numerous number of builtin types which can be used in
# type-hinting

from typing import Any, Sequence, Union, Callable, Optional, Hashable, Collection, Text, Reversible, Iterator


# Any
# As the names suggests Any, refers to any kind of datatype, no matter what we hint or pass as the arguments, mypy runs
# smoothly with no errors


def any_calculator(param: Any) -> Any:
    return param * 2


value_1 = any_calculator("Scorpus")
value_2 = any_calculator(46)
value_3 = any_calculator([[1, 2, 3], [4, 5, 6]])

print(value_1)
print(value_2)
print(value_3)


# Sequence
# As the name suggests Sequence refers to an sequence type
# Note: set and dict are not sequences

def iterate_sequence(sequence: Sequence) -> None:
    for element in sequence:
        print(element)


iterate_sequence("Scorpus")
iterate_sequence([True, False, True])
iterate_sequence((5, 6, 1, .9))
iterate_sequence({4, 6, 1})
iterate_sequence({'a': 1, 'b': 2})


def iterate_sequence_explicit(sequence: Sequence[int]) -> None:
    for element in sequence:
        print(element * element)


iterate_sequence_explicit(range(0, 4))
iterate_sequence_explicit([4.6, 8.9, 0.4])


# Union
# Union is a combination of multiple data-types


def find_value(dictionary: dict, value: Union[int, str]) -> Union[int, str]:
    keys: list = list(dictionary.keys())
    values: list = list(dictionary.values())

    if value in dictionary:
        return value
    if value in values:
        return keys[values.index(value)]
    return f"Not found - The input '{value}' is neither a key nor a value."


my_dict: dict[str, int] = {'a': 1, 'b': 2, 'c': 3}

finder_1: Union[int, str] = find_value(my_dict, 1)
finder_2: Union[int, str] = find_value(my_dict, 'c')
finder_3: Union[int, str] = find_value(my_dict, 'x')
finder_4: Union[int, str] = find_value(my_dict, 'b')

print(finder_1)
print(finder_2)
print(finder_3)
print(finder_4)


# Callable
# Defines something that can be invoked or called


def validator(param_1, param_2) -> int:
    if param_1 != param_2:
        return 0
    return 1


def login_by_match(password: str, validator_fn: Callable) -> None:
    old_password: str = "123321123"

    if not validator_fn(password, old_password):
        print("The password is incorrect please!")
    else:
        print("Password matches, Logged in...")


login_by_match("123321123", validator)
login_by_match("000111222", validator)


# This function validates whether the passwords are of the same length to yield True, otherwise False

def length_validator(param_1: str, param_2: str) -> bool:
    if len(param_1) != len(param_2):
        return False
    return True


# The Callable parameter that will we pass in must be a callable which has arguments of str and str and return value
# of bool

def login_by_length(password: str, validator_fn: Callable[[str, str], bool]) -> None:
    old_password: str = "123321123"

    if not validator_fn(password, old_password):
        print("The password is incorrect please!")
    else:
        print("Password matches, Logged in...")


login_by_length("123456789", length_validator)
login_by_length("8010199", length_validator)

# This will run in python bcs the passwords will match, but will throw an error in mypy because of incompatible types
# in parameters and the return value

login_by_length("123321123", validator)


# closure
# closures always return callables, a very good implementation of the Callable typehint


def outer() -> Callable:
    value: int = 0

    def inner():
        nonlocal value

        value += 1
        return value

    return inner


caller_1 = outer()

print(caller_1())
print(caller_1())
print(caller_1())


# Optional
# Defines parameters that accept optional values and have default declarations
# Note: Hinting that a parameter is Optional without specifying the value will throw an exception in python
# Note: Whenever we hint our param to Optional, mypy treats it as None

optional_elements = Optional[Union[int, float]]


def force_calculator(mass: Union[int, float], acceleration: optional_elements = 9.8) -> float:
    return round(mass * acceleration, 2)


eval_1 = force_calculator(4.66, 89)
eval_2 = force_calculator(9.1)

print(eval_1)
print(eval_2)


# Hashable (int, str, bool, float)
# Refers to something that can be used as key in a dictionary or any other complex data-structure


def finder(dictionary: dict, value: Hashable) -> str:
    return str(dictionary.get(value))


dict_1: dict[str, int] = {'a': 1, 'b': 2}

print(finder(dict_1, "a"))
# print(finder(dict_1, [1, 2, 3]))

# Collection (str, list, tuple, dict, set)
# All iterable types can also be defined as Collections


def iterate_collection(iterable: Collection) -> None:
    for element in iterable:
        print(element)


iterate_collection([1, 2, 3])
iterate_collection(("a", "b"))
iterate_collection("Scorpus")
iterate_collection({'1': 'a'})
iterate_collection({4, 6, 2, 4, 1, 2, 9})
iterate_collection([[1, 2, 3], 4])


# Text
# str data-type can also be called Text, is just the alternative name, nothing changes in the implementation

def greeting(name: Text) -> None:
    print(f"Good morning, {name}")


greeting("Scorpus")
greeting(89)  # runs in python, but fails in mypy


# Reversible
# Any type that can be reversed

def reverse(value: Reversible) -> Iterator:
    return value.__reversed__()


print(reverse([1, 2, 3]))  # <list_reverseiterator object at 0x000001A4C41C8520>
print(list(reverse([1, 2, 3])))
# print(reverse((1, 2, 3)))

