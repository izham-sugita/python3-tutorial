class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello, My name is "+self.name)
        
#Create an object of Person
p1 = Person("John",40) #must initiate name and age


