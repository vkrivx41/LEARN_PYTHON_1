# Flags: Bitwise operators are used in flags creation in different applications and programs

# READ, WRITE, EXECUTE, CHANGE POLICY

person_1 = 0b1001
person_2 = 0b0011
person_3 = 0b1100
person_4 = 0b1011
person_5 = 0b1000

collective_permission = person_1 & person_2 & person_3 & person_4 & person_5
together = person_1 | person_2 | person_3 | person_4 | person_5

print(bin(collective_permission)[2:])
print(bin(together)[2:])

# Characteristics

# Tall, Big, Light skin, Blue eyes

boy_1 = 0b1001
boy_2 = 0b1110
boy_3 = 0b1010
boy_4 = 0b1000

# What all boys have in common

together_1 = boy_1 & boy_2 & boy_3 & boy_4
print(bin(together_1)[2:])

# What at least any of them got

together_2 = boy_1 | boy_2 | boy_3 | boy_4
print(bin(together_2)[2:])

# What at least any one has others don't

together_3 = boy_1 ^ boy_2 ^ boy_3 ^ boy_4
print("0" + bin(together_3)[2:])

# Flags

NEURAL_WRITE = 0b1000
NEURAL_READ = 0b0100
NEURAL_EXEC = 0b0010
NEURAL_CHANGE = 0b0001


def myFunction(permission):
    return bin(permission)


print(myFunction(NEURAL_WRITE))
print(myFunction(NEURAL_READ | NEURAL_EXEC))
print(myFunction(NEURAL_WRITE & NEURAL_READ | NEURAL_CHANGE))

# swapping two number without the placeholder

number_1 = 10
number_2 = 5

# Approach 1

number_1, number_2 = number_2, number_1
print(number_1, number_2)

# Approach 2

number_2 += number_1
number_1 = number_2 - number_1
number_2 -= number_1

print(number_1, number_2)

# Approach 3

# number_1 = 01010, number_2 = 00101

number_1 ^= number_2  # 10001
number_2 ^= number_1  # 01010
number_1 ^= number_2

print(number_1, number_2)

# Checking for odd or even numbers

number_3 = 18

if number_3 & 1 == 0:
    print("Even")
else:
    print("Odd")

# Finding prime numbers

prime_1 = 3
prime_2 = 5
prime_3 = 7
prime_4 = 11
prime_5 = 13
prime_6 = 17

print(15 ^ 100)

print("000" + bin(prime_1)[2:])
print("00" + bin(prime_2)[2:])
print("00" + bin(prime_3)[2:])
print("0" + bin(prime_4)[2:])
print("0" + bin(prime_5)[2:])
print(bin(prime_6)[2:])


def switch_case(case):
    switch_dict = {
        'case1': 'This is case 1',
        'case2': 'This is case 2',
        'case3': 'This is case 3',
    }
    return switch_dict.get(case, 'This is the default case')


# Example usage:
result = switch_case('case2')
print(result)  # Output: This is case 2

result = switch_case('case4')  # Using the default case
print(result)  # Output: This is the default case
