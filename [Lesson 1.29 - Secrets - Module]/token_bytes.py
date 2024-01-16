
# token_bytes: generate a bytes-version secret , default = 32

from secrets import token_bytes

token_32 = token_bytes(32)
print(token_32)

token_16 = token_bytes(16)
print(token_16)
