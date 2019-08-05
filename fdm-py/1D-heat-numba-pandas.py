import numpy as np
from numba import jit, njit
import time

@jit(nopython=True, nogil=True, cache=True, parallel=True)
def theloop(itermax,imax,icenter,coeff,dt,fx,fxnew,peak,tminus):
    for iter in range(itermax):
        for i in range(1,imax):
            fxnew[i] = fx[i] + coeff*( fx[i-1] - 2.0*fx[i] + fx[i+1] )
        peak.append(fxnew[icenter])
        tminus.append((iter+1)*dt)
        fx = fxnew
        
pi = np.pi
imax = int(input("Enter imax: "))
itermax = int(input("Enter maximum iteration: "))

#parameters
dx = 1.0/float(imax)
kappa = 0.25
dt = 0.1*(dx*dx)
coeff = kappa*dt/(dx*dx)

#array using numpy
x = np.arange(0.0, 1.0+dx, dx)
fx = np.sin(pi*x)
fxnew = np.zeros_like(fx)
initfx = fx

peak = []
tminus = []
icenter = int(imax/2)
peak.append(fx[icenter])
tminus.append(0.0)

theloop(1,imax,icenter,coeff,dt,fx,fxnew,peak,tminus) #warm-up compilation

ts = time.time()
theloop(itermax,imax,icenter,coeff,dt,fx,fxnew,peak,tminus)
ts = time.time() - ts

print("Elapsed time after %d steps: %f"%(itermax, ts))

import matplotlib
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(x, initfx)
ax.plot(x,fxnew)
ax.set(xlabel='x', ylabel='f(x)',
       title='Initial value')
ax.grid()
fig.savefig("test-numba.png")
#plt.show()

#next plot
fig0, decay = plt.subplots()
decay.plot(tminus, peak)
decay.set(xlabel='time', ylabel='f(x)_max',
       title='Peak decay')
decay.grid()
fig0.savefig("decay-numba.png")

#Output data file to csv
import pandas as pd

#Create a dictionary data type
todf = {'x':x[:],'fx':fxnew[:]}

#Convert to pandas DataFrame
df = pd.DataFrame(todf,columns=['x','fx'])

#Save to csv
save_csv = df.to_csv('1DheatNumba.csv',index=None, header=True)
