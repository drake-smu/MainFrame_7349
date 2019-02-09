import pprint


def toggleBit(int_type, offset):
    mask = 1 << offset
    return(int_type ^mask)


def high_density_generator(block_size):
    """
    This function makes array of high density 
    strings of size block_size
    """
    low_density= low_density_generator(block_size)
    resp = []
    for block in low_density:
        # temp = ''
        # for val in block: 
        #     temp+= bin(toggleBit(int(val,2),0))[2:]
        temp = ''.join(map(lambda x: bin(toggleBit(int(x,2),0))[2:],block))
        resp.append(temp)
    return resp


def low_density_generator(block_size):
    """
    This function makes array of low density 
    strings of size block_size
    """
    resp = [bin(0)[2:].zfill(block_size)]

    for i in range(block_size):
        if(i>0):
            for j in range(i):
                resp.append(bin(1<<i|1<<j)[2:].zfill(block_size))
        else:
            for k in range(block_size):
                resp.append(bin(1<<k)[2:].zfill(block_size))
        # print('-----cycle: %s-----'%(i))
    return resp

# test = high_density_generator(30)   # High Tensity Test
# test = low_density_generator(30)    # Low Density Test

# pprint.pprint(test)
