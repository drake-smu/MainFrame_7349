# make generic function

def make_permutations(block_size):
    print(bin(0).zfill(block_size))
    for i in range(block_size-2):
        print(bin(1<<i).zfill(block_size))

make_permutations(10)
