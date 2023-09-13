# Create a class called Vehicle with the following attributes and methods:
#
# Attributes:
# make: a string representing the make of the vehicle
# model: a string representing the model of the vehicle
# year: an integer representing the year the vehicle was made
# color: a string representing the color of the vehicle
# mileage: a float representing the current mileage of the vehicle
#
# Methods:
# _init_(self, make, model, year, color, mileage): initializes the attributes with the given values
# drive(self, distance): takes a float representing the distance driven and updates the mileage attribute
# accordingly
# get_info(self): returns a string with the vehicle's make, model, year, color, and mileage attributes
# in a formatted way
# Create a subclass called Car that inherits from the Vehicle class with the following additional
# attributes and methods:
# Attributes:
# num_doors: an integer representing the number of doors the car has
# engine_type: a string representing the type of engine the car has
# Methods:
# _init_(self, make, model, year, color, mileage, num_doors, engine_type): initializes the attributes with the given
# values
# get_info(self): overrides the get_info method of the Vehicle class to include the num_doors and engine_type attributes
# Create an instance of the Vehicle class and call the drive method with a distance of 100. Then call the get_info
# method to print out the vehicle's information.
#
# Create an instance of the Car class and call the drive method with a distance of 50. Then call the get_info method
# to print out the car's information.
# """
#
# """
# Question:
#     Define a class, which have a class parameter and have a same instance parameter.
class vehicle():
    def __init__(self,make,model,year,color,milage):
        self.make=make
        self.model=model
        self.year=year
        self.milage=milage
        self.color=color
# modelx=vehicle("bm",5,23,"yellow",18)
# print(modelx.make,modelx.model,modelx.year,modelx.color,modelx.milage)
    def drive(self,distance):

        #print("milage:",self.milage)
        distance=distance/self.milage
        self.milage=distance
        #print("upmil:",distance)
    def get_info(self):
        print("vehicle's details:",self.make,self.model,self.year,self.color,self.milage)
class car(vehicle):
    def __init__(self,make,model,year,color,milage,num_doors,engine_type):
        super().__init__(make,model,year,color,milage) #super parent class properties na child claasilk call cheyan
        self.num_doors=num_doors
        self.engine_type=engine_type
    def get_info(self):
        print("vehicle's details:",self.make,self.model,self.year,self.color,self.milage,self.num_doors, self.engine_type)

obj1=vehicle("bmw",3,2023,"red",40)
obj1.drive(100)
obj1.get_info()

obj2=car("tata",2,2023,"yellow",50,4,"v7")
obj2.drive(50)
obj2.get_info()
print("........................")
#2 define a class which have a class parameter and have a same instance parameter
#hints:define a instance
class myclass:
    class_param="class parameter"
    def __init__(self,instance_param):
        self.instance_param=instance_param
#creating an object of myclass and initializing the instance parameter
my_object=myclass("instance parameter")
#accessing class para
print(myclass.class_param)
#accessing instance
print(my_object.instance_param)

print("........................")
"""
When the method signature (name and parameters) are the same in the superclass and the child class, it's called overriding. 
When two or more methods in the same class have the same name but different parameters, it's called overloading 
over loading not used in python

"""

class Animal:
    def __init__(self,name):
        self.name=name
        print(f"my name {self.name}")
    def breath(self):
        print("i breath o2")
    def food(self):
        print("i eat food")
class Dog(Animal):
    def food(self):# method over ride
        print("i eat food")
obj=Dog("mickey")
obj.food()
obj.breath()

print("........................")

class company:
    def company_name(self):
        return 'google'
class employee(company):
    def info(self):
        #calling superclass methods usind super
        c_name=super().company_name()
        print("ree works at",c_name)
emp=employee()
emp.info()

print("........................")
# string format and class asses
class person:
    name="person"
    def __init__(self,name):
        self.name=name
obj=person("reethu")
print("%s name is %s"%(person.name,obj.name))
obj1=person("rajan")
print(f"person name is {obj1.name}")

print("........................")
"""
The circle class models a circle with a radius and color

attributes : radius , color

methods :

Circle
getRadius()
getCircumference()
getArea()
"""


import math
import turtle
class Circle:


    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
    def circle(self):
        print("circle")
    def getradius(self):
        print("radius",self.radius)
    def getarea(self):
        area = math.pi*self.radius**2
        print("Area of the circle is: ",area)
    def getcircum(self):
        circum = 2*math.pi*self.radius
        print("circum of the circle is: ",circum)

    def drawcircle(self):
        t = turtle.Turtle()
        t.fillcolor(self.color)
        t.begin_fill()
        t.circle(self.radius)
        t.end_fill()
        turtle.done()
c = Circle(100,'red')
c.getradius()
c.getcircum()
c.getarea()
c.drawcircle()
c.circle()
