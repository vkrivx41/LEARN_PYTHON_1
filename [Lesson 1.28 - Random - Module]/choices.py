
# choices: is a method that chooses a bunch of values from a list or sequence of elements

from random import choices

roulette_colors: list[str] = ["Red", "Black", "Green"]

# k: is a keyword argument that sets the number of elements to be chosen, DEFAULT = 1

color_choice = choices(roulette_colors)
color_choices = choices(roulette_colors, k=10)


print(color_choice)
print(color_choices)

# Note: in a real roulette game there are 18 red pockets, 18 black pockets, and 2 green pockets. That determines
# the odd of getting or choosing that color
# Note: green has a 2 / 38 chances of being chosen, i.e it will come quite often

# weight=[element_1, element_2, element_n]
# Note: The value of the weights must match the population

color_choices_with_weight = choices(roulette_colors, weights=[18, 18, 2], k=10)

print(color_choices_with_weight)

# a prizes token simulation in a game

prizes: list[str] = ["$ 100", "$ 200", "$ 500", "A car", "A gun", "Infinity ammo", "An amour"]

prizes_roll = choices(prizes, weights=[20, 18, 6, 4, 2, 1, 1], k=1)

print(prizes_roll)

for _ in range(32):
    print(choices(prizes, weights=[10, 8, 6, 4, 2, 1, 1], k=1))


