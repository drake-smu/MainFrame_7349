from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


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
        IV = (CT)


(loopfun(n=128))
