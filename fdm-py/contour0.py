import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

def plot2D(x,y,z):
    fig, ax = plt.subplots()
    cs = ax.contour(x,y,z)
    ax.clabel(cs, inline=1, fontsize=10)
    ax.set_title('Simple 2D Contour')
    fig.savefig("test-simple.png")

'''    
delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2
plot2D(X,Y,Z)
'''

'''
print(X.shape)
print(Y.shape)
print(Z.shape)
'''

'''
fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=1, fontsize=10)
ax.set_title('Simplest default with labels')

plt.show()
'''
