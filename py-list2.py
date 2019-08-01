import math as m

imax = 8
jmax = 8

print("Array from 2D list (list of list)")

list2D =[[0.0]*imax for j in range(jmax) ]
#print(list2D)

pi = m.pi
dx = 1.0/float(imax-1)
dy = dx

for i in range(imax):
    for j in range(jmax):
        list2D[i][j] = m.sin(i*dx*pi)*m.sin(j*dy*pi)
        #print(list2D[i][j], i, j)

xc = int(imax/2)
yc = int(jmax/2)
print(list2D[xc][yc])

print("Array from linear list")

linear =[]
for i in range(imax):
    for j in range(jmax):
        linear.append(m.sin(i*dx*pi)*m.sin(j*dy*pi))

xc =int( (imax/2)*jmax + (jmax/2))
print(linear[xc])

import numpy as np

print("Array from numpy")

a = np.ndarray(shape=(imax,jmax))

for i in range(imax):
    for j in range(jmax):
        a[i][j] = m.sin(i*dx*pi)*m.sin(j*dy*pi)

xc = int(imax/2)
yc = int(jmax/2)
print(a[xc][yc])

