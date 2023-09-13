"""Assignment – Oops

1. Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters

2. Define a class with a generator which can iterate the numbers, which are divisible by 7,
 between a given range 0 and n.
(Just try )

Hints:
Consider use yield

3. Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value later

4. Define a class named American which has a static method called printNationality.

Hints:

Use @staticmethod decorator to define class static method.

5. Define a class named American and its subclass NewYorker.

Hints:

Use class Subclass(ParentClass) to define a subclass.

6. Define a class named Circle which can be constructed by a radius.
The Circle class has a method which can compute the area.

Hints:

Use def methodName(self) to define a method.

7. Define a class named Rectangle which can be constructed by a length and width.
The Rectangle class has a method which can compute the area.

Hints:

Use def methodName(self) to define a method.

8. Define a class named Shape and its subclass Square. The Square class has an init function
 which takes a length as argument. Both classes have a area function
 which can print the area of the shape where Shape's area is 0 by default.

Hints:

To override a method in super class, we can define a method with the same name in the super class.

9. Define a class Person and its two child classes: Male and Female.
All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

Hints:
Use Subclass(Parentclass) to define a child class.
"""
"""
#1. Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.

Hints:
Use __init__ method to construct some parameters
"""
# class strr:
#
#     def __init__(self):
#         self.strr=''
#     def getstring(self):
#         self.str=input("enter a string:")
#     def printstring(self):
#         print(f'uppercas:{self.str.upper()}')
#     def tests(self):
#         print("test the class methods")
# strr=strr()
# strr.getstring()
# strr.printstring()
# strr.tests()
# print("....................")
'''2. Define a class with a generator which can iterate the numbers, which are divisible by 7,
 between a given range 0 and n.
(Just try )

Hints:
Consider use yield
'''
# class divi:
#     def __init__(self):
#         self.n=''
#     def range(self):
#         self.n=int(input("enter a number"))
#     def divis(self):
#         for i in range(self.n):
#             if i%7==0:
#                 print(i)
# divi=divi()
# divi.range()
# divi.divis()
# print("............")
'''
3. Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value later
'''
# class ins:
#     clapara="class parameter" # class parameter parameter before constructor
#     def __init__(self,instancepara):
#         self.instancepara="iam instancepara" # inatance para
#         #self.instancepara=instancepara # set value later
#         #print(self.instancepara)
#     def getpara(self): # init object with construct parameter
#
#         print(self.instancepara)
# obj=ins("set the value later")
# print(obj.clapara)
# obj.getpara()
#
# print("............")
"""
4. Define a class named American which has a static method called printNationality.

Hints:

Use @staticmethod decorator to define class static method.
 """
# class American:
#     #@staticmethod
#     def printnationality(American):
#
#         print("american")
# american=American()
# american.printnationality()
# print("............")
#
# class American:
#     @staticmethod
#     def printnationality():
#
#         print("american")
# american=American()
# american.printnationality()
# #American.printnationality()
# print("............")
'''
5. Define a class named American and its subclass NewYorker.
Hints:
Use class Subclass(ParentClass) to define a subclass.
'''
class American:
    def __init__(self,nation):
        self.nation=nation
    def display(self):
        print(f"Nation:{self.nation}")
class NewYorker(American):
    def display(self):
        print("NewYorker")
obj=NewYorker("American")
obj.display()
obj_a=American("American")
obj_a.display()
print("..............")



'''

6. Define a class named Circle which can be constructed by a radius.
The Circle class has a method which can compute the area.

Hints:

Use def methodName(self) to define a method.
'''
# import math
#
# class Circle:
#
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def getradius(self):
#         print("radius",self.radius)
#     def getarea(self):
#         area = math.pi*self.radius**2
#         print("Area of the circle is: ",area)
#
# c = Circle(100)
# c.getradius()
# c.getarea()
#
# print(".............")

'''
7. Define a class named Rectangle which can be constructed by a length and width.
The Rectangle class has a method which can compute the area.

Hints:

Use def methodName(self) to define a method.
'''
# class RECTANGLE:
#
#
#     def __init__(self,LENGTH,width):
#         self.LENGTH = LENGTH
#         self.width=width
#
#     def getpara(self):
#         print("legth,width",self.LENGTH,self.width)
#     def getarea(self):
#         area = self.LENGTH*self.width
#         print("Area of the rectangle is: ",area)
#
# c = RECTANGLE(100,50)
# c.getpara()
# c.getarea()
# print(".............")
'''
8. Define a class named Shape and its subclass Square. The Square class has an init function
 which takes a length as argument. Both classes have a area function
 which can print the area of the shape where Shape's area is 0 by default.

Hints:

To override a method in super class, we can define a method with the same name in the super class.
'''
# class shape:
#     def __init__(self):
#         self.area=0
#     def areas(self):
#         print(self.area)
#
# class square(shape):
#     def __init__(self,length):
#            super().__init__()
#            self.length=length
#     def areas(self):
#         area=self.length*self.length
#         print(area)
# obj=square(4)
# obj.areas()
# obj1=shape()
# obj1.areas()
# print(".............")
'''
9. Define a class Person and its two child classes: Male and Female.
All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

Hints:
Use Subclass(Parentclass) to define a child class.
'''
# class person:
#
#     pass
# class male(person):
#     def getgender(self):
#         print("male")
# class female(person):
#     def getgender(self):
#         print("female")
# obj=male()
# obj.getgender()
# obj1=female()
# obj1.getgender()
# print(".............")
"""1: Write a Program to create a class by name Students, and initialize attributes like 
name, age, and grade while creating an object.
Solution: To create a class in Python, we can use the class, 
and to initialize the attribute during object creation, we can define the __init__() method."""
class Students:
    #initialize the properties
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

#create object
raj = Students('Raj', 16, '11th')
print("..............")
"""Write a Program to create a valid empty class by name Students, with no properties"""
class Students:
    pass

#create object
raj = Students()
"""The pass keyword allows us to leave a block code without any body definition."""
'''Write a program to create a child class Teacher that will inherit the properties of Parent class Staff'''
class Staff:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def show_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Role:", self.role)
        print("Department:", self.dept)

#inherit from the Staff class
class Teacher(Staff):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # initialize the Parent  class
        super().__init__("Teacher", "Science", 25000)


teacher = Teacher("Raj", 28)

#access the Staff Method
teacher.show_details()
print(".........")
"""Write a Program to create a class and, using the class instance, print all the writable 
attributes of that object."""

class Staff:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def show_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Role:", self.role)
        print("Department", self.dept)

#inherit from the Staff class
class Teacher(Staff):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # initialize the Parent  class
        super().__init__("Teacher", "Science", 25000)

teacher = Teacher("Raj", 45)

#display all the namespaces
print(teacher.__dict__)
print(".............")
"""What would be the output of the following program?"""
class Staff:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def show_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Role:", self.role)
        print("Department", self.dept)

#inherit from the Staff class
class Teacher(Staff):
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # initialize the Parent  class
        super().__init__("Teacher", "Science", 25000)

teacher = Teacher("Raj", 45)

print(isinstance(teacher, Teacher))

print(isinstance(teacher,Staff))
print(".............")
""" Create a class Teacher with name, age, and salary attributes,
 where salary must be a private attribute that cannot be accessed outside the class."""
class Teacher():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age

        # private variable
        self.__salary = salary

    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)

        #access private attribute inside the class
        print("Salary: ", self.__salary)

teacher = Teacher("Raj", 45, 25000)

teacher.show_details()

# print(teacher.name)   #Raj

#access private member outside the class will throw error
# print(teacher.__salary)   #error

print(".............")
""" Write a Python program that overloads the operator + and > for a custom class."""
class Orders:
    def __init__(self, items):
        self.items = items

    # overload the + operator
    def __add__(self, other):
        return self.items + other.items

    # overload the > operator
    def __gt__(self, other):
        return len(self.items) > len(other.items)

order1 = Orders([1, 2, 3, 4, 5, 6])

order2 = Orders([10, 20, 30])

print("order1 + order2=", order1 + order2)
print("order1 > order2=", order1 > order2)
print(".............")

"""Write a Python class Square, and define two methods that return the square area and perimeter."""
class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4*(self.side)

#initialize the objects of Square class
square1 = Square(10)
square2 = Square(20)

print("The Area of square1 is:", square1.area())
print("The Perimeter of square1 is:", square1.perimeter())

print("\n\nThe Area of square2 is:", square2.area())
print("The Perimeter of square2 is:", square2.perimeter())
print(".............")

"""Write a program that prints the class name using its object."""
class Animal:
    pass


# Animal class object
lion = Animal()

print("The ClassName of the lion object is: ", lion.__class__.__name__)
print(".............")
""" Write a Program in Python to implement a Stack Data Structure using Class and Objects,
 with push, pop, and traversal methods."""
class Stack:
    # initialize an empty list
    def __init__(self):
        # conventional private member
        self.__stack = []

    # add items to the stack
    def push(self, item):
        self.__stack.append(item)

    # pop item from the stack
    def pop(self):
        self.__stack.pop()

    def traverse(self):
        for item in self.__stack[::-1]:
            print("|", item, "|")

# initialize the object
stack = Stack()

# push item to the stack
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)
stack.push(9)

# pop items from the stack
stack.pop()
stack.pop()

# traverse through the stack
stack.traverse()
print(".............")
"""Write a Python program that lists out all the default as well as custom properties of the class."""
class Teacher:
    def __init__(self, name, age):
        self.name = name
        self.age = age

teacher = Teacher("Lokesh", 36)
print("Teacher class's object  all properties")

print(dir(teacher))
"""Write a Python program that checks if one class is a subclass of another."""
class Staff:
    def show_details(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

# inherit from the Staff class
class Teacher(Staff):
    def __init__(self, name, age):
        self.name = name
        self.age = age

print("Is Teacher a subclass of Staff:", issubclass(Teacher, Staff))
print("Is Staff a subclass of Teacher:", issubclass(Staff, Teacher))
print(".............")
"""dictonary"""
class ANIMALCLASS:
    def __init__(self,identity,age):
        self.identity=identity
        self.age=age
    def feature(self):
        if self.age=='10':
            return True
        else:
            return False

ac=ANIMALCLASS('LION',11)
print(ac.__dict__)
print(".............")
class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def __str__(self):
        return f'rectangle with length={self.length}and width={self.width}'
rect=rectangle(6,8)
print(rect.__dict__)
print(rect.__str__())
print(".............")


# class teacher:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.__salary=salary
#     def show_details(self):
#         print(self.age)
#         print(self.name)
#         print(self.__salary)
# obj=teacher("ree","28","25000")
# obj.show_details()
# print(obj.name)
# #print(obj.salary)# error
# print(".............")