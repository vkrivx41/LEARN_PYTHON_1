
# reduce: runs elements of an iterable through the current and accumulator

from functools import reduce


numbers: list = list(range(1, 5))

sum_total = reduce(lambda acc, curr: acc + curr, numbers)
sum_total_start_with_1 = reduce(lambda acc, curr: acc + curr, numbers, 1)

print(sum_total)
print(sum_total_start_with_1)

# other alternatives

print(sum(numbers))
print(sum(numbers, 1))

# ex:

names: list[str] = ["Nik Bun", "Scorpus Mugnes", "Harry Potter"]


def array_names_len_counter(acc: int, curr: str) -> int:
    return acc + len(curr)


names_length = reduce(array_names_len_counter, names, 0)

print(names_length)
