
# deque: is a double-ended cue where elements can be added or removed from the start or end

from collections import deque

deque_1: deque = deque()

print(deque_1)  # deque([])
# add or append
# this appends an element to the end of the deque

deque_1.append(6)
deque_1.append("Scorpus")
deque_1.append(False)
deque_1.append(6)

deque_1_list: list = list(deque_1)
deque_1_tuple: tuple = tuple(deque_1)
deque_1_set: set = set(deque_1)  # duplicates will be omitted

print(deque_1)
print(deque_1_list)
print(deque_1_tuple)
print(deque_1_set)

# appendleft(element)
# adds an element at the beginning of the deque

deque_1.appendleft(56.90)
deque_1.appendleft("Mugnes")

print(deque_1)

# pop() -> element
# pops an element off the end of the deque and returns it

popped_element = deque_1.pop()

print(popped_element)
print(deque_1)

# popleft() -> element
# pops an element off the start of the deque and returns it

popped_element = deque_1.popleft()

print(popped_element)
print(deque_1)

# extend(Iterable)
# extends the deque at the end with an iterable

deque_1.extend([True, None])

print(deque_1)

# extendleft(Iterable)
# extends the deque at the start, with an iterable
# Note: when appending the last element in the iterable take the first place, it goes from left[-to-right

deque_1.extendleft([True, "Pascal", "Nik"])

print(deque_1)

# rotate(number) -> None
# rotates the deque elements certain rotation counts to the right
# Note: the elements are pushed the passed counts to the right, so the last comes all the way to the beginning
# Note: when the number is negative, it goes reverse way

deque_2 = deque()

deque_2.extend("Scorpus")
print(deque_2)

deque_2.rotate(1)
deque_2.rotate(-2)
print(deque_2)

# reverse()
# reverses the deque

deque_3: deque = deque()

deque_3.extendleft("Mugnes")
print(deque_3)

deque_3.reverse()
print(deque_3)

# copy()
# creates a shallow copy of the deque

original_deque: deque = deque()

original_deque.extend("nik bun")
copy_deque: deque = original_deque.copy()

print(original_deque)
print(copy_deque)

original_deque.popleft()
copy_deque.pop()

print(original_deque)
print(copy_deque)

# count, index, clear
# Works the same as in list datatype
