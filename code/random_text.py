import random
import string
from Crypto.Cipher import AES
from bitarray import bitarray
from Crypto.Random import get_random_bytes
def random_generator(size=128, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

## Encrypt with Random Keys
key = get_random_bytes(16)
cipher = AES.new(key,AES.MODE_ECB)

random_txt = random_generator() # b'0123456789abcdef'
print(random_txt)
cypher_block = cipher.encrypt(random_txt)

# print(random_generator())


print(cypher_block)
print(cipher.decrypt(cypher_block))