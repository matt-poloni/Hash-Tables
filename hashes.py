import time
import hashlib
# import bcrypt

key = b"hello"

def djb2(key):
    # Start from arbitrarily large prime
    hash_value = 5381
    # bit-shift and sum value for each char
    for char in key:
        hash_value = ((hash_value << 5) + hash_value) + char
    return hash_value

print(djb2(key))