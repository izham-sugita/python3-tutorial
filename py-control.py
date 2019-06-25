print("if Statement\n")

x = int(input("Please enter an integer: "))

if x < 0:
	x = 0
	print("Negative value will turn to ZERO")

elif x == 0:
	print("Zero")
	
elif x == 1:
	print("Single")
	
else:
	print("x = %d"%(x))
	

words = ['I', 'me', 'you', 'him']

for w in words:
	print(w, len(w))

for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equals ', x, 'x', n//x)
			break
	else:
		print(n, 'is a prime number')

