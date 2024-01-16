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

played_keys: dict[str, list[str]] = {}
x_keys: list[str] = []
o_keys: list[str] = []

counter: int = 0
valid_moves: int = 9
key: str = " "
game_over: bool = False

combination_keys: set = set()
chosen_keys: set = set()

for keys in winning_combinations:
    for key in keys:
        combination_keys.add(key)


# variable in fx should be lowercase

def get_player(count: int) -> str:

    """
    Returns a players name according to the count of the move
    :param count: The count for the game, states the player to picked
    :return: A players name
    """

    if count % 2 == 0:
        selected_player: str = "X"
    else:
        selected_player: str = "O"
    return selected_player


#
#

while key != "":

    PLAYER: str = get_player(counter)

    msg: str = PLAYER + " " + "Enter a block number: "
    key: str = input(msg)

    #  check if the key is in the combination keys, otherwise ask the player to choose again
    if key not in combination_keys:
        print("Invalid key")
        continue

    #  check if the key is in the chosen keys, and then asked the player to chose again
    if key in chosen_keys:
        print("Key already played")
        continue

    # add a valid, un-chosen key to the chosen_keys set
    chosen_keys.add(key)

    # decrement the valid moves of the game by 1, to check for a DRAW
    valid_moves -= 1

    # Add a key to the appropriate section of the played_keys dictionary
    # if player is X, then add to X section or key, otherwise to O

    if PLAYER == "X":
        x_keys.append(key)
        played_keys[PLAYER] = sorted(x_keys)
    else:
        o_keys.append(key)
        played_keys[PLAYER] = sorted(o_keys)

    # check if the combination being chosen matches any of the winning ones to catch a win for either X or O

    for combination in winning_combinations:
        if sorted(x_keys) == sorted(combination):
            print("X Wins")

            game_over = True

        elif sorted(o_keys) == sorted(combination):
            print("O Wins")

            game_over = True

    # if game_over is True, end the game
    if game_over is True:
        break

    # if valid_moves is zero, end the game
    if valid_moves <= 0:
        print("DRAW: ")
        break

    # increment the counter by 1, to generate new options for a player's selection
    counter += 1


print(played_keys)
