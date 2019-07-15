import numpy
a = numpy.ndarray(shape=(10), dtype=numpy.float32)

for i in range(10):
    a[i] = float(i)

print(a)

for i in range(10):
    a[i] = 1.0

print(a)

b = numpy.zeros(shape=(10), dtype=float)
print(b)

del b

b = numpy.zeros(shape=(10,10), dtype=float)

print( b)

#multipletype = ['dog', 1, 2, 'cat']
#print(multipletype)
#print(len(multipletype))

#Comment

'''
words = ['I','me','you','him']
print(len(words))
for w in words:
    print(w, len(w))
'''

x = int(input("Enter an integer: "))
if x > 0:
    print("Test succeed!\n")

print("Hello\n")
print("World\n")
