# test="hello hai"
# wd=test.split( )
# print(wd)
# lst=[10,20,30]
# t=lst.append(90)
# print(lst)
# lst=list()

# st=set()
# class student:
#     name=str
#     age=int
#     id=int
#     course=str
#     def add_student(self,name,age,id,course):
#         self.name=name
#         self.age=age
#         self.id=id
#         self.course=course
#     def get_student(self):
#         print(self.name,self.age)
# obj=student()
# obj.add_student("amm",12,3,"sds")
# obj.get_student()
# class bank:
#     # instance variable<> here is acno,balance,....
#     acno:int
#     balance:int
#     ac_type:str
#     p_name:str
#     # java,c++ <> constructor be Class name
#     # javascrpt<> constructor
#     # python<> __init__
#     def __init__(self,acno,bal,ac_type,p_name): #def create_account
#         # initializing instance variable<> constructor  variable start with always self thats constructor
#         self.acno=acno
#         self.balance=bal
#         self.ac_type=ac_type
#         self.p_name=p_name
#     def deposit(self,amount):
#         self.balance+=amount
#         print(f'your sbi account{self.acno} has been credit {amount} avl balance is {self.balance}')
#
#     def withdraw(self,amount):
#         if self.balance>=amount:
#
#             self.balance-=amount
#             print(f'your sbi account{self.acno} has been debit {amount} avl balance is {self.balance}')
#         else:
#             print(f'insufficeient balance')
#
#
#
#
#
#
# obj1=bank(776,8989,"fixed","ammu") # constructor calling
# obj2=bank(75,889,"saving","au")
# # obj.create_account(776,8989,"fixed","ammu")
# obj1.withdraw(1000)
# obj2.deposit(3000)
#



# class users:
#     data=[{"id":1,"username":"hari","email":"hgmhbm@"},
#           {"id": 2, "username": "ri", "email": "hgmhbm@"},
#           {"id": 3, "username": "hi", "email": "hgmhbm@"},
#           {"id": 4, "username": "ari", "email": "hgmhbm@"}
#
#
#
#           ]
#     def get(self):
#         return self.data
#
#     def retriew(self,id):
#         return[u for u in self.data if u.get("id")==id ]
#     def post(self,obj):
#         self.data.append(obj)
#     def destroy(self,id):
#         obj=[u for u in self.data if u.get("id")==id][0]    #[0] only get one value
#         self.data.remove(obj)
#     def put(self,id,values):  # values :ee id ulladina ee value vech update akka\
#         obj = [u for u in self.data if u.get("id") == id][0]
#         # print(values[0]) in case tuple
#         pos=self.data.index(obj)
#         self.data[pos]=values
#
#
#
# obj=users()
# data={"id": 4, "username": "hhhhari", "email": "hgmhbm@"}
# print(obj.retriew(4))
#
# obj.put(4,data)
# print(obj.retriew(4))
#
#
# print(obj.get())

# obj.destroy(1)
# print(obj.get())


# student_data={"id":7,"username":"i","email":"hgmhbm@"}
# obj.post(student_data) # only add it after that we get that data by caling metod get
# print(obj.get()) # print bcoz return in program


# print(obj.retriew(3))
# print(obj.getall_users())

# book,..(c.u.r.d) create update read delete
# list=get() #get all
# detail=retriew(id)
# create=post()
# update=put(id)
# delte=destroy(id)



# position arguments args

# def create_person(*args):
#    print(args)
#
# create_person("hari","12")

# kwars

# def create_person(**kwargs):
#     print(kwargs.get("name"))
#
#
#
# create_person(name="hari",age="12")
"""
output in dictionary format print kwars only annakil
args tuple

kwars dictionary
"""

# sorting based on words count desending order
#
# text="hai hello eveening"
#
# words=text.split()
# print(sorted(words,key=lambda w:len(w),reverse=True))

#
#
# class student:
#     rollno=int
#     name=str
#     def __init__(self,**kwars):
#         self.rollno=kwars.get("rollno")
#         self.name=kwars.get("name")
#         # print(kwars.get("rollno"))
#         print(self.rollno,self.name)
#     def __str__(self):  #method over riding
#         return self.name
#     def get_id(self):
#         print(self.rollno)
# obj=student(rollno=100,name="vijay")
# # obj.get_student()
# # print(obj) #without __str__ this cant print
# print(obj.get_id())

""' inheritance (inheritance (is a )always done with main class object)reethu nn car ind ridhay kk illya but ridhay use cheyunn reethunta inheritance allakil ridhay paisa koduth car vedikannam '
# class parent:
#     def car(self):
#         print("swift")
#     def mobile(self):
#         print("i20")
# class child(parent):
#     pass
# obj=child()
# obj.car()

""" __str__ is work even if not defined as method ,not show __str__ not defined ; bcoz all class as main class as object.. 
wheater we inherit or not anything object be working in object aall methods are defined as str ,init etcetc so we get value as main $5x..."""
# car annu parent shift child ..
# class car:
#      def breakes(self):
#          print("car break")
#      def accererate(self):
#          print("car accerate")
# class shift(car):
#     pass
# # method over riding
#
# obj=shift()
# obj.breakes()
# method over riding if parent as phone that inherit to child its inheritance once child become teenage he buy another phone
# so thats over riding (same method"mobile" that of parent)
# print(".................")
# class parent:
#     def mobile(self):
#         print("i20")
# class child(parent):
#     def mobile(self):
#         print("oneplue")
# ch=child()
# ch.mobile()
# decorator
# class student:
#     rollno=int
#     name=str
#     def __init__(self,**kwars):
#         self.rollno=kwars.get("rollno")
#         self.name=kwars.get("name")
#         # print(kwars.get("rollno"))
#         print(self.rollno,self.name)
#     def __str__(self):  #method over riding
#         return self.name
#     @property
#     def get_id(self):
#         print(self.rollno)
# obj=student(rollno=100,name="vijay")
# # obj.get_student()
# # print(obj) #without __str__ this cant print
# #print(obj.get_id) # we can call it as a attribute/property not as method no need this ()
#
# class mobile(object): #is a
#     name:str
#     price:int
#     display:str
#     def __init__(self,**kwargs):
#         self.name=kwargs.get("name")
#         self.price = kwargs.get("price")
#         self.display = kwargs.get("display")
#     def __str__(self):
#         return self.name
#     @property
#
#     def get_price(self):
#         return self.price
#     @property
#     def get_disc_price(self):
#         return self.price-1000
#
#
#
# obj=mobile(name="hari",price=1200,display="ii2o")
# print(obj.get_disc_price) # without() method we can cal it as attibute for that use property as decorator
"""""
decorator
def sub(n1,n2):
return(n1-n2)
def div(n1,n2):
return(n1/n2) 
here div and sub possible only when n1 is  greater else not work so we want to make that condition by using decorator
if n1<n2:
(n1,n2)=(n2,n1)




social<> postlist,like comment,follow,unfollow..all this done only when we login that app so these all are methods and 
login is decorator
decorator
def dec_name(fn)  deceorator always accept function inside decorator there is another inner function'
def inner_fun(n1,n2) this is for identify that fun which is to be decorate inside that all parameter that want to decorate should 
present here it is n1,n2
parameter name should not need to be same
if n1<n2:
(n1,n2)=(n2,n1)
return fn(n1,n2)
 over loading means method same but diff number of parameter
 its not suppot in python
 def add(n1+n2)
 def add(n1+n2+n3)
 print(100,200) here only know last method in python case so error as one argument is missing consider only last method
 
 over ride means child as inherit but add same metod but diff thing 

"""""
# def dec_fun(fn):#fn=sub(10,20)
#     def inner_fun(n1,n2):#inner_fun(10,20)
#         if n1<n2:  #10<20
#             (n1,n2) = (n2,n1)#n1=20,n2=10
#         return fn(n1,n2) #sub(20,10)
#     return inner_fun
#
#
#
# @dec_fun
# def sub(n1,n2):
#     return n1-n2
#
# @dec_fun
# def div(n1,n2):
#     return(n1/n2)
#
# print(sub(10,20))



# def dec_square(fn):
#     def wrapper(n1,n2):
#         return fn(n1**2,n2**2)
#     return wrapper
# @dec_square
# def add(n1,n2):
#     return n1+n2
# @dec_square
# def product(n1,n2):
#     return n1*n2
# print(add(2,3))
# print(product(2,2))


""" def dec_name(fn):
def wrapper(*args,**kwargs):
return fn((*args,**kwargs)
return wrapper"""
#
# class cali:
#
#     def add(self,*args,**kwargs):
#         return sum(args)
#
# obj=cali()
# obj.add(1,2,1)

""" abstartion hiding implementation details import abc.py class ABC abstractmethod there is no implementation 
details only the methhod name which class is inherit there only it details added, means child onlydetails give main class
have method name only

class car(ABC):
@abstract method
def start():

class swift(car):
def start():
print(sswift start)



"""
# from abc import ABC,abstractmethod
# class car(ABC):
#     def start(self):
#         pass
# class shift(car):
#
#     def start(self):
#         print("shift")
# obj=car()
# obj.start()





















