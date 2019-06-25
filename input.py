
str = input("Enter something\n")
print(str)

str = str+".txt"
print(str)

file0 = open(str,'w')
file0.write("Writing something to this file.\n")
file0.write("To test how to access a file.\n")
