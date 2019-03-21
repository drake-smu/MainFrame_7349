from Crypto.Cipher import AES
import random
import string
from Crypto.Random import get_random_bytes
import bitarray



def aes_cbc_encrypt(IV, key, data, mode=AES.MODE_CBC):
    aes = AES.new(key, mode, IV)
    new_data = aes.encrypt(data)
    return new_data


def loopfun(n=16):
    key = get_random_bytes(16)
    txt = str().zfill(16)
    IV = "0"*16
    for i in range(n):
        CT = (aes_cbc_encrypt(IV=IV, key=key, data=txt))
        print(CT)
        # Help!!! How do I get this fixed? Must make the ciphertext
        IV = (CT)


(loopfun(n = 128))
