# Chained Comparison: is a python specific approach that reduces code duplicity when using if control statements


grade = int(input("Enter your score? "))

if grade >= 90 and grade <= 100:
    print("Grade: A")
elif grade >= 80 and grade < 90:
    print("Grade: B")
elif grade >= 70 and grade < 80:
    print("Grade: C")
elif grade >= 60 and grade < 70:
    print("Grade: D")
elif grade >= 50 and grade < 60:
    print("Grade: E")
else:
    print("Grade: F")

# Approach 2:
# In this approach we try to compare the score with the grade just flipping the score and the grade
# In this approach the signs of comparison tends to change too.

if 90 <= grade and 100 >= grade:
    print("Grade: A")
elif 80 <= grade and grade < 90:
    print("Grade: B")
elif 70 <= grade and grade < 80:
    print("Grade: C")
elif 60 <= grade and grade < 70:
    print("Grade: D")
elif 50 <= grade and grade < 60:
    print("Grade: E")
else:
    print("Grade: F")

# Approach 3: Chained method
# In this approach the duplicity of the grade is eliminated and replaced by the comparison beign applied on both the left and the right side

if 90 <= grade <= 100:
    print("Grade: A")
elif 80 <= grade < 90:
    print("Grade: B")
elif 70 <= grade < 80:
    print("Grade: C")
elif 60 <= grade < 70:
    print("Grade: D")
elif 50 <= grade < 60:
    print("Grade: E")
else:
    print("Grade: F")


# Approach 4: Descending approach
# this approach allows us to reduce the amount of calculation being done by the computer by just beginning from the largest comparison set to the smallest rather than using the ranges

if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
elif grade >= 60:
    print("Grade: D")
elif grade >= 50:
    print("Grade: E")
else:
    print("Grade: F")


# Approach 5: Ascending approach
# This approach is somehow same to the descending one but it also checks with the ranges
# First the number is being checked if it is below 50 and if not then checked to be below 60 and if not 70, if not 80, and else 90 and above being grade A

if grade < 50:
    print("Grade: F")
elif grade <= 50:
    print("Grade: E")
elif grade <= 60:
    print("Grade: D")
elif grade <= 70:
    print("Grade: C")
elif grade <= 80:
    print("Grade: B")
else:
    print("Grade: A")

