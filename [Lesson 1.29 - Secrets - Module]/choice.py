
# choice: picks a single value from a sequence or list

from secrets import choice

names: list = ["nik", "bun", "ella", "joe", "gave", ["dave", "tu"]]

choice_name = choice(names)

print(choice_name)
