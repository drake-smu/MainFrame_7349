from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes, random
import string

def random_generator(size=128, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

print(random_generator())
#print("Hello World!")
#key = get_random_bytes(16)
key = b"the key is here!"
randstr = random_generator()
#data = bytes(randstr,encoding="utf8")
#key = random.getrandbits(128)
data=b"This is super confidential message"
cipher = AES.new(key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(data)
#print(hex(key))
file_out = open("encrypted.bin", "wb")
[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
