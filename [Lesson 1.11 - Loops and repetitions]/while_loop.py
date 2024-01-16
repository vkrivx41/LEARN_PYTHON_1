# while loop: is a type of loop that runs statement a determined amount of times

"""
Values: - The counter variable needs to be pre-defined
        - Must consider an escape period to avoid infinite looping
"""
# print hello, scorpus, 3 times

# ex: 1

print("hello, scorpus")
print("hello, scorpus")
print("hello, scorpus")

# ex: 2, Ascending algorithm

counter = 0

while counter < 3:  # while counter <= 2
    print("hello, scorpus")

    counter += 1

# ex: 3, Descending algorithm

counter = 3

while counter != 0:
    print("hello, scorpus")

    counter -= 1

# ex: 4 True
# => we often use True we need to run something infinitely ,
# or when there is a question to be asked and only to be escaped when we find a specific answer

# break: Terminate the execution of a while loop
# continue: Continues the execution of a while loop

while True:
    number: int = int(input("Enter a number: "))

    if number < 0:
        continue
    else:
        break

# use of break only

while True:
    number: int = int(input("Enter a number: "))

    if number >= 0:
        break

# chat bot:
# Here the bot keeps showing up for you to ask it questions, until you input an empty question

while True:
    question: str = input("Me: ")

    if question == "" or question == "bye" or question == "close":
        print("Bot: Ok, see you next time!")
        break

    print("Bot: Hello again!, I will shut when you click enter.")


closing_questions = ["bye", "close", "end", "terminate", "see you", "break", "exit", "finish", ""]
harassing_questions = ["fuck", "bitch", "fucking", "dick"]


def find_harassment_match(words):
    for word in words:
        if word in harassing_questions:
            return True
        return False


while True:
    question: str = input("Me: ")

    if question in closing_questions:
        print("Bot: Ok, see you next time!")
        break

    words = question.split(" ")

    if find_harassment_match(words):
        print("Bot: Sorry, I was not made to answer that question please.")
        break

    print("Bot: Hello again!, I will shut when you click enter.")
