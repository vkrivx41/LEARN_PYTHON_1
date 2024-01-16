
# tee: is an itertools method used to create shallow copies of the original iterator to prevent iterators exhausting
# and enable an iterator to be assigned to different variables that can be used on the way

"""
Values: - The original iterator is not to be used again because it can cause copies to get exhausted too
        - Once one of the copies is exhausted, the original iterator gets exhausted too
"""

from itertools import groupby, tee
from typing import Union

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
    {
        'name': "Musa Camara",
        'city': "Brooklyn"
    }
]


def get_state(person: dict[str, str]) -> Union[str, None]:
    return person.get('state', None)


people_by_states = groupby(people, get_state)

copy1, copy2 = tee(people_by_states)

for state, group in copy1:
    copy3 = tee(group)
    print(state, ":", len(list(copy3)))
    for person in group:
        print(person)
