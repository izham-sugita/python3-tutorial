#define a class
class vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.0
    def description(self):
        desc_str = \
        "My %s is a %s %s worth $%.2f." \
        %(self.name,self.color,self.kind,self.value)
        return desc_str

"""
mycar = vehicle()
mycar.name ="Honda"
mycar.color ="white"
print(mycar.description())
"""

car_list = []

for i in range(5):
    car_list.append(i)
    car_list[i] = vehicle()
    

print(len(car_list))

for i in range(len(car_list)):
    print(car_list[i].description())


class employee:
    #functions to initiate
    def __init__(self, name, salary):
        self.__name=name     #protected attribute, hence private
        self.__salary=salary #protected attribute


e1 = employee("John", 1000)
print(e1._employee__name) #can access and rewrite name
print( "print(e1.__name) cannot access the variable." )
