import numpy as np
import matplotlib.pyplot as plt

import ThreeDimPlot as TDP
import time

import numba
from numba import jit #decorator @jit(nopython=True, nogil=True, cache=True)

@jit(nopython=True, nogil=True, cache=True)
def theloop2D(itermax,imax,icenter,jcenter,rec,coeff,dt,fx,fxnew,peak,tminus):
    ops = 0.0
    for iter in range(itermax):
            for i in range(1,imax-1):
                for j in range(1,jmax-1):
                    fxnew[i,j] = fx[i,j] +coeff*(
                        (fx[i-1,j] -2.0*fx[i,j] + fx[i+1,j])
                        +(fx[i,j-1] -2.0*fx[i,j] + fx[i,j+1]) )

            fx = fxnew
            ops +=7.0*float(imax-2)*float(jmax-2)

            if iter%rec == 0:
                thepeak = fx[icenter,jcenter]
                peak.append(thepeak)
                tminus.append((iter+1)*dt)
                print('Iteration:',iter,' f(x)_peak:',thepeak,)

    return ops

pi = np.pi
imax = 128
jmax = 128
dx = 1.0/float(imax-1)
dy = 1.0/float(jmax-1)

x = np.arange(0.0, 1.0+dx, dx)
y = np.arange(0.0, 1.0+dy, dy)

#print(x.shape, y.shape)
#print(len(x))
#print(x[:])

#for plotting
X, Y = np.meshgrid(x,y)
#print(X.shape, Y.shape)

kappa = 0.25
dt = 0.1*(dx*dx)
coeff = kappa*dt/(dx*dx) # dx == dy; no need to change def.

fx = np.ndarray(shape=(imax,jmax))
for i in range(imax):
    for j in range(jmax):
        fx[i,j] = np.sin(pi*x[i])*np.sin(pi*y[j])

fxnew = np.zeros_like(fx)
initfx = fx

#print(fxnew.shape)

icenter = int(imax/2)
jcenter = int(jmax/2)
peak = [0.0]
tminus = [0.0]
itermax = 10000
rec = 1000

#warm up loop
ops = theloop2D(1,imax,icenter,jcenter,1,coeff,dt,fx,fxnew,peak,tminus)

#reset fx value
fx = initfx
fxnew = np.zeros_like(fx)
ops = 0.0

#real loop
ts = time.time()
ops = theloop2D(itermax,imax,icenter,jcenter,rec,coeff,dt,fx,fxnew,peak,tminus)
ts = time.time() - ts
flops = (ops/ts)*1.0e-9

print('Total operation %f'%ops)
print('Elapsed time: %f'%ts)
print('Performance: %.4f FLOPS'%flops)

'''
for iter in range(itermax):
    for i in range(1,imax-1):
        for j in range(1,jmax-1):
            fxnew[i,j] = fx[i,j] +coeff*(
                (fx[i-1,j] -2.0*fx[i,j] + fx[i+1,j])
                +(fx[i,j-1] -2.0*fx[i,j] + fx[i,j+1]) )

    fx = fxnew

    #peak.append(fx[icenter,jcenter])
    #tminus.append((iter+1)*dt)
'''
    
#print(fxnew.shape)
#print(X.shape)
#print(Y.shape)

import contour0 as con
con.plot2D(X,Y,fxnew)

TDP.simple3D(X,Y,fxnew)
