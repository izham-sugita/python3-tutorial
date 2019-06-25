import time
import numpy as np

size_of_vec = 100000

def pure_python_version():
    t1=time.time()
    x = range(size_of_vec)
    y = range(size_of_vec)
    z = [ x[i]+y[i] for i in range(len(x)) ]
    return time.time()-t1

def numpy_version():
    t1=time.time()
    x = np.arange(size_of_vec)
    y = np.arange(size_of_vec)
    z = x+y
    return time.time()-t1

t1 = pure_python_version()

t2 = numpy_version()

print("Pure version %.8f secs"%t1)
print("Numpy version %.8f secs"%t2)
