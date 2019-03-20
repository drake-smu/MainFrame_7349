from Crypto.Cipher import AES
import random
import string
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)
txt = str().zfill(128)
IV = "0"*128
# print(IV)
# print(txt)
# print(key)

