

class MyRange:

    def __init__(self, start=0, end=None, step=1) -> None:
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self) -> int:
        """
        Returns the next value in the iteration, following certain provided criteria
        :return: int
        """

        #  if the end is not provided -- only start, then make the end equal to the start and the start back to zero
        if self.end is None:
            self.end = self.start
            self.start = 0

        # store the start value in the current variable
        current = self.start

        # if step is greater or equal to 1, then stop the iteration if the start reaches the end
        # if the step is zero, the defaults it back to 1
        # and then if it is negative reverse it so that the iteration will stop if the end reaches the start
        if self.step >= 1:
            if self.start >= self.end:
                raise StopIteration
        elif self.step == 0:
            self.step = 1
        else:
            if self.start <= self.end:
                raise StopIteration

        # increment the start by the step and then return the current
        self.start += self.step
        return current


odd_numbers_range: MyRange = MyRange(1, 10, 2)
even_numbers_range = MyRange(0, 10, 2)
reversed_even_numbers_range = MyRange(10, 0, -2)  # this cannot work bcs start is greater than end already
numbers = MyRange(1, 5)

print(odd_numbers_range, "__next__" in dir(odd_numbers_range), "__iter__" in dir(odd_numbers_range))

print(list(numbers))
for number in odd_numbers_range:
    print(number)

print(list(odd_numbers_range))

# even
print("Even: ")
for number in even_numbers_range:
    print(number)

print(list(even_numbers_range))


# even reversed
print("Even Reversed: ")
for number in reversed_even_numbers_range:
    print(number)

print(list(reversed_even_numbers_range))

# testing the size

odd_numbers_range_class = MyRange(1, 10, 2)
odd_numbers_range: range = range(1, 10, 2)
odd_numbers_range_list = [1, 3, 5, 7, 9]
odd_numbers_range_tuple = (1, 3, 5, 7, 9)

print("Size of MyRange: ", list(odd_numbers_range_class), ": ", odd_numbers_range_class.__sizeof__(), "Bytes")
print("Size of range(): ", list(odd_numbers_range), ": ", odd_numbers_range.__sizeof__(), "Bytes")
print("Size of list   : ", list(odd_numbers_range_list), ": ", odd_numbers_range_list.__sizeof__(), "Bytes")
print("Size of tuple  : ", list(odd_numbers_range_tuple), ": ", odd_numbers_range_tuple.__sizeof__(), "Bytes")


