
# frexp: returns the mantissa as a float and the exponent as an integer of x


from math import frexp, ldexp

number_1: int = 128
number_2: int = -81

value_1 = frexp(number_1)
value_2 = frexp(number_2)

print(value_1)
print(value_2)

# ldexp: Essentially the reverse of frexp, returns a float

value_3 = ldexp(value_1[0], value_1[1])
value_4 = ldexp(value_2[0], value_2[1])

print(value_3)
print(value_4)

