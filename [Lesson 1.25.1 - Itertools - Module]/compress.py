
# compress: Is an Itertools method that return data elements corresponding to True selector elements.

from itertools import compress

permissions = ["NEURAL_READ", "NEURAL_WRITE", "NEURAL_UPDATE", "NEURAL_CHANGE_POLICY"]

person_1 = [True, True, False, False]
person_2 = [False, True, True, True]

result_1 = compress(permissions, person_1)
result_2 = compress(permissions, person_2)

for permission in result_1:
    print(permission)

print("Person 2:", list(result_2))


def for_readers(perms: list[str]) -> str:
    if "NEURAL_READ" not in perms:
        return "This person can't read."
    return "We are looking for a novel for you, because you are reader!"


result_1 = compress(permissions, person_1)
result_2 = compress(permissions, person_2)

reader_1 = for_readers(list(result_1))
reader_2 = for_readers(list(result_2))

print(reader_1)
print(reader_2)
