import numpy as np
import ctypes
from ctypes import *

lib = ctypes.CDLL('./myAddition.so')
myAdd = lib['myAddition']

a = 1
b = 2
myAdd(a,b)

c = myAdd(a,b)

print(myAdd(a,b))

print(c)

