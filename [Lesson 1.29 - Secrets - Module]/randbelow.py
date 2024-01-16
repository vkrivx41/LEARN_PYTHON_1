
# randbelow: generates a random number from 0 to a given exclusive upper-bound


from secrets import randbelow

for _ in range(5):
    rand_number = randbelow(100)

    print(rand_number)

# ex: 2

names: list[str] = ["nik", "bun", "ella", "joe", "gave"]

rand_name: str = names[randbelow(len(names))]

print(rand_name)



