
# Bitwise operators: bitwise operators allows you to perform operations on the individual bits of integers

number_1 = 4683
number_2 = 5927

print(bin(number_1)[2:])  # 1001001001011
print(bin(number_2)[2:])  # 1011100100111

# Bitwise AND (&):
# The bitwise AND operator compares each pair of corresponding bits in two integers and
# sets the corresponding bit in the result to 1 if both bits are 1.

number_3 = number_1 & number_2
print(bin(number_3)[2:])  # 1001000000011

# Bitwise OR (|):
# The bitwise OR operator compares each pair of corresponding bits in two integers and
# sets the corresponding bit in the result to 1 if at least one of the bits is 1.

number_4 = number_1 | number_2
print(bin(number_4)[2:])

# Bitwise XOR (^):

# The bitwise XOR (exclusive OR) operator compares each pair of corresponding bits in two integers and
# sets the corresponding bit in the result to 1 if the bits are different.

number_5 = number_1 ^ number_2
print("00" + bin(number_5)[2:])

# Bitwise NOT (~):
# The bitwise NOT (complement) operator inverts the bits of a single integer, changing 1s to 0s and 0s to 1s.
# But this one here works differently by inverting only the sign of the integer
# -- negative to positive and the vice-versa

# Note: When inverting from positive to negative 1 is added to the result set but with a negative sign,
# and when inverting from negative to positive 1 is subtracted from the result giving out a positive answer

number_6 =  ~number_1
number_7 = ~-4262


print(bin(number_6)[3:], number_6)
print(bin(number_7)[2:], number_7)

# Left Shift (<<):

# The left shift operator shifts the bits of an integer to the left by a specified number of positions.
# This effectively multiplies the integer by 2 raised to the power of the shift amount.

# Note: Negative shift counts are disallowed

a = 5  # Binary: 0101  => 5 * (2 ^ 2) => 5 * 4 => 20
b = -10

result = a << 2  # Result: 20 (Binary: 10100)  => 0101 - 010100
b <<= 3  # -10 * (2 ^ 3) = -10 * 8 => -80

print(result)
print(b)


# Right Shift (>>):

# The right shift operator shifts the bits of an integer to the right by a specified number of positions.
# This effectively divides the integer by 2 raised to the power of the shift amount,
# discarding the remainder.This effectively multiplies the integer by 2 raised to the power of the shift amount.

a = 20  # Binary: 10100
b = 5  # Binary: 0101

result = a >> 2  # Result: 5 (Binary: 0101) => 20 / (2 ^ 2) => 20 / 4 => 5
result_b = b >> 6  # Result: 1 (Binary: 0101) => 5 / (2 ^ 6) => 5 / 64 => 0

print(result, result_b)


# Reversing bits

number_8 = 8961

print(bin(number_8)[2:])
print("0"+bin(0b11111111111111 - number_8)[2:])


print(0b11111111111111)
print(0b10001100000001)
print(0b11111111111111 - 0b10001100000001)

print(0b101 - 0b11)