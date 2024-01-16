
# Nested if condition: a nested if condition is generally used to control the flow of the program inside another condition

"""
Values: - It prevents us from using logical operators in case we don't want to
        - Lead to code complexity sometimes when used roughly
"""

# Note: This approach is generally used in cases where we have to compare a lot things but with one major thing to start with and don't need to be repeating it everywhere

motivated = True
patient = False
name = "Fabian"

# Logical operators approach:
# In this approach we repeat the validation of the starting F twice which is not D.R.Y

if name.startswith("F") and motivated:
    print(f"Yes his name {name} starts with an F and he is truly motivated")
elif name.startswith("F") and not motivated:
    print(f"Yes his name {name} starts with an F but he is not truly motivated")


# the nested if approach

name = "Felas"
motivated = False

if name.startswith("F"):
    if motivated:
        print(f"Yes his name {name} starts with an F and he is truly motivated")
    else:
        print(f"Yes his name {name} starts with an F but he is not truly motivated")
    if patient:
        print(f"Yes his name {name} starts with an F and he is truly patient")
    else:
        print(f"Yes his name {name} starts with an F but he is not truly patient")
else:
    print("Name doesn't start with an F")

# Let assume that there is a job landing opportunity and the one to be granted it must be female firts
# After that other checks like grades, years of experience and salary demand are to be considered


gender: str = "feMale"
years_of_experience: int = 7
grades: int = 89
salary_demand: int = 5_000

if gender.casefold() == "female":
    if years_of_experience >= 10 and grades >= 90:
        print("You are eligible to grab the job with the maximum salary demand.")
    elif years_of_experience >= 10 and 90 > grades >= 80:
        if salary_demand >= 10_000:
            print("Your grades and experiences are great but that's a high salary demand")
        else:
            print(f"With your experience of {years_of_experience} years and grades you are awarded the job.")
    elif years_of_experience >= 5 and 80 > grades >= 70:
        if salary_demand >= 7_000:
            print("Your grades and experiences are great but that's a high salary demand")
        else:
            print(f"With your experience of {years_of_experience} years and grades you are awarded the job.")
    elif years_of_experience >= 3 and 70 > grades >= 60:
        if salary_demand >= 5_000:
            print("Your grades and experiences are great but that's a high salary demand")
        else:
            print(f"With your experience of {years_of_experience} years and grades you are awarded the job.")
    else:
        print("You are not eligible to grab the job.")
else:
    print("Hoops: Only Female employees are to be awarded this opportunity")


#

good_emotions = ['happy', 'relaxed', 'courageous', 'satisfied', 'proud', 'calm', 'peaceful']
bad_emotions = ['angry', 'sad', 'upset', 'fear', 'anxiety', 'lonely', 'jealous', 'confused', 'worry', 'frustrated', 'guilt', 'aggressive', 'stressed']
good_events = ['coding', 'sleeping', 'movies', 'music', 'wondering', 'eating', 'resting']
bad_events = ['phoning', 'complaining', 'negative self talking']

my_emotion = "courageous"
time = 10


def emotion_and_time_analyzer(emotion):
    if my_emotion in bad_emotions:
        if 0 <= time <= 6:
            print("It's night time why am I negative? Let me forget about my worries.")
        elif 6 <= time <= 10:
            print("I must have had a bad night. I need to start afresh.")
        elif 11 <= time <= 15:
            print("I must be hungry, tired or bored. Let me take a rest.")
        else:
            print("I must have had a bad day. I need to refocus again.")
    else:
        print("Am grad to be positive state.🤣")


emotion_and_time_analyzer(my_emotion)