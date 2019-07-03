def func1():
    print("This is func1()")
    return

def func2(arg1, arg2, arg3):
    print("This is func2(); it changes mutable object")
    arg3[:] = arg1[:] + arg2[:]
    return
