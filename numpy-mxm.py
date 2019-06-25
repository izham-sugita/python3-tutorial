# For more details read the numpy documentation online
import numpy as np

#matrix n x n
imax = np.int64(input("Enter imax \n"))

A = np.float64( np.random.rand(imax,imax) )
B = np.float64( np.random.rand(imax,imax) )
C = np.float64( np.zeros((imax,imax)) )

# multiplication A x B = C
import time

ts = np.float64( time.time() )
C = np.dot(A,B)
te = np.float64( time.time() )

elapsed = te - ts
print(type(elapsed))

dmax = np.float64(imax)
gflops = ((2.0*dmax*dmax*dmax - dmax*dmax) / elapsed )*1.0e-9

'''print(A)
print("\n")
print(B)
print("\n")
print(C)'''

print("Elapsed time : %.8f secs \n"%(elapsed))
print("Performance: %.4f GFLOPS \n"%gflops)
