def func(arg1):
    print(arg1)

name ="Sugita"
func(name)

a =1
func(a)

del a

def func1(arg1,arg2):
    a = arg1 +1
    b = arg2 +2
    return a, b


a = 1
b = 1

a, b = func1(a,b)

print(a,b)


def func2(arg1, arg2, arg3):
    arg3[0] = arg2[0] + arg1[0]
    return

a = [1]
b = [2]
c = [0]

func2(a,b,c)
print("c[0]=%d\n"%(c[0]))
