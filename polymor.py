"""polymorphism is the ability of an object to take many forms"""
#polymorphism with inheritance and method over ride
# class Vehicle:
#     def __int__(self,name,color,price):
#         self.name=name
#         self.color=color
#         self.price=price
#     def show(self):
#        print(f"Name:{self.name},Color:{self.color},Price:{self.price}")
#     def max_speed(self):
#         print("max speed is 150")
#     def change_gear(self):
#         print("vehicle change 6 gear")
# class Car(Vehicle):
#     def show(self):
#        print(f"Name:{self.name},Color:{self.color},Price:{self.price}")
#     def max_speed(self):
#         print("max speed is 240")
#     def change_gear(self):
#         print("vehicle change 7 gear")
# car=Car('ford','grey',25000)
# car.show()
# car.max_speed()
# car.change_gear()
# vehicle=Vehicle('bmw','black',68686)
# vehicle.show()


""" different forms of an object is polymorphism
"""
class Vehicle:
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price
    def show(self):
        print(f"Name:{self.name},Color:{self.color},Price:{self.price}")
    def max_speed(self):
        print("max speed is 150")
    def change_gear(self):
        print("vehicle change 6 gear")
class car(Vehicle):
    def show(self):
        print(f"Name:{self.name},Color:{self.color},Price:{self.price}")
    def max_speed(self):
        print("max speed is 240")
    def change_gear(self):
        print("vehicle change 7 gear")

car = car("ford","grey",25000)
car.show()
car.max_speed()
car.change_gear()
vehicle=Vehicle('bmw','black',68686)
vehicle.show()
vehicle.change_gear()


import math
class Shape:
    def __init__(self,name):
        self.name=name
    def area(self):
        pass
    def fact(self):
        return "iam a 2D shape"
    def __str__(self):
        return self.name
class Square(Shape):
    def __init__(self,length):
        super().__init__("reethu's Square")
        self.length=length
    def area(self):
        return self.length**2
    def fact(self):
        return "All sides length are equal"
class Circle(Shape):
    def __init__(self,radius):
        super().__init__("reethu's Circle")
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
    def fact(self):
        return "Diameter is twice the radius "
sq=Square(4)
ci=Circle(5)
print(sq.name)
print(sq.area())
print(sq.fact())
print("_____________________")
print(ci.name)
print(ci.area())
print(ci.fact())
# ### OUTPUT ###
# Silpa's Square
# 16
# All sides length are equal
# _____________________
# Silpa's Circle
# 78.53981633974483
# Diameter is twice the radius """
# """

class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Move!")
class Car(Vehicle):
    pass
class Ship(Vehicle):
    def move(self):
        print("Sail!")
class Plane(Vehicle):
    def move(self):
        print("Fly!")
obj_c=Car("bmw",2023)
obj_s=Ship("Kavarathy",2023)
obj_p=Plane("CR-7",2023)
for x in (obj_c,obj_s,obj_p):
    print(f"Brand:{x.brand},Model:{x.model}")
    x.move()
# ### OUTPUT ###
# Brand:bmw,Model:2023
# Move!
# Brand:Kavarathy,Model:2023
# Sail!
# Brand:CR-7,Model:2023
# Fly!
# """

print("..........")
class cat:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f'iam a cat.myname is{self.name}.iam {self.age}years old')
    def sound(self):
        print("meow")
class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print(f'iam a dog.myname is{self.name}.iam {self.age} years old')
    def sound(self):
        print("bark")
cat1=cat("kitty",2)
dog1=dog("kuttu",4)
for animal in (cat1,dog1):
    animal.sound()
    animal.info()


