
# compare_digest: compare two inputs using a “constant-time compare” to reduce the risk of timing attacks

from secrets import compare_digest
from timeit import default_timer as timer

password: str = "abc123"
user_input: str = "abc123"

# method 1
start = timer()
if user_input == password:
    print("You are logged in!")
end = timer()

print(end - start)


# method 2

start = timer()
if compare_digest(user_input, password):
    print("You are logged in!")
end = timer()

print(end - start)
