# class cali:
#
#     def add(self, *args, **kwargs):
#        return sum(args)
#
#
# obj = cali()
# obj.add(1, 2, 1)

""" even though same method defined but in different class and both that inherit in c1 there it work as first one first
trial this is not possible in java
"""
# class p1:
#     def m1(self):
#         print("class p1")
# class p2:
#     def m1(self):
#         print("class p2")
# class c1(p1,p2): # if c1(p2,p1) then first check c1,p2,p1 this order
#     pass
# obj=c1()
# obj.m1()

# abstract method



# from abc import ABC,abstractmethod
# class ide(ABC):
#     @abstractmethod
#     def debug(self):
#         pass
# class pycharm(ide):
#    def debug(self):
#         print("pycharm debug")
#
#
# obj=pycharm()
# obj.debug()

#here we are giving attribute and also caaling time we giving values

# from abc import ABC,abstractmethod
# class shape(ABC):
#     shape_name:str
#     def __init__(self,name):
#         self.shape_name=name
#     @abstractmethod
#     def draw(self):
#         pass
# class rectangle(shape):
#     def draw(self):
#         print(f'drawing {self.shape_name}')
# class triangle(shape):
#     def __init__(self,name):
#         super().__init__(name)
#
#     def draw(self):
#         print(f'drawing {self.shape_name}')
#
# obj=rectangle("rectan")
# obj.draw()
# obj1=triangle("tri")
# obj1.draw()


# from abc import ABC,abstractmethod
# class bike(ABC):
#     name:str
#     model:str
#     def __init__(self,name,model):
#         self.name=name
#         self.model=model
#     @abstractmethod
#     def start(self):
#         pass
#
# class hunter(bike):
#     def __init__(self,name,model):
#         super().__init__(name,model)
#
#     def start(self):
#         print(f'starting {self.name} model {self.model}')
#
# obj1=hunter("hunter",2023)
# obj1.start()

# from abc import ABC,abstractmethod
# class employee(ABC):
#     name:str
#     salery:int
#     def __init__(self,name,salery):
#         self.name=name
#         self.salery=salery
#     @abstractmethod
#     def calculate_salery(self):
#         pass
#
# class manager(employee):
#     def __init__(self,name,salery):
#         super().__init__(name,salery)
#
#     def calculate_salery(self):
#         print(f" manager {self.name} {self.salery+2500} ")
#
# class developer(employee):
#     def __init__(self,name,salery):
#         super().__init__(name,salery)
#
#     # def calculate_salery(self):
#     #     print(f"developer {self.name} {self.salery+2000} ")
#     def calculate_salery(self):
#         return self.salery+2000

#
# obj1=manager("riya",2000)
# obj1.calculate_salery()
# obj2=developer("siva",2000)
# print(obj2.calculate_salery())

# class my_class:
#     def instance_method(self):
#         print("inside instance")
#     @staticmethod
#     def stactic_method():
#         print("static method")
# obj=my_class()
# obj.instance_method()
# obj.stactic_method()
# my_class.stactic_method()

# attirbute
# static method here we can call with its object as myclass.staticmethod like that main object coby its get to all other
# but main class static copy no one else can acss
# instance method self


# static ulitlity karyam  static method bound with class all other bound with object
# import datetime
# # from datetime import date
# class operations:
#     num1:int
#     num2:int
#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
#     def add(self):
#         return self.num1+self.num2
#     @staticmethod
#     def gettime():
#         return datetime.date.today()
# obj=operations(2,3)
# print(obj.add())
# print(operations.gettime())

class parent:
    def mobile(self):
        self.context=["oneplus","i20"]
        return self.context
class child(parent):
    def mobile(self):
        self.context=super().mobile()
        self.context.append("iphone")
        return self.context

c=child()
print(c.mobile())
ci=parent()
print(ci.mobile())















