
# token_urlsafe: generate a secret urlsafe token, that can be used in creating random url addresses for authentication
# and password resets


from secrets import token_urlsafe

for _ in range(3):
    token = token_urlsafe(16)

    print(token)

# ex:

website: str = "www.scorpus.com"

for _ in range(3):
    secure_token: str = token_urlsafe(32)
    password_reset = f"{website}/security?password_reset={secure_token}"

    print(password_reset)
