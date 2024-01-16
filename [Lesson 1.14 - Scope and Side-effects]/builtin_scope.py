
# Builtin scope: This is a scope composed of all python pre-defined variables and functions

"""
Values: The builtin scope is scanned after the Local -> Enclosing -> Global scopes are scanned
"""

# using a builtin method
import builtins

m = min(8, 3, 7, 4, 9)

print(m)

# Builtin function re-creation


def min():
    pass


# This call doesn't call the min() builtin but calls the user-defined global function min()
# Note: An error is issued cause we are trying to pass in some arguments, but our function doesn't accept any

# m = min(6, 4, 5, 1)  # ERROR: TypeError: min() takes 0 positional arguments but 4 were given
m = min()

print(m)

# All builtin functions
# => A lot of them are errors, warnings, exceptions and other usefull functions

functions = dir(builtins)

for function in functions:
    print(function)