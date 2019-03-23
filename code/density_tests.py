from bitarray import bitarray
import numpy
from pprint import pprint
import high_density as hd 
from ..randomtest import randtest


test = hd.hd_text(3)
bitss = [{"a":x,"b": bytes(x).hex()} for x in test[2]["blocks"]]
print(bitss)
test2 = [int(el["b"],base=16) for el in bitss] 



pprint(test2)