"""
1. Write a Program to create a class by name Students, and initialize attributes like name,
 age, and grade while creating an object.
 """
# class Students:
#     name:str
#     age:int
#     grade:str
#     def __init__(self,name,age,grade):
#         self.name=name
#         self.age=age
#         self.grade=grade
# obj=Students("REETHU",28,"A")
# print("name",obj.name)
# print("age",obj.age)
# print("grade",obj.grade)

"""

2. Write a program to create a child class Teacher that will inherit the properties of Parent 
 Staff
 """
# class Staff:
#     skill:str
#     discipline:str
#     def __init__(self,skill,discipline):
#         self.skill=skill
#         self.discipline=discipline
# class Teacher(Staff):
#     pass
# obj=Teacher(" COMMUNICATION","DISCIPLINE")
# print(obj.skill)




"""3.Write a Python class Square, and define two methods that return the square area and perimeter."""


# class Square:
#     side:int
#     def __init__(self,side):
#         self.side=side
#     def area(self):
#         return self.side**2
#
#     def perimeter(self):
#
#         return 4*self.side
#
# obj=Square(2)
# print(obj.area())
# print(obj.perimeter())
"""4.define an account class with attributes ac no,ac name,balance.
"""
# class Account:
#     ac_no:int
#     ac_name:str
#     balance:int
#     def __init__(self,ac_no,ac_name,balance):
#         self.ac_no=ac_no
#         self.ac_name=ac_name
#         self.balance=balance
# obj=Account(1234,"reethu",5555)
# print(obj.ac_name)
# print(obj.ac_no)
# print(obj.balance)
# print(f"my account name is {obj.ac_name} account number is {obj.ac_no} and balance is {obj.balance}")

"""
5.Create classes for a school management system. Have classes like Student, Teacher, and Course. 
Implement methods to enroll students, assign teachers, and display course details.
"""



class Student:
    student_id:int
    name:str
    age:int
    def __init__(self,student_id,name,age):
        self.student_id=student_id
        self.name=name
        self.age=age
    def enroll(self):
        print(f"Id {self.student_id} student {self.name} of age {self.age} ")

class Teacher:
    def __init__(self,teacher_id,name,subject):
        self.teacher_id=teacher_id
        self.name=name
        self.subject=subject
    def assign_teachers(self):
        print(f"Id {self.teacher_id} teacher {self.name} subject {self.subject}")

class Course:
    def __init__(self,course_code,course_name):
        self.course_code=course_code
        self.course_name=course_name

    def display_coursedetails(self):

        print(f"course code {self.course_code} course name {self.course_name}")



std=Student(1,"reethu",28)
std.enroll()

tcr=Teacher(1,"rennu","python")
tcr.assign_teachers()

crse=Course(1234,"django")
crse.display_coursedetails()



