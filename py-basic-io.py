#Basic terminal input
var0 = input("Enter something:")
print(var0) #input by default is STRING ONLY!

var1 = input("Enter integer: ")
var1 = int(var1)
print(var1, var1+var1)
print(var1, var1, var1, var1) #you can print a lot

var2 = input("Enter real number: ")
var2 = float(var2)
print(var2)

print(format(var2, 'e')) # e <-scientific notation
