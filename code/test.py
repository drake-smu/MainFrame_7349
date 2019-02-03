from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes, random

#print("Hello World!")

key = random.getrandbits(128)
#cipher = AES.new(key, AES.MODE_EAX)
#ciphertext, tag = cipher.encrypt_and_digest(data)
print(hex(key))
#file_out = open("encrypted.bin", "wb")
#[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]


