
# copysign: is a math module's method that returns the magnitude of x, but with the sign of y

from math import copysign

speed: float = 4.5  # km/h
distance: float = -60  # m

velocity = copysign(speed, distance)

print(velocity)
