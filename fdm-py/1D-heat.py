import numpy as np
import time

pi = np.pi

imax = 100
dx = 1.0/float(imax)

x = np.arange(0.0, 1.0+dx, dx)
#print(x)
#print(x[0])
#print(x[imax])

kappa = 0.25
dt = 0.1*(dx*dx)
coeff = kappa*dt/(dx*dx)

fx = np.sin(pi*x)
fxnew = np.zeros_like(fx)
initfx = fx
#print(fx)

peak = []
tminus = []
icenter = int(imax/2)
peak.append(fx[icenter])
tminus.append(0.0)
#print(peak)
itermax = 5000

ts = time.time()
#iterative loop
for iter in range(itermax):
    for i in range(1,imax):
        fxnew[i] = fx[i] + coeff*( fx[i-1] - 2.0*fx[i] + fx[i+1] )

    #update
    peak.append(fxnew[icenter])
    tminus.append((iter+1)*dt)
    fx = fxnew


ts = time.time() -ts
print("Elapsed time after %d steps: %f"%(itermax, ts))
#print(tminus[:])
    
import matplotlib
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(x, initfx)
ax.plot(x,fxnew)

ax.set(xlabel='x', ylabel='f(x)',
       title='Initial value')
ax.grid()

fig.savefig("test.png")
#plt.show()

#next plot
fig0, decay = plt.subplots()
decay.plot(tminus, peak)

decay.set(xlabel='time', ylabel='f(x)_max',
       title='Peak decay')
decay.grid()

fig0.savefig("decay.png")
