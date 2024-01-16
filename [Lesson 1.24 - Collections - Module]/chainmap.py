
# ChainMap: is a dictionary like class for creating single view of multiple mapping

from collections import ChainMap

courses_1: dict[int, str] = {1: "Maths", 2: "CS"}
courses_2: dict[int, str] = {1: "Python", 2: "Business Creation"}

courses_chain: ChainMap = ChainMap(courses_1, courses_2)

print(courses_chain)

# update
# updates the first mapping

courses_chain.update({2:"English"})
courses_chain.update({3:"Physics"})

for mapping in courses_chain.items():
    print(mapping)

print(courses_chain.values())  # ValuesView(ChainMap({1: 'Maths', 2: 'English', 3: 'Physics'}, {1: 'Python', 2: 'Business Creation'}))