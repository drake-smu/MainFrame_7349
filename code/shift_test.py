# make generic function

def make_permutations(block_size):
    print(bin(0)[2:].zfill(block_size))
    for i in range(block_size):
        #print(bin(1<<i).zfill(block_size))
        if(i>0):
            for j in range(i):
                print(bin(1<<i|1<<j)[2:].zfill(block_size))
        else:
            for k in range(block_size):
                print(bin(1<<k)[2:].zfill(block_size))
        print('-----cycle: %s-----'%(i))
make_permutations(32)
