import numpy as np
import matplotlib
import matplotlib.pyplot as plt

pi = np.pi

imax = 16
dx = 1.0/float(imax)

x = np.arange(0.0, 1.0+dx, dx)
#print(x)
#print(x[0])
#print(x[imax])

kappa = 1.0
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
itermax = 35

anim, gr = plt.subplots()

#iterative loop
for iter in range(itermax):
    for i in range(1,imax):
        fxnew[i] = fx[i] + coeff*( fx[i-1] - 2.0*fx[i] + fx[i+1] )

    #update
    peak.append(fxnew[icenter])
    tminus.append((iter+1)*dt)
    fx = fxnew
    gr.clear()
    gr.set_ylim([0.0,1.2])
    gr.plot(x,fxnew)
    gr.set(xlabel='x', ylabel='f(x)',title='Decay animation')
    gr.grid()
    anim.savefig("anim_"+str(iter)+".png")


