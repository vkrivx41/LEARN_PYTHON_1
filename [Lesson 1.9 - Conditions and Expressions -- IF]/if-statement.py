
# if-statement => is a control flow technic that help us to control our program using boolean expressions

number_1: int = int(input("Enter a number: "))
number_2: int = int(input("Enter another number: "))

# Using this syntax enable the program to move on even if the expression turned out to be False

if number_1 < number_2:
    print(f"{number_1} is less than {number_2}")
if number_1 > number_2:
    print(f"{number_1} is greater than {number_2}")
if number_1 == number_2:
    print(f"{number_1} is equal to {number_2}")


# example 2
# In this example we are giving our program a lot of work to do because
# we keep asking questions even after the expression has yielded a False value, which in the best case could just stop the execution
# this can lead to improper code and bugs in the future

number_1: int = 15

if number_1 < 10:
    print(f"{number_1} is less than 10")
if number_1 < 20:
    print(f"{number_1} is less than 20")
if number_1 < 30:
    print(f"{number_1} is less than 30")



#

good_emotions = ['happy', 'relaxed', 'courageous', 'satisfied', 'proud', 'calm', 'peaceful']
bad_emotions = ['angry', 'sad', 'upset', 'fear', 'anxiety', 'lonely', 'jealous', 'confused', 'worry', 'frustrated', 'guilt', 'aggressive', 'stressed']

harrys_emotion = "sad"

if harrys_emotion in good_emotions:
    print("Harry's emotional state is good")
if harrys_emotion in bad_emotions:
    print("Harry's emotional state is bad")
