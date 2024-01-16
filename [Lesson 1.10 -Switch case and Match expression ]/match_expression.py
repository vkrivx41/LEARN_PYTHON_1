# Match expression => is a new feature that emphasizes cleaner code to run and execute control flow statements rather than writing long and nested if else statements

"""
Values: - Better to have a default case, that is marked by an "_"
        - Cases can be chained using the pipe operator "|"
        - Once a name or identifier's name is used as case, it becomes the default case automatically
        - This expression is too limited cause it can't operate with membership operators and other complex ones
        - cases in the expression can't call function, they are limited to calling classes only
"""

liverpool: list = ["Salah", "Konate", "Mac-Allister", "Trent", "Van Dijk"]
man_city: list = ["Haaland", "Debryune", "Doku", "Alvarez"]

countries: tuple = ("Ghana", "Cameron", "Egypt", "Morocco")

player: str = input("Enter the player's name: ")

# example 1

if player == "Salah" or player == "Mac-Allister" or player == "Konate":
    print("Liverpool")
elif player == "Haaland" or player == "Debryune":
    print("Man.City")
else:
    print("No team")
#
# # example 2
#
# if player in liverpool:
#     if player == "Salah":
#         print("Salah wears number 11.")
#     else:
#         print("Player's numbers not available.")
# elif player in man_city:
#     number: int = int(input("Enter the jersey number: "))
#
#     if player == "Haaland" and number == 9:
#         print("Haaland wears number 9 in Man.City.")
#     elif player == "Doku" or player == "Alvarez":
#         print("Players number not available.")
#     else:
#         print("Player's number will be available next week.")
# else:
#     print(f"Player: {player} not found in the teams Liverpool or Man.City.")
#
# # Using Match

match player:
    case "Salah" | "Mac-Allister" | "Konate":
        print("Liverpool")
    case "Haaland" | "Debryune":
        print("Man.City")
    case _:
        print("No team")
#
#
# # example 2 can not be implemented in match expression
#
# # complex example using both

match player.casefold():
    case "haaland":
        number: int = int(input("Enter the jersey number: "))

        if number == 9:
            print("Haaland wears number 9 in Man.City")
        else:
            print("That number is incorrect for Haaland")
    case "salah":
        country: str = input("Enter the player's nation.")

        if country not in countries:
            print("That country doesn't exits.")
        else:
            if country == "Egypt":
                print("Yes, Salah's country is Egypt")
            else:
                print("Incorrect country for Salah")
    case _:
        print("Unknown player")









