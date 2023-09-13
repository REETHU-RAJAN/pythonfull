""" encapsulation :wrapping the data in a single unit.
public,private,protect
public and protect are almost same here ._ for protect and .__ for private
they are access modifiers

"""
class Bank:
    def __init__(self,b_name,b_transations):
        self.name=b_name
        # self._trans=b_transations# protect but it same as public can access
        self.__trans=b_transations# private only access to that in case any class also call it then it not access there error
    def test(self):
        print("trans",self.__trans)# private acess within that class
bank=Bank("SBI",1234566)
bank.test()
# print( bank._trans) #protect info access
# print( bank.__trans)



class Customer(Bank):
    def bank_data(self):
        print(self.name)
        # print(self.__trans)#private access but cant access
obj=Customer("SBI",66756453)
obj.bank_data()


class Employee:
    def __init__(self,name,salery):
        self.name=name
        self.__salery=salery
    def show(self):
        print("name",self.name,"salery:",self.__salery) # same class private can access
# class person(Employee):
#     def person_data(self):
#         print("name",self.name,"salery:",self.__salery)
emp=Employee("reethu","12345")
#emp=person("reethu","12345") # seperate class private not access
emp.show()
#emp.person_data()
