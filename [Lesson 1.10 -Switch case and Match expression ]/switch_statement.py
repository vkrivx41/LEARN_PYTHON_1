
# Switch statement: Python itself doesn't have a built method of switch statement, a user needs to define it using a dictionary
# Note: This method doesn't allow using and, or, not operators

player: str = input("Enter a player's name: ")


def playersTeams(name):

    players = {
        'Salah' or "Trent": "Liverpool",
        'Haaland': "Man.City",
        'Harry': "Man.Utd",
    }

    return players.get(name, "Player not found.")


print(playersTeams(player))
