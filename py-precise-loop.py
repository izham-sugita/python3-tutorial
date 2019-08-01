import numpy as np

a = np.ndarray(shape=(10),dtype=np.float32)

for i in range(10):
    a[i] = np.random.random()
    #print(a[i])

b = np.random.rand(10)
#print(b)

#print precise
for i in range(6,1,-1):
    print("a[%d]=%.4f"%(i,a[i]))

print()
for i in range(1,6):
    print("a[%d]=%.4f"%(i,a[i]))
    

