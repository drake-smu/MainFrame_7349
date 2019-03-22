
from Crypto.Cipher import AES
from bitarray import bitarray
from Crypto import Random

iv = Random.get_random_bytes(8)

## Our text generators
from shift_test import  low_density_generator,high_density_generator

key = bitarray(high_density_generator(128)[100]).tobytes()

cipher = AES.new(key,AES.MODE_ECB)
random_txt = Random.new().read(AES.block_size) # b'0123456789abcdef'
#print(random_txt)
cypher_block = cipher.encrypt(random_txt)

print(cypher_block)
print(cipher.decrypt(cypher_block))
