
# Loop Control Statements: are statements that determines or changes the loop normal iteration sequence, to either break or restart again

"""
Values: break => terminates the execution of the loop
        continue => continues to the next iteration of the loop -- it restarts back again to the top
        pass => does nothing programmatically, it acts as a placeholder

        - Sometimes break and continue yields the same result according to the algorithm
"""

# This code right here will keep asking for an even number btn 0 and 100, and break after being found
while True:

    number = input("Enter an even number from 0 to 100: ")

    if number != "":
        number = int(number)
    else:
        number = 0

    if number % 2 == 0 and 100 >= number >= 0:
        break


# continue

for number in range(1, 100):
    if number % 3 == 0:
        if number % 5 == 0:
            print(f"{number}: Fizz Buzz")
            continue  # the loop will restart over once it finds out this number
        print(f"{number}: Fizz")
    elif number % 5 == 0:
        print(f"{number}: Buzz")
    else:
        print(f"{number}:")


# pass

for number in range(1, 10):
    if number == 6:
        pass
    print(number)

# break

for number in range(1, 10):
    if number > 6:
        break  # breaks 6
    print(number)

for number in range(1, 10):
    if number == 6:
        break  # breaks on 5 not 6
    print(number)

# continue

print()
for number in range(1, 10):
    if number > 6:
        continue  # breaks on 6
    print(number)