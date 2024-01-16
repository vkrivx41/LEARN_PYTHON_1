
# print() => The print function help to print or display texts to the filestream

"""
Values: - It can take as many objects as your pass through it
        - The named parameter are also option to specify
        - print(*objects, sep=' ', end='\n', file='stdout', flush=False)
        - None being passed to either sep or end picks the default value
"""

name = input("What is your name? ")


print("How are you", name, end="\t", sep="-")

print("Hello,", end=None, sep="???")
print(name)


print('Hi,', name, sep="->")
