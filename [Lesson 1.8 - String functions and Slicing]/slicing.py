
# Slicing: is a method of creating a substring by extracting elements from another string
# use slice() or []


# [start: end: step]
# Note: The start index can't be a negative number
# Note: Leaving the parameter empty makes it 0 by default if it's the start
# Note: Leaving the parameter empty makes it -1 by default if it's the end
# Note: Leaving the parameter empty makes it 1 by default if it's the step

name = "Scorpus Mnugnes"

first_name_1 = name[0:7]
first_name_2 = name[:7]
last_name_1 = name[8:-1]
last_name_2 = name[8:]
funky_name_1 = name[1:12]
funky_name_2 = name[4:-1]
step_name_1 = name[::2]
step_name_2 = name[:7:3]
reversed_name_1 = name[::-1]
reversed_name_2 = name[::-2]

print(first_name_1, first_name_2)
print(last_name_1, last_name_2)
print(funky_name_1, funky_name_2)
print(step_name_1, step_name_2)
print(reversed_name_1, reversed_name_2)

# slice(start, stop, step)
# Note: a slice has a class or type of slice, <class 'slice'>

webiste_1 = "https://netvex.com"

slice_1 = slice(8, -4)
slice_2 = slice(8, -1)
slice_3 = slice(8, 15, 2)

website_name_1 = webiste_1[slice_1]
website_name_2 = webiste_1[slice_2]
website_name_3 = webiste_1[slice_3]

print(slice_1, type(slice_1))

print(website_name_1)
print(website_name_2)
print(website_name_3)
