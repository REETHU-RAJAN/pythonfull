"""The constructor is a method that is called when an object is created of a class.

The creation of the constructor depends on the programmer, or else Python will automatically generate
the default constructor.
It can be used in three types - Parameterized Constructor, Non-Parameterized Constructor, Default Constructor."""
 # parameterized constructor
class pyclass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
obj=pyclass("ree",12)
print(obj.name)


#default
class myclass:
    name="reet" # class parameter parameter pass before constructor
    def __init__(self): # default already  store just call

        pass
obj=myclass()
print(obj.name)# creating an object without passing parameter


#nonparametrized
class pyclass:
    def __init__(self): # values assign may be deafult but in constructor there is no parameter assign
        self.name="reethu"
        self.age=12
obj=pyclass()
print(obj.name)
