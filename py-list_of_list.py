import numpy as np

pi = np.pi
#create list of list
list1D = []

imax = 11
jmax = 11
dx = 1.0/(imax-1)
dy = dx

for i in range(imax):
    list1D.append(0.0)

list2D = []
for j in range(jmax):
    list2D.append([0.0 for i in range(imax)])
    #list2D.append(list1D) <-cannot be used because object list1D needs
    #to be changed; not from index i j only

print(list2D)

print()

for i in range(imax):
    for j in range(jmax):
        list2D[i][j] = np.sin(i*dx*pi)*np.sin(j*dy*pi) #i*jmax + j
        #print(list2D[i][j])

xc = int(imax/2)
yc = int(jmax/2)
print(list2D[xc][yc])





