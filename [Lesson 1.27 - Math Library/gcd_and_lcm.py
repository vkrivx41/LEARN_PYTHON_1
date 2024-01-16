
# gcd: short for "Greatest Common Divisor", and as the name suggests the functionality complies

from math import gcd, lcm

number_1: int = 18
number_2: int = 36
number_3: int = 45

gcd_1 = gcd(number_1, number_2)
gcd_2 = gcd(number_1, number_2, number_3)

print(gcd_1)
print(gcd_2)

# lcm: short for "Lowest Common Multiple", and as the name suggests the functionality complies
# python: v: 3.9
lcm_1 = lcm(number_1, number_2)
lcm_2 = lcm(number_1, number_3, number_2)

print(lcm_1)
print(lcm_2)
