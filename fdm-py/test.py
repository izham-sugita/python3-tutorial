import numpy as np
import matplotlib.pyplot as plt

# Make data.
#X = np.arange(-5, 5, 0.25)
#Y = np.arange(-5, 5, 0.25)
#X, Y = np.meshgrid(X, Y)
#R = np.sqrt(X**2 + Y**2)
#Z = np.sin(R)

X = np.arange(0.0, 1.0, 0.05)
Y = np.arange(0.0, 1.0, 0.05)
X, Y = np.meshgrid(X,Y)

pi = np.pi
Z = np.sin(pi*X)*np.sin(pi*Y)

print(Z.shape)

import ThreeDimPlot as TDP
TDP.simple3D(X,Y,Z)

#plt.show()
