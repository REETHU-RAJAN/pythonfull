"""
data store cheyan vendi data base relational db data to data dependancy rdms sql structured query language,
dml,reginarinshy143@R passwrd sql  mysql-u root -p for selection show databases;
Decorators are a very powerful and useful tool in Python since it allows programmers to modify
the behaviour of a function or class. Decorators allow us to wrap another function in order to extend
the behaviour of the wrapped function, without permanently modifying it.
@  symbol
@gfg_decorator
def hello_decorator():
    print("Gfg")

'''Above code is equivalent to -

def hello_decorator():
    print("Gfg")

hello_decorator = gfg_decorator(hello_decorator)'''`
"""
# def deco_func(func):
#     def wrapper():
#         print("before func execution")
#         func()
#         print("after function execution")
#     return wrapper
#
# @deco_func
# def my_func():
#     print("inside the my func")
# my_func()
#
print("...............")
# def decor_func(f):
#     def inner():
#         print("i got decorator")
#         f()
#     return inner
# @decor_func
# def test_fun():
#     print("a test func")
# test_fun()
print("...............")
# def decor_func(f):
#     def inner():# inner func
#         print("i got decorator")
#         f() # calling test_fun
#
#
#     return inner # return inner func
#
#
# @decor_func
# def test_fun():
#     print("a test func")
# #test_fun()
#
# decorated_fun=decor_func(test_fun()) #decorate test fn without testfn()
# # decorated_fun()# calling decorated func
print("...............")
def upper_decor(fun):
    def wrapper(name):
        result=fun(name)

        return result.upper()
    return wrapper


@upper_decor
def hello_name(name):
    return "hello"+name
print(hello_name(" karthik"))
print("...............")
def upper_decor(fun):
    def wrapper(name):
        result=fun(name)
        out="hello "+result.upper()
        return out
    return wrapper


@upper_decor
def hello_name(name):
    return name
print(hello_name(" karthik"))
print("...............")
def upper_decor(fun):
    def wrapper(name):
        result=fun(name)
        out=result.upper()
        print("hello",out)

    return wrapper


@upper_decor
def hello_name(name):
    return name
hello_name(" karthik")
print("...............")
# def upper_decor(fun):
#     def wrapper():
#         result=fun().upper()
#         return result
#     return wrapper
#
#
# @upper_decor
# def say_hello():
#     return "hello,world!"
# print(say_hello())
# print("...............")
#
# """ 1. Simple Decorator program"""
# def dec(func):
#     def inner():
#         print("Decorator inner function")
#         func()
#     return inner
# @dec
# def normal_func():
#     print("Normal function")
# normal_func()
# """
# ___OUTPUT___
# Decorator inner function
# Normal function
# """
#
# """ 2. Decorating functions with parameters"""
# def dec(func):
#     def inner(a,b):
#         print(f"iam going to divide {a} and {b}")
#         if b==0:
#             print(f"can't divide {a} and {b}")
#             return
#         return func(a,b)
#     return inner
# @dec
# def divide(a,b):
#     print(f"Result of {a} / {b}:",a/b)
# divide(4,2)
# divide(4,0)
# """
# ___OUTPUT___
# iam going to divide 4 and 2
# Result of 4 / 2: 2.0
# iam going to divide 4 and 0
# can't divide 4 and 0
# """
#
# """ 3. Chaining decorators"""
# def star(func):
#     def inner(msg):
#         print("*"*10)
#         func(msg)
#         print("*"*10)
#     return inner
# def symbol_(func):
#     def inner(msg):
#         print("_"*10)
#         func(msg)
#         print("_"*10)
#     return inner
# @star
# @symbol_
# def display(msg):
#     print(msg)
# display("hai silpa !")
# """def star(func):
#     def inner(msg):
#         print("*"*10)
#         func(msg)
#         print("*"*10)
#     return inner
# def symbol_(func):
#     def inner(msg):
#         print("_"*10)
#         func(msg)
#         print("_"*10)
#     return inner
# @star
# @symbol_
# def display(msg):
#     print(msg)
# display("hai silpa !")
# "
# ___OUTPUT___
# **********
# __________
# hai silpa !
# __________
# **********
# """
# def star(func):
#     def inner(msg):
#         print("*"*10)
#         print("_" * 10)
#         func(msg)
#         print("_"*10)
#
#         print("*"*10)
#
#     return inner
#
# @star
#
# def display(msg):
#     print(msg)
# display("hai reethu!")

# importing libraries
import time
import math
# decorator to calculate duration
# taken by any function.
def calculate_time(func):
    # added arguments inside the inner1,
    # if function takes any arguments,
    # can be added like this.
    def inner1(*args, **kwargs):
        # storing time before function execution
        begin = time.time()

        func(*args, **kwargs)

        # storing time after function execution
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)

    return inner1


# this can be added to any function present,
# in this case to calculate a factorial
@calculate_time
def factorial(num):
    # sleep 2 seconds because it takes very less time
    # so that you can see the actual difference
    time.sleep(2)
    print(math.factorial(num))


# calling the function.
factorial(10)


def hello_decorator(func):
    def inner1(*args, **kwargs):
        print("before Execution")

        # getting the returned value
        returned_value = func(*args, **kwargs)
        print("after Execution")

        # returning the value to the original frame
        return returned_value

    return inner1


# adding decorator to the function
@hello_decorator
def sum_two_numbers(a, b):
    print("Inside the function")
    return a + b
a, b = 1, 2
#
#
# # code for testing decorator chaining
def decor1(func):
    def inner():
        x = func()
        return x * x

    return inner


def decor(func):
    def inner():
        x = func()
        return 2 * x

    return inner


@decor1
@decor
def num():
    return 10


@decor
@decor1
def num2():
    return 10


print(num())
print(num2())

# getting the value through return of the function
print("Sum =", sum_two_numbers(a, b))

# print(".............")
# #class method
# class myclass:
#     class_vari="hello"
#     @classmethod
#     def class_method(cls):
#         print(cls.class_vari) # covert class inside class
# #myclass.class_method()# class name.class method
#
# obj=myclass()
# obj.class_method()
# print(".............")
# class rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         return self.length*self.width
#     def perimeter(self):
#         return 2*(self.length+self.width)
#     @classmethod
#     def create_square(cls,side):
#         return cls(side,side) #cls(side,side*side)
# rectangle=rectangle(7,6)
# print(rectangle.area())
# print(rectangle.perimeter())
# square=rectangle.create_square(4)
# print(square.area())
# print(square.perimeter())
#
# print(".............")
# class bankaccount:
#     interest_rate=0.08
#     def __init__(self,account_number,balance):
#         self.account_number=account_number
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance+= amount
#     def withdraw(self,amount):
#         if self.balance>= amount:
#             self.balance-= amount
#         else:
#             print("insufficinet funds...")
#
#
#     def calculate_interest(self):
#         return self.balance * self.interest_rate
#
#
#     @classmethod
#     def set_interest_rate(cls,rate):
#         cls.interest_rate=rate
#         print("classmethod,interest updated")
# bank=bankaccount("sbinoo7",10000)
# print(bankaccount.interest_rate)
# bankaccount.set_interest_rate(0.07)
#
# print(bankaccount.interest_rate)
# interest=bank.calculate_interest()
# print(interest)
# print("................")
# """
# #static method allow you to group related functions together within a class.
# # even if those functuons donot require acess to instance_specific data
# reuse and readbility
# """
# class American:
#     @staticmethod
#     def printnationality():
#
#         print("american")
# american=American()
# american.printnationality()
# #American.printnationality()
# print("............")
#
# class math:
#     @staticmethod
#     def multiply(a,b):
#         return a* b
#     @staticmethod
#     def is_even(number):
#
#         return number % 2== 0
# result=math.multiply(5,6)
# print(result)
# print(math.is_even(10))
# print(math.is_even(7))
# print("............")
#
# # def is_even(number):
# #     if number %2==0:
# #         print("the num is even")
# #     else:
# #         print("the num is odd")
#
# from datetime import date
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     @classmethod
#     def frombirthyear(cls,name,year):
#         return cls(name,date.today().year- year)
#     def display(self):
#         print("name :",self.name,"age:",self.age)
# person = person("maya",21)
# person.display()
# print(".....")
# class geeks:
#     course="dsa"
#     def purchase(obj):
#         print("purchase course:",obj.course)
# geeks.purchase=classmethod(geeks.purchase)
# geeks.purchase()
# print("............")
#
