# Multi_dimensional list: Is a list with two or more dimensions

blocks: list[list[int]] = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(blocks)

for block in blocks:
    print(block)

# These arrays can help us create wonderful contents, patterns on the screen

for block in blocks:
    for b in block:
        print("[*]", end=" ")
    print()

print()

for block in blocks:
    for b in block:
        if b == 1 or b == 3 or b == 4 or b == 6:
            print("    ", end="")
            continue
        print("[*]", end=" ")

    print()

print()

counter = 9

for block in blocks:
    for b in block:
        counter -= 1
        print(" " * (counter + 1) + "[]" * b)

print()

# tic-tac-toe

winning_combinations = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['1', '4', '7'],
    ['2', '5', '8'],
    ['3', '6', '9'],
    ['1', '5', '9'],
    ['3', '5', '7'],
]

print(len(winning_combinations))

for combination in winning_combinations:
    print(combination)


 #
 #
 #
 #
