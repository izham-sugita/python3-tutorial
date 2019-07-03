import numpy as np
import sys
a = 32
b = np.int32(a)
c = np.int64(a)
d = np.float32(a)
e = np.float64(a)

print(sys.getsizeof(b),"bytes")
print(sys.getsizeof(c),"bytes")
print(sys.getsizeof(d),"bytes")
print(sys.getsizeof(e),"bytes")
