
from Crypto.Cipher import AES
from bitarray import bitarray
from Crypto import Random

## Our text generators
from blocks.density_generators import  low_density_generator,high_density_generator

def generate_random_sets(n=1):
    sets = []
    for i in range(n):
        temp_rand = Random.new().read(AES.block_size)
        sets.append(temp_rand)
    
    return sets

def ld_text(sets=300):
    output = []
    keys = generate_random_sets(sets)
    text_blocks = high_density_generator(128)
    ld_text_blocks = [bitarray(v).tobytes() for v in text_blocks]
    for key in keys:
        cipher = AES.new(key,AES.MODE_ECB)
        temp_set = {
            "key": key,
            "blocks": []
        }
        for text_block in ld_text_blocks:
            cipher_block = cipher.encrypt(text_block)
            temp_set["blocks"].append(cipher_block)
        output.append(temp_set)
    return output

def ld_key(sets=300):
    output = []
    keys = low_density_generator(128)
    ld_keys = [bitarray(v).tobytes() for v in keys]
    random_text_blocks = generate_random_sets(sets)    
    for text_block in random_text_blocks:
        temp_set = {
            "plain": text_block,
            "blocks": []
        }
        for key in ld_keys:
            cipher = AES.new(key,AES.MODE_ECB)
            cipher_block = cipher.encrypt(temp_set["plain"])
            temp_set["blocks"].append(cipher_block)
        output.append(temp_set)
    
    return output