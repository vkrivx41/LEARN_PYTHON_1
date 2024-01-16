
# Nesting loops: is a technique that is used when we want to reach a point where an iteration occurs inside another one

"""
Values: - You can nest while loops in for loops or the vice-versa
        - The outer loop runs for the second time after the inner loop as finished it iteration
"""


# Square of blocks (3, 3)

blocks = 3
for _ in range(blocks):
    for block in range(blocks):
        print("[]", end="")
    print()


# using while loops

counter = 0
while counter < blocks:
    count = 0
    while count < blocks -1:
        print("[]", end="")
        count += 1
    print("[]")
    counter += 1


# stars
# => here we are looping j in the range of i -- which is the count of the outer loop, the inner loop will print 1 star when i -- or the count of the outer loop is 1, and 2 if the i of the outer loop is 2, so on and so forth

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

# the reverse program of the above example

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

