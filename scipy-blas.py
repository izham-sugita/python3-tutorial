#! /usr/bin/env python3

import numpy as np
from scipy.linalg import blas
import time

print("Enter matrix size, m x n x l")
m = int(input("\n"))
n =int(input("\n"))
l =int(input("\n"))

a = np.random.random((m,l)).astype('float32')

b = np.identity((l)).astype('float32')

c = np.zeros((m,n)).astype('float32')

itermax = 10

ts = time.time()
for iteration in range(itermax):
    c = blas.sgemm(1.0,a,b)
    
#c = blas.sgemm(1.0,a,b)

te = time.time()
duration = te - ts
flops = 2.0*(np.double(m) * np.double(n) *np.double(l) ) - (np.double(m)*np.double(n) )

gflops = (itermax*flops/duration) * 1.0e-9

print("c")
print(c)

print("a")
print(a)

print("Elapsed time : %.4f secs"%(duration))
print("Performance: %.4f GFLOPS"%(gflops))
