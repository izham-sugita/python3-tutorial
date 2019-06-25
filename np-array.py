import numpy as np

a = np.ndarray(shape=(10), dtype=float) #basic array shape 1D
b = np.ndarray(shape=(10,10), dtype=float) #basic array shape 2D

print(np.random.random())

mylist = []
for i in range(10):
    mylist.append(i)
    mylist[i] = np.random.random()

print(mylist)

a1 = np.array(mylist)
print(a1)
