import array
import bz2
import base64

# list -> bytes -> bz2 -> base85
def compress(int_array): return base64.b85encode(bz2.compress(array.array('I', int_array).tobytes()))

# base85 -> bz2 -> bytes -> list
def decompress(compressed): return array.array('I', bz2.decompress(base64.b85decode(compressed))).tolist()
    # Used in Solution code