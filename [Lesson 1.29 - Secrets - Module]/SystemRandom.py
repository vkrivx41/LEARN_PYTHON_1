
# SystemRandom: creates a new random object from the secrets module that generates random numbers and perform other
# random operations

from secrets import SystemRandom

random = SystemRandom()

# random()

num_1: float = random.random()
print(num_1)

# randint

num_2: float = random.randint(1, 10)
print(num_2)

# randrange

num_3 = random.randrange(1, 10, 2)
print(num_3)

# choice

names: list[str] = ["nik", "bun", "ella", "joe", ]
choice_name: str = random.choice(names)

print(choice_name)

# choices

roulette_colors: list[str] = ["Red", "Blue", "Green"]
choices = random.choices(roulette_colors, weights=[18, 18, 2], k=10)

print(choices)

# sample

deck: list[int] = list(range(1, 53))
hand = random.sample(deck, k=5)

print(hand)

# uniform

rand: float = random.uniform(1, 11)
print(rand)

# shuffle

random.shuffle(deck)
print(deck)


