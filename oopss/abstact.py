"""abstract base classes (ABC) according to pep 3119
a decorator indicating abstract method.
 Abstraction in python is defined as a process of handling complexity by hiding
 unnecessary information from the user.
 This is one of the core concepts of object-oriented programming (OOP) languages.
 Abstract Base Class
The main goal of the abstract base class is to provide a standardized way to test
whether an object adheres to a given specification. It can also prevent any attempt
 to instantiate a subclass that doesn’t override a particular method in the superclass.
 And finally, using an abstract class, a class can derive identity from another class
 without any object inheritance.

Declaring an Abstract Base Class
Python has a module called abc (abstract base class) that offers the necessary tools
for crafting an abstract base class. First and foremost, you should understand the ABCMeta metaclass
provided by the abstract base class. The rule is every abstract class must use ABCMeta metaclass.


"""

from abc import ABC,abstractmethod

class shape(ABC):
    @abstractmethod #decorator @
    def area(self):

      pass




class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius



class rectangle(shape):
    def __init__(self, length,width):
        self.length = length
        self.width=width

    def area(self):
        return self.length*self.width
circle=circle(5)
rectangle=rectangle(4,6)
print("area of circle",circle.area())
print("area of recatngle",rectangle.area())






