import numpy as np
import time
from numba import jit

@jit(nopython=True, cache=True, nogil=True)
def mc(particle):
    count = 0.0
    for i in range(particle):
        xp = np.random.random()
        yp = np.random.random()
        rad = np.sqrt(xp*xp + yp*yp)
        if rad < 1.0:
            count +=1.0
    return count

#init run
total=mc(1)

particle = int(input("Number of random particles: "))
ts = time.time()
count = 0
for i in range(particle):
    xp = np.random.random()
    yp = np.random.random()
    rad = np.sqrt(xp*xp + yp*yp)
    if rad < 1.0:
        count +=1
te = time.time()
normal_time = te-ts

print("Particle inside curvature: ", count)
ratio = np.float64(count)/np.float64(particle)

mypi = ratio*4.0
print("Numpy's pi: ", np.pi)
print("Monte-Carlo's pi: ", mypi, "Time: ",normal_time, "s")

ts = time.time()
total = mc(particle)
te = time.time()
numba_time = te-ts
ratio = total/np.float64(particle)
mypi = ratio*4.0
print("Monte-Carlo's pi: ",mypi, "Time(numba): ", numba_time, "s")

        
