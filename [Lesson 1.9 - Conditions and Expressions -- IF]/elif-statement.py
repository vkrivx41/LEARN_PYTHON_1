
# elif statement: Improve our code readability and reduces bugs in the future
# by stopping the execution after encoutering a False expression

number_1: int = int(input("Enter a number: "))
number_2: int = int(input("Enter another number: "))

# Using this syntax enable the program to move on to the last check of checking if the number are to
# be equal which is improper because it has passed not being greater than or less one another

if number_1 < number_2:
    print(f"{number_1} is less than {number_2}")
elif number_1 > number_2:
    print(f"{number_1} is greater than {number_2}")
elif number_1 == number_2:
    print(f"{number_1} is equal to {number_2}")


good_emotions = ['happy', 'relaxed', 'courageous', 'satisfied', 'proud', 'calm', 'peaceful']
bad_emotions = ['angry', 'sad', 'upset', 'fear', 'anxiety', 'lonely', 'jealous', 'confused', 'worry', 'frustrated', 'guilt', 'aggressive', 'stressed']

harrys_emotion = "confused"

if harrys_emotion in good_emotions:
    print("Harry is in a good emotional state")
elif harrys_emotion not in good_emotions:
    print("Harry is not in a good emotional state")