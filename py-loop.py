edibles = ["nasi", "ayam", "ikan", "kuih"]

for food in edibles:
	if food == "nasi":
		print( food+" is good")
		
	else:
		print("No "+food)


#Example of simple loop
import numpy as np
imax = 64
a = np.ndarray(shape=(imax), dtype=float)
for i in range(imax):
        a[i] = 1.0

#print(a)
#print(type(a))

#del a
#print(a) #a is deleted. can be re-used. neat. very neat.

words = ['I', 'me', 'you', 'him']
for w in words:
	print(w, len(w))
