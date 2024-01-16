
# local variables: are variables declared inside a particular function, and it can not be accessed outside of that
# global variables: are variables declared outside of an particular function, and it can not accessed outside of that

x = "global x"  # This variable is accessible inside any function in this file and outside of them


def scope():
    y = "local y"  # This variable is only available in this function, and can trigger an error once used outside

    print(y)  # local y
    print(x)  # global x


scope()
print(x)  # local x
# print(y) ERROR: NameError: name 'y' is not defined


# UnboundLocalError
# Note: we can not access global variable as a local variable where is not associated with a value, thus every global variable must be mutated with a value to be directly used

global_var_1 = "global var 1"


def scope_function_1():
    # print(global_var_1) # ERROR: UnboundLocalError: cannot access local variable 'global_var_1' where it is not associated with a value

    global_var_1 = "global var 1: Mutated"
    print(global_var_1)


scope_function_1()
print()


# global variable mutation using global keyword: Not recommended
# Note: using the global keyword mutates the value of the variable completely, the variable is assigned to a value that it is going to use for the rest of it's lifespan in the program


global_var_2 = "global var 2"
global_var_3 = "global var 3"


def scope_function_2():
    global global_var_2, global_var_3  # signifies that we are going to use our global variable and assign new values to it

    print(global_var_2, global_var_3)  # the unboundLocalError is no longer issued in this case

    global_var_2 = "global var 2: Mutated"  # the variable wears the new value assigned to it
    global_var_3 = "global var 3: Mutated"  # the variable wears the new value assigned to it

    print(global_var_2, global_var_3)  # the new values


scope_function_2()
print(global_var_2)  # mutation has occurred and now the variable contains the value from the function
print(global_var_3)  # mutation has occurred and now the variable contains the value from the function


# parameter variable
# Note: Variable passed as params are considered local variables in python
# Note: A variable can not be used as a param and global at once

def scope_function_3(param_1):
    # global param_1 ERROR: SyntaxError: name 'param_1' is parameter and global
    print(param_1)

    param_1 = "param 1: Mutated"

    print(param_1)


scope_function_3("param 1")
# print(param_1) ERROR: NameError: name 'param_1' is not defined


# Same names but global and local

var_1 = "global var"


def scope_function_4():
    var_1 = "local var"

    print(var_1)


scope_function_4()
print(var_1)  # hasn't changed still the global

