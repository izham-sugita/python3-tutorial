import numpy as np #btter option for scientific computing

a = np.float32(input("Enter a number: ") )

if a>20:
	print("a=%f > 20\n"%a)
elif a<20:
	print("a=%f < 20\n"%a)
else:
	print("Number not in range\n")
