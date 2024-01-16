
#

# analyze texts
from typing import Any


def analyze_text(txt: str) -> dict:
    return {
        'words': (words := txt.split()),
        'amount': len(words),
        'chars': len(''.join(words)),
        'reversed': list(reversed(words))
    }


text_1 = analyze_text("Hello, world!")

print(text_1)


# if statements

user_input: str = "Hello, Scorpus"

if (text := len(user_input)) > 5:
    print(text, "Good")
else:
    print(text, "Bad")

# check value


def return_some() -> Any:
    return None


if value := return_some():
    print(value)
else:
    print(None)


