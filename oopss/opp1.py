""""""#oops  object orintened program .
# class=user define template,is a group of similar objects,is a logical entity, collection of objects
# object=triangle,car, is a real-world entity ,is a physical entity, instance of a class
#pep8 python enhancement proposal format
#inheritance= parent class ullath fetch cheidh eduka
#polymorphism= multiple forms of object (fly and non fly bird)
#epcapsulation= datas wrap of data amt (some data hide cheya) private cheidh vekya aact number public avum
#abstraction=data hide chiedh vekya atm cash edukun background process hide cheidh vekya
#The primary focus of PEP 8 is to improve the readability and consistency of Python code.
# PEP stands for Python Enhancement Proposal, and there are several of them.
""""""

class Car:
    def __init__(self, car_name, model, color,oil):  # constructor
        self.car_name = car_name
        self.color = color
        self.model = model
        self.oil = oil# constructor self init
    def drive(self):#method
        print("driving",self.car_name,self.model)
    def details(self):
        print("details",self.color,self.oil)

obj = Car("vento", 2023, "grey","diesel")  # attributes paranj koduth
print(obj.car_name)
print(obj.oil)
objs=Car("odii", 2022, "black","petrol")
objs.drive()
objs.details()
print("........................")
#2 define a class which have a class parameter and have a same instance parameter
class Dog:
 #class attribute
      attr1 = "mammal"


#Instance attribute:
      def __init__(self, name):
          self.name = name


# Driver code
# Object instantiation
obj = Dog("rodger")


#Accessing class attributes
print("Rodger is a {}".format(obj.__class__.attr1))
print("Tommy is also a {}".format(obj.__class__.attr1))

# Accessing instance attribute
obj1=Dog("rocky")
print(obj1.attr1)
print("My name is {}".format(obj1.name))
print("........................")
# sum of 2 num in a array 9
def printPairs(arr, n, sum):
    # count = 0

    # Consider all possible
    # pairs and check their sums
    for i in range(0, n):
        for j in range(i + 1, n):
            if (arr[i] + arr[j] == sum):
                print("(", arr[i],
                      ", ", arr[j],
                      ")", sep="")


# Driver Code
arr = [1, 5, 7, -1, 9]
n = len(arr)
sum = 6
printPairs(arr, n, sum)



print("........................")