import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

imax = 101
jmax = 101
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

kappa = 1.0
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
peak = []
tminus = []
itermax = 100

for iter in range(itermax):
    for i in range(1,imax-1):
        for j in range(1,jmax-1):
            fxnew[i,j] = fx[i,j] +coeff*(
                (fx[i-1,j] -2.0*fx[i,j] + fx[i+1,j])
                +(fx[i,j-1] -2.0*fx[i,j] + fx[i,j+1]) )

    fx = fxnew

    #print(fx[icenter,jcenter])
    #peak.append(fx[icenter,jcenter])
    #tminus.append((iter+1)*dt)

'''
peak = []
tminus = []
icenter = int(imax/2)
peak.append(fx[icenter])
tminus.append(0.0)
#print(peak)
itermax = 500

#iterative loop
for iter in range(itermax):
    for i in range(1,imax):
        fxnew[i] = fx[i] + coeff*( fx[i-1] - 2.0*fx[i] + fx[i+1] )

    #update
    peak.append(fxnew[icenter])
    tminus.append((iter+1)*dt)
    fx = fxnew


#print(tminus[:])

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(x, initfx)
ax.plot(x,fxnew)
ax.set(xlabel='x', ylabel='f(x)',
       title='Initial value')
ax.grid()
fig.savefig("test.png")
#plt.show()
'''

'''
#next plot
fig0, decay = plt.subplots()
decay.plot(tminus, peak)
decay.set(xlabel='time', ylabel='f(x)_max',
       title='Peak decay')
decay.grid()
fig0.savefig("decay2D.png")
'''

import contour0 as con
con.plot2D(X,Y,fxnew)

import ThreeDimPlot
ThreeDimPlot.simple3D(X,Y,fxnew)
