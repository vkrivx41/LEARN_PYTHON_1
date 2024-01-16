
# token_hex: generates a random text from the HEX, hexadecimal system with a specific length or bytes

"""
Values: - the default bytes is 32
"""

from secrets import token_hex

for _ in range(3):
    token = token_hex(16)

    print(token)
