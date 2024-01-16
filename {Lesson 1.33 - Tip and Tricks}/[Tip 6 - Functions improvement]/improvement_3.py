
# 3: using the asterisk unpacker, to unpack values passed into the arguments as a single iterable parameter


def find_prime_numbers(*numbers) -> list:
    prime_numbers: list = []

    for number in numbers:
        if number % 2 != 0 and number % 3 != 0 and number % 5 != 0:
            prime_numbers.append(number)

    return prime_numbers


primes = find_prime_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9)

print(primes)



