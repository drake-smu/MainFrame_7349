from Crypto.Cipher import AES
from Crypto import Random
from randomtests import randtest
from blocks import low_density
from pprint import pprint
from bitarray import bitarray
import time, sys

samples = low_density.ld_text()
# pprint(sample)
# i = Random.get_random_bytes(AES.block_size)
# a = bitarray()
# a.frombytes(i)
# b = a.to01()
# print(b)
sbits = ''
sbytes = bytearray()

print(len(samples))
print(len(samples[0]["blocks"]))
for sample in samples:
    for bit_set in sample["blocks"]:
        testbits = bitarray()
        testbits.frombytes(bit_set)
        sbits += testbits.to01()
        sbytes.extend(bytes(bit_set))
    # print(bytes(bit_set), testbits.tobytes())
# print(len(sbytes))
sys.stdout.buffer.write(sbytes)
# pprint(sbytes)