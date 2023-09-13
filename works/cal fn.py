#convert a list integers  into single integer
x=[12,13,15]
for i in x:
     print(i,end="")
print("\n...................")
#using map
def covert_(list):
    nums=int("".join(map(str,list)))
    return nums
list=[12,13,15]
print(covert_(list))
#maths
import math
a=-10
b=5
print(math.fabs(a)) # absolute value
print(math.factorial(b))
# #triangle
# import turtle
# t=turtle.Turtle()
# t.fillcolor("red")
# t.begin_fill()
# for i in range(3):
#
#     t.forward(100)
#     t.right(240)
#
# t.end_fill()
# turtle.done()
import random
list1=[1,4,5]
print(random.choice(list1))


