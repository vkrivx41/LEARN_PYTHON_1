
# namedtuple: Creates a tuple that can be accessed using names not indices


"""
Values: - Creates a class-like object behind the scenes with the name as passed in the first positional argument
"""

from collections import namedtuple

Point = namedtuple("Point", "x, y")

coordinates_1: Point = Point(3, 7)
coordinates_2: Point = Point(-.9, 4.6)

print(coordinates_1)  # Point(x=3, y=7)
print(coordinates_2)  # Point(x=-0.9, y=4.6)

# access
# => we use dot notation to access values

print(coordinates_1.x, coordinates_1.y)
print(coordinates_2.x, coordinates_2.y)

Course = namedtuple("Course", "name, price")

course_1: Course = Course("Machine Learning", 7_891)
course_2: Course = Course("Data Science", 4_000)

print(course_1)
print(course_2)

print(course_1.name, " => ", course_1.price)


# iteration

for course in course_1:
    print(course)
