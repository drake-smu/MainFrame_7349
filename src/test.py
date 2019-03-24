from Crypto.Cipher import AES
from Crypto import Random
from randomtests import randtest
from blocks import high_density
from pprint import pprint
from bitarray import bitarray
sample = high_density.hd_key(1)
# pprint(sample)
# i = Random.get_random_bytes(AES.block_size)
# a = bitarray()
# a.frombytes(i)
# b = a.to01()
# print(b)
sbits = ''
sbytes =bytearray()
for bit_set in sample[0]["blocks"]:
    testbits = bitarray()
    testbits.frombytes(bit_set)
    sbits += testbits.to01()
    print(bytearray(bit_set), testbits.tobytes())

#randtest.testall(sbits)
