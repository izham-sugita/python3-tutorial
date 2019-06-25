'''
def functionname(parameters):
	"function comment"
	function_suite
	return [expression]
'''

def printme( str ):
	"This function prints the string input"
	print( str )
	return

#calling the function
#str = "This is the string to print"
#printme(str)

#pass by value
def changeme( mylist ):
	"This changes a passed list"
	print ("Value before: ", mylist)
	
	mylist[2] = 50
	print ("Value after: ", mylist)
	return

#mylist = [10,20,30]
#changeme(mylist)

# *vartuple is a tupple, more or less like a dynamic array
def printinfo( *vartuple ):
	for var in vartuple:
		print( var )
	return

#printinfo(1, 2, 3, 4)

def sum( arg1, arg2 ):
	total = arg1 + arg2
	print("Inside the function : ", total)
	return total

#addition = sum(10,20)
#print(addition) # will print "None" because nothing is returned

if __name__ == '__main__':
	print(sum(10,10))
	str = "Sugita"
	printme(str)
