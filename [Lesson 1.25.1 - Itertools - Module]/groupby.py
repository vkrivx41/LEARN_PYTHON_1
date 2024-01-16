
# groupby: is an itertools method that groups elements in a list of dictionary or a JSON like format iterable using a
# certain sorted key

"""
Values: - The values to be groupby must be sorted using that sort key, otherwise other values corresponding to that key
            will create another group downwards and can't be attached to the first grouap
"""

from itertools import groupby

people: list[dict[str, str]] = [
    {
        'name': "Scorpus Mugnes",
        'city': "Dallas",
        'state': "TX",
    },
    {
        'name': "Honey Mugnes",
        'city': "Houston",
        'state': "TX",
    },
    {
        'name': "Nik Bun",
        'city': "Austin",
        'state': "TX",
    },
{
        'name': "John Doe",
        'city': "Gotham",
        'state': "NY",
        },
    {
        'name': "Jane Doe",
        'city': "Kings Landing",
        'state': "NY",
    },
    {
        'name': "Sam Danes",
        'city': "Hinton",
        'state': "WV",
    },

    {
        'name': "Sam Kent",
        'city': "Rand",
        'state': "WV",
    },
    {
        'name': "Nicolle K",
        'city': "Asheville",
        'state': "NC",
    },
    {
        'name': "Richard Masters",
        'city': "Rand 2",
        'state': "WV",
    },
]


def get_state(person: dict[str, str]) -> str:
    return person.get('state', "NY")


people_by_states = groupby(people, get_state)


for state, group in people_by_states:
    print(state)
    for person in group:
        print(person)


persons: list[dict] = [
    {
        'name': "nik", 'age': 20
    },
{
        'name': "bun", 'age': 15
    },
{
        'name': "ella", 'age': 57
    },
{
        'name': "joe", 'age': 11
    },
{
        'name': "gave", 'age': 45
    },
{
        'name': "dave", 'age': 31
    },

]


def between_10_and_20(per: dict) -> bool:
    return per['age'] in range(10, 21)


groups = groupby(persons, between_10_and_20)

for name, group in groups:
    print(name, list(group))

