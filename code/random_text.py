import random
import string


def random_generator(size=128, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


print(random_generator())
