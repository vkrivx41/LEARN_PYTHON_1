
# product: is an Itertools method that calculates the cartesian product of the elements of the given iterable


"""
Values: - Similar to the combinations_with_replacement function
"""

from itertools import product


numbers_1: list[int] = [1, 2]
numbers_2: list[int] = [3, 4]

products_1 = product(numbers_1, numbers_2, repeat=1)
products_2 = product(numbers_1, numbers_2, repeat=2)

print(list(products_1))
print(list(products_2))


# We are going to create a password cracker to crack a 4 digits password, and return the tries it takes to crack it

numbers: list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
numbers_and_letters: list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e']

possible_passwords_4 = product(numbers, repeat=4)
possible_passwords_4_letters = product(numbers_and_letters, repeat=4)

possible_passwords_4_list = list(possible_passwords_4)
possible_passwords_4_letters_list = list(possible_passwords_4_letters)


def password_cracker(passwords: list, set_password: str) -> dict:
    counter: int = 0
    output = {
        'tries': 0,
        'hidden_password': "Not found"
    }

    for password in passwords:
        counter += 1

        pin = "".join(password)

        if pin == set_password:
            output = {
                'tries': counter,
                'hidden_password': pin,
            }

    return output


cracked_password_1 = password_cracker(possible_passwords_4_letters_list, "abc6")
cracked_password_2 = password_cracker(possible_passwords_4_list, "0009")

print(cracked_password_1)
print(cracked_password_2)




