"""
child class(subclass, derived class) inherits the properties of parent class(super class,base class)
code reusability
•	It represents real-world relationships well.
•	It provides the reusability of a code. We don’t have to write the same code again and again.
 Also, it allows us to add more features to a class without modifying it.
•	It is transitive in nature, which means that if class B inherits from another class A, then all the subclasses of B
 would automatically inherit from class A

 SELF represents the instance of class. This handy keyword allows you to access variables, attributes, and methods of a defined class in Python.
 The self parameter doesn't have to be named “self,” as you can call it by any other name.
single,multiple,multilevel, hierachial ,hybrid are types inheritnce

"""
## single inheritance: one parent one child class inherit
# class Animal: # no need
#     def __init__(self,name):
#          self.name=name
#     def speak(self):
#          pass
#
# class dog(Animal):
#     def speak(self):# method
#         print(self.name,"barks")
#         print("dog name is",self.name)
#
# class cat(Animal):
#     def speak(self):
#         print(self.name, "meow")
# obj_dog=dog("rockey")
# obj_cat=cat("kitty")
# obj_dog.speak()# call
# obj_cat.speak()
# obj=Animal("abcd")
# obj.speak()
# hierachial inheritance one parent 2 child if only one child then single inheritance
class Animal:
    def __init__(self,name,category):
         self.name=name
         self.category=category
    def test(self):
        print("parent class")
class dog(Animal):
    def speak(self):# method
        print(self.name,"barks")
        print("dog name is",self.name,self.category)

class cat(Animal):
    def speak(self):
        print(self.name, "meow")
obj_dog=dog("rockey","danger")
obj_cat=cat("kitty","baby")
obj_dog.speak()# call
obj_cat.speak()
obj=Animal("abcd","hghjg")
obj.test()
class bird:
    def __init__(self,flys,sound):
         self.flys=flys
         self.sound=sound
    def test(self):
        print("parent class")
class duck(bird):
    def speak(self):# method
        print(self.sound,self.flys,"quii","nofly")#print(self.sound,self.flys)
        print("duck name is",self.flys,self.sound)

class crow(bird):
    def speak(self):
        print(self.sound, "crew")
obj_duck=duck("quick","nofly")

obj_crow=crow("flyy","cree")
obj_duck.speak()# call
obj_crow.speak()
obj=bird("abcd","hghjg")
obj.test()


# print only common elements
# array1 = [1, 2, 3, 4, 5]
# array2 = [4, 5, 6, 7, 8]
# common_elements = set(array1).intersection(array2)
# print("Common elements:", common_elements)


#pascals triangle
# def print_pattern(n):
#     row = [1]
#     for i in range(n):
#          print(" ".join(str(x) for x in row))
#
#          next_row = [1]
#          for j in range(1, len(row)):
#              next_row.append(row[j - 1] + row[j])
#          next_row.append(1)
#          row = next_row
# print_pattern(6)
#
# #num_rows=5
## display the triangle
# for i in range(num_rows):
#     #print leading spaces for visual alignment
#     for j in range(num_rows-i-1):
#         print(" ",end="")
# # initializing each row as 1
#     val=1
#     for j in range(i+1):
#         print(val,end=" ")
#     # calculate the next value based on the previous value
#         val=val*(i-j)//(j+1)
#     print()
#print()


# def is_armstrong_number(num):
#     # Convert the number to a string to count the number of digits
#     num_str = str(num)
#     # Calculate the power to be used for each digit
#     power = len(num_str)
#     # Initialize the sum of the powered digits
#     sum_of_digits = 0
#
#     # Calculate the sum of the powered digits
#     for digit in num_str:
#         sum_of_digits += int(digit) ** power
#
#     # Check if the number is an Armstrong number
#     if num == sum_of_digits:
#         return True
#     else:
#         return False
#
# number = int(input("Enter a number: "))
# if is_armstrong_number(number):
#     print(number, "is an Armstrong number.")
# else:
#     print(number, "is not an Armstrong number.")


# find the digits with sum 9
# def find_pairs(arr, target_sum):
#     pairs = []
#     left = 0
#     right = len(arr) - 1
#
#     while left < right:
#         current_sum = arr[left] + arr[right]
#         if current_sum == target_sum:
#             pairs.append((arr[left], arr[right]))
#             left += 1
#             right -= 1
#         elif current_sum < target_sum:
#             left += 1
#         else:
#             right -= 1
#
#     return pairs
#
# arr = [2, 3, 4, 5, 6]
# target = 9
#
# result = find_pairs(arr, target)
# if len(result) > 0:
#     print("Pairs which give sum", target, "are:")
#     for pair in result:
#         print(pair)
# else:
#     print("No pairs found with sum", target)


##mutilpe inheritanc: one child class can inherit from multiple parent class
class vehicle: # parent1
    def vehicle_info(self):
        print("inside vehicle class")
class car:#parent2
    def car_info(self):
        print("inside car class")
 # child class
class super_car(car,vehicle):
    def super_car_info(self):

      print ("inside super car class")
obj=super_car()
obj.car_info()
obj.super_car_info()
obj.vehicle_info()
print("........................")
#multilevel inheritance: a,b,c c inherit from b and b inherit from a
class vehicle: # parent1
    def vehicle_info(self):
        print("inside vehicle class")
class car(vehicle):#child 1
    def car_info(self):
        print("inside car class")
 # child class
class super_car(car):
    def super_car_info(self):

      print ("inside super car class")

car=car()
car.car_info()
car.vehicle_info()
super_car=super_car()
super_car.super_car_info()
super_car.vehicle_info()
super_car.car_info()
print("............................")

#hierachical inheritance: more than one child class impliment from single parent class some what same as single inheritance
class vehicle:
    def info(self):
        print("this is vehicle")
class car(vehicle):
    def car_info(self,name):
        print("car name is",name)
class truck(vehicle):
    def truck_info(self,name):
        print("truck name is",name)
obj1=car()
obj1.car_info("bmw")
obj1.info()
obj2=truck()
obj2.truck_info("tata")


obj2.info()
print("........................")
# combination of multiple(diff) inheritance is called hybrid here hierachial plus mutilpe inheritance
class vehicle:
    def info(self):
        print("this is vehicle")
class car(vehicle):
    def car_info(self,name):
        print("car name is",name)
class truck(vehicle):
    def truck_info(self,name):
        print("truck name is",name)
class supercar(car,truck):
    def super_car_info(self):
        print("inside the sports car class")
super_car=supercar()
super_car.car_info("bmw")
super_car.info()
super_car.truck_info("tata")

print("...................")

