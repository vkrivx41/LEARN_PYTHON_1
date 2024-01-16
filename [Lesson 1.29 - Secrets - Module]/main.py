
# secrets module: is a module that is used to create cryptographically strong random numbers and texts that can be used
# in security purposes likes passwords and tokens generation, account authentication, and other related secrets

"""
Values: - the default entropy of the secrets module is 32 -- 32 bytes, entropy is the measure of randomness or disorder
"""

import secrets


def main():
    counter: int = 0

    for method in dir(secrets):
        if "__" not in method:
            counter += 1
            print(counter, method)

    print(f"DEFAULT ENTROPY: {secrets.DEFAULT_ENTROPY}")


if __name__ == '__main__':
    main()
