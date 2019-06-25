import numpy as np
a = 5
print("a=%f"%a)
a = "Any character"
print(a)

x=int(input("Enter an integer: "))
print(x)

x = np.float32(input("Enter a single precision number ") )
print(x)

print("\nWill print numbers with different precision\n")

x = np.float64(np.random.random())
print(x)
x = np.float32(np.random.random())
print(x)
