from numba import jit, cuda

@jit(nopython=True, cache=True, nogil=True, parallel=True)
def mm(a,b,c,imax,jmax,kmax):
    for k in range(kmax):
        for i in range(imax):
            sum = 0.0
            for j in range(jmax):
                sum += a[i,j]*b[j,k]


                c[i,k] = sum

@jit(nopython=True, cache=True, nogil=True, parallel=True)
def dotproduct(a,b,imax):
    sum = 0.0
    for i in range(imax):
        sum +=a[i]*b[i]
    return sum


import numpy as np
import time

imax = 128
jmax = 128
kmax = 128

a = np.random.rand(imax,jmax)
b = np.random.rand(jmax,kmax)
c = np.full((imax,kmax),0.0)
d = np.full((imax,kmax),0.0)

#print(a)
#print(b)
#print(c)

#new c
ts = time.time()
c = np.matmul(a,b)
te = time.time()
elapsed=te-ts
print("Time: %.8f\n"%elapsed)


#first call
a1 = np.random.rand(2,2)
d1 = np.full((2,2),0.0)
mm(a1,a1,d1,2,2,2)

ts = time.time()
#second call
mm(a,b,d,imax,jmax,kmax)
te = time.time()
elapsed = te -ts
print("Time: %.8f"%elapsed)

#print(d-c)

print("Dot product")

v1 = np.random.rand(imax)
v2 = np.random.rand(imax)

v1dotv2 = dotproduct(v1,v2,imax)

npv1dotv2 = np.dot(v1,v2)

print(v1dotv2 - npv1dotv2)
