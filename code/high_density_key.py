
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


# print(cypher_block)
# print(cipher.decrypt(cypher_block))

def generate_random_sets(n=1):
    sets = []
    for i in range(n):
        temp_rand = Random.new().read(AES.block_size)
        sets.append(temp_rand)
    return sets

def high_density_key(sets=300):
    output = []
    keys = high_density_generator(128)
    hd_keys = [bitarray(v).tobytes() for v in keys]
    random_text_blocks = generate_random_sets(sets)    
    for text_block in random_text_blocks:
        temp_set = {
            "plain": text_block,
            "blocks": []
        }
        for key in hd_keys:
            cipher = AES.new(key,AES.MODE_ECB)
            cipher_block = cipher.encrypt(temp_set["plain"])
            temp_set["blocks"].append(cipher_block)
        output.append(temp_set)
    
    return output

9a1692
